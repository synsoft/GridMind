"""
Enumeracije za Knowledge Graph prema metodologiji relejne zaštite.

Izvor: Metodologija Relejne zaštite - GridMind 15-02.md
"""

from enum import Enum, auto


class SwitchStatus(Enum):
    """
    Status uklopnog stanja rasklopne opreme (RO).
    
    Iz metodologije (sekcija 8224):
    - Status uklopnog stanja "uključen" u binarnom obliku je 1
    - Status uklopnog stanja "isključen" u binarnom obliku je 0
    """
    UKLJUCEN = 1    # Veza sa prethodnikom/sledbenikom NIJE prekinuta
    ISKLJUCEN = 0   # Veza sa prethodnikom/sledbenikom JE prekinuta


class VoltageLevel(Enum):
    """
    Naponski nivoi u prenosnom sistemu (PS).
    
    Iz metodologije:
    - Električna energija se kroz PS prenosi na 400 kV, 220 kV i 110 kV
    - Naponi u DS (35, 20, 10, 0.4 kV) se označavaju sa x kV
    """
    V_400 = 400
    V_220 = 220
    V_110 = 110
    V_X = 0  # Distribucija (35, 20, 10, 0.4 kV) - nije relevantno za PS


class FieldType(Enum):
    """
    Tipovi polja (PO) u EEO.
    
    Iz metodologije (Nivo 2 podele PO):
    """
    DVP = "DVP"      # Dalekovodno polje
    KBP = "KBP"      # Kablovsko polje
    TRPVN = "TRPVN"  # Transformatorsko polje - viši napon
    TRPNN = "TRPNN"  # Transformatorsko polje - niži napon
    GSP = "GSP"      # Glavno spojno polje
    PSP = "PSP"      # Pomoćno spojno polje


class BusbarType(Enum):
    """
    Tipovi sistema sabirnica (SS).
    
    Iz metodologije (Nivo 2 podele SS):
    """
    GSS = "GSS"  # Glavni sistem sabirnica
    PSS = "PSS"  # Pomoćni sistem sabirnica


class ElementType(Enum):
    """
    Tipovi osnovnih elemenata (listovi stabla).
    
    Rasklopna oprema (RO):
    """
    # Rasklopna oprema
    P = "P"        # Prekidač
    SR = "SR"      # Sabirnički rastavljač
    IR = "IR"      # Izlazni rastavljač (linijski rastavljač)
    IRSU = "IRSU"  # Izlazni rastavljač sa sistemskim uzemljenjem (GRANIČNI)
    
    # Merna oprema (MO)
    SMT = "SMT"    # Strujni merni transformator (GRANIČNI)
    NMT = "NMT"    # Naponski merni transformator (GRANIČNI)


class LineType(Enum):
    """
    Tipovi vodova (oprema van EEO).
    
    Iz metodologije (Nivo 2 podele VO):
    """
    DV = "DV"  # Dalekovod
    KB = "KB"  # Kabal
    MV = "MV"  # Mešoviti vod (DV+KB ili KB+DV)


class TransformerType(Enum):
    """
    Tipovi energetskih transformatora (ET).
    
    Iz metodologije (Nivo 2 podele ET):
    """
    TR_400_220 = "TR_400_220"  # 400/220 kV
    TR_400_110 = "TR_400_110"  # 400/110 kV
    TR_220_110 = "TR_220_110"  # 220/110 kV
    TR_400_X = "TR_400_X"      # 400/x kV (ka distribuciji)
    TR_220_X = "TR_220_X"      # 220/x kV (ka distribuciji)
    TR_110_X = "TR_110_X"      # 110/x kV (ka distribuciji)


class Phase(Enum):
    """
    Faze trofaznog EES.
    
    Iz metodologije:
    - Faza L1 (ravnopravno se koristi i oznaka - faza "0")
    - Faza L2 (ravnopravno se koristi i oznaka - faza "4")
    - Faza L3 (ravnopravno se koristi i oznaka - faza "8")
    """
    L1 = "L1"  # Faza 0
    L2 = "L2"  # Faza 4
    L3 = "L3"  # Faza 8
