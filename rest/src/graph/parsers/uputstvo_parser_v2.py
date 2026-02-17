#!/usr/bin/env python3
"""
Poboljšani parser za Uputstva za pogon TS/RP.

v2.0 - Poboljšanja:
- Bolje hvatanje DV sa svih naponskih nivoa
- Parsiranje susednih TS iz sekcije 4
- Parsiranje svih uklopnih stanja (normalno, bez DZS, bez TR)
- Bolje hvatanje SP statusa
- Ekstrakcija paralelnih radova i ograničenja
"""

import re
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Tuple
import cyrtranslit


@dataclass
class DalekovodInfo:
    """Informacije o dalekovodu."""
    oznaka: str  # npr. "DV 403"
    broj: str    # npr. "403"
    destinacija_kod: Optional[str] = None
    destinacija_naziv: Optional[str] = None
    napon_kv: Optional[int] = None
    drugi_kraj_eeo: Optional[str] = None  # Kod EEO na drugom kraju


@dataclass
class TransformatorInfo:
    """Informacije o transformatoru."""
    oznaka: str
    vn_kv: int
    nn_kv: int
    snaga_mva: Optional[int] = None
    ima_regulaciju: bool = False
    treci_namot: Optional[int] = None  # Tercijer kV


@dataclass
class SusedniEEOInfo:
    """Informacije o susednom EEO."""
    kod: str
    naziv: str
    napon_kv: int
    dv_oznake: List[str] = field(default_factory=list)
    uklopno_stanje: Optional[str] = None


@dataclass
class UklopnoStanje:
    """Uklopno stanje za jedan naponski nivo."""
    napon_kv: int
    naziv: str = "normalno"  # "normalno", "bez_dzs", "bez_tr", etc.
    polja_gs1: List[str] = field(default_factory=list)
    polja_gs2: List[str] = field(default_factory=list)
    spojno_polje: str = "nepoznato"  # "ukljuceno", "iskljuceno", "rasklopljeno"
    dzs_aktivna: bool = False
    poduzni_rastavljac: str = "nepoznato"
    napomene: List[str] = field(default_factory=list)


@dataclass 
class ParalelniRad:
    """Informacije o paralelnom radu."""
    sa_eeo: str
    preko: List[str]  # Lista EEO kroz koje ide
    dozvoljen: bool
    napomena: Optional[str] = None


@dataclass
class EEOParsedDataV2:
    """Parsirani podaci za jedan EEO - v2."""
    kod: str
    naziv: str
    tip: str
    naponski_nivoi: List[int]
    godina: Optional[int] = None
    
    # Oprema
    dalekovodi: Dict[int, List[DalekovodInfo]] = field(default_factory=dict)  # napon -> [DV]
    transformatori: List[TransformatorInfo] = field(default_factory=list)
    
    # Susedni objekti (iz sekcije 4)
    susedni_eeo: Dict[int, List[SusedniEEOInfo]] = field(default_factory=dict)  # napon -> [susedni]
    
    # Uklopna stanja
    uklopna_stanja: Dict[str, Dict[int, UklopnoStanje]] = field(default_factory=dict)
    # "normalno" -> {400: UklopnoStanje, 220: ..., 110: ...}
    # "bez_dzs_400" -> {...}
    
    # Paralelni radovi
    paralelni_radovi: List[ParalelniRad] = field(default_factory=list)
    
    # Matrica povezanosti za ovaj EEO
    connectivity: List[Tuple[str, int, str, int, int]] = field(default_factory=list)
    # (ovaj_eeo, dvp_index, drugi_eeo, drugi_dvp_index, napon)


