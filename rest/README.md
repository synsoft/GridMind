# GridMind RAG System - Unified Server

RAG sistem za pretragu i odgovaranje na pitanja iz tehničke dokumentacije.

## Arhitektura

**Unified Server** - jedan server koji:
- Interno koristi RAGAgent iz `chunks/scripts/rag_agent.py` za retrieval
- Komunicira sa LLM-om (Ollama/OpenAI) za generisanje odgovora
- Nema REST API pozive za retrieval - sve je interno!

## Struktura projekta

```
bge_test_0.9/
├── server.py              # Glavni server sa internim RAG retrieval-om
├── chat_rag_api.py        # OllamaRAGChat klasa za import
├── manage_knowledge.py    # CLI za upravljanje stored knowledge
├── config.json            # Konfiguracija
├── requirements.txt       # Python zavisnosti
│
├── data/                  # Lokalni podaci
├── eval/                  # Evaluacija
│   ├── generate_llm_answers.py
│   ├── score_answer.py
│   └── run_eval.py
└── scripts/               # Helper skripte
```

## Pokretanje

### Server
```bash
python server.py --host 0.0.0.0 --port 5000
```

Ili sa start.sh:
```bash
./start.sh
```

### Chat CLI
```bash
python chat_rag_api.py
```

Sa izvorima:
```bash
python chat_rag_api.py --sources
```

## API Endpoints

- `POST /v1/chat/completions` - OpenAI-compatible chat endpoint
- `GET /health` - Health check
- `POST /search` - Direct document search
