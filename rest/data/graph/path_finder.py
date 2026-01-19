"""
Path finding algorithms for power grid network.

Provides BFS, DFS, and depth-limited search for finding routes
between substations via transmission lines.
"""

from collections import deque
from typing import List, Tuple, Optional, Dict, Set
from dataclasses import dataclass

from .graph_builder import GridGraph, get_grid_graph


@dataclass
class PathSegment:
    """Represents a segment in a path."""
    from_station: str
    to_station: str
    line_id: str
    voltage_kv: int = 110  # Default to 110 kV


@dataclass
class PathResult:
    """Represents a complete path between two stations."""
    segments: List[PathSegment]
    
    @property
    def length(self) -> int:
        """Number of hops (intermediate stations) in the path."""
        return len(self.segments)
    
    @property
    def stations(self) -> List[str]:
        """List of all stations in order."""
        if not self.segments:
            return []
        result = [self.segments[0].from_station]
        for seg in self.segments:
            result.append(seg.to_station)
        return result
    
    @property
    def lines(self) -> List[str]:
        """List of all line IDs used in the path."""
        return [seg.line_id for seg in self.segments]
    
    @property
    def voltages(self) -> List[int]:
        """List of voltage levels for each segment."""
        return [seg.voltage_kv for seg in self.segments]
    
    @property
    def is_single_voltage(self) -> bool:
        """Check if all segments are at the same voltage level."""
        if not self.segments:
            return True
        return len(set(self.voltages)) == 1
    
    @property
    def voltage_kv(self) -> Optional[int]:
        """Get the voltage level if all segments are at the same level."""
        if self.is_single_voltage and self.segments:
            return self.segments[0].voltage_kv
        return None
    
    def to_dict(self) -> dict:
        """Convert to dictionary representation."""
        return {
            "length": self.length,
            "stations": self.stations,
            "lines": self.lines,
            "voltages": self.voltages,
            "is_single_voltage": self.is_single_voltage,
            "voltage_kv": self.voltage_kv,
            "segments": [
                {
                    "from": seg.from_station,
                    "to": seg.to_station,
                    "line": seg.line_id,
                    "voltage_kv": seg.voltage_kv
                }
                for seg in self.segments
            ]
        }
    
    def to_text(self) -> str:
        """Human-readable text representation."""
        if not self.segments:
            return "Празна путања"
        
        lines = []
        voltage_info = f" ({self.voltage_kv} kV)" if self.is_single_voltage else " (мешовити напони)"
        lines.append(f"Путања ({self.length} {'скок' if self.length == 1 else 'скокова'}){voltage_info}:")
        lines.append(f"  {self.segments[0].from_station}")
        for seg in self.segments:
            lines.append(f"    ──[ДВ {seg.line_id} ({seg.voltage_kv} kV)]──>")
            lines.append(f"  {seg.to_station}")
        return "\n".join(lines)


