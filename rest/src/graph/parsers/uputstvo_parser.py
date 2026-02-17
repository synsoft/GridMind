#!/usr/bin/env python3
"""
Parser za Uputstva za pogon TS/RP.

Izvlači strukturirane podatke iz .txt fajlova:
- Metadata EEO (naziv, kod, naponski nivoi)
- Dalekovodi i njihove destinacije
- Transformatori
- Uklopna stanja po naponskim nivoima
"""

import re
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional
import cyrtranslit


@dataclass
class DalekovodInfo:
    """Informacije o dalekovodu."""
    oznaka: str  # npr. "DV 403"
    destinacija_kod: Optional[str] = None  # npr. "BOR2"
    destinacija_naziv: Optional[str] = None  # npr. "TS Bor 2"
    napon_kv: Optional[int] = None


@dataclass
class TransformatorInfo:
    """Informacije o transformatoru."""
    oznaka: str  # npr. "TR2"
    vn_kv: int  # viši napon
    nn_kv: int  # niži napon
    snaga_mva: Optional[int] = None
    ima_regulaciju: bool = False
    napomena: Optional[str] = None


@dataclass
class UklopnoStanjePolje:
    """Polje u uklopnom stanju."""
    tip: str  # "DV", "TR", "SP"
    oznaka: str
    sistem_sabirnica: int  # 1 ili 2
    status: str  # "ukljucen", "iskljucen", "raskloplјen"


@dataclass
class UklopnoStanje:
    """Uklopno stanje za jedan naponski nivo."""
    napon_kv: int
    polja_gs1: list[str] = field(default_factory=list)
    polja_gs2: list[str] = field(default_factory=list)
    spojno_polje_status: str = "nepoznato"
    dzs_aktivna: bool = False
    napomene: list[str] = field(default_factory=list)


@dataclass
class EEOParsedData:
    """Parsirani podaci za jedan EEO."""
    kod: str
    naziv: str
    tip: str  # "TS" ili "RP"
    naponski_nivoi: list[int]
    godina: Optional[int] = None
    
    dalekovodi: list[DalekovodInfo] = field(default_factory=list)
    transformatori: list[TransformatorInfo] = field(default_factory=list)
    uklopna_stanja: dict[str, UklopnoStanje] = field(default_factory=dict)
    # kljuc = "normalno", "bez_dzs_400", "bez_dzs_110", "bez_tr"...
    
    susedni_eeo: list[str] = field(default_factory=list)
    raw_sections: dict[str, str] = field(default_factory=dict)


