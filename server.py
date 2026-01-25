#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GridMind RAG Server - Unified
=============================

Unified server that uses:
- OllamaRAGChat with internal RAGAgent (no REST API calls)
- StoredKnowledgeManager for expert knowledge
- SessionMemoryManager for conversation memory
- OpenAI-compatible API endpoints

Endpoints:
- POST /v1/chat/completions - OpenAI-compatible chat endpoint
- POST /retrieve - Retrieval endpoint
- GET /health - Health check
- GET /v1/models - Lista modela
- GET /admin/stored-knowledge - List stored knowledge
- GET /admin/sessions - List active sessions
"""

import json
import os
import sys
import time
import uuid
import logging
import argparse
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional
from logging.handlers import TimedRotatingFileHandler

# ============================================================================
# Setup paths
# ============================================================================

ROOT_DIR = Path(__file__).parent

# Add rest/src to path for imports
sys.path.insert(0, str(ROOT_DIR / "rest"))
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
# Flask imports
# ============================================================================

from flask import Flask, request, jsonify, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ============================================================================
# Configuration
# ============================================================================

def load_config() -> dict:
    """Load configuration from config.json in root."""
    config_path = ROOT_DIR / "config.json"
    if config_path.exists():
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    # Fallback to rest/config.json
    rest_config = ROOT_DIR / "rest" / "config.json"
    if rest_config.exists():
        with open(rest_config, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    return {}

CONFIG = load_config()

# ============================================================================
# RAG Chat Instance
# ============================================================================

# Import after path setup
from src.core.chat_rag_api import OllamaRAGChat
from src.core.model_manager import get_model_manager, ModelConfig

# Global RAG chat instance
rag_chat: Optional[OllamaRAGChat] = None


def initialize_rag():
    """Initialize RAG chat with all features."""
    global rag_chat
    
    if rag_chat is not None:
        return
    
    logger.info("\n" + "=" * 60)
    logger.info("GRIDMIND UNIFIED SERVER - Initializing")
    logger.info("=" * 60)
    
    # Use config.json from rest folder (where OllamaRAGChat expects it)
    config_path = str(ROOT_DIR / "rest" / "config.json")
    
    # Initialize OllamaRAGChat with internal RAG (no REST API calls)
    logger.info(f"\n📦 Loading OllamaRAGChat with internal RAG...")
    rag_chat = OllamaRAGChat(config_path=config_path, silent=True, use_internal_rag=True)
    rag_chat.log_chunks = True
    
    logger.info(f"✅ RAG Chat initialized with internal RAGAgent")
    
    # Initialize stored knowledge with BGE reranker
    if rag_chat.use_stored_knowledge:
        try:
            logger.info("📚 Loading stored knowledge with BGE reranker...")
            model_manager = get_model_manager(ModelConfig())
            reranker = model_manager.bge_reranker
            rag_chat.initialize_stored_knowledge(reranker)
            logger.info(f"✅ Stored knowledge ready ({rag_chat.stored_knowledge.count()} entries)")
        except Exception as e:
            logger.warning(f"⚠️ Could not initialize stored knowledge: {e}")
            rag_chat.use_stored_knowledge = False
    
    logger.info("\n✅ RAG system fully initialized!")


# ============================================================================
# Utility Functions
# ============================================================================

def extract_user_question(messages: List[Dict]) -> str:
    """Extract the last user message from messages list."""
    for msg in reversed(messages):
        if msg.get('role') == 'user':
            return msg.get('content', '')
    return ''


def get_session_id(request_data: dict) -> str:
    """Get or generate session ID from request.
    
    OpenWebUI sends chat_id in header 'X-OpenWebUI-Chat-Id' when forwarding requests.
    This is the most reliable way to identify a conversation.
    """
    import hashlib
    
    # Try OpenWebUI specific header first (most reliable)
    session_id = request.headers.get('X-OpenWebUI-Chat-Id')
    
    # Try other common headers
    if not session_id:
        session_id = request.headers.get('X-Session-ID') or \
                     request.headers.get('X-Conversation-ID')
    
    # Try request data (including metadata)
    if not session_id:
        metadata = request_data.get('metadata', {}) or {}
        session_id = metadata.get('chat_id') or \
                     metadata.get('conversation_id') or \
                     metadata.get('session_id') or \
                     request_data.get('session_id') or \
                     request_data.get('conversation_id') or \
                     request_data.get('chat_id')
    
    # Fallback: Generate stable ID from FIRST user message
    if not session_id:
        messages = request_data.get('messages', [])
        
        # Get first user message
        first_user_msg = ""
        for msg in messages:
            if msg.get('role') == 'user':
                # Normalize: strip, lowercase for consistency
                first_user_msg = msg.get('content', '').strip().lower()[:200]
                break
        
        if first_user_msg:
            session_hash = hashlib.sha256(first_user_msg.encode()).hexdigest()[:16]
            session_id = f"chat_{session_hash}"
        else:
            session_id = f"temp_{uuid.uuid4().hex[:8]}"
    
    return session_id


# ============================================================================
# API Endpoints
# ============================================================================

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy",
        "rag_loaded": rag_chat is not None and rag_chat.rag_agent is not None,
        "timestamp": datetime.utcnow().isoformat()
    })


@app.route('/v1/models', methods=['GET'])
@app.route('/models', methods=['GET'])
def list_models():
    """List available models."""
    model_name = CONFIG.get('llm', {}).get('model', 'gemma3:27b')
    # Return multiple model variants to be compatible with different clients
    models = [
        "rag-model",
        "gridmind",
        "gridmind-rag",
        model_name,
        "gpt-3.5-turbo",
        "gpt-4",
    ]
    return jsonify({
        "object": "list",
        "data": [
            {
                "id": m,
                "object": "model",
                "created": int(time.time()),
                "owned_by": "gridmind"
            } for m in models
        ]
    })


@app.route('/retrieve', methods=['POST'])
def retrieve():
    """Retrieval endpoint for document search."""
    if rag_chat is None or rag_chat.rag_agent is None:
        return jsonify({"error": "RAG not initialized"}), 503
    
    data = request.get_json()
    question = data.get('question', '')
    top_k = data.get('top_k', 8)
    
    if not question:
        return jsonify({"error": "question is required"}), 400
    
    try:
        # Use internal RAGAgent
        results = rag_chat.rag_agent.retrieve(question, final_k=top_k)
        
        # Format results
        formatted = []
        for r in results:
            formatted.append({
                "text": r.get('content', ''),
                "score": r.get('rerank_score', r.get('faiss_score', 0)),
                "metadata": {
                    "filename": r.get('doc_title', ''),
                    "section": f"{r.get('section_number', '')} {r.get('section_title', '')}".strip(),
                    "item_number": r.get('object_code', '')
                }
            })
        
        return jsonify({
            "results": formatted,
            "total": len(formatted)
        })
        
    except Exception as e:
        logger.error(f"Retrieve error: {e}")
        return jsonify({"error": str(e)}), 500


@app.route('/v1/chat/completions', methods=['POST'])
def chat_completions():
    """OpenAI-compatible chat completions endpoint."""
    request_start = time.time()
    
    logger.info(f"\n{'='*60}")
    logger.info(f"📨 Request received at {datetime.now().strftime('%H:%M:%S')}")
    logger.info(f"{'='*60}")
    
    if rag_chat is None:
        return jsonify({"error": "RAG not initialized"}), 503
    
    try:
        data = request.get_json(force=True, silent=True)
        
        if data is None:
            return jsonify({
                "error": {
                    "message": "Invalid JSON in request body",
                    "type": "invalid_request_error"
                }
            }), 400
        
        if 'messages' not in data:
            return jsonify({
                "error": {
                    "message": "messages field is required",
                    "type": "invalid_request_error"
                }
            }), 400
        
        messages = data['messages']
        stream = data.get('stream', False)
        model = data.get('model', 'rag-model')
        
        # Get session ID for conversation memory
        session_id = get_session_id(data)
        logger.info(f"📋 Session: {session_id[:12]}...")
        
        # Extract user question
        user_message = extract_user_question(messages)
        logger.info(f"❓ Question: {user_message[:100]}{'...' if len(user_message) > 100 else ''}")
        
        if not user_message:
            return jsonify({
                "error": {
                    "message": "No user message found",
                    "type": "invalid_request_error"
                }
            }), 400
        
        # Check for special commands
        if user_message.strip().lower().startswith('/store '):
            # Handle /store command
            content_to_store = user_message[7:].strip()
            try:
                rag_chat.ensure_stored_knowledge_lazy()
                entry = rag_chat.stored_knowledge.add_entry(content_to_store, stored_by="expert")
                response_text = f"""✅ **Informacija uspešno sačuvana!**

