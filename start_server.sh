#!/bin/bash

# Start server.py with virtual environment

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cd "$SCRIPT_DIR"

# Activate virtual environment
source venv/bin/activate

# Start server in background
nohup python3 server.py &

echo "server.py started with PID: $!"
