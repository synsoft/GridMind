"""
StationMatcher - Zajednička klasa za prepoznavanje stanica/objekata.

Koristi se od strane:
- DalekvodChecker (za traženje dalekovoda između stanica)
- ObjectInfoProvider (za dohvatanje normalnog uklopnog stanja)
"""

import json
import logging
import re
from pathlib import Path
from typing import Optional, Dict, List, Any
from rapidfuzz import fuzz, process

logger = logging.getLogger(__name__)

# Compute absolute path to data directory
_THIS_DIR = Path(__file__).parent
_DATA_DIR = _THIS_DIR.parent.parent / "data"
_CHUNKS_DIR = Path(__file__).parent.parent.parent.parent / "chunks"


class StationMatcher:
    """
    Singleton klasa za prepoznavanje i matching stanica/objekata.
    
    Učitava podatke iz:
    - dv_station_map_complete.json (lista stanica iz grafa)
    - object_registry.json (podaci o objektima sa normalnim uklopnim stanjima)
    """
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        
        self._load_data()
        self._build_lookup_tables()
        self._initialized = True
        logger.info(f"[STATION-MATCHER] ✓ Inicijalizovan ({len(self.all_stations)} stanica, {len(self.objects_by_code)} objekata)")
    
    def _load_data(self):
        """Učitaj sve potrebne podatke."""
        # 1. Učitaj mapu dalekovoda za listu stanica
        dv_map_path = _DATA_DIR / "dv_station_map_complete.json"
        with open(dv_map_path, 'r', encoding='utf-8') as f:
            self.dv_map = json.load(f)
        
        # 2. Učitaj object registry
        registry_path = _CHUNKS_DIR / "metadata" / "object_registry.json"
        with open(registry_path, 'r', encoding='utf-8') as f:
            self.registry = json.load(f)
    
    def _build_lookup_tables(self):
        """Napravi lookup tabele za brzo pretraživanje."""
        # 1. Lista svih stanica iz grafa
        stations = set()
        for connections in self.dv_map.values():
            for pair in connections:
                stations.add(pair[0])
                stations.add(pair[1])
        self.all_stations = list(stations)
        
        # 2. Objekti po kodu
        self.objects_by_code: Dict[str, Dict] = {}
        for obj in self.registry.get('objects', []):
            code = obj.get('code')
            if code:
                self.objects_by_code[code] = obj
        
        # 3. Objekti po imenu (latinica i ćirilica)
        self.objects_by_name: Dict[str, Dict] = {}
        for obj in self.registry.get('objects', []):
            name = obj.get('name', '').lower()
            name_cyr = obj.get('name_cyrillic', '').lower()
            if name:
                self.objects_by_name[name] = obj
            if name_cyr:
                self.objects_by_name[name_cyr] = obj
            # Dodaj i aliase
            for alias in obj.get('aliases', []):
                self.objects_by_name[alias.lower()] = obj
        
        # 4. Normalizovane stanice za fuzzy matching
        self.normalized_stations = {
            self._normalize_name(s): s for s in self.all_stations
        }
    
    def _normalize_name(self, name: str) -> str:
        """Normalizuj naziv za lakše poređenje."""
        if not name:
            return ""
        
        # Konvertuj u latinicu
        try:
            from cyrtranslit import to_latin
            name = to_latin(name, 'sr')
        except ImportError:
            pass
        
        name_lower = name.lower().strip()
        
        # Zameni dijakritike za česte gradove (Nis -> Niš, Cacak -> Čačak)
        diacritic_map = {
            'nis ': 'niš ',
            'nis$': 'niš',
            'cacak': 'čačak',
            'sabac': 'šabac',
            'pancevo': 'pančevo',
            'subotica': 'subotica',  # već OK
        }
        
        import re
        for pattern, replacement in diacritic_map.items():
            if pattern.endswith('$'):
                if name_lower.endswith(pattern[:-1]):
                    name_lower = name_lower[:-len(pattern)+1] + replacement
            else:
                name_lower = name_lower.replace(pattern, replacement)
        
        # Mapiranje skraćenica
        replacements = {
            'bg': 'beograd',
            'ns': 'novi sad',
            'sm': 'sremska mitrovica',
            'kr': 'kragujevac',
            'ni': 'niš',
            'su': 'subotica',
            'pa': 'pančevo',
            'va': 'valjevo',
            'ca': 'čačak',
            'sa': 'šabac',
            'le': 'leskovac',
            'vr': 'vranje',
            'so': 'sombor',
            'zr': 'zrenjanin',
        }
        
        for abbr, full in replacements.items():
            if name_lower.startswith(abbr + ' '):
                name_lower = name_lower.replace(abbr + ' ', full + ' ', 1)
        
        return name_lower
    
    def find_station(self, query: str, threshold: int = 50) -> Optional[str]:
        """
        Pronađi stanicu po nazivu koristeći fuzzy matching.
        
        Args:
            query: Naziv stanice (može biti neprecizan)
            threshold: Minimalni score za fuzzy match (0-100)
        
        Returns:
            Tačan naziv stanice ili None
        """
        query_normalized = self._normalize_name(query)
        
        # 1. Tačno podudaranje
        if query_normalized in self.normalized_stations:
            return self.normalized_stations[query_normalized]
        
        # 2. Dodaj "ts " prefix ako nije prisutan
        prefixes = ['ts ', 'rp ', 'he ', 'te ', 'prp ']
        has_prefix = any(query_normalized.startswith(p) for p in prefixes)
        
        if not has_prefix:
            for prefix in ['ts ', 'rp ']:
                query_with_prefix = prefix + query_normalized
                if query_with_prefix in self.normalized_stations:
                    return self.normalized_stations[query_with_prefix]
        
        # 3. Fuzzy matching
        result = process.extractOne(
            query_normalized,
            self.normalized_stations.keys(),
            scorer=fuzz.WRatio,
            score_cutoff=threshold
        )
        
        if result:
            matched_normalized = result[0]
            return self.normalized_stations[matched_normalized]
        
        return None
    
    def find_object(self, query: str) -> Optional[Dict[str, Any]]:
        """
        Pronađi objekat iz registra po nazivu ili kodu.
        
        Args:
            query: Naziv ili kod objekta
        
        Returns:
            Dict sa podacima o objektu ili None
        """
        query_lower = query.lower().strip()
        query_normalized = self._normalize_name(query)
        
        # 1. Tačno podudaranje po kodu
        query_upper = query.upper().strip()
        if query_upper in self.objects_by_code:
            return self.objects_by_code[query_upper]
        
        # 2. Tačno podudaranje po imenu
        if query_lower in self.objects_by_name:
            return self.objects_by_name[query_lower]
        
        # 3. Direktno poređenje sa svim objektima (sa brojevima!)
        # Ovo je bitno jer "Beograd 5" != "Beograd 3"
        for obj in self.registry.get('objects', []):
            obj_name = self._normalize_name(obj.get('name', ''))
            obj_name_cyr = self._normalize_name(obj.get('name_cyrillic', ''))
            
            # Tačno podudaranje (sa brojevima)
            if query_normalized == obj_name or query_normalized == obj_name_cyr:
                return obj
            
            # Podudaranje sa TS/RP prefiksom
            for prefix in ['ts ', 'rp ', 'prp ', 'he ', 'te ']:
                if prefix + query_normalized == obj_name:
                    return obj
                if prefix + query_normalized == obj_name_cyr:
                    return obj
        
        # 4. Fuzzy matching ALI samo ako se brojevi poklapaju
        import re
        query_num = re.search(r'\d+', query_normalized)
        query_number = query_num.group() if query_num else None
        
        best_match = None
        best_score = 0
        
        for obj in self.registry.get('objects', []):
            obj_name = self._normalize_name(obj.get('name', ''))
            
            # Izvuci broj iz imena objekta
            obj_num = re.search(r'\d+', obj_name)
            obj_number = obj_num.group() if obj_num else None
            
            # Ako oba imaju brojeve, moraju se poklapati
            if query_number and obj_number and query_number != obj_number:
                continue
            
            score = fuzz.ratio(query_normalized, obj_name)
            if score > best_score and score > 80:
                best_score = score
                best_match = obj
        
        return best_match
    
    def _find_object_by_station_name(self, station_name: str) -> Optional[Dict]:
        """Pronađi objekat po nazivu stanice iz grafa."""
        station_normalized = self._normalize_name(station_name)
        
        for obj in self.registry.get('objects', []):
            obj_name = self._normalize_name(obj.get('name', ''))
            obj_name_cyr = self._normalize_name(obj.get('name_cyrillic', ''))
            
            if station_normalized == obj_name or station_normalized == obj_name_cyr:
                return obj
            
            # Probaj fuzzy matching
            if fuzz.ratio(station_normalized, obj_name) > 85:
                return obj
            if fuzz.ratio(station_normalized, obj_name_cyr) > 85:
                return obj
        
        return None
    
    def get_normalno_uklopno_stanje(self, query: str) -> Optional[str]:
        """
        Dohvati normalno uklopno stanje za dati objekat.
        
        Args:
            query: Naziv ili kod objekta (npr. "TS Beograd 5", "BG5", "Београд 5")
        
        Returns:
            Tekst normalnog uklopnog stanja ili None
        """
        obj = self.find_object(query)
        if obj:
            return obj.get('normalno_uklopno_stanje')
        return None
    
    def get_object_info(self, query: str) -> Optional[Dict[str, Any]]:
        """
        Dohvati sve informacije o objektu.
        
        Args:
            query: Naziv ili kod objekta
        
        Returns:
            Dict sa svim podacima o objektu ili None
        """
        return self.find_object(query)
    
    def extract_stations_from_text(self, text: str) -> List[str]:
        """
        Izvuci sve stanice pomenute u tekstu.
        
        Args:
            text: Tekst za analizu
        
        Returns:
            Lista pronađenih stanica
        """
        found = []
        
        # Pattern za TS/RP nazive
        patterns = [
            r'ТС\s+[А-Яа-яЂђЉљЊњЋћЏџ\s]+\d*',  # ćirilica
            r'TS\s+[A-Za-zčćžšđČĆŽŠĐ\s]+\d*',   # latinica
            r'РП\s+[А-Яа-яЂђЉљЊњЋћЏџ\s]+\d*',  # ćirilica RP
            r'RP\s+[A-Za-zčćžšđČĆŽŠĐ\s]+\d*',   # latinica RP
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, text)
            for match in matches:
                station = self.find_station(match.strip())
                if station and station not in found:
                    found.append(station)
        
        return found


# Singleton instance
_matcher_instance: Optional[StationMatcher] = None


def get_station_matcher() -> StationMatcher:
    """Dohvati singleton instancu StationMatcher-a."""
    global _matcher_instance
    if _matcher_instance is None:
        _matcher_instance = StationMatcher()
    return _matcher_instance
