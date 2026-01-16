#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GridMind RAG Server
====================

REST API server za RAG retrieval, kompatibilan sa OpenAI API standardom.

Endpoints:
- POST /retrieve - Retrieval endpoint za pretragu dokumenata
- GET /health - Health check endpoint
- GET /models - Lista dostupnih modela

Pokretanje:
    python server.py
    
Ili sa uvicorn:
    uvicorn server:app --host 0.0.0.0 --port 8888 --reload
"""

import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional
from contextlib import asynccontextmanager

# Dodaj scripts folder u path za import rag_agent-a
sys.path.insert(0, str(Path(__file__).parent / "chunks" / "scripts"))

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

# ============================================================================
# Konfiguracija
# ============================================================================

CONFIG_PATH = Path(__file__).parent / "config" / "server_config.json"

def load_server_config() -> dict:
    """Učitava server konfiguraciju."""
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        # Default konfiguracija
        return {
            "server": {
                "host": "0.0.0.0",
                "port": 8888,
                "debug": False,
                "reload": False
            },
            "retrieval": {
                "top_k": 8,
                "embedding_top_k": 80,
                "score_threshold": 0.5
            },
            "rag_config_path": str(Path(__file__).parent / "chunks" / "config" / "rag_config.json")
        }

SERVER_CONFIG = load_server_config()

# ============================================================================
# Pydantic Modeli (OpenAI-style)
# ============================================================================

class MessageItem(BaseModel):
    """Message item for OpenAI-style requests."""
    role: str
    content: str


class RetrieveRequest(BaseModel):
    """Request model za /retrieve endpoint. Podržava i query i messages format."""
    query: Optional[str] = Field(None, description="Tekst upita za pretragu")
    messages: Optional[List[MessageItem]] = Field(None, description="OpenAI-style messages format")
    top_k: Optional[int] = Field(None, description="Broj rezultata za vraćanje (override server config)")
    score_threshold: Optional[float] = Field(None, description="Minimalni score za filtriranje rezultata")
    include_metadata: Optional[bool] = Field(True, description="Da li uključiti metapodatke u odgovor")
    model: Optional[str] = Field(None, description="Model ID (ignorisano, za kompatibilnost)")
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "query": "Da li TS Beograd 5 i TS Beograd 20 rade u paralelnom radu?",
                    "top_k": 8,
                    "score_threshold": 0.5,
                    "include_metadata": True
                }
            ]
        }
    }


class RetrievedDocument(BaseModel):
    """Model za jedan pronađeni dokument."""
    chunk_id: str = Field(..., description="Jedinstveni ID chunk-a")
    content: str = Field(..., description="Sadržaj chunk-a")
    score: float = Field(..., description="Relevance score (0-1)")
    rank: int = Field(..., description="Rang u rezultatima")
    
    # Metapodaci (opcioni)
    doc_id: Optional[str] = Field(None, description="ID dokumenta")
    doc_title: Optional[str] = Field(None, description="Naslov dokumenta")
    section_number: Optional[str] = Field(None, description="Broj sekcije")
    section_title: Optional[str] = Field(None, description="Naslov sekcije")
    parent_title: Optional[str] = Field(None, description="Naslov parent sekcije")
    object_code: Optional[str] = Field(None, description="Kod objekta (npr. BG5)")
    object_name: Optional[str] = Field(None, description="Ime objekta")
    voltage_levels: Optional[List[str]] = Field(None, description="Naponski nivoi")
    keywords: Optional[List[str]] = Field(None, description="Ključne reči")


class RetrieveUsage(BaseModel):
    """Usage statistike za retrieve request."""
    query_tokens: int = Field(..., description="Procenjeni broj tokena u upitu")
    total_chunks_searched: int = Field(..., description="Ukupan broj chunk-ova u bazi")
    candidates_evaluated: int = Field(..., description="Broj kandidata evaluiranih rerankerom")


class RetrieveResponse(BaseModel):
    """Response model za /retrieve endpoint (OpenAI-style)."""
    id: str = Field(..., description="Jedinstveni ID zahteva")
    object: str = Field("retrieve.response", description="Tip objekta")
    created: int = Field(..., description="Unix timestamp kreiranja")
    model: str = Field(..., description="Korišćeni model za retrieval")
    
    results: List[RetrievedDocument] = Field(..., description="Lista pronađenih dokumenata")
    
    usage: RetrieveUsage = Field(..., description="Usage statistike")
    
    # Dodatne informacije
    query: str = Field(..., description="Originalni upit")
    top_k: int = Field(..., description="Broj traženih rezultata")
    score_threshold: float = Field(..., description="Korišćeni score threshold")


class ModelInfo(BaseModel):
    """Informacije o modelu."""
    id: str
    object: str = "model"
    created: int
    owned_by: str


class ModelsResponse(BaseModel):
    """Response za /models endpoint."""
    object: str = "list"
    data: List[ModelInfo]


class HealthResponse(BaseModel):
    """Response za /health endpoint."""
    status: str
    timestamp: str
    version: str
    models_loaded: bool
    total_chunks: int


class ErrorResponse(BaseModel):
    """Error response model."""
    error: Dict[str, Any]


# ============================================================================
# OpenAI Chat Completions Modeli
# ============================================================================

class ChatMessage(BaseModel):
    """OpenAI Chat Message format."""
    role: str = Field(..., description="Role: system, user, assistant")
    content: str = Field(..., description="Sadržaj poruke")


class ChatCompletionRequest(BaseModel):
    """OpenAI Chat Completion Request format."""
    model: str = Field("GridMind_0.9", description="ID modela")
    messages: List[ChatMessage] = Field(..., description="Lista poruka")
    temperature: Optional[float] = Field(0.7, description="Temperature za sampling")
    max_tokens: Optional[int] = Field(None, description="Max tokens u odgovoru")
    top_p: Optional[float] = Field(1.0, description="Top-p sampling")
    stream: Optional[bool] = Field(False, description="Da li streamovati odgovor")
    
    # GridMind specifični parametri
    top_k: Optional[int] = Field(None, description="Broj rezultata za retrieval")
    include_sources: Optional[bool] = Field(True, description="Da li uključiti izvore u odgovor")


class ChatCompletionChoice(BaseModel):
    """OpenAI Chat Completion Choice."""
    index: int
    message: ChatMessage
    finish_reason: str = "stop"


class ChatCompletionUsage(BaseModel):
    """OpenAI Chat Completion Usage."""
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class ChatCompletionResponse(BaseModel):
    """OpenAI Chat Completion Response format."""
    id: str
    object: str = "chat.completion"
    created: int
    model: str
    choices: List[ChatCompletionChoice]
    usage: ChatCompletionUsage


# ============================================================================
# RAG Agent Singleton
# ============================================================================

class RAGAgentSingleton:
    """Singleton wrapper za RAG Agent."""
    
    _instance = None
    _agent = None
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def __init__(self):
        self._agent = None
        self._loaded = False
        self._total_chunks = 0
    
    def load(self, config_path: str):
        """Učitava RAG Agent."""
        if self._loaded:
            return
        
        from rag_agent import RAGAgent
        self._agent = RAGAgent(config_path)
        self._total_chunks = len(self._agent.chunks)
        self._loaded = True
    
    @property
    def agent(self):
        return self._agent
    
    @property
    def loaded(self) -> bool:
        return self._loaded
    
    @property
    def total_chunks(self) -> int:
        return self._total_chunks


rag_singleton = RAGAgentSingleton.get_instance()

# ============================================================================
# FastAPI App
# ============================================================================

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifecycle manager za učitavanje modela pri startu."""
    # Startup
    print("\n" + "=" * 60)
    print("GRIDMIND RAG SERVER")
    print("=" * 60)
    
    rag_config_path = SERVER_CONFIG.get("rag_config_path", 
                                         str(Path(__file__).parent / "chunks" / "config" / "rag_config.json"))
    
    print(f"\nUčitavanje RAG Agent-a iz: {rag_config_path}")
    rag_singleton.load(rag_config_path)
    
    server_cfg = SERVER_CONFIG.get("server", {})
    print(f"\nServer pokrenut na http://{server_cfg.get('host', '0.0.0.0')}:{server_cfg.get('port', 8888)}")
    print("=" * 60 + "\n")
    
    yield
    
    # Shutdown
    print("\nGašenje servera...")


