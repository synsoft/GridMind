#!/usr/bin/env python3
"""
Demo: Kreiranje Knowledge Graph-a za TS Niš 2 prema metodologiji.

Pokazuje kako se koristi GridKnowledgeGraph za modelovanje:
- EEO (TS Niš 2)
- Sistema sabirnica (GSS 400 kV)
- Dalekovodnog polja (DVP 400 kV)
- Osnovnih elemenata (SR, P, SMT, IRSU, NMT)
- Galvanskih veza između elemenata
"""

import sys
from pathlib import Path

# Dodaj parent folder u path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.graph import GridKnowledgeGraph


def create_demo_graph():
    """Kreira demo graf za TS Niš 2."""
    
    # Inicijalizuj graf
    kg = GridKnowledgeGraph()
    
    print("=" * 60)
    print("GridMind Knowledge Graph - Demo")
    print("Prema: Metodologija Relejne zaštite - GridMind 15-02.md")
    print("=" * 60)
    
    # =========================================================================
    # 1. DODAJ EEO (Elektroenergetske objekte)
    # =========================================================================
    print("\n[1] Dodajem EEO...")
    
    kg.add_eeo(
        id="NI2",
        name="TS 400/220/110 kV Niš 2",
        code="NI2",
        type="TS",
        voltage_levels=[400, 220, 110],
    )
    
    kg.add_eeo(
        id="LE2",
        name="TS 400/220/110 kV Leskovac 2",
        code="LE2",
        type="TS",
        voltage_levels=[400, 220, 110],
    )
    
    print(f"   Dodato EEO: NI2, LE2")
    
    # =========================================================================
    # 2. DODAJ SISTEME SABIRNICA
    # =========================================================================
    print("\n[2] Dodajem sisteme sabirnica...")
    
    # NI2 - GSS na 400 kV
    kg.add_busbar(eeo_id="NI2", type="GSS", voltage_kv=400, index=1)
    kg.add_busbar(eeo_id="NI2", type="GSS", voltage_kv=400, index=2)
    
    # LE2 - GSS na 400 kV
    kg.add_busbar(eeo_id="LE2", type="GSS", voltage_kv=400, index=1)
    
    print(f"   Dodato: NI2_GSS_400_1, NI2_GSS_400_2, LE2_GSS_400_1")
    
    # =========================================================================
    # 3. KREIRAJ KOMPLETNO DVP SA ELEMENTIMA
    # =========================================================================
    print("\n[3] Kreiram dalekovodno polje sa svim elementima...")
    
    # NI2 DVP 400 kV 1 (ka Leskovcu)
    ni2_dvp1 = kg.create_dvp_with_elements(
        eeo_id="NI2",
        voltage_kv=400,
        index=1,
        line_name="DV Niš-Leskovac",
        gss_index=1,
        all_status=1,  # Svi prekidači uključeni
    )
    
    print(f"   Kreirano DVP: {ni2_dvp1['field_id']}")
    print(f"   Elementi: SR={ni2_dvp1['sr_gss']}, P={ni2_dvp1['p']}, ")
    print(f"             SMT={ni2_dvp1['smt']}, IRSU={ni2_dvp1['irsu']}, NMT={ni2_dvp1['nmt']}")
    
    # LE2 DVP 400 kV 1 (ka Nišu)
    le2_dvp1 = kg.create_dvp_with_elements(
        eeo_id="LE2",
        voltage_kv=400,
        index=1,
        line_name="DV Leskovac-Niš",
        gss_index=1,
        all_status=1,
    )
    
    print(f"   Kreirano DVP: {le2_dvp1['field_id']}")
    
    # =========================================================================
    # 4. DODAJ DALEKOVOD IZMEĐU EEO
    # =========================================================================
    print("\n[4] Dodajem dalekovod između NI2 i LE2...")
    
    dv_id = kg.add_line(
        type="DV",
        name="DV 400 kV Niš-Leskovac",
        voltage_kv=400,
        from_eeo_id="NI2",
        from_field_id=ni2_dvp1['field_id'],
        from_field_index=1,
        to_eeo_id="LE2",
        to_field_id=le2_dvp1['field_id'],
        to_field_index=1,
        length_km=45.0,
    )
    
    # Poveži IRSU sa DV
    kg.add_povezuje(ni2_dvp1['irsu'], dv_id, side="from")
    kg.add_povezuje(le2_dvp1['irsu'], dv_id, side="to")
    
    print(f"   Dodat DV: {dv_id}")
    print(f"   Povezano: {ni2_dvp1['irsu']} <-> DV <-> {le2_dvp1['irsu']}")
    
    # =========================================================================
    # 5. PREGLED GRAFA
    # =========================================================================
    print("\n[5] Statistike grafa:")
    stats = kg.get_stats()
    print(f"   Ukupno čvorova: {stats['total_nodes']}")
    print(f"   Ukupno ivica: {stats['total_edges']}")
    print(f"   Čvorovi po tipu:")
    for node_type, count in stats['nodes_by_type'].items():
        print(f"      {node_type}: {count}")
    
    # =========================================================================
    # 6. UPITI NAD GRAFOM
    # =========================================================================
    print("\n[6] Upiti nad grafom:")
    
    # Galvanski povezani sa IRSU
    galvanski = kg.get_galvanski_povezani(ni2_dvp1['irsu'])
    print(f"   Galvanski povezani sa {ni2_dvp1['irsu']}:")
    for g in galvanski:
        print(f"      - {g}")
    
    # Granični elementi NI2
    boundary = kg.get_boundary_elements("NI2")
    print(f"   Granični elementi NI2: {boundary}")
    
    # Matrica povezanosti
    matrix = kg.get_connectivity_matrix(voltage_kv=400)
    print(f"   Matrica povezanosti (400 kV):")
    for entry in matrix:
        print(f"      {entry.to_tuple()} -> {entry.line_id}")
    
    # =========================================================================
    # 7. ANALIZA PUTANJE
    # =========================================================================
    print("\n[7] Analiza putanje:")
    
    # Putanja od GSS NI2 do GSS LE2
    path = kg.find_path("NI2_GSS_400_1", "LE2_GSS_400_1", respect_status=True)
    if path:
        print(f"   Putanja NI2_GSS_400_1 -> LE2_GSS_400_1:")
        for i, node in enumerate(path):
            print(f"      {i+1}. {node}")
    else:
        print("   Nema putanje!")
    
    print("\n" + "=" * 60)
    print(f"Graf: {kg}")
    print("=" * 60)
    
    return kg


if __name__ == "__main__":
    kg = create_demo_graph()
