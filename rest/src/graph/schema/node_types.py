"""
Definicije tipova čvorova (Node Types) prema metodologiji relejne zaštite.

Izvor: Metodologija Relejne zaštite - GridMind 15-02.md

Hijerarhija:
===========
Nivo 0: EEO (Elektroenergetski objekat) - TS, RP, PRP
Nivo 1: PO (Polje), ET (Energetski transformator), SS (Sistem sabirnica), UEEO (Uzemljenje)
Nivo 2: DVP, KBP, TRPVN, TRPNN, GSP, PSP | TR tipovi | GSS, PSS
Nivo 3: Naponski nivo (400, 220, 110, x kV)
Nivo 4: Konkretna instanca (DVP 400 kV 1, DVP 400 kV 2, ...)
Nivo 5: Osnovni elementi (P, SR, SMT, NMT, IRSU) - LISTOVI

Oprema van EEO:
==============
Nivo 1: VO (Vod)
Nivo 2: DV, KB, MV
Nivo 3: Naponski nivo
Nivo 4: DV 400 kV EEO x EEO y (koji EEO povezuje)
Nivo 5: DV 400 kV EEO x(m) EEO y(n) - konkretna polja
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field


# =============================================================================
# KONSTANTE
# =============================================================================

VOLTAGE_LEVELS = [400, 220, 110]  # kV nivoi u PS (x kV = distribucija)

FIELD_TYPES = ["DVP", "KBP", "TRPVN", "TRPNN", "GSP", "PSP"]

BUSBAR_TYPES = ["GSS", "PSS"]

ELEMENT_TYPES_RO = ["P", "SR", "IR", "IRSU", "OP"]  # Rasklopna oprema

ELEMENT_TYPES_MO = ["SMT", "NMT"]  # Merna oprema

BOUNDARY_ELEMENTS = ["IRSU", "SMT", "NMT", "OP"]  # Granični elementi (prelaz EEO → DV/KB)

LINE_TYPES = ["DV", "KB", "MV"]


# =============================================================================
# DATACLASS DEFINICIJE ČVOROVA
# =============================================================================

@dataclass
class EEONode:
    """
    Elektroenergetski objekat (TS, RP, PRP).
    
    Ovo je ROOT čvor za svu opremu koja pripada jednom objektu.
    """
    id: str                          # Jedinstveni identifikator (npr. "NI2", "BG5")
    name: str                        # Puno ime (npr. "TS 400/220/110 kV Niš 2")
    code: str                        # Skraćeni kod (npr. "NI2")
    type: str                        # Tip objekta: "TS", "RP", "PRP"
    voltage_levels: List[int]        # Lista naponskih nivoa [400, 220, 110]
    
    # Brojači elemenata po tipu i naponu (iz metodologije)
    n_dvp: Dict[int, int] = field(default_factory=dict)   # {400: 3, 220: 2, 110: 5}
    n_kbp: Dict[int, int] = field(default_factory=dict)
    n_trp: Dict[int, int] = field(default_factory=dict)
    n_gss: Dict[int, int] = field(default_factory=dict)
    n_pss: Dict[int, int] = field(default_factory=dict)
    n_gsp: Dict[int, int] = field(default_factory=dict)
    n_psp: Dict[int, int] = field(default_factory=dict)
    
    # Transformatori
    transformers: List[str] = field(default_factory=list)  # ["TR1", "TR2"]


@dataclass
class BusbarNode:
    """
    Sistem sabirnica (GSS ili PSS).
    
    Iz metodologije (Nivo 2 podele SS):
    - GSS sa pripadajućom opremom
    - PSS
    """
    id: str                  # "NI2_GSS_400_1" 
    eeo_id: str              # Pripadajući EEO
    type: str                # "GSS" ili "PSS"
    voltage_kv: int          # 400, 220, 110
    index: int               # Redni broj (1, 2, ...)
    
    # Elementi na sabirnici (reference)
    connected_fields: List[str] = field(default_factory=list)


@dataclass  
class FieldNode:
    """
    Polje (PO) - DVP, KBP, TRPVN, TRPNN, GSP, PSP.
    
    Iz metodologije (Nivo 2-4 podele PO):
    - DVP 400 kV 1, DVP 400 kV 2, ...
    """
    id: str                  # "NI2_DVP_400_1"
    eeo_id: str              # Pripadajući EEO
    type: str                # "DVP", "KBP", "TRPVN", "TRPNN", "GSP", "PSP"  
    voltage_kv: int          # 400, 220, 110
    index: int               # Redni broj polja na tom naponu
    
    # Za DVP/KBP - ime voda koji izlazi
    line_name: Optional[str] = None      # "DV Niš-Leskovac"
    line_id: Optional[str] = None        # "DV_NI2_LE2_400"
    
    # Indeks GSS na koju je polje priključeno (1 ili 2)
    gss_index: Optional[int] = None
    
    # Za TRP - povezani transformator
    transformer_id: Optional[str] = None  # "NI2_TR1"
    
    # Za GSP/PSP - koje sabirnice povezuje
    connects_busbars: List[str] = field(default_factory=list)


@dataclass
class ElementNode:
    """
    Osnovni element (LIST stabla) - P, SR, IRSU, SMT, NMT.
    
    Iz metodologije (Nivo 5 - listovi):
    - SR DVP 400 kV i GSS j
    - P DVP 400 kV i
    - SMT DVP 400 kV i
    - IRSU DVP 400 kV i
    - NMT DVP 400 kV i
    """
    id: str                  # "NI2_DVP_400_1_P"
    eeo_id: str              # Pripadajući EEO
    field_id: str            # Pripadajuće polje
    type: str                # "P", "SR", "IRSU", "SMT", "NMT"
    voltage_kv: int          # 400, 220, 110
    
    # Za SR - na koju sabirnicu je vezan
    connected_busbar: Optional[str] = None  # "GSS_1" ili "PSS_1"
    connected_busbar_id: Optional[str] = None  # "NI2_GSS_400_1"
    
    # Status uklopnog stanja (samo za RO)
    # s(element) ∈ {0, 1} - 1=uključen, 0=isključen
    status: Optional[int] = None  # None za MO (SMT, NMT)
    
    # Da li je granični element
    is_boundary: bool = False


@dataclass
class TransformerNode:
    """
    Energetski transformator (ET).
    
    Iz metodologije (Nivo 2 podele ET):
    - TR 400/220 kV/kV
    - TR 400/110 kV/kV
    - itd.
    """
    id: str                  # "NI2_TR1"
    eeo_id: str              # Pripadajući EEO
    name: str                # "TR1", "TR2"
    vn_kv: int               # Viši napon (400, 220)
    nn_kv: int               # Niži napon (220, 110, x)
    index: int               # Redni broj
    
    # Povezana polja
    trpvn_field_id: Optional[str] = None  # Polje na višem naponu
    trpnn_field_id: Optional[str] = None  # Polje na nižem naponu
    
    # Tehnički podaci
    power_mva: Optional[float] = None
    

@dataclass
class LineNode:
    """
    Vod (DV, KB, MV) - oprema VAN EEO.
    
    Iz metodologije (Oprema koja ne pripada EEO):
    - DV 400 kV EEO x(m) EEO y(n)
    - Četvorka (x, m, y, n) određuje vod
    """
    id: str                  # "DV_NI2_LE2_400"
    type: str                # "DV", "KB", "MV"
    name: str                # "DV Niš-Leskovac"
    voltage_kv: int          # 400, 220, 110
    
    # Krajevi voda (EEO i polja)
    from_eeo_id: str         # "NI2"
    from_field_id: str       # "NI2_DVP_400_1"
    from_field_index: int    # m iz četvorke
    
    to_eeo_id: str           # "LE2"
    to_field_id: str         # "LE2_DVP_400_1"
    to_field_index: int      # n iz četvorke
    
    # Za MV - tip kombinacije
    mv_type: Optional[str] = None  # "DV+KB" ili "KB+DV"
    
    # Tehnički podaci
    length_km: Optional[float] = None


# =============================================================================
# NODE_TYPES REGISTRY
# =============================================================================

NODE_TYPES = {
    # === OPREMA KOJA PRIPADA EEO ===
    
    "EEO": {
        "class": EEONode,
        "description": "Elektroenergetski objekat (TS, RP, PRP)",
        "level": 0,
        "attrs": ["id", "name", "code", "type", "voltage_levels"],
    },
    
    "GSS": {
        "class": BusbarNode,
        "description": "Glavni sistem sabirnica",
        "level": 1,
        "parent": "EEO",
        "attrs": ["id", "eeo_id", "type", "voltage_kv", "index"],
    },
    
    "PSS": {
        "class": BusbarNode,
        "description": "Pomoćni sistem sabirnica", 
        "level": 1,
        "parent": "EEO",
        "attrs": ["id", "eeo_id", "type", "voltage_kv", "index"],
    },
    
    "DVP": {
        "class": FieldNode,
        "description": "Dalekovodno polje",
        "level": 2,
        "parent": "EEO",
        "attrs": ["id", "eeo_id", "type", "voltage_kv", "index", "line_name"],
    },
    
    "KBP": {
        "class": FieldNode,
        "description": "Kablovsko polje",
        "level": 2,
        "parent": "EEO",
        "attrs": ["id", "eeo_id", "type", "voltage_kv", "index", "line_name"],
    },
    
    "TRPVN": {
        "class": FieldNode,
        "description": "Transformatorsko polje - viši napon",
        "level": 2,
        "parent": "EEO",
        "attrs": ["id", "eeo_id", "type", "voltage_kv", "index", "transformer_id"],
    },
    
    "TRPNN": {
        "class": FieldNode,
        "description": "Transformatorsko polje - niži napon",
        "level": 2,
        "parent": "EEO", 
        "attrs": ["id", "eeo_id", "type", "voltage_kv", "index", "transformer_id"],
    },
    
    "GSP": {
        "class": FieldNode,
        "description": "Glavno spojno polje",
        "level": 2,
        "parent": "EEO",
        "attrs": ["id", "eeo_id", "type", "voltage_kv", "index", "connects_busbars"],
    },
    
    "PSP": {
        "class": FieldNode,
        "description": "Pomoćno spojno polje",
        "level": 2,
        "parent": "EEO",
        "attrs": ["id", "eeo_id", "type", "voltage_kv", "index", "connects_busbars"],
    },
    
    "TR": {
        "class": TransformerNode,
        "description": "Energetski transformator",
        "level": 1,
        "parent": "EEO",
        "attrs": ["id", "eeo_id", "name", "vn_kv", "nn_kv", "index"],
    },
    
    # Osnovni elementi (LISTOVI)
    "P": {
        "class": ElementNode,
        "description": "Prekidač",
        "level": 3,
        "parent": "FIELD",  # DVP, KBP, TRPVN, TRPNN, GSP, PSP
        "is_ro": True,      # Rasklopna oprema
        "has_status": True,
        "attrs": ["id", "eeo_id", "field_id", "type", "voltage_kv", "status"],
    },
    
    "SR": {
        "class": ElementNode,
        "description": "Sabirnički rastavljač",
        "level": 3,
        "parent": "FIELD",
        "is_ro": True,
        "has_status": True,
        "attrs": ["id", "eeo_id", "field_id", "type", "voltage_kv", "status", "connected_busbar"],
    },
    
    "IR": {
        "class": ElementNode,
        "description": "Izlazni rastavljač (linijski)",
        "level": 3,
        "parent": "FIELD",
        "is_ro": True,
        "has_status": True,
        "attrs": ["id", "eeo_id", "field_id", "type", "voltage_kv", "status"],
    },
    
    "IRSU": {
        "class": ElementNode,
        "description": "Izlazni rastavljač sa sistemskim uzemljenjem (GRANIČNI)",
        "level": 3,
        "parent": "FIELD",
        "is_ro": True,
        "has_status": True,
        "is_boundary": True,  # Granični element
        "attrs": ["id", "eeo_id", "field_id", "type", "voltage_kv", "status", "is_boundary"],
    },
    
    "SMT": {
        "class": ElementNode,
        "description": "Strujni merni transformator (GRANIČNI)",
        "level": 3,
        "parent": "FIELD",
        "is_ro": False,       # Merna oprema
        "has_status": False,
        "is_boundary": True,
        "attrs": ["id", "eeo_id", "field_id", "type", "voltage_kv", "is_boundary"],
    },
    
    "NMT": {
        "class": ElementNode,
        "description": "Naponski merni transformator (GRANIČNI)",
        "level": 3,
        "parent": "FIELD",
        "is_ro": False,
        "has_status": False,
        "is_boundary": True,
        "attrs": ["id", "eeo_id", "field_id", "type", "voltage_kv", "is_boundary"],
    },
    
    "OP": {
        "class": ElementNode,
        "description": "Uzemljivač / zaštitna oprema (ZO)",
        "level": 3,
        "parent": "FIELD",
        "is_ro": True,
        "has_status": True,
        "is_boundary": True,
        "attrs": ["id", "eeo_id", "field_id", "type", "voltage_kv", "status", "is_boundary"],
    },
    
    # === OPREMA KOJA NE PRIPADA EEO (VODOVI) ===
    
    "DV": {
        "class": LineNode,
        "description": "Dalekovod",
        "level": 0,
        "parent": None,  # Ne pripada nijednom EEO
        "attrs": ["id", "name", "type", "voltage_kv", "from_eeo_id", "to_eeo_id"],
    },
    
    "KB": {
        "class": LineNode,
        "description": "Kabal",
        "level": 0,
        "parent": None,
        "attrs": ["id", "name", "type", "voltage_kv", "from_eeo_id", "to_eeo_id"],
    },
    
    "MV": {
        "class": LineNode,
        "description": "Mešoviti vod (DV+KB ili KB+DV)",
        "level": 0,
        "parent": None,
        "attrs": ["id", "name", "type", "voltage_kv", "from_eeo_id", "to_eeo_id", "mv_type"],
    },
}


# =============================================================================
# HELPER FUNKCIJE
# =============================================================================

def get_node_type_info(node_type: str) -> Dict[str, Any]:
    """Vraća informacije o tipu čvora."""
    return NODE_TYPES.get(node_type, {})


def is_boundary_element(node_type: str) -> bool:
    """Da li je element granični (prelaz EEO → DV/KB)?"""
    return NODE_TYPES.get(node_type, {}).get("is_boundary", False)


def is_switchgear(node_type: str) -> bool:
    """Da li je element rasklopna oprema (ima status)?"""
    return NODE_TYPES.get(node_type, {}).get("is_ro", False)


def get_field_types() -> List[str]:
    """Vraća listu tipova polja."""
    return FIELD_TYPES


def get_voltage_levels() -> List[int]:
    """Vraća listu naponskih nivoa PS."""
    return VOLTAGE_LEVELS
