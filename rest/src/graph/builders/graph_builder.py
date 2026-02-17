#!/usr/bin/env python3
"""
Graph Builder - kreira GridKnowledgeGraph iz parsiranih podataka.

Koristi UputstvoParser za ekstrakciju podataka i popunjava graf
prema metodologiji relejne zaštite.
"""

import sys
from pathlib import Path
from typing import Optional

# Popravi import path
_current_dir = Path(__file__).parent
_graph_dir = _current_dir.parent
_src_dir = _graph_dir.parent
_rest_dir = _src_dir.parent

sys.path.insert(0, str(_rest_dir))

from src.graph import GridKnowledgeGraph
from src.graph.parsers import UputstvoParser
from src.graph.parsers.uputstvo_parser import EEOParsedData


class GraphBuilder:
    """Builder za kreiranje grafa iz Uputstava za pogon."""
    
    def __init__(self):
        self.parser = UputstvoParser()
        self.graph = GridKnowledgeGraph()
        self._processed_eeo: set[str] = set()
        self._processed_lines: set[str] = set()
    
    def build_from_directory(self, dirpath: Path) -> GridKnowledgeGraph:
        """Gradi graf iz svih uputstava u direktorijumu."""
        # Parsiraj sva uputstva
        all_data = self.parser.parse_directory(dirpath)
        
        # Prvo dodaj sve EEO
        for data in all_data:
            self._add_eeo(data)
        
        # Zatim dodaj dalekovode (povezuje EEO)
        for data in all_data:
            self._add_dalekovodi(data)
        
        # Dodaj transformatore
        for data in all_data:
            self._add_transformatori(data)
        
        return self.graph
    
    def build_from_file(self, filepath: Path) -> GridKnowledgeGraph:
        """Gradi graf iz jednog uputstva."""
        data = self.parser.parse_file(filepath)
        if data:
            self._add_eeo(data)
            self._add_dalekovodi(data)
            self._add_transformatori(data)
        return self.graph
    
    def _add_eeo(self, data: EEOParsedData):
        """Dodaj EEO i njegove osnovne komponente."""
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
        
        # Dodaj sisteme sabirnica za svaki naponski nivo
        for napon in data.naponski_nivoi:
            # Dva sistema sabirnica (GS1, GS2) za 400 i 110 kV
            # Jedan sistem za 220 kV (obično)
            if napon in (400, 110):
                self.graph.add_busbar(eeo_id=data.kod, type="GSS", voltage_kv=napon, index=1)
                self.graph.add_busbar(eeo_id=data.kod, type="GSS", voltage_kv=napon, index=2)
            else:
                self.graph.add_busbar(eeo_id=data.kod, type="GSS", voltage_kv=napon, index=1)
        
        # Dodaj polja iz uklopnog stanja
        for key, us in data.uklopna_stanja.items():
            self._add_polja_from_uklopno_stanje(data.kod, us)
        
        self._processed_eeo.add(data.kod)
    
    def _add_polja_from_uklopno_stanje(self, eeo_id: str, us):
        """Dodaj polja iz uklopnog stanja."""
        # GS1 polja
        for polje_oznaka in us.polja_gs1:
            self._add_polje(eeo_id, us.napon_kv, polje_oznaka, gss_index=1)
        
        # GS2 polja
        for polje_oznaka in us.polja_gs2:
            self._add_polje(eeo_id, us.napon_kv, polje_oznaka, gss_index=2)
    
    def _add_polje(self, eeo_id: str, napon_kv: int, oznaka: str, gss_index: int):
        """Dodaj pojedinačno polje."""
        # Odredi tip polja
        if oznaka.startswith("DV"):
            field_type = "DVP"
            # Izvuci indeks iz oznake (DV403 -> 403)
            index_str = oznaka[2:].replace("/", "_")
            field_id = f"{eeo_id}_DVP_{napon_kv}_{index_str}"
            
            # Kreiraj kompletno DVP sa elementima
            self.graph.create_dvp_with_elements(
                eeo_id=eeo_id,
                voltage_kv=napon_kv,
                index=index_str,
                line_name=oznaka,
                gss_index=gss_index,
                all_status=1  # Normalno uklopno stanje - sve uključeno
            )
            
        elif oznaka.startswith("TR"):
            # Transformatorsko polje - dodaćemo posebno
            pass
    
    def _add_dalekovodi(self, data: EEOParsedData):
        """Dodaj dalekovode i poveži EEO."""
        for dv in data.dalekovodi:
            dest_kod = dv.destinacija_kod
            if not dest_kod:
                continue
            
            # Napravi jedinstveni ključ za DV
            line_key = tuple(sorted([data.kod, dest_kod]))
            if line_key in self._processed_lines:
                continue
            
            # Odredi napon (iz uklopnog stanja ili pretpostavi 400 za međusistemske)
            napon_kv = dv.napon_kv or 400
            
            # Nađi polja na oba kraja
            # Ovo je pojednostavljeno - u realnosti treba tražiti po oznaci
            from_field_id = self._find_dvp_for_line(data.kod, dv.oznaka, napon_kv)
            
            # Dodaj placeholder za drugi kraj ako nema EEO
            if dest_kod not in self._processed_eeo:
                # Dodaj placeholder EEO
                self.graph.add_eeo(
                    id=dest_kod,
                    name=f"TS {dest_kod}",
                    code=dest_kod,
                    type="TS",
                    voltage_levels=[napon_kv]
                )
                self.graph.add_busbar(eeo_id=dest_kod, type="GSS", voltage_kv=napon_kv, index=1)
            
            # Dodaj dalekovod
            line_id = self.graph.add_line(
                type="DV",
                name=dv.oznaka,
                voltage_kv=napon_kv,
                from_eeo_id=data.kod,
                from_field_id=from_field_id,
                from_field_index=1,
                to_eeo_id=dest_kod,
                to_field_id=None,  # Placeholder
                to_field_index=1
            )
            
            # Poveži IRSU sa DV ako ima
            if from_field_id:
                irsu_id = f"{from_field_id}_IRSU"
                if self.graph.get_node(irsu_id):
                    self.graph.add_povezuje(irsu_id, line_id, side="from")
            
            self._processed_lines.add(line_key)
    
    def _find_dvp_for_line(self, eeo_id: str, dv_oznaka: str, napon_kv: int) -> Optional[str]:
        """Nađi DVP ID za datu liniju."""
        # Izvuci broj iz oznake
        import re
        match = re.search(r"DV\s*(\d+(?:/\d+)?)", dv_oznaka)
        if match:
            index_str = match.group(1).replace("/", "_")
            field_id = f"{eeo_id}_DVP_{napon_kv}_{index_str}"
            if self.graph.get_node(field_id):
                return field_id
        return None
    
    def _add_transformatori(self, data: EEOParsedData):
        """Dodaj transformatore."""
        for tr in data.transformatori:
            # Izvuci indeks iz oznake (TR2 -> 2)
            import re
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