class PathFinder:
    """
    Path finding service for the power grid network.
    
    Provides three search strategies:
    1. BFS - finds shortest path (fewest hops)
    2. DFS - finds all possible paths
    3. Limited search - finds paths up to a maximum depth
    
    All methods support optional voltage filtering.
    """
    
    def __init__(self, graph: Optional[GridGraph] = None):
        """
        Initialize PathFinder.
        
        Args:
            graph: GridGraph instance. If None, uses cached global instance.
        """
        self.graph = graph or get_grid_graph()
    
    def find_shortest_path(
        self, 
        start: str, 
        end: str, 
        voltage_kv: Optional[int] = None
    ) -> Optional[PathResult]:
        """
        Find the shortest path between two stations using BFS.
        
        Args:
            start: Starting station name
            end: Destination station name
            voltage_kv: If provided, only use lines at this voltage level
        
        Returns:
            PathResult if path exists, None otherwise.
        """
        if start == end:
            return PathResult(segments=[])
        
        if not self.graph.station_exists(start) or not self.graph.station_exists(end):
            return None
        
        # BFS with path reconstruction
        queue = deque([(start, [])])  # (current_station, path_so_far)
        visited: Set[str] = {start}
        
        while queue:
            current, path = queue.popleft()
            
            for neighbor, line_id, v in self.graph.get_neighbors(current, voltage_kv):
                if neighbor == end:
                    # Found the destination
                    new_path = path + [PathSegment(current, neighbor, line_id, v)]
                    return PathResult(segments=new_path)
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = path + [PathSegment(current, neighbor, line_id, v)]
                    queue.append((neighbor, new_path))
        
        return None  # No path found
    
    def find_all_paths(
        self, 
        start: str, 
        end: str, 
        max_depth: int = 5,
        max_results: int = 10,
        voltage_kv: Optional[int] = None
    ) -> List[PathResult]:
        """
        Find all paths between two stations using DFS with depth limit.
        
        Args:
            start: Starting station name
            end: Destination station name
            max_depth: Maximum number of hops allowed
            max_results: Maximum number of paths to return
            voltage_kv: If provided, only use lines at this voltage level
        
        Returns:
            List of PathResult objects, sorted by length.
        """
        if start == end:
            return [PathResult(segments=[])]
        
        if not self.graph.station_exists(start) or not self.graph.station_exists(end):
            return []
        
        results: List[PathResult] = []
        
        def dfs(current: str, path: List[PathSegment], visited: Set[str]):
            if len(results) >= max_results:
                return
            
            if len(path) > max_depth:
                return
            
            for neighbor, line_id, v in self.graph.get_neighbors(current, voltage_kv):
                if neighbor == end:
                    new_path = path + [PathSegment(current, neighbor, line_id, v)]
                    results.append(PathResult(segments=new_path))
                elif neighbor not in visited and len(path) < max_depth:
                    visited.add(neighbor)
                    new_path = path + [PathSegment(current, neighbor, line_id, v)]
                    dfs(neighbor, new_path, visited)
                    visited.remove(neighbor)
        
        visited = {start}
        dfs(start, [], visited)
        
        # Sort by path length
        results.sort(key=lambda p: p.length)
        return results
    
    def find_paths_limited(
        self, 
        start: str, 
        end: str, 
        max_depth: int = 3,
        voltage_kv: Optional[int] = None
    ) -> List[PathResult]:
        """
        Find all paths up to a specified depth (recommended for queries).
        
        This is the recommended method for answering user queries as it
        limits results to practical routes.
        
        Args:
            start: Starting station name
            end: Destination station name
            max_depth: Maximum number of hops (default 3)
            voltage_kv: If provided, only use lines at this voltage level
        
        Returns:
            List of PathResult objects within depth limit, sorted by length.
        """
        return self.find_all_paths(start, end, max_depth=max_depth, max_results=20, voltage_kv=voltage_kv)
    
    def get_direct_lines(self, station1: str, station2: str, voltage_kv: Optional[int] = None) -> List[Tuple[str, int]]:
        """
        Get transmission lines that directly connect two stations.
        
        Args:
            station1: First station name
            station2: Second station name
            voltage_kv: If provided, filter by voltage level
        
        Returns:
            List of (line_id, voltage_kv) tuples that directly connect the stations.
        """
        return self.graph.get_direct_connections(station1, station2, voltage_kv)
    
    def find_connection(
        self, 
        start: str, 
        end: str, 
        max_depth: int = 4,
        voltage_kv: Optional[int] = None
    ) -> dict:
        """
        Main method for answering connection queries.
        
        Returns a comprehensive result including:
        - Direct connections (if any)
        - Shortest path
        - Alternative paths grouped by voltage level
        
        Args:
            start: Starting station name
            end: Destination station name
            max_depth: Maximum search depth
            voltage_kv: If provided, only search at this voltage level
        
        Returns:
            Dictionary with connection information.
        """
        result = {
            "start": start,
            "end": end,
            "start_exists": self.graph.station_exists(start),
            "end_exists": self.graph.station_exists(end),
            "voltage_filter": voltage_kv,
            "direct_lines": [],
            "direct_lines_by_voltage": {},  # Grouped by voltage
            "shortest_path": None,
            "paths_by_voltage": {},  # Paths grouped by voltage (only single-voltage paths)
            "mixed_voltage_paths": [],  # Paths that cross voltage levels
            "alternative_paths": [],  # Legacy - all alternatives
            "suggestions": {}
        }
        
        # Check if stations exist
        if not result["start_exists"]:
            result["suggestions"]["start"] = self.graph.find_similar_stations(start)
        if not result["end_exists"]:
            result["suggestions"]["end"] = self.graph.find_similar_stations(end)
        
        if not result["start_exists"] or not result["end_exists"]:
            return result
        
        # Check for direct connections - group by voltage
        direct = self.get_direct_lines(start, end, voltage_kv)
        result["direct_lines"] = [{"line": l, "voltage_kv": v} for l, v in direct]
        
        # Group direct lines by voltage
        for line, v in direct:
            if v not in result["direct_lines_by_voltage"]:
                result["direct_lines_by_voltage"][v] = []
            result["direct_lines_by_voltage"][v].append(line)
        
        # Find all paths
        all_paths = self.find_paths_limited(start, end, max_depth=max_depth, voltage_kv=voltage_kv)
        
        if all_paths:
            result["shortest_path"] = all_paths[0].to_dict()
            
            # Group paths by voltage level
            for path in all_paths[1:]:  # Skip shortest (already shown)
                path_dict = path.to_dict()
                if path.is_single_voltage and path.voltage_kv:
                    v = path.voltage_kv
                    if v not in result["paths_by_voltage"]:
                        result["paths_by_voltage"][v] = []
                    # Limit to 3 per voltage level
                    if len(result["paths_by_voltage"][v]) < 3:
                        result["paths_by_voltage"][v].append(path_dict)
                else:
                    # Mixed voltage path
                    if len(result["mixed_voltage_paths"]) < 3:
                        result["mixed_voltage_paths"].append(path_dict)
            
            # Legacy: all alternatives (for backward compatibility)
            if len(all_paths) > 1:
                result["alternative_paths"] = [p.to_dict() for p in all_paths[1:5]]
        
        return result
    
    def format_answer(self, start: str, end: str, max_depth: int = 4, voltage_kv: Optional[int] = None) -> str:
        """
        Format a human-readable answer for connection query.
        
        Args:
            start: Starting station name
            end: Destination station name
            max_depth: Maximum search depth
            voltage_kv: If provided, filter by voltage level
        
        Returns:
            Formatted answer string in Serbian.
        """
        conn = self.find_connection(start, end, max_depth, voltage_kv)
        
        lines = []
        
        # Show voltage filter if applied
        if voltage_kv:
            lines.append(f"**Филтер:** Само {voltage_kv} kV далеководи\n")
        
        # Handle non-existent stations
        if not conn["start_exists"]:
            lines.append(f"Станица '{start}' није пронађена у бази.")
            if conn["suggestions"].get("start"):
                lines.append(f"Можда сте мислили: {', '.join(conn['suggestions']['start'])}")
            return "\n".join(lines)
        
        if not conn["end_exists"]:
            lines.append(f"Станица '{end}' није пронађена у бази.")
            if conn["suggestions"].get("end"):
                lines.append(f"Можда сте мислили: {', '.join(conn['suggestions']['end'])}")
            return "\n".join(lines)
        
        # Direct connections grouped by voltage
        if conn["direct_lines_by_voltage"]:
            lines.append(f"**Директне везе:**")
            for v in sorted(conn["direct_lines_by_voltage"].keys(), reverse=True):
                dv_list = conn["direct_lines_by_voltage"][v]
                dv_str = ", ".join([f"ДВ {dv}" for dv in dv_list])
                lines.append(f"  • {v} kV: {dv_str}")
            lines.append("")
        
        # Shortest path
        if conn["shortest_path"]:
            path = conn["shortest_path"]
            if path["length"] == 0:
                lines.append("Исте станице - нема потребе за везом.")
            elif conn["direct_lines"]:
                pass  # Already shown above
            else:
                voltage_info = f" ({path['voltage_kv']} kV)" if path.get("is_single_voltage") and path.get("voltage_kv") else " (мешовити напони)"
                lines.append(f"**Најкраћа путања** ({path['length']} скок/ова){voltage_info}:")
                segments = path["segments"]
                lines.append(f"  {segments[0]['from']}")
                for seg in segments:
                    lines.append(f"    ──[ДВ {seg['line']} ({seg['voltage_kv']} kV)]──> {seg['to']}")
        else:
            voltage_msg = f" на {voltage_kv} kV" if voltage_kv else ""
            lines.append(f"Није пронађена путања{voltage_msg} између {start} и {end} (у оквиру {max_depth} скокова).")
            return "\n".join(lines)
        
        # Alternative paths grouped by voltage level
        if conn["paths_by_voltage"]:
            lines.append("")
            lines.append("**Алтернативне путање по напонском нивоу:**")
            
            for v in sorted(conn["paths_by_voltage"].keys(), reverse=True):
                paths = conn["paths_by_voltage"][v]
                lines.append(f"\n  **{v} kV:**")
                for i, alt in enumerate(paths, 1):
                    via = " → ".join(alt["stations"])
                    dv_list = ", ".join([f"ДВ {l}" for l in alt["lines"]])
                    lines.append(f"    {i}. {via}")
                    lines.append(f"       ({dv_list})")
        
        # Mixed voltage paths (if any, show separately with warning)
        if conn["mixed_voltage_paths"]:
            lines.append("")
            lines.append("**Путање са мешовитим напонима** (захтевају трансформацију):")
            for i, alt in enumerate(conn["mixed_voltage_paths"], 1):
                via = " → ".join(alt["stations"])
                line_info = [f"ДВ {l} ({v} kV)" for l, v in zip(alt["lines"], alt["voltages"])]
                lines.append(f"  {i}. {via}")
                lines.append(f"     ({', '.join(line_info)})")
        
        return "\n".join(lines)


# Convenience function
def find_route(start: str, end: str, max_depth: int = 4, voltage_kv: Optional[int] = None) -> str:
    """
    Quick function to find route between two stations.
    
    Args:
        start: Starting station name
        end: Destination station name
        max_depth: Maximum search depth
        voltage_kv: If provided, filter by voltage level (110, 220, or 400)
    
    Returns:
        Formatted answer string.
    """
    finder = PathFinder()
    return finder.format_answer(start, end, max_depth, voltage_kv)
