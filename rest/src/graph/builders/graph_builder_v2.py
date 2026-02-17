#!/usr/bin/env python3
"""
Graph Builder v2 - koristi UputstvoParserV2 sa punim mapiranjem DV destinacija.

Poboljšanja nad v1:
- Koristi parser v2 sa voltage-grouped DV
- Mapira sve 110kV DV na susedne EEO
- Dodaje connectivity matricu pravilno
- Snima/učitava graf u JSON format (perzistencija)
"""

import json
import sys
import re
from pathlib import Path
from typing import Optional, Dict, List
from dataclasses import asdict

# Popravi import path
_current_dir = Path(__file__).parent
_graph_dir = _current_dir.parent
_src_dir = _graph_dir.parent
_rest_dir = _src_dir.parent

sys.path.insert(0, str(_rest_dir))
sys.path.insert(0, str(_graph_dir / "parsers"))

from src.graph import GridKnowledgeGraph
from uputstvo_parser_v2 import UputstvoParserV2, EEOParsedDataV2


class GraphBuilderV2:
    """Builder za kreiranje grafa iz Uputstava za pogon - v2."""
    
    SAVE_PATH = Path(__file__).parent.parent.parent.parent / "data" / "knowledge_graph.json"
    
    def __init__(self):
        self.parser = UputstvoParserV2()
        self.graph = GridKnowledgeGraph()
        self._processed_eeo: set = set()
        self._processed_lines: set = set()
    
    def build_from_directory(self, dirpath: Path) -> GridKnowledgeGraph:
        """Gradi graf iz svih uputstava u direktorijumu."""
        all_data = self.parser.parse_directory(dirpath)
        
        # Faza 1: Dodaj sve EEO sa kompletnom strukturom
        for data in all_data:
            self._add_eeo_full(data)
        
        # Faza 2: Dodaj dalekovode sa ispravnim destinacijama
        for data in all_data:
            self._add_dalekovodi_v2(data)
        
        # Faza 3: Dodaj transformatore
        for data in all_data:
            self._add_transformatori(data)
        
        return self.graph
    
    def build_from_file(self, filepath: Path) -> GridKnowledgeGraph:
        """Gradi graf iz jednog uputstva."""
        data = self.parser.parse_file(filepath)
        if data:
            self._add_eeo_full(data)
            self._add_dalekovodi_v2(data)
            self._add_transformatori(data)
        return self.graph
    
    # =========================================================================
    # EEO DODAVANJE
    # =========================================================================
    
    def _add_eeo_full(self, data: EEOParsedDataV2):
        """Dodaj EEO sa kompletnom hijerarhijom čvorova."""
        if data.kod in self._processed_eeo:
            return
        
        # Dodaj EEO čvor
        self.graph.add_eeo(
            id=data.kod,
            name=data.naziv,
            code=data.kod,
            type=data.tip,
            voltage_levels=data.naponski_nivoi
        )
        
        # Dodaj UEEO čvor (uzemljenje EEO) — referentna tačka za OP elemente
        ueeo_id = f"{data.kod}_UEEO"
        self.graph._graph.add_node(ueeo_id, node_type="UEEO", eeo_id=data.kod, id=ueeo_id)
        self.graph._nodes_by_type["UEEO"].add(ueeo_id)
        self.graph._nodes_by_eeo[data.kod].add(ueeo_id)
        self.graph._graph.add_edge(data.kod, ueeo_id, edge_type="SADRZI")
        
        # Napravi lookup transformatora po broju za VN/NN određivanje
        self._tr_lookup: Dict[int, 'TransformatorInfo'] = {}
        for tr in data.transformatori:
            match = re.search(r"TR(\d+)", tr.oznaka)
            if match:
                self._tr_lookup[int(match.group(1))] = tr
        
        # Dodaj sisteme sabirnica za svaki naponski nivo
        # Broj GS određujemo iz uklopnog stanja (da li postoje polja na GS2)
        normalno = data.uklopna_stanja.get("normalno", {})
        for napon in data.naponski_nivoi:
            self.graph.add_busbar(eeo_id=data.kod, type="GSS", voltage_kv=napon, index=1)
            # Dodaj GS2 ako uklopno stanje ima polja na drugom sistemu sabirnica
            us = normalno.get(napon)
            has_gs2 = us and len(us.polja_gs2) > 0
            if has_gs2 or napon in (400, 110):
                self.graph.add_busbar(eeo_id=data.kod, type="GSS", voltage_kv=napon, index=2)
        
        # Dodaj polja iz normalnog uklopnog stanja
        normalno = data.uklopna_stanja.get("normalno", {})
        for napon_kv, us in normalno.items():
            self._add_polja_from_uklopno_stanje(data.kod, us, data)
        
        # Ako nema uklopnog stanja, dodaj polja iz DV liste
        if not normalno:
            self._add_polja_from_dalekovodi(data)
        
        self._processed_eeo.add(data.kod)
    
    def _add_polja_from_uklopno_stanje(self, eeo_id: str, us, data: EEOParsedDataV2):
        """Dodaj polja iz uklopnog stanja."""
        # GS1 polja
        for polje_oznaka in us.polja_gs1:
            self._add_polje(eeo_id, us.napon_kv, polje_oznaka, gss_index=1)
        
        # GS2 polja
        for polje_oznaka in us.polja_gs2:
            self._add_polje(eeo_id, us.napon_kv, polje_oznaka, gss_index=2)
        
        # Spojno polje → GSP (ako postoji dupli GS)
        gss2_id = f"{eeo_id}_GSS_{us.napon_kv}_2"
        if us.spojno_polje in ("ukljuceno", "iskljuceno") and self.graph.get_node(gss2_id):
            sp_status = 1 if us.spojno_polje == "ukljuceno" else 0
            self.graph.create_gsp_with_elements(
                eeo_id=eeo_id,
                voltage_kv=us.napon_kv,
                index=1,
                gss_from_index=1,
                gss_to_index=2,
                all_status=sp_status,
            )
    
    def _add_polja_from_dalekovodi(self, data: EEOParsedDataV2):
        """Dodaj polja direktno iz liste dalekovoda (kada nema uklopnog stanja)."""
        for napon, dvs in data.dalekovodi.items():
            for dv in dvs:
                oznaka = dv.oznaka.replace("DV ", "DV").replace(" ", "")
                self._add_polje(data.kod, napon, oznaka, gss_index=1)
    
    def _add_polje(self, eeo_id: str, napon_kv: int, oznaka: str, gss_index: int):
        """Dodaj pojedinačno polje sa elementima.
        
        Handles DV (dalekovod), KB (kabel), MV (merenje/veza) entries.
        """
        if oznaka.startswith("DV"):
            index_str = oznaka[2:].replace("/", "_")
            
            # Kreiraj kompletno DVP sa elementima
            self.graph.create_dvp_with_elements(
                eeo_id=eeo_id,
                voltage_kv=napon_kv,
                index=index_str,
                line_name=oznaka,
                gss_index=gss_index,
                all_status=1  # Normalno - sve uključeno
            )
        elif oznaka.startswith("KB"):
            # Kabelsko polje - tretiraj isto kao DV
            index_str = oznaka[2:].replace("/", "_")
            self.graph.create_dvp_with_elements(
                eeo_id=eeo_id,
                voltage_kv=napon_kv,
                index=index_str,
                line_name=oznaka,
                gss_index=gss_index,
                all_status=1
            )
        elif oznaka.startswith("MV"):
            # Merno polje - tretiraj isto kao DV
            index_str = oznaka[2:].replace("/", "_")
            self.graph.create_dvp_with_elements(
                eeo_id=eeo_id,
                voltage_kv=napon_kv,
                index=index_str,
                line_name=oznaka,
                gss_index=gss_index,
                all_status=1
            )
        elif oznaka.startswith("TR"):
            # Transformatorsko polje — odredi VN ili NN stranu
            match = re.search(r"TR\s*(\d+)", oznaka)
            tr_num = int(match.group(1)) if match else 1
            index_str = f"TR{tr_num}"
            
            tr_info = self._tr_lookup.get(tr_num)
            tr_node_id = f"{eeo_id}_TR_{tr_num}"
            
            if tr_info and napon_kv == tr_info.vn_kv:
                # Viša strana → TRPVN
                self.graph.create_trpvn_with_elements(
                    eeo_id=eeo_id,
                    voltage_kv=napon_kv,
                    index=index_str,
                    line_name=oznaka,
                    gss_index=gss_index,
                    tr_node_id=tr_node_id if self.graph.get_node(tr_node_id) else None,
                    all_status=1,
                )
            elif tr_info and napon_kv == tr_info.nn_kv:
                # Niža strana → TRPNN
                self.graph.create_trpnn_with_elements(
                    eeo_id=eeo_id,
                    voltage_kv=napon_kv,
                    index=index_str,
                    line_name=oznaka,
                    gss_index=gss_index,
                    tr_node_id=tr_node_id if self.graph.get_node(tr_node_id) else None,
                    all_status=1,
                )
            elif tr_info and tr_info.treci_namot and napon_kv == tr_info.treci_namot:
                # Tercijer → TRPNN
                self.graph.create_trpnn_with_elements(
                    eeo_id=eeo_id,
                    voltage_kv=napon_kv,
                    index=index_str,
                    line_name=oznaka,
                    gss_index=gss_index,
                    tr_node_id=tr_node_id if self.graph.get_node(tr_node_id) else None,
                    all_status=1,
                )
            else:
                # Nepoznat TR ili nema VN/NN info — fallback na DVP
                self.graph.create_dvp_with_elements(
                    eeo_id=eeo_id,
                    voltage_kv=napon_kv,
                    index=index_str,
                    line_name=oznaka,
                    gss_index=gss_index,
                    all_status=1,
                )
    
    # =========================================================================
    # DALEKOVODI
    # =========================================================================
    
    def _add_dalekovodi_v2(self, data: EEOParsedDataV2):
        """Dodaj dalekovode sa ispravnim destinacijama (v2)."""
        for napon, dvs in data.dalekovodi.items():
            for dv in dvs:
                dest_kod = dv.destinacija_kod
                if not dest_kod:
                    continue
                
                # Jedinstveni ključ: sortirani EEO + DV broj
                line_key = (tuple(sorted([data.kod, dest_kod])), dv.broj)
                if line_key in self._processed_lines:
                    continue
                
                # Osiguraj da destinacija postoji kao EEO
                if dest_kod not in self._processed_eeo:
                    self.graph.add_eeo(
                        id=dest_kod,
                        name=f"TS {dest_kod}",
                        code=dest_kod,
                        type="TS",
                        voltage_levels=[napon]
                    )
                    self.graph.add_busbar(
                        eeo_id=dest_kod, type="GSS",
                        voltage_kv=napon, index=1
                    )
                
                # Nađi DVP na ovoj strani
                from_field_id = self._find_dvp_for_line(data.kod, dv.oznaka, napon)
                
                # Dodaj DV čvor
                line_id = self.graph.add_line(
                    type="DV",
                    name=dv.oznaka,
                    voltage_kv=napon,
                    from_eeo_id=data.kod,
                    from_field_id=from_field_id,
                    from_field_index=1,
                    to_eeo_id=dest_kod,
                    to_field_id=None,
                    to_field_index=1
                )
                
                # Poveži IRSU -> DV
                if from_field_id:
                    irsu_id = f"{from_field_id}_IRSU"
                    if self.graph.get_node(irsu_id):
                        self.graph.add_povezuje(irsu_id, line_id, side="from")
                
                self._processed_lines.add(line_key)
    
    def _find_dvp_for_line(self, eeo_id: str, dv_oznaka: str, napon_kv: int) -> Optional[str]:
        """Nađi DVP ID za datu liniju."""
        match = re.search(r"DV\s*(\d+(?:/\d+)?[A-Za-z]*)", dv_oznaka)
        if match:
            index_str = match.group(1).replace("/", "_").replace(" ", "")
            field_id = f"{eeo_id}_DVP_{napon_kv}_{index_str}"
            if self.graph.get_node(field_id):
                return field_id
        return None
    
    # =========================================================================
    # TRANSFORMATORI
    # =========================================================================
    
    def _add_transformatori(self, data: EEOParsedDataV2):
        """Dodaj transformatore i poveži ih sa TRPVN/TRPNN poljima."""
        for tr in data.transformatori:
            match = re.search(r"TR(\d+)", tr.oznaka)
            index = int(match.group(1)) if match else 1
            
            self.graph.add_transformer(
                eeo_id=data.kod,
                name=tr.oznaka,
                vn_kv=tr.vn_kv,
                nn_kv=tr.nn_kv,
                index=index,
                power_mva=tr.snaga_mva
            )
            
            tr_node_id = f"{data.kod}_TR_{index}"
            
            # Poveži TR sa TRPVN/TRPNN poljima (galvanske veze SMT↔TR, OP↔TR)
            for field_type in ("TRPVN", "TRPNN"):
                field_id = f"{data.kod}_{field_type}_{tr.vn_kv}_TR{index}"
                if not self.graph.get_node(field_id):
                    field_id = f"{data.kod}_{field_type}_{tr.nn_kv}_TR{index}"
                if not self.graph.get_node(field_id):
                    # Probaj tercijer
                    if tr.treci_namot:
                        field_id = f"{data.kod}_{field_type}_{tr.treci_namot}_TR{index}"
                if not self.graph.get_node(field_id):
                    continue
                
                # SMT ↔ TR
                smt_id = f"{field_id}_SMT"
                if self.graph.get_node(smt_id):
                    self.graph.add_galvanska_veza(smt_id, tr_node_id)
                
                # OP ↔ TR
                op_id = f"{field_id}_OP"
                if self.graph.get_node(op_id):
                    self.graph.add_galvanska_veza(op_id, tr_node_id)
                
                # NMT ↔ TR (samo za TRPNN)
                if field_type == "TRPNN":
                    nmt_id = f"{field_id}_NMT"
                    if self.graph.get_node(nmt_id):
                        self.graph.add_galvanska_veza(nmt_id, tr_node_id)
                
                # Ažuriraj transformer_id na polju
                field_node = self.graph.get_node(field_id)
                if field_node:
                    self.graph._graph.nodes[field_id]['transformer_id'] = tr_node_id
    
    # =========================================================================
    # PERZISTENCIJA
    # =========================================================================
    
    def save_graph(self, filepath: Optional[Path] = None) -> Path:
        """Snimi graf u JSON format."""
        filepath = filepath or self.SAVE_PATH
        filepath.parent.mkdir(parents=True, exist_ok=True)
        
        import networkx as nx
        from networkx.readwrite import json_graph
        
        data = json_graph.node_link_data(self.graph._graph)
        
        # Dodaj metadata
        data['_metadata'] = {
            'version': '2.0',
            'nodes_count': self.graph._graph.number_of_nodes(),
            'edges_count': self.graph._graph.number_of_edges(),
            'eeo_count': len(self.graph._eeo_index),
            'processed_eeo': sorted(self._processed_eeo),
        }
        
        # Dodaj connectivity matricu
        data['_connectivity'] = [
            asdict(entry) for entry in self.graph._connectivity_matrix
        ]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2, default=str)
        
        return filepath
    
    def load_graph(self, filepath: Optional[Path] = None) -> Optional[GridKnowledgeGraph]:
        """Učitaj graf iz JSON formata."""
        filepath = filepath or self.SAVE_PATH
        
        if not filepath.exists():
            return None
        
        import networkx as nx
        from networkx.readwrite import json_graph
        
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        metadata = data.pop('_metadata', {})
        connectivity = data.pop('_connectivity', [])
        
        self.graph._graph = json_graph.node_link_graph(data)
        
        # Rekonstruiši indekse
        for node_id, node_data in self.graph._graph.nodes(data=True):
            node_type = node_data.get('node_type', node_data.get('type', ''))
            if node_type:
                self.graph._nodes_by_type[node_type].add(node_id)
            
            # EEO indeks
            if node_type == 'EEO':
                from src.graph.schema.node_types import EEONode
                self.graph._eeo_index[node_id] = node_data
            
            # Nodes by EEO indeks
            eeo_id = node_data.get('eeo_id')
            if eeo_id:
                self.graph._nodes_by_eeo[eeo_id].add(node_id)
        
        # Rekonstruiši connectivity matricu
        from src.graph.schema.edge_types import ConnectivityMatrixEntry
        for entry_data in connectivity:
            self.graph._connectivity_matrix.append(
                ConnectivityMatrixEntry(**entry_data)
            )
        
        self._processed_eeo = set(metadata.get('processed_eeo', []))
        
        return self.graph
    
    def build_or_load(self, dirpath: Path, force_rebuild: bool = False) -> GridKnowledgeGraph:
        """Učitaj sačuvani graf ili izgradi iz dokumenata."""
        if not force_rebuild:
            graph = self.load_graph()
            if graph:
                stats = graph.get_stats()
                print(f"[GraphBuilder] Loaded from cache: {stats['total_nodes']} nodes, {stats['total_edges']} edges")
                return graph
        
        print("[GraphBuilder] Building graph from documents...")
        graph = self.build_from_directory(dirpath)
        
        # Snimi za sledeći put
        save_path = self.save_graph()
        stats = graph.get_stats()
        print(f"[GraphBuilder] Built: {stats['total_nodes']} nodes, {stats['total_edges']} edges")
        print(f"[GraphBuilder] Saved to: {save_path}")
        
        return graph


