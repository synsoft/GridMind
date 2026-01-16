#!/usr/bin/env python3
"""
RAG API Server - glavna aplikacija
"""

import sys
import logging
from pathlib import Path
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime

# Dodaj root direktorijum u Python path
root_dir = Path(__file__).parent
sys.path.insert(0, str(root_dir))

# Kreiraj logs direktorijum
log_dir = root_dir / "logs"
log_dir.mkdir(exist_ok=True)

# Podesi logging sa dnevnim rotiranjem
log_file = log_dir / "server.log"

# Console handler - prikazuje INFO i više
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter('%(message)s')
console_handler.setFormatter(console_formatter)

# File handler - rotira svaki dan u ponoć, čuva poslednih 30 dana
file_handler = TimedRotatingFileHandler(
    filename=log_file,
    when='midnight',
    interval=1,
    backupCount=30,
    encoding='utf-8'
)
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
file_handler.setFormatter(file_formatter)

# Root logger konfiguracija
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
root_logger.addHandler(console_handler)
root_logger.addHandler(file_handler)

# Preusmeri print() u logger
class PrintLogger:
    def write(self, message):
        if message.strip():
            logging.info(message.rstrip())
    def flush(self):
        pass

sys.stdout = PrintLogger()

print(f"🚀 Server started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"📁 Logs saved to: {log_file}")

from src.api.openai_api_server import app, initialize_rag

if __name__ == '__main__':
    initialize_rag()
    
    import argparse
    parser = argparse.ArgumentParser(description='RAG API Server')
    parser.add_argument('--host', type=str, default='0.0.0.0', help='Host address')
    parser.add_argument('--port', type=int, default=5000, help='Port number')
    args = parser.parse_args()
    
    app.run(host=args.host, port=args.port, debug=False)

