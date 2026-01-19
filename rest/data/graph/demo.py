#!/usr/bin/env python3
"""
Demo script for grid graph path finding.

Usage:
    python -m rest.data.graph.demo
    
Or run directly:
    python rest/data/graph/demo.py
"""

import sys
from pathlib import Path

# Add parent to path for direct execution
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from rest.data.graph import GridGraph, PathFinder
from rest.data.graph.path_finder import find_route


def main():
    print("=" * 60)
    print("ДЕМО: Претрага путања у преносној мрежи")
    print("=" * 60)
    print()
    
    # Build graph
    print("Учитавање графа...")
    graph = GridGraph.from_json_file()
    print(f"  {graph}")
    print()
    
    # Initialize path finder
    finder = PathFinder(graph)
    
    # Example 1: Direct query from the user's question
    print("-" * 60)
    print("ПРИМЕР 1: ТС Сремска Митровица 2 → ТС Нови Сад 1")
    print("-" * 60)
    answer = finder.format_answer("ТС Сремска Митровица 2", "ТС Нови Сад 1")
    print(answer)
    print()
    
    # Example 2: Direct connection
    print("-" * 60)
    print("ПРИМЕР 2: ТС Београд 3 → ТС Београд 5 (директна веза)")
    print("-" * 60)
    answer = finder.format_answer("ТС Београд 3", "ТС Београд 5")
    print(answer)
    print()
    
    # Example 3: Multiple hops
    print("-" * 60)
    print("ПРИМЕР 3: ТС Суботица 3 → ТС Ниш 2 (више скокова)")
    print("-" * 60)
    answer = finder.format_answer("ТС Суботица 3", "ТС Ниш 2", max_depth=5)
    print(answer)
    print()
    
    # Example 4: Non-existent station
    print("-" * 60)
    print("ПРИМЕР 4: Непостојећа станица")
    print("-" * 60)
    answer = finder.format_answer("ТС Нови Сад", "ТС Београд 5")
    print(answer)
    print()
    
    # Example 5: Using convenience function
    print("-" * 60)
    print("ПРИМЕР 5: Брза функција find_route()")
    print("-" * 60)
    print(find_route("ТС Беочин", "ТС Нови Сад 3"))
    print()
    
    # Show raw data for one path
    print("-" * 60)
    print("ПРИМЕР 6: Сирови подаци (JSON формат)")
    print("-" * 60)
    conn = finder.find_connection("ТС Сремска Митровица 2", "ТС Нови Сад 1")
    import json
    print(json.dumps(conn, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