app = FastAPI(
    title="GridMind RAG API",
    description="REST API za RAG retrieval, kompatibilan sa OpenAI API standardom",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================================
# Endpoints
# ============================================================================

@app.get("/health", response_model=HealthResponse, tags=["System"])
@app.get("/v1/health", response_model=HealthResponse, tags=["System"], include_in_schema=False)
async def health_check():
    """Health check endpoint."""
    return HealthResponse(
        status="healthy" if rag_singleton.loaded else "loading",
        timestamp=datetime.utcnow().isoformat(),
        version="1.0.0",
        models_loaded=rag_singleton.loaded,
        total_chunks=rag_singleton.total_chunks
    )


@app.get("/models", response_model=ModelsResponse, tags=["System"])
@app.get("/v1/models", response_model=ModelsResponse, tags=["System"], include_in_schema=False)
async def list_models():
    """Lista dostupnih modela."""
    models = [
        ModelInfo(
            id="GridMind_0.9",
            created=int(time.time()),
            owned_by="gridmind"
        )
    ]
    
    return ModelsResponse(data=models)


@app.post("/retrieve", tags=["Retrieval"])
@app.post("/v1/retrieve", tags=["Retrieval"], include_in_schema=False)
async def retrieve(request: Request):
    """
    Retrieve relevantne dokumente za dati upit.
    
    Koristi hibridnu pretragu (FAISS + BM25) sa BGE-M3 rerankerom.
    
    **Request Body:**
    - `query` ili `question`: Tekst upita za pretragu
    - `messages`: OpenAI-style messages format (alternativa za query)
    - `top_k`: Broj rezultata za vraćanje (opciono, default iz config-a)
    - `score_threshold`: Minimalni score za filtriranje (opciono)
    - `include_metadata`: Da li uključiti metapodatke (opciono, default True)
    
    **Response:**
    - OpenAI-style response sa listom pronađenih dokumenata
    """
    if not rag_singleton.loaded:
        raise HTTPException(
            status_code=503,
            detail={"error": {"message": "RAG Agent nije učitan", "type": "service_unavailable"}}
        )
    
    # Parse raw JSON body za maksimalnu fleksibilnost
    try:
        body = await request.json()
    except Exception:
        body = {}
    
    # Izvuci query - podržava razne formate
    query = None
    
    # Format 1: direktno query polje
    if "query" in body:
        query = body["query"]
    
    # Format 2: question polje (bge_test klijent koristi ovo)
    if not query and "question" in body:
        query = body["question"]
    
    # Format 3: OpenAI messages format
    if not query and "messages" in body:
        messages = body.get("messages", [])
        user_messages = [m for m in messages if isinstance(m, dict) and m.get("role") == "user"]
        if user_messages:
            query = user_messages[-1].get("content", "")
    
    # Format 4: input polje (neki klijenti koriste ovo)
    if not query and "input" in body:
        query = body["input"]
    
    # Format 5: prompt polje
    if not query and "prompt" in body:
        query = body["prompt"]
    
    # Format 6: text polje
    if not query and "text" in body:
        query = body["text"]
    
    if not query:
        raise HTTPException(
            status_code=400,
            detail={"error": {"message": "Morate proslediti 'query', 'messages', 'input', 'prompt' ili 'text'", "type": "invalid_request"}}
        )
    
    # Odredi parametre
    retrieval_cfg = SERVER_CONFIG.get("retrieval", {})
    top_k = body.get("top_k") or retrieval_cfg.get("top_k", 8)
    score_threshold = body.get("score_threshold") or retrieval_cfg.get("score_threshold", 0.5)
    embedding_top_k = retrieval_cfg.get("embedding_top_k", 80)
    include_metadata = body.get("include_metadata", True)
    
    # Izvršti retrieval
    try:
        results = rag_singleton.agent.retrieve(
            query=query,
            initial_k=embedding_top_k,
            final_k=top_k
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"error": {"message": str(e), "type": "retrieval_error"}}
        )
    
    # Filtriraj po score_threshold
    filtered_results = [r for r in results if r.get('rerank_score', 0) >= score_threshold]
    
    # Konvertuj u format koji očekuje bge_test klijent
    # Klijent očekuje: result.metadata.{filename, section, item_number}, result.text, result.score
    formatted_results = []
    for rank, r in enumerate(filtered_results, 1):
        # Formatiraj section string
        section_num = str(r.get('section_number', '')) if r.get('section_number') else ''
        section_title = r.get('section_title', '')
        section_str = f"{section_num}: {section_title}" if section_num and section_title else section_num or section_title or ''
        
        result_item = {
            "text": r.get('content', ''),
            "score": round(r.get('rerank_score', 0), 4),
            "rank": rank,
            "chunk_id": r.get('chunk_id', ''),
            "metadata": {
                "filename": r.get('doc_title', ''),
                "section": section_str,
                "item_number": r.get('chunk_id', '').split(':')[-1] if r.get('chunk_id') else '',
                "doc_id": r.get('doc_id', ''),
                "object_code": r.get('object_code', ''),
                "object_name": r.get('object_name', ''),
                "parent_title": r.get('parent_title', ''),
                "voltage_levels": r.get('voltage_levels', []),
                "keywords": r.get('keywords', [])
            }
        }
        formatted_results.append(result_item)
    
    # Vrati jednostavan JSON response koji klijent očekuje
    return {
        "results": formatted_results,
        "query": query,
        "top_k": top_k,
        "total_results": len(formatted_results)
    }