class UputstvoParserV2:
    """Poboljšani parser za Uputstva za pogon."""
    
    def __init__(self):
        self.eeo_code_map = self._build_eeo_code_map()
        
    def _build_eeo_code_map(self) -> Dict[str, str]:
        """Mapa punih naziva na kodove EEO - proširena."""
        base_map = {
            # Glavne TS
            "nis 2": "NI2", "niš 2": "NI2", "ni 2": "NI2",
            "nis 1": "NI1", "niš 1": "NI1",
            "nis 3": "NI3", "niš 3": "NI3",
            "nis 5": "NI5", "niš 5": "NI5",
            "nis 8": "NI8", "niš 8": "NI8",
            "nis 13": "NI13", "niš 13": "NI13",
            "nis 15": "NI15", "niš 15": "NI15",
            "leskovac 2": "LE2",
            "leskovac 4": "LE4",
            "bor 2": "BOR2",
            "jagodina 4": "JA4",
            "krusevac 1": "KR1", "kruševac 1": "KR1",
            "beograd 5": "BG5",
            "beograd 8": "BG8",
            "beograd 3": "BG3",
            "beograd 20": "BG20",
            "novi sad 3": "NS3",
            "pancevo 2": "PA2", "pančevo 2": "PA2",
            "smederevo 3": "SD3",
            "zrenjanin 2": "ZR2",
            "valjevo 3": "VA3",
            "vranje 4": "VR4",
            "kragujevac 2": "KG2",
            "kraljevo 3": "KR3",
            "pozega": "PO", "požega": "PO",
            "obrenovac": "OBR",
            "bajina basta": "BB", "bajina bašta": "BB",
            "derdap 1": "DJE1", "đerdap 1": "DJE1",
            "derdap 2": "DJE2", "đerdap 2": "DJE2",
            "drmno": "DRM",
            "mladost": "ML",
            # Susedni
            "svrljig": "SVRLJ", "svrljig": "SVRLJ",
            "pirot 1": "PI1",
            "pirot 2": "PI2",
            "prokuplje": "PROK",
            "aleksinac": "ALEKS",
            "knjazevac": "KNJAZ", "knjazevac": "KNJAZ",
            "kursumlia": "KURS", "kuršumlija": "KURS",
            "aleksandrovac": "ALEK",
            # PRP objekti
            "kosava": "KOŠ", "košava": "KOŠ",
            "alibunar": "ALI",
            "cibuk 1": "CIB1", "čibuk 1": "CIB1",
            "kovacica": "KOV", "kovačica": "KOV",
            "bor 4": "BO4",
            "bor 5": "BO5",
            "krivaca": "KRI", "krivača": "KRI",
            "veliki krivelj 2": "VK2",
            "zrenjanin": "ZR",
            "pancevo": "PRPPA", "pančevo": "PRPPA",
            # Susedni TS (dodatni)
            "vrsac 1": "VRS1", "vršac 1": "VRS1",
            "vrsac 2": "VRS2", "vršac 2": "VRS2",
            "debeljaca": "DEB", "debeljača": "DEB",
            "kacerevo": "KAC", "kačarevo": "KAC",
            "bela crkva": "BC",
            "pancevo 1": "PA1", "pančevo 1": "PA1",
            # TENT objekti
            "tent b": "TENTB",
            "tent a": "TENTA",
            "te kolubara": "TEKOL", "te kolubara": "TEKOL",
            # Strani
            "sofija zapad": "SOFIA_W",
            "kosovo b": "KOS_B",
            "koman": "KOMAN",
            "pec 3": "PEC3", "peć 3": "PEC3",
            "urosevac 2": "UROS2", "uroševac 2": "UROS2",
        }
        return base_map
    
    def _to_latin(self, text: str) -> str:
        """Konvertuj ćirilicu u latinicu."""
        try:
            return cyrtranslit.to_latin(text, "sr")
        except:
            return text
    
    @staticmethod
    def _strip_diacritics(text: str) -> str:
        """Skini dijakritike sa srpskih latiničnih slova.
        
        š→s, č→c, ć→c, ž→z, đ→dj
        Potrebno jer cyrtranslit zadržava dijakritike (uključeno, zaštita itd.)
        """
        replacements = {
            'š': 's', 'Š': 'S',
            'č': 'c', 'Č': 'C', 
            'ć': 'c', 'Ć': 'C',
            'ž': 'z', 'Ž': 'Z',
            'đ': 'dj', 'Đ': 'Dj',
        }
        for src, dst in replacements.items():
            text = text.replace(src, dst)
        return text
    
    def _extract_eeo_code(self, naziv: str) -> Optional[str]:
        """Izvuci kod EEO iz naziva."""
        naziv_lower = self._to_latin(naziv).lower().strip()
        
        # Direktni match - duži ključevi imaju prioritet ("nis 13" pre "nis 1")
        for full_name, code in sorted(self.eeo_code_map.items(), key=lambda x: len(x[0]), reverse=True):
            if full_name in naziv_lower:
                return code
        
        # Pattern matching za TS Xxx N format
        match = re.search(r"ts\s+(\w+)\s+(\d+)", naziv_lower)
        if match:
            ime = match.group(1)
            broj = match.group(2)
            # Skrati ime na 2-3 karaktera
            prefix = ime[:2].upper() if len(ime) >= 2 else ime.upper()
            return f"{prefix}{broj}"
        
        return None
    
    def _extract_voltage_from_context(self, text: str, default: int = 110) -> int:
        """Izvuci naponski nivo iz konteksta.
        
        Traži POSLEDNJU (najbližu DV-u) referencu na naponski nivo.
        """
        text_latin = self._to_latin(text).lower()
        
        # Nađi SVE reference na naponske nivoe i uzmi poslednju (najbližu DV-u)
        last_voltage = default
        last_pos = -1
        
        for voltage_str, voltage_val in [("400 kv", 400), ("400kv", 400),
                                           ("220 kv", 220), ("220kv", 220),
                                           ("110 kv", 110), ("110kv", 110),
                                           ("35 kv", 35), ("35kv", 35)]:
            pos = text_latin.rfind(voltage_str)
            if pos > last_pos:
                last_pos = pos
                last_voltage = voltage_val
        
        return last_voltage
    
    def parse_filename(self, filename: str) -> Optional[Dict]:
        """Parsiraj metadata iz naziva fajla."""
        filename_latin = self._to_latin(filename)
        
        # Kod može imati razmak (npr. "TENT B", "TENT A") - hvatamo sve do _YYYY
        code_pattern = r"[A-Za-zŠŽĐČĆšžđčć0-9][A-Za-zŠŽĐČĆšžđčć0-9 ]*[A-Za-zŠŽĐČĆšžđčć0-9]|[A-Za-zŠŽĐČĆšžđčć0-9]"
        
        # Pattern sa naponskim nivoima u nazivu
        # Podržava: "TS 400_220_110 kV Niš 2", "RP TENT B 400_220 kV", "TS 110_6,3 kV"
        # Tip može biti praćen opcionim nazivom pre napona (npr. "RP TENT B 400_220 kV")
        match = re.match(
            rf"[\d.]+\s*UP-({code_pattern})_(\d{{4}})\s+.+?(PRP|ПРП|[TР][SС]|[РR][ПP])\s+(?:[A-Za-zŠŽĐČĆšžđčć][A-Za-zŠŽĐČĆšžđčć0-9 ]*\s+)?(\d+(?:[/_,]\d+)*)\s*kV(?:\s+(.+?))?\.txt",
            filename_latin,
            re.IGNORECASE
        )
        
        if match:
            kod = match.group(1).replace(" ", "").upper()
            godina = int(match.group(2))
            tip_raw = match.group(3).upper()
            if tip_raw in ("TS", "ТС"):
                tip = "TS"
            elif tip_raw in ("PRP", "ПРП"):
                tip = "PRP"
            else:
                tip = "RP"
            naponi_str = match.group(4).replace("_", "/").replace(",", ".")
            # Filtriraj samo cele napone (ignoriši decimalne kao 6.3)
            naponi_parts = naponi_str.split("/")
            naponi = []
            for p in naponi_parts:
                try:
                    v = float(p)
                    if v == int(v):
                        naponi.append(int(v))
                    # else: decimalni napon (6.3 kV) - preskačemo za glavni naponski nivo
                except:
                    pass
            naponi = sorted(naponi, reverse=True)
            if not naponi:
                naponi = [110]  # fallback
            naziv = (match.group(5) or "").strip()
            
            full_name = f"{tip} {naponi_str} kV"
            if naziv:
                full_name += f" {naziv}"
            
            return {
                "kod": kod,
                "godina": godina,
                "tip": tip,
                "naponski_nivoi": naponi,
                "naziv": full_name
            }
        
        # Fallback: PRP/TS/RP bez naponskog nivoa u nazivu (npr. "PRP Bor 5.txt")
        match2 = re.match(
            rf"[\d.]+\s*UP-({code_pattern})_(\d{{4}})\s+.+?(PRP|ПРП|[TР][SС]|[РR][ПP])\s+(.+)\.txt",
            filename_latin,
            re.IGNORECASE
        )
        
        if match2:
            kod = match2.group(1).replace(" ", "").upper()
            godina = int(match2.group(2))
            tip_raw = match2.group(3).upper()
            if tip_raw in ("TS", "ТС"):
                tip = "TS"
            elif tip_raw in ("PRP", "ПРП"):
                tip = "PRP"
            else:
                tip = "RP"
            naziv = match2.group(4).strip()
            # Pokušaj izvući napon iz sadržaja fajla ili podrazumevaj 110kV
            naponi = [110]  # Default za PRP bez napona u nazivu
            
            return {
                "kod": kod,
                "godina": godina,
                "tip": tip,
                "naponski_nivoi": naponi,
                "naziv": f"{tip} {naziv}"
            }
        
        return None
    
    def parse_dalekovodi_all(self, text: str, eeo_naponi: List[int]) -> Dict[int, List[DalekovodInfo]]:
        """Parsiraj SVE dalekovode iz teksta, grupisane po naponskom nivou."""
        text_latin = self._to_latin(text)
        result = {napon: [] for napon in eeo_naponi}
        seen_dvs = set()
        
        # Pattern 1: "DV XXX sa TS YYY" iz sekcije 2
        pattern1 = re.compile(
            r"DV\s+(\d+(?:/\d+)?[A-Za-z]*)\s+(?:sa|ka|prema)\s+(?:TS\s+)?([^;,\n\(]+)",
            re.IGNORECASE
        )
        
        # Pattern 2: "DV XXX" u uklopnom stanju (sekcija 5+)
        pattern2 = re.compile(r"DV\s+(\d+(?:/\d+)?[A-Za-z]*)", re.IGNORECASE)
        
        # Iz sekcije 2 (explicitne veze sa destinacijama)
        for match in pattern1.finditer(text_latin):
            dv_broj = match.group(1).strip()
            dest_naziv = match.group(2).strip()
            
            # Odredi napon prema broju DV
            napon = self._guess_voltage_from_dv_number(dv_broj, eeo_naponi)
            
            dv_key = f"DV{dv_broj}"
            if dv_key not in seen_dvs:
                dv = DalekovodInfo(
                    oznaka=f"DV {dv_broj}",
                    broj=dv_broj,
                    destinacija_naziv=dest_naziv,
                    destinacija_kod=self._extract_eeo_code(dest_naziv),
                    napon_kv=napon
                )
                result[napon].append(dv)
                seen_dvs.add(dv_key)
        
        # Iz uklopnih stanja - samo brojevi bez destinacija
        sections = self._split_sections(text_latin)
        for section_num, section_text in sections.items():
            if int(section_num) >= 5:  # Uklopna stanja
                # Nađi naponski nivo iz konteksta
                for match in pattern2.finditer(section_text):
                    dv_broj = match.group(1).strip()
                    dv_key = f"DV{dv_broj}"
                    
                    if dv_key not in seen_dvs:
                        # Odredi napon
                        context_start = max(0, match.start() - 200)
                        context = section_text[context_start:match.start()]
                        napon = self._extract_voltage_from_context(context, 110)
                        
                        dv = DalekovodInfo(
                            oznaka=f"DV {dv_broj}",
                            broj=dv_broj,
                            napon_kv=napon
                        )
                        
                        if napon in result:
                            result[napon].append(dv)
                        seen_dvs.add(dv_key)
        
        return result
    
    def _guess_voltage_from_dv_number(self, dv_broj: str, naponi: List[int]) -> int:
        """Pogodi naponski nivo prema broju DV."""
        # Pravila za EMS:
        # 4xx - 400 kV
        # 2xx - 220 kV  
        # 1xxx ili 1xx - 110 kV
        try:
            num = int(re.match(r"(\d+)", dv_broj).group(1))
            if 400 <= num < 500:
                return 400
            elif 200 <= num < 300:
                return 220
            elif num < 200 or num >= 1000:
                return 110
        except:
            pass
        
        return naponi[-1] if naponi else 110  # Default najniži
    
    def parse_transformatori(self, text: str) -> List[TransformatorInfo]:
        """Parsiraj transformatore."""
        text_latin = self._to_latin(text)
        transformatori = []
        seen = set()
        
        # Pattern: "TR2 - 400/110 kV od 300 MVA"
        pattern = re.compile(
            r"TR(\d+)\s*[-–]\s*(\d+)/(\d+)\s*kV\s+(?:od\s+)?(\d+)\s*MVA",
            re.IGNORECASE
        )
        
        for match in pattern.finditer(text_latin):
            oznaka = f"TR{match.group(1)}"
            if oznaka in seen:
                continue
            
            tr = TransformatorInfo(
                oznaka=oznaka,
                vn_kv=int(match.group(2)),
                nn_kv=int(match.group(3)),
                snaga_mva=int(match.group(4))
            )
            
            # Proveri regulaciju
            context_end = min(len(text_latin), match.end() + 100)
            context = text_latin[match.start():context_end].lower()
            
            if "regulacija" in context:
                if "moguca" in context and "nije" not in context:
                    tr.ima_regulaciju = True
                elif "nije moguca" in context or "ne postoji" in context:
                    tr.ima_regulaciju = False
            
            transformatori.append(tr)
            seen.add(oznaka)
        
        return transformatori
    
    def parse_susedni_eeo(self, text: str) -> Dict[int, List[SusedniEEOInfo]]:
        """Parsiraj susedne EEO iz sekcije 4."""
        text_latin = self._to_latin(text)
        result = {400: [], 220: [], 110: []}
        
        sections = self._split_sections(text_latin)
        section4 = sections.get("4", "")
        
        if not section4:
            return result
        
        current_voltage = 400
        
        # Traži "Na strani XXX kV"
        lines = section4.split('\n')
        
        for i, line in enumerate(lines):
            line_lower = line.lower()
            
            # Promeni napon
            if "400 kv" in line_lower and "strani" in line_lower:
                current_voltage = 400
            elif "220 kv" in line_lower and "strani" in line_lower:
                current_voltage = 220
            elif "110 kv" in line_lower and "strani" in line_lower:
                current_voltage = 110
            
            # Nađi ## X.X. TS Naziv
            if line.strip().startswith("##") and "TS" in line:
                # Izvuci naziv TS
                match = re.search(r"TS\s+(.+)", line)
                if match:
                    ts_naziv = match.group(1).strip()
                    ts_kod = self._extract_eeo_code(ts_naziv)
                    
                    # Pročitaj sledeće linije za uklopno stanje
                    uklopno = []
                    for j in range(i+1, min(i+10, len(lines))):
                        if lines[j].strip().startswith("##") or lines[j].strip().startswith("###"):
                            break
                        uklopno.append(lines[j])
                    
                    susedni = SusedniEEOInfo(
                        kod=ts_kod or ts_naziv[:10],
                        naziv=f"TS {ts_naziv}",
                        napon_kv=current_voltage,
                        uklopno_stanje="\n".join(uklopno).strip()
                    )
                    
                    result[current_voltage].append(susedni)
        
        return result
    
    def parse_uklopna_stanja(self, text: str, eeo_naponi: List[int]) -> Dict[str, Dict[int, UklopnoStanje]]:
        """Parsiraj sva uklopna stanja iz sekcija 5, 6, 7..."""
        text_latin = self._to_latin(text)
        result = {}
        
        sections = self._split_sections(text_latin)
        
        # Mapiranje sekcija na nazive
        section_names = {
            "5": "normalno",
            "6": "bez_tr",
            "7": "bez_dzs"
        }
        
        for section_num, section_name in section_names.items():
            if section_num in sections:
                section_text = sections[section_num]
                stanja = {}
                
                for napon in eeo_naponi:
                    us = self._parse_uklopno_stanje_za_napon(section_text, napon)
                    if us:
                        us.naziv = section_name
                        stanja[napon] = us
                
                if stanja:
                    result[section_name] = stanja
        
        return result
    
    def _parse_uklopno_stanje_za_napon(self, section_text: str, napon_kv: int) -> Optional[UklopnoStanje]:
        """Parsiraj uklopno stanje za konkretan naponski nivo.
        
        Handles ALL busbar naming patterns found across TS files:
        - "GS 1 (ili GS 2) sistem sabirnica:" (NI2, BG3, KG2, KR3, PA2, SD3, etc.)
        - "1. (ili 2.) sistem sabirnica:" (BG5, BG8, ZR2, SM2, SA3, DJE2)
        - "1A/1B/2A/2B sistem sabirnica:" (BG5 110kV, OBR)
        - "GS 1A/GS 1B/GS 2A/GS 2B sistem sabirnica:" (OBR, ML)
        - "GS I / GS II sistem sabirnica:" (NS3 - Roman numerals)
        - "glavni sistem sabirnica:" (VA3, VR4, LE2, PO, JA4, BG20, DJE2, SO3)
        - "GS sistem sabirnica:" (NI2 220kV single busbar)
        - bare "sistem sabirnica:" (BB, SM2, KOS)
        """
        text_lower = self._strip_diacritics(section_text.lower())
        
        # Napravi fuzzy pattern za napon koji dozvoljava OCR razmake (npr. "11 0" umesto "110")
        napon_str = str(napon_kv)
        # Za svaki broj, dozvoli opcioni razmak između cifara: "110" -> "1\s*1\s*0"
        napon_fuzzy = r"\s*".join(napon_str)
        
        # Nađi sekciju za ovaj napon
        # "postrojenje" ili "postojenje" (česta OCR/tipografska greška - nedostaje "r")
        pattern = re.compile(
            rf"postr?ojenje\s+{napon_fuzzy}\s*kv(.+?)(?=postr?ojenje|\Z)",
            re.IGNORECASE | re.DOTALL
        )
        
        match = pattern.search(text_lower)
        if not match:
            return None
        
        napon_text = match.group(1)
        
        us = UklopnoStanje(napon_kv=napon_kv)
        
        # Find ALL "sistem sabirnica" declarations in this voltage section
        sb_pattern = re.compile(
            r'-?\s*(.{0,50}?)\bsistem\s*sabirnica\s*[:\s]+([^;\n]+)',
            re.IGNORECASE | re.MULTILINE
        )
        
        for m in sb_pattern.finditer(napon_text):
            prefix = m.group(1).strip().lower()
            field_text = m.group(2)
            fields = self._parse_polja_list(field_text)
            
            if not fields:
                continue
            
            gs = self._classify_busbar_prefix(prefix)
            
            if gs == 1:
                us.polja_gs1.extend(fields)
            elif gs == 2:
                us.polja_gs2.extend(fields)
            else:  # gs == 0: single/main busbar → treat as GS1
                us.polja_gs1.extend(fields)
        
        # Deduplicate while preserving order
        us.polja_gs1 = list(dict.fromkeys(us.polja_gs1))
        us.polja_gs2 = list(dict.fromkeys(us.polja_gs2))
        
        # Spojno polje
        if re.search(r"spojno\s+polje\s+(?:\d+\s*kv\s+)?(?:je\s+)?ukljuceno", napon_text):
            us.spojno_polje = "ukljuceno"
        elif re.search(r"poprecn\w+\s+spojn\w+\s+polj\w+\s+(?:\d+\s*kv\s+)?(?:je\s+)?ukljucen", napon_text):
            us.spojno_polje = "ukljuceno"
        elif "spojno polje" in napon_text and re.search(r"iskljuceno|rasklopljeno|rastavljeno", napon_text):
            us.spojno_polje = "iskljuceno"
        
        # DZS
        if "aktivna" in napon_text and "diferencijalna zastita" in napon_text:
            us.dzs_aktivna = True
        
        # Podužni rastavljač
        if "poduzni" in napon_text:
            if "ukljucen" in napon_text:
                us.poduzni_rastavljac = "ukljucen"
            elif "iskljucen" in napon_text:
                us.poduzni_rastavljac = "iskljucen"
        
        return us
    
    def _classify_busbar_prefix(self, prefix: str) -> int:
        """Classify busbar prefix → 1 (GS1), 2 (GS2), 0 (single/main).
        
        Handles: gs1, gs 1, gs i, 1., 1a, 1b, gs2, gs 2, gs ii, 2., 2a, 2b,
                 glavni, gs (alone), bare prefix, etc.
        """
        p = prefix.strip().lower()
        
        # Remove "(ili ...)" parenthetical to avoid false matches
        # e.g., "2. (ili 1.)" should classify as 2, not 1
        p_clean = re.sub(r'\(ili[^)]*\)', '', p).strip()
        
        # --- GS with explicit number ---
        # GS1, GS 1, GS1A, GS 1A, GS 1B
        if re.search(r'\bgs\s*1', p_clean):
            return 1
        if re.search(r'\bgs\s*2', p_clean):
            return 2
        
        # --- GS with Roman numerals: GS I, GS II ---
        if re.search(r'\bgs\s+ii\b', p_clean):
            return 2
        if re.search(r'\bgs\s+i\b', p_clean):
            return 1
        
        # --- Numbered without GS: "1.", "1 (", "1a", "1b" ---
        # After removing "(ili ...)" part, look for the leading number
        if re.search(r'(?:^|[\s-])1\s*[\.\s]', p_clean) or re.search(r'(?:^|[\s-])1[a-z]\b', p_clean):
            return 1
        if re.search(r'(?:^|[\s-])2\s*[\.\s]', p_clean) or re.search(r'(?:^|[\s-])2[a-z]\b', p_clean):
            return 2
        
        # --- Single busbar variants ---
        if 'glavni' in p or 'glavno' in p:
            return 0
        
        # "GS sistem sabirnica" (single GS, no number)
        if re.search(r'\bgs\s*$', p_clean):
            return 0
        
        # Bare "sistem sabirnica:" or "- sistem sabirnica:"
        return 0
    
    def _parse_polja_list(self, text: str) -> List[str]:
        """Parsiraj listu polja iz teksta.
        
        Handles: DV XXX, KB XXX, MV XXX, TR X, EVO/EVP entries.
        """
        polja = []
        text = text.strip()
        
        # Razdvoji po zarezi i "i"
        items = re.split(r"[,،]\s*|\s+i\s+|\s+и\s+", text)
        
        for item in items:
            item = item.strip()
            if not item:
                continue
            
            # DV XXX (dalekovod)
            dv_match = re.match(r"dv\s*(\d+(?:/\d+)?[a-z]*)", item, re.IGNORECASE)
            if dv_match:
                polja.append(f"DV{dv_match.group(1).upper()}")
                continue
            
            # KB XXX (kabel)
            kb_match = re.match(r"kb\s*(\d+(?:/\d+)?[a-z]*)", item, re.IGNORECASE)
            if kb_match:
                polja.append(f"KB{kb_match.group(1).upper()}")
                continue
            
            # MV XXX (merenje/veza)
            mv_match = re.match(r"mv\s*(\d+(?:/\d+)?[a-z]*)", item, re.IGNORECASE)
            if mv_match:
                polja.append(f"MV{mv_match.group(1).upper()}")
                continue
            
            # TR X (transformator) - direktno ili sa prefiksom "transformator"
            tr_match = re.match(r"(?:transformator\s+)?tr\s*(\d+)", item, re.IGNORECASE)
            if tr_match:
                polja.append(f"TR{tr_match.group(1)}")
                continue
            
            # Blok TR (za RP sa generatorima)
            blok_match = re.match(r"blok\s+tr\s*(\d+)", item, re.IGNORECASE)
            if blok_match:
                polja.append(f"TR{blok_match.group(1)}")
                continue
        
        return polja
    
    def _split_sections(self, text: str) -> Dict[str, str]:
        """Razdeli tekst na sekcije."""
        sections = {}
        pattern = re.compile(r"###\s*(\d+)\.?\s+(.+?)(?=###|\Z)", re.DOTALL)
        
        for match in pattern.finditer(text):
            section_num = match.group(1)
            section_content = match.group(2)
            sections[section_num] = section_content
        
        return sections
    
    def parse_file(self, filepath: Path) -> Optional[EEOParsedDataV2]:
        """Parsiraj ceo fajl uputstva."""
        if not filepath.exists():
            return None
        
        meta = self.parse_filename(filepath.name)
        if not meta:
            return None
        
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        content_latin = self._to_latin(content)
        
        data = EEOParsedDataV2(
            kod=meta["kod"],
            naziv=meta["naziv"],
            tip=meta["tip"],
            naponski_nivoi=meta["naponski_nivoi"],
            godina=meta["godina"]
        )
        
        # Sačuvaj raw tekst za fallback mapiranje
        data._raw_text_latin = content_latin
        
        # Parsiraj sve komponente
        data.dalekovodi = self.parse_dalekovodi_all(content_latin, data.naponski_nivoi)
        data.transformatori = self.parse_transformatori(content_latin)
        data.susedni_eeo = self.parse_susedni_eeo(content_latin)
        data.uklopna_stanja = self.parse_uklopna_stanja(content_latin, data.naponski_nivoi)
        
        # Dopuni DV destinacije iz susednih EEO (sekcija 4 + uklopna stanja susednih)
        self._map_dv_to_susedni(data)
        
        # Izgradi connectivity matricu
        data.connectivity = self._build_connectivity(data)
        
        return data
    
    def _build_connectivity(self, data: EEOParsedDataV2) -> List[Tuple[str, int, str, int, int]]:
        """Izgradi matricu povezanosti za ovaj EEO."""
        connectivity = []
        
        for napon, dvs in data.dalekovodi.items():
            for i, dv in enumerate(dvs, 1):
                if dv.destinacija_kod:
                    entry = (
                        data.kod,        # x - ovaj EEO
                        i,               # i - indeks DVP u ovom EEO
                        dv.destinacija_kod,  # y - drugi EEO
                        1,               # j - pretpostavka da je 1 na drugom kraju
                        napon            # naponski nivo
                    )
                    connectivity.append(entry)
        
        return connectivity

    def _map_dv_to_susedni(self, data: EEOParsedDataV2):
        """
        Mapira DV bez destinacija na susedne EEO koristeći uklopna stanja susednih.
        
        Logika: Ako susedni EEO (iz sekcije 4) u svom uklopnom stanju 
        pominje DV sa istim brojem, taj DV ide ka tom EEO.
        
        Primer: DV 113/1 nema destinaciju, ali TS Niš 1 u svom uklopnom stanju
        ima "DV 113/1" -> znači DV 113/1 ide ka NI1.
        """
        def normalize_dv(s: str) -> str:
            """Normalizuj DV oznaku za poređenje: ukloni razmake, uppercase."""
            return re.sub(r'\s+', '', s).upper()
        
        # Napravi mapu: DV_broj -> susedni EEO kod (iz uklopnih stanja susednih)
        dv_to_susedni: Dict[str, str] = {}
        
        for napon, susedni_list in data.susedni_eeo.items():
            for susedni in susedni_list:
                if not susedni.uklopno_stanje:
                    continue
                # Nađi sve DV u uklopnom stanju susednog
                for m in re.finditer(r"DV\s+(\d+(?:\s*/?\s*\d+)?(?:\s*[A-Za-z])?)", susedni.uklopno_stanje, re.IGNORECASE):
                    dv_raw = m.group(1).strip()
                    dv_key = normalize_dv(dv_raw)
                    if dv_key not in dv_to_susedni:
                        dv_to_susedni[dv_key] = susedni.kod
        
        # Dopuni destinacije DV koji ih nemaju
        unmapped_dvs = set()
        for napon, dvs in data.dalekovodi.items():
            for dv in dvs:
                if dv.destinacija_kod:
                    continue  # Već ima destinaciju
                
                # Normalizuj DV broj za poređenje
                dv_key = normalize_dv(dv.broj)
                
                if dv_key in dv_to_susedni:
                    dv.destinacija_kod = dv_to_susedni[dv_key]
                    dv.drugi_kraj_eeo = dv_to_susedni[dv_key]
                else:
                    unmapped_dvs.add(dv_key)
        
        # Fallback: sekcija 2 - "sa TS X ... (po DV Y)" ili "... DV Y ... TS X"
        if unmapped_dvs:
            self._map_dv_from_section2(data, unmapped_dvs)
    
    def _map_dv_from_section2(self, data: EEOParsedDataV2, unmapped_dvs: set):
        """Fallback: mapira nemapirane DV koristeći sekciju 2 teksta.
        
        Traži obrasce kao:
        - "sa TS Leskovac 2 ... DV 1278"
        - "paralelnom radu sa TS X ... (po DV Y)"
        - "preko DV 1278"
        """
        def normalize_dv(s: str) -> str:
            return re.sub(r'\s+', '', s).upper()
        
        raw_text = getattr(data, '_raw_text_latin', '')
        if not raw_text:
            return
        
        sections = self._split_sections(raw_text)
        section2 = sections.get("2", "")
        
        if section2:
            # Za svaki paragraf (razdvojen sa "- 2.XX"), traži TS i DV parove
            paragraphs = re.split(r'-\s*2\.\d+', section2)
            
            for para in paragraphs:
                # Nađi sve TS referencirane u paragrafu
                ts_matches = re.findall(r"(?:TS|ts)\s+([A-Za-zčćžšđČĆŽŠĐ]+(?:\s+\d+)?)", para)
                ts_codes = []
                for ts_name in ts_matches:
                    ts_name = ts_name.strip()
                    code = self._extract_eeo_code(ts_name)
                    if code and code != data.kod:
                        ts_codes.append(code)
                
                if not ts_codes:
                    continue
                
                # Nađi sve DV u paragrafu
                dv_matches = re.findall(r"DV\s+(\d+(?:\s*/?\s*\d+)?(?:\s*[A-Za-z])?)", para, re.IGNORECASE)
                
                for dv_raw in dv_matches:
                    dv_key = normalize_dv(dv_raw)
                    if dv_key in unmapped_dvs:
                        # Nađi najvažniji TS u paragrafu
                        # Uzmi prvi nakon "sa" ili "prema" ili poslednji pomenut
                        # Za "paralelnom radu sa TS X ... DV Y", X je destinacija
                        sa_match = re.search(
                            r"(?:sa|prema)\s+(?:TS\s+)?([A-Za-zčćžšđČĆŽŠĐ]+(?:\s+\d+)?)",
                            para, re.IGNORECASE
                        )
                        if sa_match:
                            code = self._extract_eeo_code(sa_match.group(1).strip())
                            if code and code != data.kod:
                                # Mapiraj
                                for napon, dvs in data.dalekovodi.items():
                                    for dv in dvs:
                                        if normalize_dv(dv.broj) == dv_key and not dv.destinacija_kod:
                                            dv.destinacija_kod = code
                                            dv.drugi_kraj_eeo = code
                                            unmapped_dvs.discard(dv_key)
        
        # Korak 2: Heuristika prefix matching za preostale
        for napon, dvs in data.dalekovodi.items():
            for dv in dvs:
                dv_key = normalize_dv(dv.broj)
                if dv_key not in unmapped_dvs or dv.destinacija_kod:
                    continue
                
                base_num = re.match(r'(\d+)', dv_key)
                if base_num:
                    base = base_num.group(1)
                    for napon2, dvs2 in data.dalekovodi.items():
                        for dv2 in dvs2:
                            if dv2.destinacija_kod and napon2 == napon:
                                dv2_base = re.match(r'(\d+)', normalize_dv(dv2.broj))
                                if dv2_base and dv2_base.group(1) == base:
                                    dv.destinacija_kod = dv2.destinacija_kod
                                    dv.drugi_kraj_eeo = dv2.destinacija_kod
                                    break
                        if dv.destinacija_kod:
                            break

    def parse_directory(self, dirpath: Path) -> List[EEOParsedDataV2]:
        """Parsiraj sve uputstva iz direktorijuma."""
        results = []
        
        for filepath in sorted(dirpath.glob("8.* UP-*.txt")):
            data = self.parse_file(filepath)
            if data:
                results.append(data)
        
        return results


