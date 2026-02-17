#!/usr/bin/env python3
"""
Exporter za vis.js format.

Konvertuje GridKnowledgeGraph u JSON format kompatibilan sa vis.js.
"""

import json
from typing import Dict, List, Any, Optional
from pathlib import Path


# Boje i oblici po tipu čvora
NODE_STYLES = {
    "EEO": {"color": "#E91E63", "shape": "box", "size": 40, "font_size": 18},
    "GSS": {"color": "#4CAF50", "shape": "dot", "size": 25, "font_size": 14},
    "PSS": {"color": "#8BC34A", "shape": "dot", "size": 20, "font_size": 12},
    "DVP": {"color": "#2196F3", "shape": "diamond", "size": 20, "font_size": 12},
    "KBP": {"color": "#00BCD4", "shape": "diamond", "size": 20, "font_size": 12},
    "TRP": {"color": "#FF9800", "shape": "diamond", "size": 20, "font_size": 12},
    "GSP": {"color": "#9C27B0", "shape": "diamond", "size": 18, "font_size": 11},
    "PSP": {"color": "#673AB7", "shape": "diamond", "size": 18, "font_size": 11},
    "P": {"color": "#F44336", "shape": "triangle", "size": 15, "font_size": 10},
    "SR": {"color": "#CDDC39", "shape": "square", "size": 12, "font_size": 10},
    "SMT": {"color": "#795548", "shape": "triangleDown", "size": 12, "font_size": 10},
    "NMT": {"color": "#607D8B", "shape": "triangleDown", "size": 10, "font_size": 9},
    "IRSU": {"color": "#FF5722", "shape": "star", "size": 15, "font_size": 10},
    "TR": {"color": "#FFC107", "shape": "hexagon", "size": 30, "font_size": 14},
    "DV": {"color": "#3F51B5", "shape": "ellipse", "size": 25, "font_size": 12},
    "KB": {"color": "#009688", "shape": "ellipse", "size": 25, "font_size": 12},
}

# Boje ivica po tipu
EDGE_STYLES = {
    "GALVANSKI_VEZAN": {"color": "#4CAF50", "dashes": False, "width": 2},
    "SADRZI": {"color": "#9E9E9E", "dashes": True, "width": 1},
    "PRIPADA": {"color": "#9E9E9E", "dashes": True, "width": 1},
    "POVEZUJE": {"color": "#2196F3", "dashes": False, "width": 3},
    "NAPAJA": {"color": "#FF9800", "dashes": False, "width": 2},
}