# CLI za testiranje
if __name__ == "__main__":
    builder = GraphBuilderV2()
    
    if len(sys.argv) > 1:
        path = Path(sys.argv[1])
        force = "--force" in sys.argv
        
        if path.is_dir():
            graph = builder.build_or_load(path, force_rebuild=force)
        else:
            graph = builder.build_from_file(path)
        
        print(f"\n{'=' * 60}")
        print(f"Graf izgrađen!")
        print(f"{'=' * 60}")
        
        stats = graph.get_stats()
        print(f"\nStatistike:")
        print(f"  Ukupno čvorova: {stats['total_nodes']}")
        print(f"  Ukupno ivica: {stats['total_edges']}")
        print(f"  Connectivity: {stats['connectivity_matrix_entries']}")
        print(f"\n  Čvorovi po tipu:")
        for node_type, count in sorted(stats['nodes_by_type'].items()):
            print(f"    {node_type}: {count}")
        
        print(f"\n  EEO objekti:")
        for node_id in sorted(graph.get_nodes_by_type("EEO")):
            node = graph.get_node(node_id)
            print(f"    - {node_id}: {node.get('name', '')}")
        
        # Matrica povezanosti
        matrix = graph.get_connectivity_matrix()
        if matrix:
            print(f"\n  Matrica povezanosti ({len(matrix)}):")
            by_voltage = {}
            for entry in matrix:
                v = entry.voltage_kv
                by_voltage[v] = by_voltage.get(v, 0) + 1
            for v, c in sorted(by_voltage.items(), reverse=True):
                print(f"    {v} kV: {c} veza")
            
            print(f"\n  Prvih 15 veza:")
            for entry in matrix[:15]:
                print(f"    {entry.to_tuple()}")
    else:
        print("Korišćenje: python graph_builder_v2.py <putanja> [--force]")