# CLI
if __name__ == "__main__":
    import sys
    import json
    
    parser = UputstvoParserV2()
    
    if len(sys.argv) > 1:
        filepath = Path(sys.argv[1])
        data = parser.parse_file(filepath)
        
        if data:
            print(f"\n{'='*60}")
            print(f"EEO: {data.kod} - {data.naziv}")
            print(f"Tip: {data.tip}, Naponi: {data.naponski_nivoi}")
            print(f"{'='*60}")
            
            # DV po naponskom nivou
            print(f"\nDALEKOVODI:")
            for napon, dvs in data.dalekovodi.items():
                if dvs:
                    print(f"  {napon} kV ({len(dvs)}):")
                    for dv in dvs:
                        dest = dv.destinacija_kod or dv.destinacija_naziv or "?"
                        print(f"    - {dv.oznaka} -> {dest}")
            
            print(f"\nTRANSFORMATORI ({len(data.transformatori)}):")
            for tr in data.transformatori:
                reg = "✓" if tr.ima_regulaciju else "✗"
                print(f"  - {tr.oznaka}: {tr.vn_kv}/{tr.nn_kv} kV, {tr.snaga_mva} MVA, reg: {reg}")
            
            print(f"\nSUSEDNI EEO:")
            for napon, susedni in data.susedni_eeo.items():
                if susedni:
                    print(f"  {napon} kV:")
                    for s in susedni:
                        print(f"    - {s.kod}: {s.naziv}")
            
            print(f"\nUKLOPNA STANJA:")
            for naziv, stanja in data.uklopna_stanja.items():
                print(f"  {naziv}:")
                for napon, us in stanja.items():
                    sp = "SP:✓" if us.spojno_polje == "ukljuceno" else "SP:✗"
                    dzs = "DZS:✓" if us.dzs_aktivna else "DZS:✗"
                    print(f"    {napon}kV: GS1={len(us.polja_gs1)} GS2={len(us.polja_gs2)} {sp} {dzs}")
            
            print(f"\nMATRICA POVEZANOSTI ({len(data.connectivity)}):")
            for entry in data.connectivity[:10]:
                print(f"  {entry}")
        else:
            print("Parsiranje nije uspelo!")
    else:
        print("Korišćenje: python uputstvo_parser_v2.py <fajl>")
