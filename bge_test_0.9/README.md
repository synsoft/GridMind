# RAG System - Elektro Prenosni Sistem

RAG sistem za pretragu i odgovaranje na pitanja iz tehničke dokumentacije.

## Struktura projekta

```
bgem3_test/
├── server.py                  # Glavni server (pokreće API)
├── manage_knowledge.py        # CLI za upravljanje stored knowledge
├── config.json                # Konfiguracija
├── requirements.txt           # Python zavisnosti
│
├── src/                       # Glavni source kod
│   ├── core/                  # Core funkcionalnosti
│   │   ├── chat_rag_api.py    # RAG chat logika
│   │   ├── search_faiss.py    # FAISS pretraga
│   │   ├── stored_knowledge.py # Stored knowledge manager
│   │   └── session_manager.py  # Session memorija
│   │
│   ├── api/                   # API endpoints
│   │   └── openai_api_server.py # OpenAI-compatible REST API
│   │
│   ├── utils/                 # Utility moduli
│   │   └── dalekovod_checker.py # Dalekovod checker
│   │
│   └── tools/                 # CLI alati
│       └── stored_knowledge_manager.py # CLI za stored knowledge
│
├── data/                      # Svi podaci
│   ├── faiss_db/              # FAISS baza
│   ├── stored_knowledge_data/ # Stored knowledge
│   ├── files/                 # Originalni dokumenti
│   ├── chunks_combined.json   # Chunk podaci
│   └── dv_station_map.json    # Mapa dalekovoda
│
├── eval/                      # Evaluacija
└── scripts/                   # Helper skripte
```

## Pokretanje

### Server
```bash
python server.py --host 0.0.0.0 --port 5000
```

### Stored Knowledge Manager
```bash
python manage_knowledge.py
```

## API Endpoints

- `POST /v1/chat/completions` - OpenAI-compatible chat endpoint
- `GET /health` - Health check
- `POST /search` - Direct document search
