#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GridMind RAG Server - Unified API
=================================

Server koji kombinuje:
- RAG retrieval iz chunks/scripts/rag_agent.py (interno, bez REST API poziva)
- LLM generisanje odgovora (Ollama/OpenAI)
- OpenAI-compatible API endpoints

Endpoints:
- POST /v1/chat/completions - OpenAI-compatible chat endpoint
- POST /retrieve - Retrieval endpoint
- GET /health - Health check
- GET /models - Lista modela

Konfiguracija:
- config/server_config.json - Server i retrieval podešavanja
- rest/config.json - LLM podešavanja
"""

import json
import os
import sys
import time
import logging
import requests
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional
from logging.handlers import TimedRotatingFileHandler

# ============================================================================
# Setup paths
# ============================================================================

ROOT_DIR = Path(__file__).parent

# Dodaj chunks/scripts u path za RAGAgent
sys.path.insert(0, str(ROOT_DIR / "chunks" / "scripts"))

# ============================================================================
# Logging setup
# ============================================================================

log_dir = ROOT_DIR / "logs"
log_dir.mkdir(exist_ok=True)
log_file = log_dir / "server.log"

# Console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('%(message)s'))

# File handler sa rotacijom
file_handler = TimedRotatingFileHandler(
    filename=log_file,
    when='midnight',
    interval=1,
    backupCount=30,
    encoding='utf-8'
)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))

# Root logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# ============================================================================
# Flask imports i app
# ============================================================================

from flask import Flask, request, jsonify, Response, stream_with_context
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ============================================================================
# Konfiguracija
# ============================================================================

def load_server_config() -> dict:
    """Učitava server konfiguraciju iz config/server_config.json."""
    config_path = ROOT_DIR / "config.json"
    if config_path.exists():
        with open(config_path, 'r', encoding='utf-8') as f:
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
            "rag_config_path": str(ROOT_DIR / "chunks" / "config" / "rag_config.json")
        }

def load_llm_config() -> dict:
    """Učitava LLM konfiguraciju iz rest/config.json."""
    config_path = ROOT_DIR / "rest" / "config.json"
    if config_path.exists():
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        # Default LLM konfiguracija
        return {
            "llm": {
                "provider": "openai",
                "model": "gemma3:27b",
                "ollama_host": "192.168.30.61",
                "ollama_port": 11434,
                "_host": "192.168.30.62",
                "openai_port": 8080,
                "temperature": 0.3,
                "timeout": 120,
                "stream_tokens": True
            }
        }

SERVER_CONFIG = load_server_config()
LLM_CONFIG = load_llm_config()

# RAG config putanja
RAG_CONFIG_PATH = SERVER_CONFIG.get("rag_config_path", 
                                     str(ROOT_DIR / "chunks" / "config" / "rag_config.json"))

# ============================================================================
# RAG Agent Singleton
# ============================================================================

class RAGAgentManager:
    """Singleton za upravljanje RAG Agent-om."""
    
    _instance = None
    _agent = None
    _loaded = False
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def initialize(self):
        """Inicijalizuje RAG Agent."""
        if self._loaded:
            return
        
        logger.info("\n" + "=" * 60)
        logger.info("GRIDMIND RAG SERVER - UNIFIED")
        logger.info("=" * 60)
        logger.info(f"\nUčitavanje RAG Agent-a iz: {RAG_CONFIG_PATH}")
        
        try:
            from rag_agent import RAGAgent
            self._agent = RAGAgent(RAG_CONFIG_PATH)
            self._loaded = True
            logger.info("✓ RAG Agent uspešno učitan!")
        except Exception as e:
            logger.error(f"❌ Greška pri učitavanju RAG Agent-a: {e}")
            raise
    
    @property
    def agent(self):
        if not self._loaded:
            self.initialize()
        return self._agent
    
    @property
    def loaded(self) -> bool:
        return self._loaded
    
    @property
    def total_chunks(self) -> int:
        if self._loaded and self._agent:
            return len(self._agent.chunks)
        return 0

rag_manager = RAGAgentManager()

# ============================================================================
# LLM Client
# ============================================================================

class LLMClient:
    """Klijent za komunikaciju sa LLM-om (Ollama ili OpenAI-compatible)."""
    
    def __init__(self, config: dict):
        self.config = config
        llm_config = config.get('llm', {})
        
        self.provider = llm_config.get('provider', 'ollama')
        self.model = llm_config.get('model', 'gemma3:27b')
        self.temperature = llm_config.get('temperature', 0.3)
        self.stream = llm_config.get('stream_tokens', True)
        self.timeout = llm_config.get('timeout', 120)
        
        if self.provider == 'ollama':
            host = llm_config.get('ollama_host', 'localhost')
            port = llm_config.get('ollama_port', 11434)
            self.base_url = f"http://{host}:{port}"
        else:
            host = llm_config.get('openai_host', 'localhost')
            port = llm_config.get('openai_port', 8080)
            self.base_url = f"http://{host}:{port}"
        
        self.api_key = llm_config.get('openai_api_key', '')
    
    def generate(self, messages: List[Dict], stream: bool = None) -> str:
        """Generiše odgovor od LLM-a."""
        if stream is None:
            stream = self.stream
        
        if self.provider == 'ollama':
            return self._generate_ollama(messages, stream=False)
        else:
            return self._generate_openai(messages, stream=False)
    
    def generate_stream(self, messages: List[Dict]):
        """Generator za streaming odgovora."""
        if self.provider == 'ollama':
            yield from self._stream_ollama(messages)
        else:
            yield from self._stream_openai(messages)
    
    def _generate_ollama(self, messages: List[Dict], stream: bool = False) -> str:
        """Generiše odgovor pomoću Ollama API-ja."""
        url = f"{self.base_url}/api/chat"
        
        payload = {
            "model": self.model,
            "messages": messages,
            "stream": False,
            "options": {
                "temperature": self.temperature
            }
        }
        
        try:
            response = requests.post(url, json=payload, timeout=self.timeout)
            response.raise_for_status()
            result = response.json()
            return result.get('message', {}).get('content', '')
        except Exception as e:
            logger.error(f"Ollama greška: {e}")
            raise
    
    def _stream_ollama(self, messages: List[Dict]):
        """Streaming odgovora pomoću Ollama API-ja."""
        url = f"{self.base_url}/api/chat"
        
        payload = {
            "model": self.model,
            "messages": messages,
            "stream": True,
            "options": {
                "temperature": self.temperature
            }
        }
        
        try:
            with requests.post(url, json=payload, stream=True, timeout=self.timeout) as response:
                response.raise_for_status()
                for line in response.iter_lines():
                    if line:
                        try:
                            data = json.loads(line)
                            content = data.get('message', {}).get('content', '')
                            if content:
                                yield content
                            if data.get('done', False):
                                break
                        except json.JSONDecodeError:
                            continue
        except Exception as e:
            logger.error(f"Ollama streaming greška: {e}")
            raise
    
    def _generate_openai(self, messages: List[Dict], stream: bool = False) -> str:
        """Generiše odgovor pomoću OpenAI-compatible API-ja."""
        url = f"{self.base_url}/v1/chat/completions"
        
        headers = {
            "Content-Type": "application/json"
        }
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": self.temperature,
            "stream": False
        }
        
        try:
            response = requests.post(url, json=payload, headers=headers, timeout=self.timeout)
            response.raise_for_status()
            result = response.json()
            return result['choices'][0]['message']['content']
        except Exception as e:
            logger.error(f"OpenAI greška: {e}")
            raise
    
    def _stream_openai(self, messages: List[Dict]):
        """Streaming odgovora pomoću OpenAI-compatible API-ja."""
        url = f"{self.base_url}/v1/chat/completions"
        
        headers = {
            "Content-Type": "application/json"
        }
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": self.temperature,
            "stream": True
        }
        
        try:
            with requests.post(url, json=payload, headers=headers, stream=True, timeout=self.timeout) as response:
                response.raise_for_status()
                for line in response.iter_lines():
                    if line:
                        line = line.decode('utf-8')
                        if line.startswith('data: '):
                            data_str = line[6:]
                            if data_str.strip() == '[DONE]':
                                break
                            try:
                                data = json.loads(data_str)
                                delta = data.get('choices', [{}])[0].get('delta', {})
                                content = delta.get('content', '')
                                if content:
                                    yield content
                            except json.JSONDecodeError:
                                continue
        except Exception as e:
            logger.error(f"OpenAI streaming greška: {e}")
            raise

llm_client = LLMClient(LLM_CONFIG)

# ============================================================================
# RAG Chat funkcionalnost
# ============================================================================

SYSTEM_PROMPT = """Ti si stručni AI asistent za elektroenergetski prenosni sistem Srbije.

