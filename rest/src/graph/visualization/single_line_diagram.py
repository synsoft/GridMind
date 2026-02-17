#!/usr/bin/env python3
"""
Generator jednopolne šeme za EEO.

Kreira SVG jednopolnu šemu sa standardnim elektro simbolima:
- Sabirnice (GSS) kao horizontalne linije
- Polja sa prekidačima, rastavljačima, IRSU
- Transformatori sa simbolom
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import json


@dataclass
class SvgConfig:
    """Konfiguracija SVG-a."""
    width: int = 1400
    height: int = 900
    margin: int = 50
    busbar_y_gap: int = 200  # Razmak između naponskih nivoa
    field_width: int = 80   # Širina polja
    field_gap: int = 20     # Razmak između polja
    
    # Boje
    color_400kv: str = "#E91E63"
    color_220kv: str = "#9C27B0"
    color_110kv: str = "#2196F3"
    color_busbar: str = "#333"
    color_closed: str = "#4CAF50"    # Zeleno - zatvoreno
    color_open: str = "#F44336"       # Crveno - otvoreno
    color_text: str = "#333"
    color_transformer: str = "#FF9800"


class SingleLineDiagramGenerator:
    """Generator jednopolne šeme."""
    
    def __init__(self, graph, config: Optional[SvgConfig] = None):
        self.graph = graph
        self.cfg = config or SvgConfig()
        
    def generate_eeo_diagram(self, eeo_id: str) -> str:
        """Generiši SVG jednopolnu šemu za EEO."""
        eeo_node = self.graph.get_node(eeo_id)
        if not eeo_node:
            return self._error_svg(f"EEO {eeo_id} nije pronađen")
        
        # Prikupi podatke
        voltage_levels = eeo_node.get('voltage_levels', [400, 220, 110])
        voltage_levels = sorted(voltage_levels, reverse=True)
        
        # Prikupi sabirnice i polja po naponskom nivou
        data = self._collect_eeo_data(eeo_id, voltage_levels)
        
        # Generiši SVG
        return self._render_svg(eeo_id, eeo_node, voltage_levels, data)
    
    def _collect_eeo_data(self, eeo_id: str, voltage_levels: List[int]) -> Dict:
        """Prikupi podatke za crtanje."""
        data = {
            'busbars': {},   # voltage -> [busbar_ids]
            'fields': {},    # voltage -> [field_data]
            'transformers': []
        }
        
        # Nađi sve čvorove za ovaj EEO
        eeo_nodes = self.graph._nodes_by_eeo.get(eeo_id, set())
        
        for node_id in eeo_nodes:
            node = self.graph.get_node(node_id)
            if not node:
                continue
            
            node_type = node.get('node_type')
            voltage = node.get('voltage_kv')
            
            if node_type == 'GSS':
                if voltage not in data['busbars']:
                    data['busbars'][voltage] = []
                data['busbars'][voltage].append(node_id)
                
            elif node_type == 'DVP':
                if voltage not in data['fields']:
                    data['fields'][voltage] = []
                
                # Prikupi elemente polja
                field_data = {
                    'id': node_id,
                    'name': node.get('name', node_id),
                    'gss_index': node.get('gss_index', 1),
                    'elements': self._get_field_elements(node_id)
                }
                data['fields'][voltage].append(field_data)
                
            elif node_type == 'TR':
                data['transformers'].append({
                    'id': node_id,
                    'name': node.get('name', node_id),
                    'vn_kv': node.get('vn_kv'),
                    'nn_kv': node.get('nn_kv'),
                    'power_mva': node.get('power_mva')
                })
        
        return data
    
    def _get_field_elements(self, field_id: str) -> Dict:
        """Prikupi elemente polja."""
        elements = {'sr': None, 'p': None, 'smt': None, 'irsu': None, 'nmt': None}
        
        # Nađi susedne čvorove
        for neighbor in self.graph._graph.neighbors(field_id):
            node = self.graph.get_node(neighbor)
            if not node:
                continue
            
            node_type = node.get('node_type', '').upper()
            if node_type == 'SR':
                elements['sr'] = {'id': neighbor, 'status': node.get('status', 1)}
            elif node_type == 'P':
                elements['p'] = {'id': neighbor, 'status': node.get('status', 1)}
            elif node_type == 'SMT':
                elements['smt'] = {'id': neighbor, 'status': node.get('status', 1)}
            elif node_type == 'IRSU':
                elements['irsu'] = {'id': neighbor, 'status': node.get('status', 1)}
            elif node_type == 'NMT':
                elements['nmt'] = {'id': neighbor, 'status': node.get('status', 1)}
        
        return elements
    
    def _render_svg(self, eeo_id: str, eeo_node: Dict, voltage_levels: List[int], data: Dict) -> str:
        """Renderuj SVG."""
        # Izračunaj dimenzije
        max_fields = max(len(data['fields'].get(v, [])) for v in voltage_levels) if data['fields'] else 5
        width = max(self.cfg.width, max_fields * (self.cfg.field_width + self.cfg.field_gap) + 200)
        height = len(voltage_levels) * self.cfg.busbar_y_gap + 200
        
        svg_parts = []
        
        # Header
        svg_parts.append(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
    <defs>
        <!-- Marker za strelice -->
        <marker id="arrow" markerWidth="10" markerHeight="10" refX="5" refY="5" orient="auto">
            <path d="M0,0 L10,5 L0,10 Z" fill="#666"/>
        </marker>
        
        <!-- Simbol transformatora -->
        <symbol id="transformer" viewBox="0 0 40 60">
            <circle cx="20" cy="15" r="12" fill="none" stroke="#FF9800" stroke-width="2"/>
            <circle cx="20" cy="45" r="12" fill="none" stroke="#FF9800" stroke-width="2"/>
            <line x1="20" y1="0" x2="20" y2="3" stroke="#333" stroke-width="2"/>
            <line x1="20" y1="57" x2="20" y2="60" stroke="#333" stroke-width="2"/>
        </symbol>
        
        <!-- Simbol prekidača zatvorenog -->
        <symbol id="breaker-closed" viewBox="0 0 20 40">
            <line x1="10" y1="0" x2="10" y2="10" stroke="#333" stroke-width="2"/>
            <rect x="2" y="10" width="16" height="20" fill="#4CAF50" stroke="#333" stroke-width="1"/>
            <line x1="10" y1="30" x2="10" y2="40" stroke="#333" stroke-width="2"/>
        </symbol>
        
        <!-- Simbol prekidača otvorenog -->
        <symbol id="breaker-open" viewBox="0 0 20 40">
            <line x1="10" y1="0" x2="10" y2="10" stroke="#333" stroke-width="2"/>
            <rect x="2" y="10" width="16" height="20" fill="#F44336" stroke="#333" stroke-width="1"/>
            <line x1="10" y1="30" x2="10" y2="40" stroke="#333" stroke-width="2"/>
            <line x1="5" y1="15" x2="15" y2="25" stroke="#fff" stroke-width="2"/>
        </symbol>
        
        <!-- Simbol rastavljača zatvorenog -->
        <symbol id="disconnector-closed" viewBox="0 0 20 30">
            <line x1="10" y1="0" x2="10" y2="8" stroke="#333" stroke-width="2"/>
            <line x1="10" y1="8" x2="10" y2="22" stroke="#4CAF50" stroke-width="3"/>
            <line x1="10" y1="22" x2="10" y2="30" stroke="#333" stroke-width="2"/>
            <circle cx="10" cy="8" r="3" fill="none" stroke="#333" stroke-width="1"/>
            <line x1="5" y1="22" x2="15" y2="22" stroke="#333" stroke-width="2"/>
        </symbol>
        
        <!-- Simbol rastavljača otvorenog -->
        <symbol id="disconnector-open" viewBox="0 0 20 30">
            <line x1="10" y1="0" x2="10" y2="8" stroke="#333" stroke-width="2"/>
            <line x1="10" y1="8" x2="18" y2="18" stroke="#F44336" stroke-width="3"/>
            <line x1="10" y1="22" x2="10" y2="30" stroke="#333" stroke-width="2"/>
            <circle cx="10" cy="8" r="3" fill="none" stroke="#333" stroke-width="1"/>
            <line x1="5" y1="22" x2="15" y2="22" stroke="#333" stroke-width="2"/>
        </symbol>
        
        <!-- Simbol IRSU (strujni transformator) -->
        <symbol id="ct" viewBox="0 0 20 20">
            <circle cx="10" cy="10" r="8" fill="none" stroke="#9C27B0" stroke-width="2"/>
            <line x1="10" y1="0" x2="10" y2="2" stroke="#333" stroke-width="2"/>
            <line x1="10" y1="18" x2="10" y2="20" stroke="#333" stroke-width="2"/>
        </symbol>
    </defs>
    
    <!-- Pozadina -->
    <rect width="100%" height="100%" fill="#fafafa"/>
    
    <!-- Naslov -->
    <text x="{width/2}" y="35" text-anchor="middle" font-size="24" font-weight="bold" fill="#333">
        {eeo_node.get('name', eeo_id)}
    </text>
    <text x="{width/2}" y="55" text-anchor="middle" font-size="14" fill="#666">
        Jednopolna šema
    </text>
''')
        
        # Crtaj naponske nivoe
        y_offset = 100
        
        for voltage in voltage_levels:
            color = self._get_voltage_color(voltage)
            fields = data['fields'].get(voltage, [])
            busbars = data['busbars'].get(voltage, [])
            
            # Sabirnica
            busbar_y = y_offset + 30
            busbar_x1 = self.cfg.margin
            busbar_x2 = width - self.cfg.margin
            
            # Labela naponskog nivoa
            svg_parts.append(f'''
    <text x="20" y="{busbar_y}" font-size="14" font-weight="bold" fill="{color}">{voltage} kV</text>
''')
            
            # Broj sistema sabirnica
            num_busbars = len(busbars) if busbars else 2
            
            for bi in range(num_busbars):
                by = busbar_y + bi * 25
                svg_parts.append(f'''
    <line x1="{busbar_x1 + 60}" y1="{by}" x2="{busbar_x2}" y2="{by}" stroke="{color}" stroke-width="4"/>
    <text x="{busbar_x1 + 65}" y="{by - 5}" font-size="10" fill="#666">GS{bi+1}</text>
''')
            
            # Polja
            field_start_x = 120
            for fi, field in enumerate(fields):
                fx = field_start_x + fi * (self.cfg.field_width + self.cfg.field_gap)
                
                # Određeni na koji sistem sabirnica ide
                gss_idx = field.get('gss_index', 1) - 1
                connect_y = busbar_y + gss_idx * 25
                
                svg_parts.append(self._render_field(fx, connect_y, field, voltage))
            
            y_offset += self.cfg.busbar_y_gap
        
        # Transformatori (između naponskih nivoa)
        if data['transformers']:
            svg_parts.append(self._render_transformers(data['transformers'], voltage_levels, width))
        
        # Legenda
        svg_parts.append(self._render_legend(width, height))
        
        svg_parts.append('</svg>')
        
        return '\n'.join(svg_parts)
    
    def _render_field(self, x: int, busbar_y: int, field: Dict, voltage: int) -> str:
        """Renderuj jedno polje."""
        elements = field.get('elements', {})
        name = field.get('name', field['id'])
        
        # Skrati ime
        short_name = name.replace(f"_{voltage}", "").replace("DVP_", "")
        if len(short_name) > 10:
            short_name = short_name[:8] + ".."
        
        parts = []
        
        # Vertikalna linija od sabirnice
        y = busbar_y
        
        # SR (sabirnički rastavljač)
        sr = elements.get('sr')
        sr_status = sr.get('status', 1) if sr else 1
        sr_symbol = 'disconnector-closed' if sr_status else 'disconnector-open'
        parts.append(f'<use href="#{sr_symbol}" x="{x-10}" y="{y}" width="20" height="30"/>')
        y += 30
        
        # Vertikalna linija
        parts.append(f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y+10}" stroke="#333" stroke-width="2"/>')
        y += 10
        
        # P (prekidač)
        p = elements.get('p')
        p_status = p.get('status', 1) if p else 1
        p_symbol = 'breaker-closed' if p_status else 'breaker-open'
        parts.append(f'<use href="#{p_symbol}" x="{x-10}" y="{y}" width="20" height="40"/>')
        y += 40
        
        # Vertikalna linija
        parts.append(f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y+10}" stroke="#333" stroke-width="2"/>')
        y += 10
        
        # SMT (strujna merenja)
        parts.append(f'<use href="#ct" x="{x-10}" y="{y}" width="20" height="20"/>')
        y += 20
        
        # Vertikalna linija
        parts.append(f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y+10}" stroke="#333" stroke-width="2"/>')
        y += 10
        
        # IRSU simbol (izlazni rastavljač)
        irsu = elements.get('irsu')
        irsu_status = irsu.get('status', 1) if irsu else 1
        irsu_symbol = 'disconnector-closed' if irsu_status else 'disconnector-open'
        parts.append(f'<use href="#{irsu_symbol}" x="{x-10}" y="{y}" width="20" height="30"/>')
        y += 30
        
        # Strelica ka dalekovodu
        parts.append(f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y+15}" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>')
        
        # Labela polja
        parts.append(f'<text x="{x}" y="{y+30}" text-anchor="middle" font-size="9" fill="#333">{short_name}</text>')
        
        return '\n'.join(parts)
    
    def _render_transformers(self, transformers: List[Dict], voltage_levels: List[int], width: int) -> str:
        """Renderuj transformatore."""
        parts = []
        
        # Pozicija desno
        tx = width - 150
        
        for i, tr in enumerate(transformers):
            ty = 150 + i * 120
            
            # Simbol
            parts.append(f'<use href="#transformer" x="{tx}" y="{ty}" width="40" height="60"/>')
            
            # Labela
            name = tr.get('name', tr['id'])
            vn = tr.get('vn_kv', '?')
            nn = tr.get('nn_kv', '?')
            mva = tr.get('power_mva', '?')
            
            parts.append(f'''
    <text x="{tx+50}" y="{ty+20}" font-size="11" fill="#333">{name}</text>
    <text x="{tx+50}" y="{ty+35}" font-size="10" fill="#666">{vn}/{nn} kV</text>
    <text x="{tx+50}" y="{ty+48}" font-size="10" fill="#666">{mva} MVA</text>
''')
        
        return '\n'.join(parts)
    
    def _render_legend(self, width: int, height: int) -> str:
        """Renderuj legendu."""
        lx = 20
        ly = height - 100
        
        return f'''
    <!-- Legenda -->
    <rect x="{lx}" y="{ly}" width="200" height="90" fill="#fff" stroke="#ddd" rx="5"/>
    <text x="{lx+10}" y="{ly+18}" font-size="12" font-weight="bold" fill="#333">Legenda</text>
    
    <use href="#breaker-closed" x="{lx+10}" y="{ly+25}" width="15" height="30"/>
    <text x="{lx+35}" y="{ly+42}" font-size="10" fill="#333">Prekidač (zatvoren)</text>
    
    <use href="#breaker-open" x="{lx+110}" y="{ly+25}" width="15" height="30"/>
    <text x="{lx+135}" y="{ly+42}" font-size="10" fill="#333">Prekidač (otvoren)</text>
    
    <use href="#disconnector-closed" x="{lx+10}" y="{ly+55}" width="15" height="25"/>
    <text x="{lx+35}" y="{ly+70}" font-size="10" fill="#333">Rastavljač (zatvoren)</text>
    
    <use href="#ct" x="{lx+110}" y="{ly+55}" width="15" height="15"/>
    <text x="{lx+135}" y="{ly+70}" font-size="10" fill="#333">Strujna merenja</text>
'''
    
    def _get_voltage_color(self, voltage: int) -> str:
        """Boja za naponski nivo."""
        if voltage >= 400:
            return self.cfg.color_400kv
        elif voltage >= 220:
            return self.cfg.color_220kv
        else:
            return self.cfg.color_110kv
    
    def _error_svg(self, message: str) -> str:
        """SVG za grešku."""
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 200" width="400" height="200">
    <rect width="100%" height="100%" fill="#fee"/>
    <text x="200" y="100" text-anchor="middle" font-size="14" fill="#c00">{message}</text>
</svg>'''


# Export funkcija za korišćenje iz servera
def generate_single_line_diagram(graph, eeo_id: str) -> str:
    """Generiši SVG jednopolnu šemu za EEO."""
    generator = SingleLineDiagramGenerator(graph)
    return generator.generate_eeo_diagram(eeo_id)
