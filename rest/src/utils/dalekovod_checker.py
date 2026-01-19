import json
import re
import logging
from pathlib import Path
from rapidfuzz import fuzz, process

logger = logging.getLogger(__name__)

# Compute absolute path to data directory
_THIS_DIR = Path(__file__).parent
_DATA_DIR = _THIS_DIR.parent.parent / "data"


class DalekvodChecker:
    def __init__(self, json_path=None):
        # Koristi kompletnu mapu dalekovoda (sa svim vezama)
        self.json_path = json_path or str(_DATA_DIR / "dv_station_map_complete.json")
        self._load_data()
        self._build_station_list()
        self._init_graph_pathfinder()
    
    def _load_data(self):
        """Učitaj mapu dalekovoda"""
        with open(self.json_path, 'r', encoding='utf-8') as f:
            self.dv_map = json.load(f)
    
    def _init_graph_pathfinder(self):
        """Inicijalizuj graf pretrage za indirektne putanje"""
        try:
            from rest.data.graph import PathFinder
            self.path_finder = PathFinder()
            logger.info(f"[DV-CHECKER] ✓ Graf inicijalizovan ({self.path_finder.graph.get_station_count()} stanica)")
        except Exception as e:
            logger.warning(f"[DV-CHECKER] ⚠ Nije moguće učitati graf: {e}")
            self.path_finder = None
    
    def _build_station_list(self):
        """Napravi listu svih jedinstvenih stanica"""
        stations = set()
        for connections in self.dv_map.values():
            for pair in connections:
                stations.add(pair[0])
                stations.add(pair[1])
        self.all_stations = list(stations)
    
    def _normalize_station_name(self, name):
        """Normalizuj naziv stanice za lakše poređenje"""
        # Ukloni dijakritike i pretvori u latinicu
        from cyrtranslit import to_latin
        name = to_latin(name, 'sr')
        
        # Mapiranje skraćenica
        replacements = {
            'bg': 'beograd',
            'ns': 'novi sad',
            'sm': 'sremska mitrovica',
            'kr': 'kragujevac',
            'ni': 'nis',
            'su': 'subotica',
        }
        
        name_lower = name.lower().strip()
        for abbr, full in replacements.items():
            if name_lower.startswith(abbr + ' '):
                name_lower = name_lower.replace(abbr + ' ', full + ' ', 1)
        
        return name_lower
    
    def _find_best_match(self, query, threshold=50):
        """Pronađi najbližu stanicu koristeći fuzzy matching"""
        query_normalized = self._normalize_station_name(query)
        logger.info(f"[DV-CHECKER] Tražim stanicu: '{query}' (normalizovano: '{query_normalized}')")
        
        # Normalizuj sve stanice za poređenje
        normalized_stations = {self._normalize_station_name(s): s for s in self.all_stations}
        
        # Prvo pokušaj tačno podudaranje
        if query_normalized in normalized_stations:
            logger.info(f"[DV-CHECKER] ✓ Tačno podudaranje: '{normalized_stations[query_normalized]}'")
            return normalized_stations[query_normalized]
        
        # Dodaj "ts " prefix ako nije prisutan (čest slučaj)
        if not query_normalized.startswith('ts ') and not query_normalized.startswith('rp ') and not query_normalized.startswith('he '):
            query_with_ts = 'ts ' + query_normalized
            if query_with_ts in normalized_stations:
                logger.info(f"[DV-CHECKER] ✓ Podudaranje sa TS: '{normalized_stations[query_with_ts]}'")
                return normalized_stations[query_with_ts]
        
        # Koristi WRatio (weighted ratio) koji bolje barata različitim dužinama
        result = process.extractOne(
            query_normalized, 
            normalized_stations.keys(), 
            scorer=fuzz.WRatio,  # WRatio je bolji za različite dužine
            score_cutoff=threshold
        )
        if result:
            matched_normalized = result[0]
            score = result[1]
            original_name = normalized_stations[matched_normalized]
            logger.info(f"[DV-CHECKER] ✓ Pronađen match: '{original_name}' (score: {score})")
            return original_name  # Vrati original
        
        logger.warning(f"[DV-CHECKER] ✗ Nije pronađen match za '{query}' (threshold: {threshold})")
        return None
    
    def get_dalekovod_info(self, dv_id):
        """Vrati info o jednom dalekovodu"""
        dv_id_str = str(dv_id)
        if dv_id_str in self.dv_map:
            stations = self.dv_map[dv_id_str]
            pairs = [f"{pair[0]} - {pair[1]}" for pair in stations]
            response = f"Dalekovod {dv_id} spaja: {'; '.join(pairs)}"
            logger.info(f"[DV-CHECKER] Info za DV {dv_id}: {response}")
            return response
        logger.info(f"[DV-CHECKER] DV {dv_id} nije pronađen u mapi")
        return None
    
    def find_dalekovods_between_stations(self, station1, station2, fuzzy=True):
        """Pronađi dalekovode između dve stanice"""
        logger.info(f"[DV-CHECKER] Tražim dalekovode između '{station1}' i '{station2}' (fuzzy={fuzzy})")
        
        if fuzzy:
            # Koristi fuzzy matching da pronađeš stvarne nazive
            matched_s1 = self._find_best_match(station1)
            matched_s2 = self._find_best_match(station2)
            
            if not matched_s1 or not matched_s2:
                logger.warning(f"[DV-CHECKER] ✗ Nije moguće naći obe stanice (s1={matched_s1}, s2={matched_s2})")
                return None
            
            # Koristi pronađene nazive
            station1 = matched_s1
            station2 = matched_s2
        
        logger.info(f"[DV-CHECKER] Pretražujem za tačne nazive: '{station1}' <-> '{station2}'")
        
        results = []
        for dv_id, connections in self.dv_map.items():
            for pair in connections:
                # Proveri oba smera
                if (station1 == pair[0] and station2 == pair[1]) or \
                   (station1 == pair[1] and station2 == pair[0]):
                    results.append({
                        'dv_id': dv_id,
                        'connection': f"{pair[0]} - {pair[1]}"
                    })
        
        if results:
            logger.info(f"[DV-CHECKER] ✓ Pronađeno {len(results)} dalekovod(a)")
            response = f"Dalekovodi između {station1} i {station2}:\n"
            for r in results:
                response += f"  - DV {r['dv_id']}: {r['connection']}\n"
            final_response = response.strip()
            logger.info(f"[DV-CHECKER] Vraćam odgovor:\n{final_response}")
            return final_response
        
        # Nema direktne veze - pokušaj pronaći indirektnu putanju preko grafa
        logger.info(f"[DV-CHECKER] Nema direktne veze, tražim indirektnu putanju...")
        graph_result = self._find_path_via_graph(station1, station2)
        if graph_result:
            return graph_result
        
        logger.warning(f"[DV-CHECKER] ✗ Nisu pronađeni dalekovodi između '{station1}' i '{station2}'")
        return None
    
    def _find_path_via_graph(self, station1, station2, max_depth=4):
        """Pronađi indirektnu putanju između stanica koristeći graf pretragu."""
        if self.path_finder is None:
            logger.warning("[DV-CHECKER] Graf nije dostupan za pretragu")
            return None
        
        try:
            conn = self.path_finder.find_connection(station1, station2, max_depth=max_depth)
            
            # Proveri da li stanice postoje u grafu
            if not conn.get("start_exists") or not conn.get("end_exists"):
                # Pokušaj naći slične stanice
                suggestions = conn.get("suggestions", {})
                if suggestions:
                    logger.info(f"[DV-CHECKER] Sugestije za stanice: {suggestions}")
                return None
            
            # Ako postoji putanja
            if conn.get("shortest_path"):
                path = conn["shortest_path"]
                
                # Formatiranje odgovora
                if path["length"] == 0:
                    return None  # Iste stanice
                
                # Ako ima direktnu vezu u grafu, vrati je grupisano po naponu
                if conn.get("direct_lines_by_voltage"):
                    response = f"**Direktne veze:**\n"
                    for v in sorted(conn["direct_lines_by_voltage"].keys(), reverse=True):
                        dv_list = conn["direct_lines_by_voltage"][v]
                        dv_str = ", ".join([f"DV {dv}" for dv in dv_list])
                        response += f"  • {v} kV: {dv_str}\n"
                    return response.strip()
                
                # Indirektna putanja
                voltage_info = f" ({path['voltage_kv']} kV)" if path.get("is_single_voltage") and path.get("voltage_kv") else " (mešoviti naponi)"
                response = f"**Indirektna veza** ({path['length']} skokova){voltage_info}:\n"
                response += f"{station1} i {station2} nisu direktno povezane, ali postoji veza preko međustanica:\n\n"
                
                segments = path["segments"]
                response += f"  {segments[0]['from']}\n"
                for seg in segments:
                    response += f"    ──[DV {seg['line']} ({seg['voltage_kv']} kV)]──> {seg['to']}\n"
                
                # Formatiraj listu dalekovoda sa naponima
                line_info = [f"DV {l} ({v} kV)" for l, v in zip(path['lines'], path['voltages'])]
                response += f"\n**Korišćeni dalekovodi:** {', '.join(line_info)}"
                
                # Dodaj alternative grupisane po naponu
                if conn.get("paths_by_voltage"):
                    response += "\n\n**Alternativne putanje po naponskom nivou:**"
                    for v in sorted(conn["paths_by_voltage"].keys(), reverse=True):
                        paths = conn["paths_by_voltage"][v]
                        response += f"\n\n  **{v} kV:**"
                        for i, alt in enumerate(paths[:2], 1):
                            response += f"\n    {i}. {' → '.join(alt['stations'])}"
                            dv_list = ", ".join([f"DV {l}" for l in alt["lines"]])
                            response += f"\n       ({dv_list})"
                
                logger.info(f"[DV-CHECKER] ✓ Pronađena indirektna putanja sa {path['length']} skokova")
                return response
            
            return None
            
        except Exception as e:
            logger.error(f"[DV-CHECKER] Greška pri pretrazi grafa: {e}")
            return None
        return None
    
    def check_question(self, question):
        """Proveri da li pitanje pominje dalekovode i vrati info"""
        logger.info(f"[DV-CHECKER] Analiziram pitanje: '{question}'")
        question_lower = question.lower()
        
        # Tip 2: "Kojim dalekovodima je TS X povezana sa TS Y?" - PRIORITET!
        # Proveri prvo da li se traže dalekovodi između stanica
        if any(word in question_lower for word in ['kojim', 'koje', 'povezan', 'spojen', 'između', 'spaja', 'kako']):
            # Jednostavnija ekstrakcija - traži sve potencijalne nazive stanica
            # Ukloni česte reči - proširena lista
            noise_words = ['kojim', 'koje', 'dalekovod', 'dalekovodima', 'je', 'povezan', 
                          'povezana', 'sa', 'i', 'spojen', 'spojena', 'spaja', 'spajaju', 
                          'između', 'sta', 'što', 'šta', 'kako', 'da', 'li', 'su', 'na',
                          'preko', 'od', 'do', 'ili', 'a', 'u', 'po', 'za', 'se', 'to',
                          'ima', 'postoji', 'veza', 'vezu', 'put', 'putanja']
            
            # Split na reči i filtriraj
            words = question_lower.split()
            potential_stations = []
            current_station = []
            
            for word in words:
                # Ukloni interpunkciju
                word = word.strip(',.?!:;')
                
                # Ako je reč prefiks stanice, počni novu stanicu
                if word in ['ts', 'тс', 'rp', 'рп', 'prp', 'прп', 'he', 'хе', 'te', 'те', 'evp', 'евп']:
                    if current_station:
                        potential_stations.append(' '.join(current_station))
                        current_station = []
                    # Dodaj prefiks kao deo sledećeg naziva stanice
                    current_station.append(word)
                    continue
                
                # Ako je šum reč, završi trenutnu stanicu
                if word in noise_words:
                    if current_station:
                        potential_stations.append(' '.join(current_station))
                        current_station = []
                    continue
                
                # Dodaj u trenutnu stanicu
                if word:
                    current_station.append(word)
            
            # Dodaj poslednju
            if current_station:
                potential_stations.append(' '.join(current_station))
            
            # Filtriraj prazne i kratke, ali zadrži one koji počinju sa ts/rp/he itd
            potential_stations = [s for s in potential_stations if len(s) > 2]
            
            logger.info(f"[DV-CHECKER] Potencijalne stanice pre filtriranja: {potential_stations}")
            
            if len(potential_stations) >= 2:
                logger.info(f"[DV-CHECKER] Detektovane stanice: {potential_stations[:2]}")
                result = self.find_dalekovods_between_stations(
                    potential_stations[0], 
                    potential_stations[1]
                )
                if result:
                    logger.info(f"[DV-CHECKER] ✓ Vraćam rezultat")
                    return result
            else:
                logger.info(f"[DV-CHECKER] Detektovano {len(potential_stations)} stanica (treba >= 2)")
        
        # Tip 1: "Šta spaja dalekovod 101?" - ako Tip 2 nije uspeo
        if 'dalekovod' in question_lower or 'dv' in question_lower:
            numbers = re.findall(r'\b\d+/?[\d/]*[АБаб]?\b', question)
            logger.info(f"[DV-CHECKER] Detektovani brojevi dalekovoda: {numbers}")
            if numbers:
                results = []
                for num in numbers:
                    info = self.get_dalekovod_info(num)
                    if info:
                        results.append(info)
                if results:
                    logger.info(f"[DV-CHECKER] ✓ Pronađeno info za dalekovode: {numbers}")
                    final_response = "\n".join(results)
                    logger.info(f"[DV-CHECKER] Vraćam odgovor:\n{final_response}")
                    return final_response
        
        logger.info(f"[DV-CHECKER] ✗ Nije pronađen relevantan odgovor")
        return None