PRAVILA:
1. Odgovaraj ISKLJUČIVO na osnovu datog konteksta
2. Ako informacija nije u kontekstu, reci "Ne mogu pronaći tu informaciju u dostupnoj dokumentaciji"
3. Budi precizan i koncizan
4. Koristi tehničku terminologiju iz konteksta
5. NE navodi izvore/dokumente na kraju odgovora - oni se dodaju automatski

FORMAT ODGOVORA:
- Koristi kratke, jasne rečenice
- Za liste koristi bullet points
- Za procedure koristi numerisane korake
"""

def build_context_from_results(results: List[Dict]) -> str:
    """Gradi kontekst string od rezultata pretrage."""
    if not results:
        return ""
    
    context_parts = []
    for i, r in enumerate(results, 1):
        doc_title = r.get('doc_title', 'Nepoznat dokument')
        section_num = r.get('section_number', '')
        section_title = r.get('section_title', '')
        content = r.get('content', '')
        
        header = f"[{i}] {doc_title}"
        if section_num:
            header += f" - Sekcija {section_num}"
        if section_title:
            header += f": {section_title}"
        
        context_parts.append(f"{header}\n{content}")
    
    return "\n\n---\n\n".join(context_parts)

def build_sources_text(results: List[Dict]) -> str:
    """Gradi tekst sa izvorima."""
    if not results:
        return ""
    
    sources = []
    for r in results:
        doc_title = r.get('doc_title', 'Nepoznat')
        section_num = r.get('section_number', '')
        
        if section_num:
            sources.append(f"{doc_title} - Sekcija: {section_num}")
        else:
            sources.append(doc_title)
    
    # Ukloni duplikate zadržavajući redosled
    unique_sources = list(dict.fromkeys(sources))
    
    return "\n📚 **Izvori:**\n" + "\n".join(f"- {s}" for s in unique_sources)

# ============================================================================
# API Endpoints
# ============================================================================

@app.route('/health', methods=['GET'])
@app.route('/v1/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy" if rag_manager.loaded else "loading",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0",
        "models_loaded": rag_manager.loaded,
        "total_chunks": rag_manager.total_chunks,
        "llm_provider": llm_client.provider,
        "llm_model": llm_client.model
    })

@app.route('/models', methods=['GET'])
@app.route('/v1/models', methods=['GET'])
def list_models():
    """Lista dostupnih modela."""
    return jsonify({
        "object": "list",
        "data": [
            {
                "id": "GridMind_0.9",
                "object": "model",
                "created": int(time.time()),
                "owned_by": "gridmind"
            }
        ]
    })

@app.route('/retrieve', methods=['POST'])
@app.route('/v1/retrieve', methods=['POST'])
def retrieve():
    """
    Retrieval endpoint - vraća relevantne dokumente.
    Interno koristi RAGAgent (bez REST API poziva).
    """
    if not rag_manager.loaded:
        return jsonify({"error": {"message": "RAG Agent nije učitan", "type": "service_unavailable"}}), 503
    
    try:
        body = request.get_json() or {}
    except Exception:
        body = {}
    
    # Izvuci query iz različitih formata
    query = (
        body.get('query') or 
        body.get('question') or 
        body.get('input') or 
        body.get('prompt') or 
        body.get('text')
    )
    
    # OpenAI messages format
    if not query and 'messages' in body:
        messages = body.get('messages', [])
        user_messages = [m for m in messages if isinstance(m, dict) and m.get('role') == 'user']
        if user_messages:
            query = user_messages[-1].get('content', '')
    
    if not query:
        return jsonify({"error": {"message": "Morate proslediti 'query', 'question', 'messages' ili 'input'", "type": "invalid_request"}}), 400
    
    # Parametri iz server_config.json
    retrieval_cfg = SERVER_CONFIG.get('retrieval', {})
    top_k = body.get('top_k') or retrieval_cfg.get('top_k', 8)
    initial_k = body.get('initial_k') or retrieval_cfg.get('embedding_top_k', 80)
    score_threshold = body.get('score_threshold') or retrieval_cfg.get('score_threshold', 0.0)
    
    # Interno pozivanje RAGAgent-a (bez REST API-a!)
    try:
        results = rag_manager.agent.retrieve(
            query=query,
            initial_k=initial_k,
            final_k=top_k
        )
    except Exception as e:
        logger.error(f"Retrieval greška: {e}")
        return jsonify({"error": {"message": str(e), "type": "retrieval_error"}}), 500
    
    # Filtriraj po score_threshold
    if score_threshold > 0:
        results = [r for r in results if r.get('rerank_score', 0) >= score_threshold]
    
    # Formatiraj rezultate
    formatted_results = []
    for rank, r in enumerate(results, 1):
        section_num = str(r.get('section_number', '')) if r.get('section_number') else ''
        section_title = r.get('section_title', '')
        section_str = f"{section_num}: {section_title}" if section_num and section_title else section_num or section_title or ''
        
        formatted_results.append({
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
        })
    
    return jsonify({
        "results": formatted_results,
        "query": query,
        "top_k": top_k,
        "total_results": len(formatted_results)
    })

@app.route('/v1/chat/completions', methods=['POST'])
@app.route('/chat/completions', methods=['POST'])
def chat_completions():
    """
    OpenAI-compatible Chat Completions endpoint.
    Koristi interni RAG retrieval + LLM za generisanje odgovora.
    """
    if not rag_manager.loaded:
        return jsonify({"error": {"message": "RAG Agent nije učitan", "type": "service_unavailable"}}), 503
    
    try:
        body = request.get_json() or {}
    except Exception:
        return jsonify({"error": {"message": "Invalid JSON", "type": "invalid_request"}}), 400
    
    messages = body.get('messages', [])
    if not messages:
        return jsonify({"error": {"message": "messages is required", "type": "invalid_request"}}), 400
    
    # Izvuci poslednju user poruku kao query
    user_messages = [m for m in messages if m.get('role') == 'user']
    if not user_messages:
        return jsonify({"error": {"message": "No user message found", "type": "invalid_request"}}), 400
    
    query = user_messages[-1].get('content', '')
    
    # Parametri
    stream = body.get('stream', False)
    model = body.get('model', 'GridMind_0.9')
    include_sources = body.get('include_sources', True)
    
    retrieval_cfg = SERVER_CONFIG.get('retrieval', {})
    top_k = body.get('top_k') or retrieval_cfg.get('top_k', 8)
    initial_k = retrieval_cfg.get('embedding_top_k', 80)
    
    # Interni RAG retrieval
    try:
        results = rag_manager.agent.retrieve(
            query=query,
            initial_k=initial_k,
            final_k=top_k
        )
    except Exception as e:
        logger.error(f"Retrieval greška: {e}")
        return jsonify({"error": {"message": str(e), "type": "retrieval_error"}}), 500
    
    # Filtriraj po score_threshold
    score_threshold = body.get('score_threshold') or retrieval_cfg.get('score_threshold', 0.0)
    if score_threshold > 0:
        results = [r for r in results if r.get('rerank_score', 0) >= score_threshold]
    
    # Gradi kontekst
    context = build_context_from_results(results)
    
    if not context:
        response_content = "Nisam pronašao relevantne informacije za vaše pitanje u dostupnoj dokumentaciji."
        
        if stream:
            return _stream_response(response_content, model)
        else:
            return _non_stream_response(response_content, model, query)
    
    # Gradi LLM poruke
    llm_messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"KONTEKST:\n{context}\n\nPITANJE: {query}"}
    ]
    
    if stream:
        return _stream_chat_response(llm_messages, model, results, include_sources)
    else:
        return _non_stream_chat_response(llm_messages, model, query, results, include_sources)

def _stream_response(content: str, model: str):
    """Vraća jednostavan streaming response."""
    def generate():
        chunk_id = f"chatcmpl-{int(time.time() * 1000)}"
        
        # Pošalji content u jednom chunk-u
        data = {
            "id": chunk_id,
            "object": "chat.completion.chunk",
            "created": int(time.time()),
            "model": model,
            "choices": [{
                "index": 0,
                "delta": {"content": content},
                "finish_reason": None
            }]
        }
        yield f"data: {json.dumps(data)}\n\n"
        
        # Finish
        data["choices"][0]["delta"] = {}
        data["choices"][0]["finish_reason"] = "stop"
        yield f"data: {json.dumps(data)}\n\n"
        yield "data: [DONE]\n\n"
    
    return Response(stream_with_context(generate()), mimetype='text/event-stream')

def _non_stream_response(content: str, model: str, query: str):
    """Vraća jednostavan non-streaming response."""
    return jsonify({
        "id": f"chatcmpl-{int(time.time() * 1000)}",
        "object": "chat.completion",
        "created": int(time.time()),
        "model": model,
        "choices": [{
            "index": 0,
            "message": {"role": "assistant", "content": content},
            "finish_reason": "stop"
        }],
        "usage": {
            "prompt_tokens": len(query) // 4,
            "completion_tokens": len(content) // 4,
            "total_tokens": (len(query) + len(content)) // 4
        }
    })

def _stream_chat_response(llm_messages: List[Dict], model: str, results: List[Dict], include_sources: bool):
    """Streaming LLM response sa RAG."""
    def generate():
        chunk_id = f"chatcmpl-{int(time.time() * 1000)}"
        full_response = ""
        
        try:
            for token in llm_client.generate_stream(llm_messages):
                full_response += token
                data = {
                    "id": chunk_id,
                    "object": "chat.completion.chunk",
                    "created": int(time.time()),
                    "model": model,
                    "choices": [{
                        "index": 0,
                        "delta": {"content": token},
                        "finish_reason": None
                    }]
                }
                yield f"data: {json.dumps(data)}\n\n"
            
            # Dodaj izvore na kraju ako je potrebno
            if include_sources and results:
                sources_text = build_sources_text(results)
                data = {
                    "id": chunk_id,
                    "object": "chat.completion.chunk",
                    "created": int(time.time()),
                    "model": model,
                    "choices": [{
                        "index": 0,
                        "delta": {"content": f"\n\n{sources_text}"},
                        "finish_reason": None
                    }]
                }
                yield f"data: {json.dumps(data)}\n\n"
            
        except Exception as e:
            logger.error(f"LLM streaming greška: {e}")
            error_data = {
                "id": chunk_id,
                "object": "chat.completion.chunk",
                "created": int(time.time()),
                "model": model,
                "choices": [{
                    "index": 0,
                    "delta": {"content": f"\n\n[Greška pri generisanju: {e}]"},
                    "finish_reason": None
                }]
            }
            yield f"data: {json.dumps(error_data)}\n\n"
        
        # Finish
        finish_data = {
            "id": chunk_id,
            "object": "chat.completion.chunk",
            "created": int(time.time()),
            "model": model,
            "choices": [{
                "index": 0,
                "delta": {},
                "finish_reason": "stop"
            }]
        }
        yield f"data: {json.dumps(finish_data)}\n\n"
        yield "data: [DONE]\n\n"
    
    return Response(stream_with_context(generate()), mimetype='text/event-stream')

def _non_stream_chat_response(llm_messages: List[Dict], model: str, query: str, results: List[Dict], include_sources: bool):
    """Non-streaming LLM response sa RAG."""
    try:
        response_content = llm_client.generate(llm_messages, stream=False)
        
        if include_sources and results:
            response_content += "\n\n" + build_sources_text(results)
        
    except Exception as e:
        logger.error(f"LLM greška: {e}")
        response_content = f"Greška pri generisanju odgovora: {e}"
    
    prompt_tokens = sum(len(m.get('content', '')) for m in llm_messages) // 4
    completion_tokens = len(response_content) // 4
    
    return jsonify({
        "id": f"chatcmpl-{int(time.time() * 1000)}",
        "object": "chat.completion",
        "created": int(time.time()),
        "model": model,
        "choices": [{
            "index": 0,
            "message": {"role": "assistant", "content": response_content},
            "finish_reason": "stop"
        }],
        "usage": {
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "total_tokens": prompt_tokens + completion_tokens
        }
    })

@app.route('/', methods=['GET'])
def root():
    """Root endpoint."""
    return jsonify({
        "name": "GridMind RAG API - Unified",
        "version": "1.0.0",
        "description": "RAG API sa internim retrieval-om (bez REST API poziva)",
        "endpoints": {
            "/health": "Health check",
            "/models": "Lista modela",
            "/retrieve": "Retrieval endpoint (POST)",
            "/v1/chat/completions": "OpenAI-compatible chat (POST)"
        },
        "rag_loaded": rag_manager.loaded,
        "total_chunks": rag_manager.total_chunks
    })

# ============================================================================
# Error handlers
# ============================================================================

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": {"message": "Endpoint not found", "type": "not_found"}}), 404

@app.errorhandler(500)
def internal_error(e):
    return jsonify({"error": {"message": str(e), "type": "internal_error"}}), 500

# ============================================================================
# Main
# ============================================================================

def initialize_rag():
    """Inicijalizuje RAG Agent pre pokretanja servera."""
    rag_manager.initialize()

if __name__ == '__main__':
    import argparse
    
    # Defaults iz server_config.json
    server_cfg = SERVER_CONFIG.get('server', {})
    default_host = server_cfg.get('host', '0.0.0.0')
    default_port = server_cfg.get('port', 8888)
    default_debug = server_cfg.get('debug', False)
    
    parser = argparse.ArgumentParser(description='GridMind RAG Server')
    parser.add_argument('--host', type=str, default=default_host, help='Host address')
    parser.add_argument('--port', type=int, default=default_port, help='Port number')
    parser.add_argument('--debug', action='store_true', default=default_debug, help='Debug mode')
    args = parser.parse_args()
    
    # Inicijalizuj RAG pre pokretanja
    initialize_rag()
    
    logger.info(f"\n🚀 Server started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info(f"📡 Listening on http://{args.host}:{args.port}")
    logger.info(f"📁 Logs saved to: {log_file}")
    logger.info(f"⚙️  Config: config/server_config.json")
    logger.info(f"🤖 LLM: {llm_client.provider} / {llm_client.model}")
    
    app.run(host=args.host, port=args.port, debug=args.debug)
