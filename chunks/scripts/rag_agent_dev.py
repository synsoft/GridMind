#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hot Reload wrapper za RAG Agent
================================

Pokreće rag_agent.py i automatski ga restartuje kada se fajl promeni.

Korišćenje:
    python rag_agent_dev.py
"""

import subprocess
import sys
import time
from pathlib import Path

try:
    from watchfiles import watch
except ImportError:
    print("Instaliranje watchfiles...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "watchfiles", "-q"])
    from watchfiles import watch


def main():
    script_path = Path(__file__).parent / "rag_agent.py"
    watch_paths = [
        str(script_path),
        str(Path(__file__).parent.parent / "config"),
    ]
    
    print(f"\033[95m{'='*60}\033[0m")
    print(f"\033[1mHOT RELOAD MODE - RAG Agent\033[0m")
    print(f"\033[95m{'='*60}\033[0m")
    print(f"\033[93mPratim promene na: {script_path.name}\033[0m")
    print(f"\033[93mCtrl+C za izlaz, zatim ponovo Ctrl+C za stop\033[0m")
    print()
    
    process = None
    
    try:
        while True:
            # Pokreni proces
            print(f"\033[92m→ Pokrećem rag_agent.py...\033[0m\n")
            process = subprocess.Popen(
                [sys.executable, str(script_path)],
                stdin=sys.stdin,
                stdout=sys.stdout,
                stderr=sys.stderr
            )
            
            # Čekaj na promene fajla ili završetak procesa
            for changes in watch(*watch_paths, stop_event=None):
                changed_files = [str(c[1]) for c in changes]
                print(f"\n\033[93m⟳ Detektovana promena: {', '.join(changed_files)}\033[0m")
                print(f"\033[93m⟳ Restartujem...\033[0m\n")
                
                # Ubij trenutni proces
                if process and process.poll() is None:
                    process.terminate()
                    try:
                        process.wait(timeout=2)
                    except subprocess.TimeoutExpired:
                        process.kill()
                
                break
            
            # Ako je proces završio normalno (korisnik izašao), izađi
            if process and process.poll() is not None:
                if process.returncode == 0:
                    break
                    
    except KeyboardInterrupt:
        print(f"\n\033[93mZaustavljam hot reload...\033[0m")
        if process and process.poll() is None:
            process.terminate()
            process.wait()
        print(f"\033[92mDoviđenja!\033[0m\n")


if __name__ == "__main__":
    main()