**ID:** `{entry['id'][:8]}...`

**Naslov:** {entry.get('title', 'N/A')}

**Sadržaj:** {content_to_store}

**Vreme:** {entry['timestamp']}

Ova informacija će sada biti dostupna svim korisnicima u svim budućim sesijama."""
            except Exception as e:
                response_text = f"❌ Greška pri čuvanju informacije: {e}"
            
            return _create_response(response_text, model, stream)
        
        if user_message.strip().lower().startswith('/recall '):
            # Handle /recall command
            query = user_message[8:].strip()
            try:
                rag_chat.ensure_stored_knowledge_lazy()
                results = rag_chat.stored_knowledge.search(query, top_k=3)
                if results:
                    response_text = "📚 Found stored knowledge:\n\n"
                    for i, r in enumerate(results, 1):
                        response_text += f"**[{i}]** (score: {r['score']:.3f})\n{r['content']}\n\n"
                else:
                    response_text = "No matching stored knowledge found."
            except Exception as e:
                response_text = f"❌ Failed to recall: {e}"
            
            return _create_response(response_text, model, stream)
        
        # Regular RAG query
        try:
            # Use chat method which handles retrieval, stored knowledge, and LLM
            response_text = rag_chat.chat(
                user_message=user_message,
                session_id=session_id
            )
            
            elapsed = time.time() - request_start
            logger.info(f"⏱️ Response generated in {elapsed:.2f}s")
            
            return _create_response(response_text, model, stream)
            
        except Exception as e:
            logger.error(f"Chat error: {e}")
            return jsonify({
                "error": {
                    "message": str(e),
                    "type": "internal_error"
                }
            }), 500
            
    except Exception as e:
        logger.error(f"Request error: {e}")
        return jsonify({
            "error": {
                "message": str(e),
                "type": "invalid_request_error"
            }
        }), 400


def _create_response(content: str, model: str, stream: bool) -> Response:
    """Create OpenAI-compatible response."""
    response_id = f"chatcmpl-{uuid.uuid4().hex[:8]}"
    
    if stream:
        def generate():
            # Send content in chunks for streaming
            chunk_size = 20
            for i in range(0, len(content), chunk_size):
                chunk = content[i:i+chunk_size]
                data = {
                    "id": response_id,
                    "object": "chat.completion.chunk",
                    "created": int(time.time()),
                    "model": model,
                    "choices": [{
                        "index": 0,
                        "delta": {"content": chunk},
                        "finish_reason": None
                    }]
                }
                yield f"data: {json.dumps(data)}\n\n"
            
            # Final chunk
            final = {
                "id": response_id,
                "object": "chat.completion.chunk",
                "created": int(time.time()),
                "model": model,
                "choices": [{
                    "index": 0,
                    "delta": {},
                    "finish_reason": "stop"
                }]
            }
            yield f"data: {json.dumps(final)}\n\n"
            yield "data: [DONE]\n\n"
        
        return Response(generate(), mimetype='text/event-stream')
    else:
        return jsonify({
            "id": response_id,
            "object": "chat.completion",
            "created": int(time.time()),
            "model": model,
            "choices": [{
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": content
                },
                "finish_reason": "stop"
            }],
            "usage": {
                "prompt_tokens": 0,
                "completion_tokens": len(content.split()),
                "total_tokens": len(content.split())
            }
        })


@app.route('/admin/stored-knowledge', methods=['GET'])
def list_stored_knowledge():
    """List all stored knowledge entries."""
    if rag_chat is None or rag_chat.stored_knowledge is None:
        return jsonify({"entries": [], "count": 0})
    
    try:
        entries = rag_chat.stored_knowledge.list_all()
        return jsonify({
            "entries": entries,
            "count": len(entries)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/admin/sessions', methods=['GET'])
def list_sessions():
    """List active sessions."""
    if rag_chat is None or rag_chat.session_manager is None:
        return jsonify({"sessions": [], "count": 0})
    
    try:
        sessions = rag_chat.session_manager.list_active_sessions()
        return jsonify({
            "sessions": sessions,
            "count": len(sessions)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/', methods=['GET'])
def root():
    """Root endpoint."""
    return jsonify({
        "name": "GridMind Unified RAG Server",
        "version": "2.0.0",
        "features": [
            "Internal RAGAgent (no REST API calls)",
            "Stored Knowledge with BGE reranker",
            "Session Memory (LangChain)",
            "OpenAI-compatible API"
        ],
        "endpoints": {
            "/health": "Health check (GET)",
            "/v1/models": "List models (GET)",
            "/retrieve": "Document retrieval (POST)",
            "/v1/chat/completions": "Chat completions (POST)",
            "/admin/stored-knowledge": "List stored knowledge (GET)",
            "/admin/sessions": "List sessions (GET)"
        }
    })


# ============================================================================
# Error Handlers
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

if __name__ == '__main__':
    # Get server config
    server_cfg = CONFIG.get('server', {})
    default_host = server_cfg.get('host', '0.0.0.0')
    default_port = server_cfg.get('port', 8888)
    
    parser = argparse.ArgumentParser(description='GridMind Unified RAG Server')
    parser.add_argument('--host', type=str, default=default_host)
    parser.add_argument('--port', type=int, default=default_port)
    parser.add_argument('--debug', action='store_true', help='Enable debug mode with auto-reload')
    parser.add_argument('--reload', action='store_true', help='Enable hot reload (for development)')
    args = parser.parse_args()
    
    # Hot reload disabled by default for production, enable with --reload
    use_reloader = args.reload if hasattr(args, 'reload') else False
    
    print(f"""
