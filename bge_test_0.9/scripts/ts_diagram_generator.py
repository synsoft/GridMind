#!/usr/bin/env python3
"""
Generator dijagrama za trafostanice iz EMS prenosnog sistema.
Koristi Graphviz za generisanje vizuelnih prikaza mreže.

Instalacija: pip install graphviz
Napomena: Potreban je i Graphviz system package (apt install graphviz)
"""

import json
from graphviz import Digraph
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional


class TSNetworkDiagram:
    """Klasa za generisanje dijagrama trafostanica i njihovih veza."""
    
    # Boje za različite naponske nivoe
    VOLTAGE_COLORS = {
        '400': '#FF0000',    # Crvena za 400 kV
        '220': '#0000FF',    # Plava za 220 kV  
        '110': '#00AA00',    # Zelena za 110 kV
        '35': '#FFA500',     # Narandžasta za 35 kV
    }
    
    # Stilovi za čvorove
    NODE_STYLES = {
        'main': {'shape': 'box', 'style': 'filled,bold', 'fillcolor': '#FFD700', 'penwidth': '4', 'fontsize': '14', 'margin': '0.3'},
        'connected_400': {'shape': 'box', 'style': 'filled,rounded', 'fillcolor': '#FFCCCC', 'fontsize': '11', 'margin': '0.2'},
        'connected_220': {'shape': 'box', 'style': 'filled,rounded', 'fillcolor': '#CCCCFF', 'fontsize': '11', 'margin': '0.2'},
        'connected_110': {'shape': 'box', 'style': 'filled,rounded', 'fillcolor': '#CCFFCC', 'fontsize': '11', 'margin': '0.2'},
        'intermediate': {'shape': 'ellipse', 'style': 'filled', 'fillcolor': '#E0E0E0', 'fontsize': '10'},
    }
    
    def __init__(self, dv_station_map_path: str):
        """
        Inicijalizacija sa putanjom do JSON fajla sa mapom dalekovoda.
        
        Args:
            dv_station_map_path: Putanja do dv_station_map.json
        """
        self.dv_map = self._load_dv_map(dv_station_map_path)
        
    def _load_dv_map(self, path: str) -> Dict:
        """Učitava mapu dalekovoda iz JSON fajla."""
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def _get_voltage_level(self, dv_number: str) -> str:
        """
        Određuje naponski nivo na osnovu broja dalekovoda.
        
        400 kV: 401-499
        220 kV: 201-299
        110 kV: 101-199, 1001-1999
        """
        # Ukloni sufikse poput /1, /2, А, Б
        base_num = dv_number.split('/')[0].rstrip('АБABab')
        
        try:
            num = int(base_num)
            if 401 <= num <= 499:
                return '400'
            elif 201 <= num <= 299:
                return '220'
            elif (101 <= num <= 199) or (1001 <= num <= 1999):
                return '110'
        except ValueError:
            pass
        
        return '110'  # Default
    
    def get_connections_for_station(self, station_name: str, depth: int = 1) -> Dict:
        """
        Pronalazi sve veze za datu trafostanicu.
        
        Args:
            station_name: Ime trafostanice (npr. "ТС Београд 5" ili "Beograd 5")
            depth: Dubina pretrage (1 = samo direktne veze, 2 = veze veza, itd.)
            
        Returns:
            Dict sa vezama po naponskim nivoima
        """
        # Normalizuj ime (podrži i latinicu i ćirilicu)
        station_variants = self._get_station_variants(station_name)
        
        connections = {
            '400': [],
            '220': [],
            '110': [],
        }
        
        for dv_number, station_pairs in self.dv_map.items():
            voltage = self._get_voltage_level(dv_number)
            
            for pair in station_pairs:
                if len(pair) == 2:
                    ts1, ts2 = pair
                    
                    # Proveri da li je naša stanica u paru
                    for variant in station_variants:
                        if variant.lower() in ts1.lower() or variant.lower() in ts2.lower():
                            other_station = ts2 if variant.lower() in ts1.lower() else ts1
                            connections[voltage].append({
                                'dv': dv_number,
                                'station': other_station,
                                'from': ts1,
                                'to': ts2
                            })
                            break
        
        return connections
    
    def _get_station_variants(self, station_name: str) -> List[str]:
        """Generiše varijante imena stanice (ćirilica/latinica)."""
        # Mapa transliteracije
        cyr_to_lat = {
            'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Ђ': 'Đ', 'Е': 'E',
            'Ж': 'Ž', 'З': 'Z', 'И': 'I', 'Ј': 'J', 'К': 'K', 'Л': 'L', 'Љ': 'Lj',
            'М': 'M', 'Н': 'N', 'Њ': 'Nj', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S',
            'Т': 'T', 'Ћ': 'Ć', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'C', 'Ч': 'Č',
            'Џ': 'Dž', 'Ш': 'Š',
            'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'ђ': 'đ', 'е': 'e',
            'ж': 'ž', 'з': 'z', 'и': 'i', 'ј': 'j', 'к': 'k', 'л': 'l', 'љ': 'lj',
            'м': 'm', 'н': 'n', 'њ': 'nj', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's',
            'т': 't', 'ћ': 'ć', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'č',
            'џ': 'dž', 'ш': 'š'
        }
        
        variants = [station_name]
        
        # Konvertuj u latinicu
        lat_name = station_name
        for cyr, lat in cyr_to_lat.items():
            lat_name = lat_name.replace(cyr, lat)
        if lat_name != station_name:
            variants.append(lat_name)
        
        # Dodaj varijante bez "ТС " prefiksa
        for v in variants.copy():
            if v.startswith('ТС '):
                variants.append(v[3:])
            elif v.startswith('TS '):
                variants.append(v[3:])
        
        return variants
    
    def generate_diagram(
        self, 
        station_name: str, 
        output_path: str = None,
        format: str = 'png',
        show_dv_numbers: bool = True,
        depth: int = 1
    ) -> str:
        """
        Generiše dijagram za datu trafostanicu.
        
        Args:
            station_name: Ime trafostanice
            output_path: Putanja za izlazni fajl (bez ekstenzije)
            format: Format izlaza ('png', 'pdf', 'svg')
            show_dv_numbers: Da li da prikaže brojeve dalekovoda
            depth: Dubina prikaza veza
            
        Returns:
            Putanja do generisanog fajla
        """
        connections = self.get_connections_for_station(station_name, depth)
        
        # Kreiraj graf sa 'dot' engine - hijerarhijski raspored
        dot = Digraph(
            name=f'TS_{station_name.replace(" ", "_")}',
            comment=f'Dijagram trafostanice {station_name}',
            format=format,
            engine='dot'
        )
        
        # Globalne postavke - horizontalni layout, veliki razmaci
        dot.attr(
            rankdir='LR',      # Levo-desno umesto gore-dole
            nodesep='0.8',     # Razmak između čvorova u istom ranku
            ranksep='2.0',     # Razmak između rankova (kolona)
            splines='polyline', # Prave linije sa prelomima
            concentrate='false',
            dpi='100'
        )
        dot.attr('node', fontname='Arial', fontsize='12')
        dot.attr('edge', fontname='Arial', fontsize='11', minlen='2')
        
        # Dodaj glavnu stanicu u centru
        main_station_id = self._sanitize_id(station_name)
        dot.node(
            main_station_id, 
            station_name,
            **self.NODE_STYLES['main']
        )
        
        added_nodes = {main_station_id}
        added_edges = set()
        
        # Grupiši stanice po naponskim nivoima u subgrafove
        for voltage in ['400', '220', '110']:
            conns = connections.get(voltage, [])
            if not conns:
                continue
                
            color = self.VOLTAGE_COLORS.get(voltage, '#000000')
            node_style = self.NODE_STYLES.get(f'connected_{voltage}', self.NODE_STYLES['intermediate'])
            
            # Subgraf za naponski nivo - grupiše čvorove zajedno
            with dot.subgraph(name=f'cluster_{voltage}kV') as sub:
                sub.attr(
                    label=f'{voltage} kV',
                    style='rounded,dashed',
                    color=color,
                    fontcolor=color,
                    fontsize='14',
                    labeljust='l'
                )
                
                for conn in conns:
                    other_station = conn['station']
                    other_id = self._sanitize_id(other_station)
                    
                    # Dodaj čvor u subgraf
                    if other_id not in added_nodes:
                        sub.node(other_id, other_station, **node_style)
                        added_nodes.add(other_id)
                    
                    # Dodaj vezu
                    edge_key = tuple(sorted([main_station_id, other_id]) + [conn['dv']])
                    if edge_key not in added_edges:
                        label = f"DV {conn['dv']}" if show_dv_numbers else ""
                        pen = '3' if voltage == '400' else ('2' if voltage == '220' else '1.5')
                        
                        dot.edge(
                            main_station_id, 
                            other_id,
                            label=label,
                            color=color,
                            penwidth=pen,
                            fontcolor=color,
                            fontsize='10'
                        )
                        added_edges.add(edge_key)
        
        # Generiši fajl
        if output_path is None:
            output_path = f'ts_diagram_{self._sanitize_id(station_name)}'
        
        output_file = dot.render(output_path, cleanup=True)
        return output_file
    
    def _sanitize_id(self, name: str) -> str:
        """Konvertuje ime u validan ID za Graphviz."""
        # Zameni problematične karaktere
        result = name.replace(' ', '_').replace('-', '_').replace('/', '_')
        result = result.replace('(', '').replace(')', '')
        return result
    
    def generate_html_report(self, station_name: str, output_path: str = None) -> str:
        """
        Generiše HTML izveštaj sa SVG dijagramom i tabelom veza.
        
        Args:
            station_name: Ime trafostanice
            output_path: Putanja za izlazni HTML fajl
            
        Returns:
            Putanja do generisanog HTML fajla
        """
        connections = self.get_connections_for_station(station_name)
        
        # Generiši SVG
        svg_path = self.generate_diagram(station_name, format='svg')
        
        # Učitaj SVG
        with open(svg_path, 'r', encoding='utf-8') as f:
            svg_content = f.read()
        
        # Generiši HTML
        html = f"""<!DOCTYPE html>
<html lang="sr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dijagram - {station_name}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
        }}
        h1 {{
            color: #333;
            border-bottom: 2px solid #FFD700;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #555;
            margin-top: 30px;
        }}
        .diagram-container {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            overflow-x: auto;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin-top: 20px;
            background: white;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }}
        th {{
            background-color: #4CAF50;
            color: white;
        }}
        tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
        tr:hover {{
            background-color: #f1f1f1;
        }}
        .voltage-400 {{ color: #FF0000; font-weight: bold; }}
        .voltage-220 {{ color: #0000FF; font-weight: bold; }}
        .voltage-110 {{ color: #00AA00; font-weight: bold; }}
        .summary {{
            display: flex;
            gap: 20px;
            margin: 20px 0;
        }}
        .summary-card {{
            background: white;
            padding: 15px 25px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .summary-card h3 {{
            margin: 0 0 10px 0;
            font-size: 14px;
            color: #666;
        }}
        .summary-card .number {{
            font-size: 32px;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <h1>🔌 Dijagram trafostanice: {station_name}</h1>
    
    <div class="summary">
        <div class="summary-card">
            <h3>400 kV veze</h3>
            <div class="number voltage-400">{len(connections['400'])}</div>
        </div>
        <div class="summary-card">
            <h3>220 kV veze</h3>
            <div class="number voltage-220">{len(connections['220'])}</div>
        </div>
        <div class="summary-card">
            <h3>110 kV veze</h3>
            <div class="number voltage-110">{len(connections['110'])}</div>
        </div>
    </div>
    
    <h2>📊 Mrežni dijagram</h2>
    <div class="diagram-container">
        {svg_content}
    </div>
    
    <h2>📋 Lista veza</h2>
"""
        
        # Tabela za svaki naponski nivo
        for voltage in ['400', '220', '110']:
            if connections[voltage]:
                html += f"""
    <h3 class="voltage-{voltage}">{voltage} kV dalekovodi</h3>
    <table>
        <tr>
            <th>DV broj</th>
            <th>Od</th>
            <th>Do</th>
        </tr>
"""
                for conn in connections[voltage]:
                    html += f"""        <tr>
            <td><strong>DV {conn['dv']}</strong></td>
            <td>{conn['from']}</td>
            <td>{conn['to']}</td>
        </tr>
"""
                html += "    </table>\n"
        
        html += """
</body>
</html>
"""
        
        # Sačuvaj HTML
        if output_path is None:
            output_path = f'ts_report_{self._sanitize_id(station_name)}.html'
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        
        return output_path


def main():
    """Primer korišćenja."""
    # Putanja do JSON fajla
    dv_map_path = Path(__file__).parent.parent / 'data' / 'dv_station_map.json'
    
    # Kreiraj generator dijagrama
    generator = TSNetworkDiagram(str(dv_map_path))
    
    # Generiši dijagram za TS Beograd 5
    station = "ТС Београд 5"
    
    print(f"Generišem dijagram za {station}...")
    
    # Generiši PNG
    png_path = generator.generate_diagram(station, format='png')
    print(f"PNG dijagram: {png_path}")
    
    # Generiši HTML izveštaj
    html_path = generator.generate_html_report(station)
    print(f"HTML izveštaj: {html_path}")
    
    # Prikaži veze
    connections = generator.get_connections_for_station(station)
    print(f"\nVeze za {station}:")
    print(f"  400 kV: {len(connections['400'])} veza")
    print(f"  220 kV: {len(connections['220'])} veza")
    print(f"  110 kV: {len(connections['110'])} veza")


if __name__ == '__main__':
    main()
