#!/usr/bin/env python3
"""
Konvertuje postojeći dv_station_map_complete.json u novu strukturu
sa naponskim nivoima koristeći heuristiku:
- 4xx = 400 kV
- 2xx, 2xxx/x = 220 kV  
- Sve ostalo (1xx, 1xxx, ostalo) = 110 kV
"""

import json
import re
from pathlib import Path


def get_voltage_kv(dv_id: str) -> int:
    """
    Određuje naponski nivo na osnovu broja dalekovoda.
    
    Heuristika:
    - 4xx = 400 kV
    - 2xx ili 2xxx/x = 220 kV
    - Sve ostalo (1xx, 1xxx, ostalo) = 110 kV
    """
    # Ukloni sufikse poput A, Б, /1, /2 itd da dobijemo osnovni broj
    # Primeri: "227/1" -> "227", "104А/3" -> "104", "1178Б" -> "1178"
    clean_id = re.sub(r'[АБВГабвгABCDabcd]', '', dv_id)  # Ukloni slova (ćirilica i latinica)
    clean_id = clean_id.split('/')[0]  # Uzmi samo prvi deo pre /
    
    try:
        num = int(clean_id)
    except ValueError:
        # Ako ne možemo parsirati, pretpostavi 110 kV
        return 110
    
    # Primeni heuristiku
    if 400 <= num < 500:
        return 400
    elif 200 <= num < 300:
        return 220
    else:
        # 100-199, 1000+, ostalo = 110 kV
        return 110


def convert_station_map():
    """Konvertuje mapu u novu strukturu sa naponskim nivoima."""
    
    # Učitaj postojeći JSON
    input_path = Path(__file__).parent.parent / "dv_station_map_complete.json"
    
    with open(input_path, 'r', encoding='utf-8') as f:
        old_map = json.load(f)
    
    # Nova struktura: { dv_id: { "stations": [...], "voltage_kv": 110/220/400 } }
    new_map = {}
    
    # Statistika
    stats = {400: 0, 220: 0, 110: 0}
    
    for dv_id, connections in old_map.items():
        voltage = get_voltage_kv(dv_id)
        stats[voltage] += 1
        
        new_map[dv_id] = {
            "stations": connections,
            "voltage_kv": voltage
        }
    
    # Sačuvaj novu mapu
    output_path = Path(__file__).parent.parent / "dv_station_map_with_voltage.json"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(new_map, f, ensure_ascii=False, indent=2)
    
    print(f"Konverzija završena!")
    print(f"Ukupno dalekovoda: {len(new_map)}")
    print(f"  400 kV: {stats[400]}")
    print(f"  220 kV: {stats[220]}")
    print(f"  110 kV: {stats[110]}")
    print(f"\nSačuvano u: {output_path}")
    
    # Prikaži primere za svaki naponski nivo
    print("\n--- Primeri ---")
    for voltage in [400, 220, 110]:
        examples = [(k, v) for k, v in new_map.items() if v['voltage_kv'] == voltage][:3]
        print(f"\n{voltage} kV:")
        for dv_id, data in examples:
            stations = data['stations'][0] if data['stations'] else []
            print(f"  ДВ {dv_id}: {' <-> '.join(stations)}")
    
    return new_map


if __name__ == "__main__":
    convert_station_map()