class UputstvoParser:
    """Parser za Uputstva za pogon."""
    
    # Regex paterni za ćirilicu
    FILENAME_PATTERN = re.compile(
        r"UP-([A-Z0-9]+)_(\d{4})\s+Uputstvo za pogon\s+(.+)\.txt",
        re.IGNORECASE
    )
    
    # DV veza: "ДВ 403 sa/sa TS Bor 2" ili "DV 403 ka TS Bor 2"
    DV_VEZA_PATTERN = re.compile(
        r"[ДD][ВV]\s*(\d+/?[АA-ZА-Я0-9]*)\s+(?:sa|ka|prema|с[аa])\s+([TТ][SС]\s+)?(.+?)(?:[;,\.]|$)",
        re.IGNORECASE
    )
    
    # Transformator: "ТР2 - 400/110 kV od 300 MVA"
    TR_PATTERN = re.compile(
        r"[TТ][РR](\d+)\s*[-–]\s*(\d+)/(\d+)\s*kV\s+(?:od|од)\s+(\d+)\s*MVA",
        re.IGNORECASE
    )
    
    # Naponski nivo iz naziva: "TS 400/220/110 kV"
    NAPON_NIVOI_PATTERN = re.compile(
        r"(\d+(?:/\d+)+)\s*kV",
        re.IGNORECASE
    )
    
    # EEO kod iz teksta
    EEO_KOD_PATTERN = re.compile(
        r"[TТ][SС]\s+([A-ZА-Я][a-zа-я]+(?:\s+\d+)?)",
        re.IGNORECASE
    )
    
    def __init__(self):
        self.eeo_code_map = self._build_eeo_code_map()
    
    def _build_eeo_code_map(self) -> dict[str, str]:
        """Mapa punih naziva na kodove EEO."""
        return {
            "nis 2": "NI2", "niš 2": "NI2",
            "leskovac 2": "LE2",
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
            "sofija zapad": "SOFIA_W",
            "kosovo b": "KOS_B",
        }
    
    def _to_latin(self, text: str) -> str:
        """Konvertuj ćirilicu u latinicu."""
        return cyrtranslit.to_latin(text, "sr")
    
    def _extract_eeo_code(self, naziv: str) -> Optional[str]:
        """Izvuci kod EEO iz naziva."""
        naziv_lower = naziv.lower().strip()
        for full_name, code in self.eeo_code_map.items():
            if full_name in naziv_lower:
                return code
        return None
    
    def parse_filename(self, filename: str) -> Optional[dict]:
        """Parsiraj metadata iz naziva fajla."""
        # Konvertuj u latinicu ako treba
        filename_latin = self._to_latin(filename)
        
        # Format: "8.20 UP-NI2_2022 Uputstvo za pogon TS 400_220_110 kV Niš 2.txt"
        match = re.match(
            r"[\d.]+\s*UP-([A-Z0-9]+)_(\d{4})\s+.+?([TР][SС]|[РR][ПP])\s+(\d+(?:[/_]\d+)*)\s*kV\s+(.+)\.txt",
            filename_latin,
            re.IGNORECASE
        )
        
        if match:
            kod = match.group(1)
            godina = int(match.group(2))
            tip = "TS" if match.group(3).upper() in ("TS", "ТС") else "RP"
            naponi_str = match.group(4).replace("_", "/")
            naponi = sorted([int(n) for n in naponi_str.split("/")], reverse=True)
            naziv = match.group(5).strip()
            
            return {
                "kod": kod,
                "godina": godina,
                "tip": tip,
                "naponski_nivoi": naponi,
                "naziv": f"{tip} {naponi_str} kV {naziv}"
            }
        
        return None
    
    def parse_dalekovodi(self, text: str) -> list[DalekovodInfo]:
        """Parsiraj informacije o dalekovodima."""
        text_latin = self._to_latin(text)
        dalekovodi = []
        
        # Pattern za "DV XXX sa TS YYY"
        pattern = re.compile(
            r"DV\s+(\d+(?:/\d+)?[A-Z]*)\s+(?:sa|ka|prema)\s+(?:TS\s+)?(.+?)(?:[;,\(\)]|\s+и\s+|\s+i\s+|$)",
            re.IGNORECASE
        )
        
        for match in pattern.finditer(text_latin):
            oznaka = f"DV {match.group(1)}"
            dest_naziv = match.group(2).strip()
            dest_kod = self._extract_eeo_code(dest_naziv)
            
            dv = DalekovodInfo(
                oznaka=oznaka,
                destinacija_naziv=dest_naziv,
                destinacija_kod=dest_kod
            )
            
            # Izbegni duplikate
            if not any(d.oznaka == dv.oznaka for d in dalekovodi):
                dalekovodi.append(dv)
        
        return dalekovodi
    
    def parse_transformatori(self, text: str) -> list[TransformatorInfo]:
        """Parsiraj informacije o transformatorima."""
        text_latin = self._to_latin(text)
        transformatori = []
        
        # Pattern: "TR2 - 400/110 kV od 300 MVA"
        pattern = re.compile(
            r"TR(\d+)\s*[-–]\s*(\d+)/(\d+)\s*kV\s+(?:od\s+)?(\d+)\s*MVA(?:\s*\(([^)]+)\))?",
            re.IGNORECASE
        )
        
        for match in pattern.finditer(text_latin):
            tr = TransformatorInfo(
                oznaka=f"TR{match.group(1)}",
                vn_kv=int(match.group(2)),
                nn_kv=int(match.group(3)),
                snaga_mva=int(match.group(4)),
                napomena=match.group(5) if match.group(5) else None
            )
            
            # Proveri regulaciju
            context_start = max(0, match.start() - 50)
            context_end = min(len(text_latin), match.end() + 100)
            context = text_latin[context_start:context_end].lower()
            
            if "regulacija napona" in context:
                tr.ima_regulaciju = "nije moguca" not in context and "ne postoji" not in context
            
            if not any(t.oznaka == tr.oznaka for t in transformatori):
                transformatori.append(tr)
        
        return transformatori
    
    def parse_uklopno_stanje(self, text: str, napon_kv: int) -> UklopnoStanje:
        """Parsiraj uklopno stanje za naponski nivo."""
        text_latin = self._to_latin(text).lower()
        
        us = UklopnoStanje(napon_kv=napon_kv)
        
        # Pattern za GS 1 sistem: "GS 1 sistem sabirnica: DV X, DV Y, TR1"
        gs1_pattern = re.compile(
            r"gs\s*1\s*(?:\(ili\s*gs\s*2\))?\s*sistem\s*sabirnica[:\s]+([^;]+?)(?:;|gs\s*2|$)",
            re.IGNORECASE | re.DOTALL
        )
        gs2_pattern = re.compile(
            r"gs\s*2\s*(?:\(ili\s*gs\s*1\))?\s*sistem\s*sabirnica[:\s]+([^;]+?)(?:;|spojno|$)",
            re.IGNORECASE | re.DOTALL
        )
        
        gs1_match = gs1_pattern.search(text_latin)
        gs2_match = gs2_pattern.search(text_latin)
        
        if gs1_match:
            polja_str = gs1_match.group(1)
            us.polja_gs1 = self._parse_polja_list(polja_str)
        
        if gs2_match:
            polja_str = gs2_match.group(1)
            us.polja_gs2 = self._parse_polja_list(polja_str)
        
        # Spojno polje
        if "spojno polje je ukljuceno" in text_latin or "spojno polje ukljuceno" in text_latin:
            us.spojno_polje_status = "ukljuceno"
        elif "spojno polje iskljuceno" in text_latin or "spojno polje je iskljuceno" in text_latin:
            us.spojno_polje_status = "iskljuceno"
        
        # DZS
        if "aktivna je diferencijalna zastita" in text_latin:
            us.dzs_aktivna = True
        
        return us
    
    def _parse_polja_list(self, text: str) -> list[str]:
        """Parsiraj listu polja iz teksta."""
        polja = []
        
        # Razdvoji po zarezi
        items = re.split(r"[,،](?:\s*i\s*|\s*и\s*|\s+)", text)
        
        for item in items:
            item = item.strip()
            
            # DV XXX
            dv_match = re.match(r"dv\s*(\d+(?:/\d+)?[a-z]*)", item, re.IGNORECASE)
            if dv_match:
                polja.append(f"DV{dv_match.group(1).upper()}")
                continue
            
            # TR X
            tr_match = re.match(r"tr\s*(\d+)", item, re.IGNORECASE)
            if tr_match:
                polja.append(f"TR{tr_match.group(1)}")
                continue
            
            # Ili direktno ako ima format
            if re.match(r"[a-z]+\d+", item, re.IGNORECASE):
                polja.append(item.upper().replace(" ", ""))
        
        return polja
    
    def parse_file(self, filepath: Path) -> Optional[EEOParsedData]:
        """Parsiraj ceo fajl uputstva."""
        if not filepath.exists():
            return None
        
        # Parsiraj filename
        meta = self.parse_filename(filepath.name)
        if not meta:
            # Pokušaj izvući bar osnovne podatke
            return None
        
        # Učitaj sadržaj
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        content_latin = self._to_latin(content)
        
        # Kreiraj rezultat
        data = EEOParsedData(
            kod=meta["kod"],
            naziv=meta["naziv"],
            tip=meta["tip"],
            naponski_nivoi=meta["naponski_nivoi"],
            godina=meta["godina"]
        )
        
        # Parsiraj dalekovode
        data.dalekovodi = self.parse_dalekovodi(content_latin)
        
        # Parsiraj transformatore
        data.transformatori = self.parse_transformatori(content_latin)
        
        # Izvuci susedne EEO iz destinacija DV
        for dv in data.dalekovodi:
            if dv.destinacija_kod and dv.destinacija_kod not in data.susedni_eeo:
                data.susedni_eeo.append(dv.destinacija_kod)
        
        # Parsiraj sekcije za uklopna stanja
        sections = self._split_sections(content_latin)
        data.raw_sections = sections
        
        # Normalno uklopno stanje (sekcija 5)
        if "5" in sections:
            for napon in data.naponski_nivoi:
                # Nađi deo za taj napon
                napon_section = self._find_napon_section(sections["5"], napon)
                if napon_section:
                    us = self.parse_uklopno_stanje(napon_section, napon)
                    data.uklopna_stanja[f"normalno_{napon}kV"] = us
        
        return data
    
    def _split_sections(self, text: str) -> dict[str, str]:
        """Razdeli tekst na sekcije po ### naslovima."""
        sections = {}
        
        # Pattern za sekcije: ### X. NASLOV
        pattern = re.compile(r"###\s*(\d+)\.?\s+(.+?)(?=###|\Z)", re.DOTALL)
        
        for match in pattern.finditer(text):
            section_num = match.group(1)
            section_content = match.group(2)
            sections[section_num] = section_content
        
        return sections
    
    def _find_napon_section(self, section_text: str, napon_kv: int) -> Optional[str]:
        """Nađi deo sekcije za određeni naponski nivo."""
        # Pattern: "## X.Y Postrojenje XXX kV"
        pattern = re.compile(
            rf"##\s*\d+\.\d+\s+Postrojenje\s+{napon_kv}\s*kV(.+?)(?=##|\Z)",
            re.DOTALL | re.IGNORECASE
        )
        
        match = pattern.search(section_text)
        if match:
            return match.group(1)
        
        return None
    
    def parse_directory(self, dirpath: Path) -> list[EEOParsedData]:
        """Parsiraj sve uputstva iz direktorijuma."""
        results = []
        
        for filepath in sorted(dirpath.glob("8.* UP-*.txt")):
            data = self.parse_file(filepath)
            if data:
                results.append(data)
        
        return results


