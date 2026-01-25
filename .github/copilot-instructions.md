# GridMind RAG System - AI Agent Instructions

## Project Overview

GridMind is a RAG (Retrieval-Augmented Generation) system for Serbian electrical power grid (EES) technical documentation. It uses BGE-M3 embeddings, FAISS vector search, and a fine-tuned BGE reranker to answer questions about transformer substations (TS), switching procedures, and operational rules.

## Architecture

```
server.py                  # Main unified Flask server (OpenAI-compatible API)
├── rest/src/core/
│   ├── chat_rag_api.py    # OllamaRAGChat - main chat orchestrator
│   ├── llm_client.py      # Unified LLM client (Ollama/OpenAI)
│   ├── session_manager.py # LangChain conversation memory per session
│   ├── stored_knowledge.py # Expert knowledge persistence with BGE reranker
│   └── model_manager.py   # Singleton for BGE-M3 and reranker models
└── chunks/scripts/
    └── rag_agent.py       # RAGAgent - FAISS + BM25 hybrid search + reranking
```

**Key Flow**: `server.py` → `OllamaRAGChat.chat()` → internal `RAGAgent.retrieve()` → LLM generation

## Configuration Files

- **Root `config.json`**: Server settings, retrieval top_k, paths to other configs
- **`rest/config.json`**: LLM provider settings, search API config, stored knowledge settings
- **`chunks/config/rag_config.json`**: Embedding/reranker models, FAISS paths, retrieval parameters

## Critical Patterns

### Internal RAG (No REST API)
The server uses `use_internal_rag=True` - retrieval happens via direct Python calls to `RAGAgent`, not HTTP:
```python
# In chat_rag_api.py
from rag_agent import RAGAgent
self.rag_agent = RAGAgent(rag_config_path)
results = self.rag_agent.retrieve(question, final_k=top_k)
```

### Session Memory
Sessions are identified via `X-OpenWebUI-Chat-Id` header or hashed from first user message. Each session gets isolated `ConversationBufferWindowMemory` (10 turns, 30min timeout).

### Cyrillic-to-Latin Conversion
Serbian documents use both scripts. Use `cyrillic_to_latin()` from `rag_agent.py` or `cyrtranslit.to_latin()` for normalization.

### Stored Knowledge Commands
Users can store expert knowledge via chat:
- `/store <content>` - Persists to `data/stored_knowledge_data/stored_knowledge.json`
- `/recall <query>` - Semantic search over stored knowledge

## Developer Commands

```bash
# Start server (uses venv)
./start_server.sh

# Stop server
./kill_server.sh

# Manual start with options
source venv/bin/activate
python server.py --host 0.0.0.0 --port 5000 --reload  # --reload for dev

# Test retrieval
curl -X POST http://localhost:5000/retrieve \
  -H "Content-Type: application/json" \
  -d '{"question": "Uklopno stanje TS Niš 2", "top_k": 5}'
```

## Document Chunking Strategy

Chunks in `chunks/output/all_chunks.jsonl` follow semantic boundaries (see [chunks/README.md](chunks/README.md)):
- **Type C (Uklopno stanje)**: Switching states per voltage level (300-1500 chars)
- **Type D (Posebna stanja)**: Special scenarios like "bez DZS" (500-1500 chars)
- Each chunk has metadata: `doc_id`, `object_code` (e.g., "NI2", "BG8"), `voltage_levels`, `section_type`

## Key Dependencies

- **FlagEmbedding**: BGE-M3 embeddings and reranker (`BAAI/bge-m3`, `BAAI/bge-reranker-v2-m3`)
- **FAISS**: Vector similarity search (CPU version)
- **LangChain**: Conversation memory (`langchain_classic.memory`)
- **Flask**: REST API server

## Model Loading

Models load lazily via `ModelManager` singleton. Fine-tuned reranker path:
```
chunks/finetune_rerank/output/bge-reranker-finetuned_*/final
```

## Testing & Evaluation

Evaluation data in `chunks/eval/`:
```bash
cd chunks/scripts
python run_eval.py        # Single eval
python run_eval_all.py    # Full evaluation suite
```

## API Compatibility

Server exposes OpenAI-compatible endpoints at `/v1/chat/completions` for integration with OpenWebUI and other clients. Models list includes aliases like `gridmind`, `rag-model`, `gpt-3.5-turbo`.
