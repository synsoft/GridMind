#!/bin/bash
# GridMind RAG Server - Unified
# Koristi interni RAG retrieval (bez REST API poziva na chunks server)

cd "$(dirname "$0")"

# Aktiviraj virtualno okruženje ako postoji
if [ -d "venv" ]; then
    source venv/bin/activate
elif [ -d "../venv" ]; then
    source ../venv/bin/activate
fi

# Pokreni server
echo "🚀 Pokretanje GridMind RAG servera..."
nohup python server.py --host 0.0.0.0 --port 5000 > nohup.out 2>&1 &

echo "✅ Server pokrenut u pozadini (PID: $!)"
echo "📋 Logovi: tail -f nohup.out"
echo "📋 Server logovi: tail -f logs/server.log"