# CLI za testiranje
if __name__ == "__main__":
    import sys
    from pprint import pprint
    
    parser = UputstvoParser()
    
    if len(sys.argv) > 1:
        filepath = Path(sys.argv[1])
        data = parser.parse_file(filepath)
        if data:
            print(f"\n{'=' * 60}")
            print(f"EEO: {data.kod} - {data.naziv}")
            print(f"Tip: {data.tip}, Naponi: {data.naponski_nivoi} kV")
            print(f"{'=' * 60}")
            
            print(f"\nDalekovodi ({len(data.dalekovodi)}):")
            for dv in data.dalekovodi:
                print(f"  - {dv.oznaka} -> {dv.destinacija_kod or dv.destinacija_naziv}")
            
            print(f"\nTransformatori ({len(data.transformatori)}):")
            for tr in data.transformatori:
                print(f"  - {tr.oznaka}: {tr.vn_kv}/{tr.nn_kv} kV, {tr.snaga_mva} MVA")
            
            print(f"\nSusedni EEO: {data.susedni_eeo}")
            
            print(f"\nUklopna stanja:")
            for key, us in data.uklopna_stanja.items():
                print(f"  {key}:")
                print(f"    GS1: {us.polja_gs1}")
                print(f"    GS2: {us.polja_gs2}")
                print(f"    SP: {us.spojno_polje_status}, DZS: {us.dzs_aktivna}")
        else:
            print("Nije uspelo parsiranje!")
    else:
        print("Korišćenje: python uputstvo_parser.py <putanja_do_fajla>")