╔═══════════════════════════════════════════════════════════════╗
║           GridMind Unified RAG Server v2.0                   ║
╠═══════════════════════════════════════════════════════════════╣
║  Host: {args.host:52s} ║
║  Port: {args.port:52d} ║
╠═══════════════════════════════════════════════════════════════╣
║  Features:                                                    ║
║    ✓ Internal RAGAgent (FAISS + BM25 + BGE reranker)         ║
║    ✓ Stored Knowledge with BGE-M3 semantic search            ║
║    ✓ Session Memory (LangChain ConversationBuffer)           ║
║    ✓ OpenAI-compatible API                                   ║
╠═══════════════════════════════════════════════════════════════╣
║  Commands:                                                    ║
║    /store <content>  - Store expert knowledge                ║
║    /recall <query>   - Search stored knowledge               ║
╚═══════════════════════════════════════════════════════════════╝
    """)
    
    # Initialize RAG
    try:
        initialize_rag()
    except Exception as e:
        logger.error(f"❌ Failed to initialize: {e}")
        print(f"⚠️ Warning: RAG will be initialized on first request")
    
    logger.info(f"\n🚀 Server starting on http://{args.host}:{args.port}")
    logger.info(f"📁 Logs: {log_file}")
    if use_reloader:
        logger.info(f"🔄 Hot reload: ENABLED")
    
    app.run(host=args.host, port=args.port, debug=args.debug, use_reloader=use_reloader)