# CLI za testiranje
if __name__ == "__main__":
    import sys
    
    builder = GraphBuilder()
    
    if len(sys.argv) > 1:
        path = Path(sys.argv[1])
        
        if path.is_dir():
            graph = builder.build_from_directory(path)
        else:
            graph = builder.build_from_file(path)
        
        print(f"\n{'=' * 60}")
        print("Graf izgrađen!")
        print(f"{'=' * 60}")
        
        stats = graph.get_stats()
        print(f"\nStatistike:")
        print(f"  Ukupno čvorova: {stats['total_nodes']}")
        print(f"  Ukupno ivica: {stats['total_edges']}")
        print(f"\n  Čvorovi po tipu:")
        for node_type, count in sorted(stats['nodes_by_type'].items()):
            print(f"    {node_type}: {count}")
        
        # Prikaži EEO
        print(f"\n  EEO objekti:")
        for node_id in graph.get_nodes_by_type("EEO"):
            node = graph.get_node(node_id)
            print(f"    - {node_id}: {node.get('name', '')}")
        
        # Matrica povezanosti
        matrix = graph.get_connectivity_matrix()
        if matrix:
            print(f"\n  Matrica povezanosti:")
            for entry in matrix[:10]:  # Prvih 10
                print(f"    {entry.to_tuple()}")
    else:
        print("Korišćenje: python graph_builder.py <putanja_do_fajla_ili_direktorijuma>")
