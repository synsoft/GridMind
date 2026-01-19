"""
Graph builder for power grid network.

Builds an undirected graph from dv_station_map_with_voltage.json where:
- Nodes: Substations (ТС, РП, ХЕ, ТЕ, etc.)
- Edges: Transmission lines with their IDs and voltage levels
"""

import json
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set, Tuple, Optional


class GridGraph:
    """
    Represents the power grid as an undirected graph.
    
    Attributes:
        adjacency: Dict mapping station -> list of (neighbor, line_id, voltage_kv) tuples
        stations: Set of all station names
        lines: Dict mapping line_id -> {"connections": [...], "voltage_kv": int}
    """
    
    def __init__(self):
        self.adjacency: Dict[str, List[Tuple[str, str, int]]] = defaultdict(list)
        self.stations: Set[str] = set()
        self.lines: Dict[str, Dict] = {}  # line_id -> {"connections": [...], "voltage_kv": int}
    
    def add_edge(self, station1: str, station2: str, line_id: str, voltage_kv: int = 110) -> None:
        """Add an undirected edge between two stations."""
        self.stations.add(station1)
        self.stations.add(station2)
        
        # Add bidirectional edges with voltage info
        self.adjacency[station1].append((station2, line_id, voltage_kv))
        self.adjacency[station2].append((station1, line_id, voltage_kv))
        
        # Track line connections with voltage
        if line_id not in self.lines:
            self.lines[line_id] = {"connections": [], "voltage_kv": voltage_kv}
        self.lines[line_id]["connections"].append((station1, station2))
    
    def get_neighbors(self, station: str, voltage_kv: Optional[int] = None) -> List[Tuple[str, str, int]]:
        """
        Get all neighbors of a station with their connecting line IDs and voltage.
        
        Args:
            station: The station name
            voltage_kv: If provided, filter only neighbors connected at this voltage level
        
        Returns:
            List of (neighbor, line_id, voltage_kv) tuples
        """
        neighbors = self.adjacency.get(station, [])
        if voltage_kv is not None:
            neighbors = [(n, l, v) for n, l, v in neighbors if v == voltage_kv]
        return neighbors
    
    def get_direct_connections(self, station1: str, station2: str, voltage_kv: Optional[int] = None) -> List[Tuple[str, int]]:
        """
        Get all line IDs that directly connect two stations.
        
        Args:
            station1, station2: Station names
            voltage_kv: If provided, filter only connections at this voltage level
        
        Returns:
            List of (line_id, voltage_kv) tuples
        """
        direct_lines = []
        for neighbor, line_id, v in self.adjacency.get(station1, []):
            if neighbor == station2:
                if voltage_kv is None or v == voltage_kv:
                    direct_lines.append((line_id, v))
        return direct_lines
    
    def get_line_voltage(self, line_id: str) -> Optional[int]:
        """Get the voltage level of a transmission line."""
        if line_id in self.lines:
            return self.lines[line_id]["voltage_kv"]
        return None
    
    def station_exists(self, station: str) -> bool:
        """Check if a station exists in the graph."""
        return station in self.stations
    
    def find_similar_stations(self, query: str, limit: int = 5) -> List[str]:
        """Find stations with names similar to the query (case-insensitive partial match)."""
        query_lower = query.lower()
        matches = []
        for station in self.stations:
            if query_lower in station.lower():
                matches.append(station)
        return sorted(matches)[:limit]
    
    def get_station_count(self) -> int:
        """Return the number of stations in the graph."""
        return len(self.stations)
    
    def get_line_count(self) -> int:
        """Return the number of unique transmission lines."""
        return len(self.lines)
    
    def get_edge_count(self) -> int:
        """Return the total number of edges (connections)."""
        return sum(len(line_data["connections"]) for line_data in self.lines.values())
    
    def get_lines_by_voltage(self, voltage_kv: int) -> List[str]:
        """Get all line IDs at a specific voltage level."""
        return [line_id for line_id, data in self.lines.items() if data["voltage_kv"] == voltage_kv]
    
    def get_voltage_stats(self) -> Dict[int, int]:
        """Get count of lines per voltage level."""
        stats = {400: 0, 220: 0, 110: 0}
        for data in self.lines.values():
            v = data["voltage_kv"]
            if v in stats:
                stats[v] += 1
        return stats

    @classmethod
    def from_json_file(cls, json_path: Optional[str] = None) -> 'GridGraph':
        """
        Build the graph from dv_station_map_with_voltage.json.
        
        Args:
            json_path: Path to the JSON file. If None, uses default location.
        
        Returns:
            GridGraph instance populated with network data.
        """
        if json_path is None:
            # Default path - try voltage map first, fall back to complete map
            voltage_path = Path(__file__).parent.parent / "dv_station_map_with_voltage.json"
            complete_path = Path(__file__).parent.parent / "dv_station_map_complete.json"
            
            if voltage_path.exists():
                json_path = voltage_path
            else:
                json_path = complete_path
        else:
            json_path = Path(json_path)
        
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        graph = cls()
        
        # Handle both old and new format
        for line_id, line_data in data.items():
            # New format: {"stations": [...], "voltage_kv": int}
            if isinstance(line_data, dict) and "stations" in line_data:
                connections = line_data["stations"]
                voltage_kv = line_data.get("voltage_kv", 110)
            # Old format: [[station1, station2], ...]
            else:
                connections = line_data
                voltage_kv = 110  # Default
            
            for connection in connections:
                if len(connection) == 2:
                    station1, station2 = connection
                    graph.add_edge(station1, station2, line_id, voltage_kv)
        
        return graph
    
    def __repr__(self) -> str:
        return f"GridGraph(stations={self.get_station_count()}, lines={self.get_line_count()}, edges={self.get_edge_count()})"


# Global cached instance
_cached_graph: Optional[GridGraph] = None


def get_grid_graph(force_reload: bool = False) -> GridGraph:
    """
    Get the cached grid graph instance, building it if necessary.
    
    Args:
        force_reload: If True, rebuild the graph even if cached.
    
    Returns:
        The GridGraph instance.
    """
    global _cached_graph
    
    if _cached_graph is None or force_reload:
        _cached_graph = GridGraph.from_json_file()
    
    return _cached_graph
