"""
Definicije tipova ivica (Edge Types) prema metodologiji relejne zaštite.

Izvor: Metodologija Relejne zaštite - GridMind 15-02.md

Tipovi veza:
============
1. GALVANSKA VEZA - fizička električna veza između elemenata unutar EEO
   - GSS <-> SR <-> P <-> SMT <-> IRSU
   - Metodologija koristi notaciju: "prethodnik <-> osnovni element <-> sledbenik"

2. HIJERARHIJSKE VEZE - pripadnost entiteta
   - EEO SADRZI Polje
   - Polje SADRZI Element
   
3. MEĐUOBJEKTNE VEZE - veze između različitih EEO
   - IRSU (EEO1) -> DV -> IRSU (EEO2)
   - Opisane matricom povezanosti
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from enum import Enum


class EdgeDirection(Enum):
    """Smer ivice u grafu."""
    UNDIRECTED = "undirected"  # Galvanske veze (bidirekcione)
    DIRECTED = "directed"      # Hijerarhijske veze (jednosmerne)


# =============================================================================
# DATACLASS DEFINICIJE IVICA
# =============================================================================

@dataclass
class GalvanskiVezanEdge:
    """
    Galvanska veza između dva elementa unutar EEO.
    
    Iz metodologije (sekcija 2876):
    "prethodnik <-> galvanska veza <-> osnovni element <-> galvanska veza <-> sledbenik"
    
    Ova veza znači da postoji fizički provodnik između elemenata.
    Ako je RO isključena, tok struje je prekinut.
    """
    source_id: str           # ID prethodnika
    target_id: str           # ID sledbenika
    
    # Uslov postojanja (iz metodologije)
    # npr. "n_PSS 400 kV = 0" - veza postoji samo ako nema PSS
    condition: Optional[str] = None


@dataclass
class SadrziEdge:
    """
    Hijerarhijska veza - roditelj SADRŽI dete.
    
    Primeri:
    - EEO SADRZI GSS
    - EEO SADRZI DVP
    - DVP SADRZI P
    """
    parent_id: str           # ID roditelja (EEO, Polje)
    child_id: str            # ID deteta (Polje, Element)


@dataclass
class PripadaEdge:
    """
    Inverzna hijerarhijska veza - dete PRIPADA roditelju.
    
    Primeri:
    - P PRIPADA DVP
    - DVP PRIPADA EEO
    """
    child_id: str
    parent_id: str


@dataclass
class PovezujeEdge:
    """
    Veza između graničnog elementa i voda (DV/KB).
    
    Iz metodologije: Granični elementi (IRSU, SMT, NMT) su tačke
    gde oprema iz EEO prelazi u opremu van EEO.
    
    IRSU (EEO1) --POVEZUJE--> DV --POVEZUJE--> IRSU (EEO2)
    """
    element_id: str          # ID graničnog elementa (IRSU)
    line_id: str             # ID voda (DV, KB)
    side: str                # "from" ili "to"


@dataclass
class NapajaEdge:
    """
    Veza napajanja - pokazuje smer toka energije.
    
    Koristi se za analizu: koji elementi ostaju napojeni
    ako se određeni element isključi.
    """
    source_id: str           # ID izvora napajanja
    target_id: str           # ID elementa koji se napaja


# =============================================================================
# DEFINICIJE LANACA VEZA UNUTAR POLJA
# =============================================================================

# Iz metodologije (sekcija 2924+): Prethodnici i sledbenici osnovnih elemenata

# DVP lanac (bez PSS)
DVP_CHAIN_NO_PSS = [
    ("GSS", "SR"),      # GSS 400 kV j <-> SR DVP 400 kV i GSS j
    ("SR", "P"),        # SR DVP 400 kV i GSS j <-> P DVP 400 kV i
    ("P", "SMT"),       # P DVP 400 kV i <-> SMT DVP 400 kV i
    ("SMT", "IRSU"),    # SMT DVP 400 kV i <-> IRSU DVP 400 kV i
    ("IRSU", "NMT"),    # IRSU DVP 400 kV i <-> NMT DVP 400 kV i (grana)
    ("IRSU", "KRAJ"),   # IRSU DVP 400 kV i <-> kraj (granica ka DV)
]

# DVP lanac (sa PSS)
DVP_CHAIN_WITH_PSS = [
    ("GSS", "SR_GSS"),      # GSS <-> SR ka GSS
    ("SR_GSS", "P"),        # SR GSS <-> P
    ("P", "IRSU"),          # P <-> IRSU
    ("IRSU", "SR_PSS"),     # IRSU <-> SR ka PSS (grana)
    ("IRSU", "SMT"),        # IRSU <-> SMT
    ("PSS", "SR_PSS"),      # PSS <-> SR ka PSS
    ("SR_PSS", "SMT"),      # SR PSS <-> SMT (grana)
    ("SMT", "NMT"),         # SMT <-> NMT
    ("SMT", "KRAJ"),        # SMT <-> kraj (granica ka DV)
]

# TRP lanac (transformatorsko polje)
TRP_CHAIN = [
    ("GSS", "SR"),          # GSS <-> SR
    ("SR", "P"),            # SR <-> P
    ("P", "TR"),            # P <-> TR (transformator)
]

# GSP lanac (glavno spojno polje)
GSP_CHAIN = [
    ("GSS_1", "SR_1"),      # GSS 1 <-> SR ka GSS 1
    ("SR_1", "P"),          # SR 1 <-> P
    ("P", "SR_2"),          # P <-> SR ka GSS 2
    ("SR_2", "GSS_2"),      # SR 2 <-> GSS 2
]


# =============================================================================
# EDGE_TYPES REGISTRY
# =============================================================================

EDGE_TYPES = {
    # === GALVANSKE VEZE (unutar EEO) ===
    
    "GALVANSKI_VEZAN": {
        "class": GalvanskiVezanEdge,
        "description": "Fizička električna veza između elemenata",
        "direction": EdgeDirection.UNDIRECTED,
        "within_eeo": True,
        "attrs": ["source_id", "target_id", "condition"],
        "semantic": "prethodnik <-> sledbenik",
    },
    
    # === HIJERARHIJSKE VEZE ===
    
    "SADRZI": {
        "class": SadrziEdge,
        "description": "Roditelj sadrži dete (EEO->Polje, Polje->Element)",
        "direction": EdgeDirection.DIRECTED,
        "within_eeo": True,
        "attrs": ["parent_id", "child_id"],
        "semantic": "parent --SADRZI--> child",
    },
    
    "PRIPADA": {
        "class": PripadaEdge,
        "description": "Dete pripada roditelju (inverzno od SADRZI)",
        "direction": EdgeDirection.DIRECTED,
        "within_eeo": True,
        "attrs": ["child_id", "parent_id"],
        "semantic": "child --PRIPADA--> parent",
    },
    
    # === MEĐUOBJEKTNE VEZE (između EEO) ===
    
    "POVEZUJE": {
        "class": PovezujeEdge,
        "description": "Veza graničnog elementa sa vodom (DV/KB)",
        "direction": EdgeDirection.UNDIRECTED,
        "within_eeo": False,
        "attrs": ["element_id", "line_id", "side"],
        "semantic": "IRSU --POVEZUJE--> DV/KB",
    },
    
    # === ANALITIČKE VEZE ===
    
    "NAPAJA": {
        "class": NapajaEdge,
        "description": "Smer toka energije (za analizu napajanja)",
        "direction": EdgeDirection.DIRECTED,
        "within_eeo": False,
        "attrs": ["source_id", "target_id"],
        "semantic": "source --NAPAJA--> target",
    },
}


# =============================================================================
# MATRICA POVEZANOSTI - Format četvorke (x, i, y, j)
# =============================================================================

@dataclass
class ConnectivityMatrixEntry:
    """
    Jedan red matrice povezanosti.
    
    Iz metodologije (sekcija 7705+):
    Svaki red je uređena četvorka (x, i, y, j):
    - x: indeks EEO 1
    - i: indeks DVP polja u EEO x  
    - y: indeks EEO 2
    - j: indeks DVP polja u EEO y
    
    Primer: (1, 2, 3, 1) znači:
    "DVP 2 iz EEO 1 povezan je sa DVP 1 iz EEO 3"
    """
    eeo_x_id: str            # ID prvog EEO (npr. "NI2")
    dvp_x_index: int         # Indeks polja u prvom EEO (i)
    eeo_y_id: str            # ID drugog EEO (npr. "LE2")
    dvp_y_index: int         # Indeks polja u drugom EEO (j)
    
    voltage_kv: int          # Naponski nivo
    line_type: str           # "DV", "KB", "MV"
    line_id: str             # ID voda
    
    def to_tuple(self) -> tuple:
        """Vraća četvorku (x, i, y, j)."""
        return (self.eeo_x_id, self.dvp_x_index, self.eeo_y_id, self.dvp_y_index)


# =============================================================================
# HELPER FUNKCIJE
# =============================================================================

def get_edge_type_info(edge_type: str) -> Dict[str, Any]:
    """Vraća informacije o tipu ivice."""
    return EDGE_TYPES.get(edge_type, {})


def get_field_chain(field_type: str, has_pss: bool = False) -> List[tuple]:
    """
    Vraća lanac veza za dati tip polja.
    
    Args:
        field_type: "DVP", "KBP", "TRPVN", "TRPNN", "GSP", "PSP"
        has_pss: Da li EEO ima PSS na tom naponskom nivou
    """
    if field_type in ["DVP", "KBP"]:
        return DVP_CHAIN_WITH_PSS if has_pss else DVP_CHAIN_NO_PSS
    elif field_type in ["TRPVN", "TRPNN"]:
        return TRP_CHAIN
    elif field_type in ["GSP", "PSP"]:
        return GSP_CHAIN
    return []


def is_within_eeo(edge_type: str) -> bool:
    """Da li je ivica unutar jednog EEO?"""
    return EDGE_TYPES.get(edge_type, {}).get("within_eeo", False)


def get_all_edge_types() -> List[str]:
    """Vraća listu svih tipova ivica."""
    return list(EDGE_TYPES.keys())