@app.get("/", tags=["System"])
async def root():
    """Root endpoint - vraća osnovne informacije o API-ju."""
    return {
        "name": "GridMind RAG API",
        "version": "1.0.0",
        "description": "REST API za RAG retrieval, kompatibilan sa OpenAI API standardom",
        "endpoints": {
            "/health": "Health check",
            "/models": "Lista modela",
            "/retrieve": "Retrieval endpoint (POST)",
            "/v1/chat/completions": "OpenAI-compatible chat completions (POST)"
        },
        "docs": "/docs",
        "openapi": "/openapi.json"
    }


@app.post("/v1/chat/completions", response_model=ChatCompletionResponse, tags=["Chat"])
@app.post("/chat/completions", response_model=ChatCompletionResponse, tags=["Chat"], include_in_schema=False)
async def chat_completions(request: ChatCompletionRequest):
    """
    OpenAI-compatible Chat Completions endpoint.
    
    Koristi RAG za pronalaženje relevantnih dokumenata i vraća odgovor
    u OpenAI Chat Completions formatu.
    
    **Request Body:**
    - `model`: ID modela (default: GridMind_0.9)
    - `messages`: Lista poruka sa role i content
    - `top_k`: Broj rezultata za retrieval (opciono)
    - `include_sources`: Da li uključiti izvore (opciono, default True)
    
    **Response:**
    - OpenAI Chat Completions format sa retrieved dokumentima
    """
    if not rag_singleton.loaded:
        raise HTTPException(
            status_code=503,
            detail={"error": {"message": "RAG Agent nije učitan", "type": "service_unavailable"}}
        )
    
    # Izvuci poslednju user poruku kao query
    user_messages = [m for m in request.messages if m.role == "user"]
    if not user_messages:
        raise HTTPException(
            status_code=400,
            detail={"error": {"message": "Nema user poruke u messages", "type": "invalid_request"}}
        )
    
    query = user_messages[-1].content
    
    # Odredi parametre
    retrieval_cfg = SERVER_CONFIG.get("retrieval", {})
    top_k = request.top_k or retrieval_cfg.get("top_k", 8)
    embedding_top_k = retrieval_cfg.get("embedding_top_k", 80)
    score_threshold = retrieval_cfg.get("score_threshold", 0.5)
    
    # Izvršti retrieval
    try:
        results = rag_singleton.agent.retrieve(
            query=query,
            initial_k=embedding_top_k,
            final_k=top_k
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"error": {"message": str(e), "type": "retrieval_error"}}
        )
    
    # Filtriraj po score_threshold
    filtered_results = [r for r in results if r.get('rerank_score', 0) >= score_threshold]
    
    # Formatiraj odgovor sa izvorima
    if filtered_results:
        # Kreiraj kontekst sa retrieved dokumentima
        context_parts = []
        sources = []
        
        for i, r in enumerate(filtered_results, 1):
            doc_title = r.get('doc_title', 'Nepoznat dokument')
            section = r.get('section_number', '')
            section_title = r.get('section_title', '')
            content = r.get('content', '')
            score = r.get('rerank_score', 0)
            
            # Dodaj u kontekst
            header = f"[{i}] {doc_title}"
            if section:
                header += f" - Sekcija {section}"
            if section_title:
                header += f": {section_title}"
            
            context_parts.append(f"{header}\n{content}")
            
            # Dodaj u sources
            sources.append({
                "rank": i,
                "doc_title": doc_title,
                "section": f"{section}: {section_title}" if section else section_title,
                "score": round(score, 3)
            })
        
        # Formatiraj finalni odgovor
        context_text = "\n\n---\n\n".join(context_parts)
        
        if request.include_sources:
            sources_text = "\n\n**Izvori:**\n"
            for s in sources:
                sources_text += f"- [{s['rank']}] {s['doc_title']} ({s['section']}) - relevantnost: {s['score']}\n"
            
            response_content = f"Na osnovu pronađenih dokumenata:\n\n{context_text}{sources_text}"
        else:
            response_content = context_text
    else:
        response_content = "Nisam pronašao relevantne informacije za vaše pitanje."
    
    # Proceni tokene
    prompt_tokens = sum(len(m.content) // 4 for m in request.messages)
    completion_tokens = len(response_content) // 4
    
    # Kreiraj OpenAI-style response
    return ChatCompletionResponse(
        id=f"chatcmpl-{int(time.time() * 1000)}",
        created=int(time.time()),
        model=request.model or "GridMind_0.9",
        choices=[
            ChatCompletionChoice(
                index=0,
                message=ChatMessage(
                    role="assistant",
                    content=response_content
                ),
                finish_reason="stop"
            )
        ],
        usage=ChatCompletionUsage(
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            total_tokens=prompt_tokens + completion_tokens
        )
    )


# ============================================================================
# Error Handlers
# ============================================================================

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail if isinstance(exc.detail, dict) else {"message": str(exc.detail)}}
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": {"message": str(exc), "type": "internal_error"}}
    )


# ============================================================================
# Main
# ============================================================================

if __name__ == "__main__":
    import uvicorn
    
    server_cfg = SERVER_CONFIG.get("server", {})
    
    uvicorn.run(
        "server:app",
        host=server_cfg.get("host", "0.0.0.0"),
        port=server_cfg.get("port", 8888),
        reload=server_cfg.get("reload", False),
        log_level="info"
    )
