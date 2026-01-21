#!/bin/bash

# Find and kill server.py process

PID=$(pgrep -f "python3 server.py")

if [ -z "$PID" ]; then
    echo "server.py process not found"
    exit 0
fi

echo "Found server.py process with PID: $PID"
kill $PID

if [ $? -eq 0 ]; then
    echo "server.py process killed successfully"
else
    echo "Failed to kill server.py process, trying with -9"
    kill -9 $PID
fi
