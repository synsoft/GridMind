#!/usr/bin/env python3
"""
Stored Knowledge Manager CLI
"""

import sys
from pathlib import Path

# Dodaj root direktorijum u Python path
root_dir = Path(__file__).parent
sys.path.insert(0, str(root_dir))

from src.tools.stored_knowledge_manager import main

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Prekinuto od strane korisnika.")
        sys.exit(0)