class VisJsExporter:
    """Exporter za vis.js vizualizaciju."""
    
    def __init__(self, graph):
        """
        Args:
            graph: GridKnowledgeGraph instanca
        """
        self.graph = graph
    
    def export_nodes(self, filter_types: Optional[List[str]] = None) -> List[Dict]:
        """
        Exportuj čvorove za vis.js.
        
        Args:
            filter_types: Lista tipova čvorova za uključiti (None = sve)
        
        Returns:
            Lista čvorova u vis.js formatu
        """
        nodes = []
        
        for node_id in self.graph._graph.nodes():
            node_data = self.graph.get_node(node_id)
            if not node_data:
                continue
            
            node_type = node_data.get("node_type", "unknown")
            
            # Filtriraj po tipu
            if filter_types and node_type not in filter_types:
                continue
            
            style = NODE_STYLES.get(node_type, {"color": "#757575", "shape": "dot", "size": 10, "font_size": 10})
            
            # Labela
            label = node_data.get("name", node_id)
            if len(label) > 20:
                label = label[:17] + "..."
            
            # Tooltip
            title = self._build_tooltip(node_id, node_data)
            
            # Level za hijerarhijski layout
            level = self._get_node_level(node_type)
            
            vis_node = {
                "id": node_id,
                "label": label,
                "title": title,
                "color": style["color"],
                "shape": style["shape"],
                "size": style["size"],
                "font": {"size": style["font_size"]},
                "level": level,
                "group": node_type,
                # Custom data
                "nodeType": node_type,
                "eeoId": node_data.get("eeo_id"),
                "voltageKv": node_data.get("voltage_kv"),
            }
            
            nodes.append(vis_node)
        
        return nodes
    
    def export_edges(self, filter_types: Optional[List[str]] = None) -> List[Dict]:
        """
        Exportuj ivice za vis.js.
        
        Args:
            filter_types: Lista tipova ivica za uključiti (None = sve)
        
        Returns:
            Lista ivica u vis.js formatu
        """
        edges = []
        seen = set()  # Za izbegavanje duplikata
        
        for u, v, data in self.graph._graph.edges(data=True):
            edge_type = data.get("edge_type", "unknown")
            
            # Filtriraj po tipu
            if filter_types and edge_type not in filter_types:
                continue
            
            # Izbegni duplikate
            edge_key = tuple(sorted([u, v])) + (edge_type,)
            if edge_key in seen:
                continue
            seen.add(edge_key)
            
            style = EDGE_STYLES.get(edge_type, {"color": "#9E9E9E", "dashes": False, "width": 1})
            
            vis_edge = {
                "from": u,
                "to": v,
                "color": {"color": style["color"]},
                "dashes": style["dashes"],
                "width": style["width"],
                "title": edge_type,
                "edgeType": edge_type,
            }
            
            # Arrows za određene tipove
            if edge_type in ("SADRZI", "PRIPADA", "NAPAJA"):
                vis_edge["arrows"] = {"to": {"enabled": True, "scaleFactor": 0.5}}
            
            edges.append(vis_edge)
        
        return edges
    
    def export_json(
        self,
        filepath: Optional[Path] = None,
        filter_node_types: Optional[List[str]] = None,
        filter_edge_types: Optional[List[str]] = None,
    ) -> Dict:
        """
        Exportuj ceo graf u JSON format.
        
        Args:
            filepath: Putanja za čuvanje JSON-a (opciono)
            filter_node_types: Lista tipova čvorova
            filter_edge_types: Lista tipova ivica
        
        Returns:
            Dict sa nodes i edges
        """
        data = {
            "nodes": self.export_nodes(filter_node_types),
            "edges": self.export_edges(filter_edge_types),
            "metadata": {
                "total_nodes": len(self.graph._graph.nodes()),
                "total_edges": len(self.graph._graph.edges()),
                "stats": self.graph.get_stats(),
            }
        }
        
        if filepath:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        
        return data
    
    def _build_tooltip(self, node_id: str, node_data: Dict) -> str:
        """Gradi HTML tooltip za čvor."""
        lines = [f"<b>{node_id}</b>"]
        
        # Tip
        if "node_type" in node_data:
            lines.append(f"Tip: {node_data['node_type']}")
        
        # Napon
        if "voltage_kv" in node_data:
            lines.append(f"Napon: {node_data['voltage_kv']} kV")
        
        # Status
        if "status" in node_data:
            status = "UKLJUČEN" if node_data["status"] == 1 else "ISKLJUČEN"
            lines.append(f"Status: {status}")
        
        # EEO
        if "eeo_id" in node_data and node_data["eeo_id"]:
            lines.append(f"EEO: {node_data['eeo_id']}")
        
        # Snaga (za TR)
        if "power_mva" in node_data and node_data["power_mva"]:
            lines.append(f"Snaga: {node_data['power_mva']} MVA")
        
        return "<br>".join(lines)
    
    def _get_node_level(self, node_type: str) -> int:
        """Vraća nivo čvora za hijerarhijski layout."""
        levels = {
            "EEO": 0,
            "GSS": 1,
            "PSS": 1,
            "DVP": 2,
            "KBP": 2,
            "TRP": 2,
            "GSP": 2,
            "PSP": 2,
            "TR": 2,
            "SR": 3,
            "P": 3,
            "SMT": 4,
            "NMT": 4,
            "IRSU": 4,
            "DV": 5,
            "KB": 5,
        }
        return levels.get(node_type, 3)
