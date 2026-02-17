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
import re
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
            "OpenAI-compatible API",
            "Knowledge Graph Visualization"
        ],
        "endpoints": {
            "/health": "Health check (GET)",
            "/v1/models": "List models (GET)",
            "/retrieve": "Document retrieval (POST)",
            "/v1/chat/completions": "Chat completions (POST)",
            "/admin/stored-knowledge": "List stored knowledge (GET)",
            "/admin/sessions": "List sessions (GET)",
            "/api/graph/export": "Export graph as JSON (GET)",
            "/graph": "Graph visualization (GET)"
        }
    })


# ============================================================================
# Knowledge Graph Endpoints
# ============================================================================

# Global graph instance (lazy loaded)
_knowledge_graph = None
_graph_exporter = None

def get_knowledge_graph():
    """Get or create knowledge graph instance."""
    global _knowledge_graph, _graph_exporter
    
    if _knowledge_graph is None:
        from pathlib import Path
        import sys
        
        # Add rest directory to path
        rest_dir = Path(__file__).parent / "rest"
        if str(rest_dir) not in sys.path:
            sys.path.insert(0, str(rest_dir))
        
        # Dodaj parser path
        parser_dir = Path(__file__).parent / "rest" / "src" / "graph" / "parsers"
        if str(parser_dir) not in sys.path:
            sys.path.insert(0, str(parser_dir))
        
        from src.graph.builders.graph_builder_v2 import GraphBuilderV2
        from src.graph.visualization import VisJsExporter
        
        # Build or load graph (sa keširanjem)
        files_dir = Path(__file__).parent / "files"
        builder = GraphBuilderV2()
        _knowledge_graph = builder.build_or_load(files_dir)
        _graph_exporter = VisJsExporter(_knowledge_graph)
        
        logger.info(f"[KG] Knowledge Graph loaded: {_knowledge_graph.get_stats()}")
    
    return _knowledge_graph, _graph_exporter


@app.route('/api/graph/export', methods=['GET'])
def export_graph():
    """Export knowledge graph as JSON for vis.js."""
    try:
        graph, exporter = get_knowledge_graph()
        
        # Get filter params
        node_types = request.args.get('nodeTypes')
        edge_types = request.args.get('edgeTypes')
        
        filter_node_types = node_types.split(',') if node_types else None
        filter_edge_types = edge_types.split(',') if edge_types else None
        
        data = exporter.export_json(
            filter_node_types=filter_node_types,
            filter_edge_types=filter_edge_types
        )
        
        return jsonify(data)
    
    except Exception as e:
        logger.error(f"[KG] Export error: {e}")
        return jsonify({"error": str(e)}), 500


@app.route('/api/graph/stats', methods=['GET'])
def graph_stats():
    """Get knowledge graph statistics."""
    try:
        graph, _ = get_knowledge_graph()
        return jsonify(graph.get_stats())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/graph/node/<node_id>', methods=['GET'])
def get_node(node_id):
    """Get node details."""
    try:
        graph, _ = get_knowledge_graph()
        node = graph.get_node(node_id)
        if node:
            return jsonify(node)
        return jsonify({"error": "Node not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/graph/path', methods=['GET'])
def find_path():
    """Find path between two nodes."""
    try:
        graph, _ = get_knowledge_graph()
        
        source = request.args.get('source')
        target = request.args.get('target')
        respect_status = request.args.get('respectStatus', 'true').lower() == 'true'
        
        if not source or not target:
            return jsonify({"error": "source and target required"}), 400
        
        path = graph.find_path(source, target, respect_status=respect_status)
        
        return jsonify({
            "source": source,
            "target": target,
            "path": path,
            "length": len(path) if path else 0
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/graph/connectivity', methods=['GET'])
def get_connectivity():
    """Get connectivity matrix entries for visualization."""
    try:
        graph, _ = get_knowledge_graph()
        
        # Get entries from internal connectivity matrix
        entries = []
        unique_eeo = set()
        by_voltage = {400: 0, 220: 0, 110: 0}
        
        # Use the graph's internal connectivity matrix
        for entry in graph._connectivity_matrix:
            entries.append({
                'eeo_x_id': entry.eeo_x_id,
                'dvp_x_index': entry.dvp_x_index,
                'eeo_y_id': entry.eeo_y_id,
                'dvp_y_index': entry.dvp_y_index,
                'voltage_kv': entry.voltage_kv,
                'line_id': entry.line_id or '',
                'line_type': entry.line_type
            })
            
            unique_eeo.add(entry.eeo_x_id)
            unique_eeo.add(entry.eeo_y_id)
            if entry.voltage_kv in by_voltage:
                by_voltage[entry.voltage_kv] += 1
        
        # Remove duplicates
        seen = set()
        unique_entries = []
        for e in entries:
            key = (e['eeo_x_id'], e['eeo_y_id'], e['voltage_kv'])
            rev_key = (e['eeo_y_id'], e['eeo_x_id'], e['voltage_kv'])
            if key not in seen and rev_key not in seen:
                seen.add(key)
                unique_entries.append(e)
        
        return jsonify({
            'entries': unique_entries,
            'total': len(unique_entries),
            'unique_eeo': len(unique_eeo),
            'by_voltage': by_voltage
        })
        
    except Exception as e:
        logger.error(f"[KG] Connectivity error: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


@app.route('/matrix', methods=['GET'])
def connectivity_matrix_viewer():
    """Serve connectivity matrix page."""
    from flask import send_file
    from pathlib import Path
    
    html_path = Path(__file__).parent / "rest" / "src" / "graph" / "visualization" / "connectivity_matrix.html"
    return send_file(html_path)


@app.route('/graph', methods=['GET'])
def graph_viewer():
    """Serve graph visualization page."""
    from flask import send_file
    from pathlib import Path
    
    html_path = Path(__file__).parent / "rest" / "src" / "graph" / "visualization" / "graph_viewer.html"
    return send_file(html_path)


@app.route('/diagram', methods=['GET'])
def single_line_viewer():
    """Serve single line diagram page."""
    from flask import send_file
    from pathlib import Path
    
    html_path = Path(__file__).parent / "rest" / "src" / "graph" / "visualization" / "single_line_viewer.html"
    return send_file(html_path)


@app.route('/api/graph/diagram/<eeo_id>', methods=['GET'])
def get_diagram(eeo_id):
    """Generate single line diagram SVG for EEO."""
    try:
        graph, _ = get_knowledge_graph()
        
        # Import generator
        from rest.src.graph.visualization.single_line_diagram import generate_single_line_diagram
        
        svg = generate_single_line_diagram(graph, eeo_id)
        
        return Response(svg, mimetype='image/svg+xml')
    
    except Exception as e:
        logger.error(f"[KG] Diagram error: {e}")
        return Response(
            f'<svg xmlns="http://www.w3.org/2000/svg" width="400" height="100"><text x="10" y="50" fill="red">{str(e)}</text></svg>',
            mimetype='image/svg+xml'
        )


# ============================================================================
# Simulator uklopnih stanja API
# ============================================================================

@app.route('/simulator', methods=['GET'])
def simulator_viewer():
    """Serve switching state simulator page."""
    from flask import send_file
    from pathlib import Path
    html_path = Path(__file__).parent / "rest" / "src" / "graph" / "visualization" / "simulator.html"
    return send_file(html_path)


@app.route('/simulator-v2', methods=['GET'])
def simulator_v2_viewer():
    """Serve v2 single-line diagram simulator page."""
    from flask import send_file
    from pathlib import Path
    html_path = Path(__file__).parent / "rest" / "src" / "graph" / "visualization" / "simulator_v2.html"
    return send_file(html_path)


@app.route('/api/graph/simulator/eeo-data/<eeo_id>', methods=['GET'])
def get_eeo_simulator_data(eeo_id):
    """Get full EEO topology for interactive simulator rendering."""
    try:
        graph, _ = get_knowledge_graph()
        
        eeo_node = graph.get_node(eeo_id)
        if not eeo_node:
            return jsonify({"error": f"EEO {eeo_id} not found"}), 404
        
        voltage_levels = sorted(eeo_node.get('voltage_levels', []), reverse=True)
        eeo_nodes = graph._nodes_by_eeo.get(eeo_id, set())
        
        # Collect busbars, fields, elements, transformers
        busbars = {}   # voltage -> [{id, index}]
        fields = {}    # voltage -> [{id, name, gss_index, elements: [{id, type, status}]}]
        transformers = []
        
        for node_id in eeo_nodes:
            node = graph.get_node(node_id)
            if not node:
                continue
            
            nt = node.get('node_type')
            voltage = node.get('voltage_kv')
            
            if nt == 'GSS':
                busbars.setdefault(voltage, []).append({
                    'id': node_id,
                    'index': node.get('index', 1),
                })
            elif nt in ('DVP', 'KBP', 'TRPVN', 'TRPNN', 'GSP', 'PSP'):
                elements = []
                for neighbor in graph._graph.neighbors(node_id):
                    n = graph.get_node(neighbor)
                    if n and n.get('node_type') in ('SR', 'P', 'SMT', 'IRSU', 'NMT', 'IR', 'OP'):
                        elements.append({
                            'id': neighbor,
                            'type': n['node_type'],
                            'status': n.get('status'),
                            'connected_busbar': n.get('connected_busbar'),
                        })
                
                fields.setdefault(voltage, []).append({
                    'id': node_id,
                    'name': node.get('name', node_id),
                    'line_name': node.get('line_name', ''),
                    'gss_index': node.get('gss_index', 1),
                    'type': nt,
                    'elements': elements,
                })
            elif nt == 'TR':
                transformers.append({
                    'id': node_id,
                    'name': node.get('name', node_id),
                    'vn_kv': node.get('vn_kv'),
                    'nn_kv': node.get('nn_kv'),
                    'power_mva': node.get('power_mva'),
                })
        
        # Get available uklopna stanja from parser data
        available_states = []
        try:
            from rest.src.graph.builders.graph_builder_v2 import GraphBuilderV2
            builder = GraphBuilderV2()
            from pathlib import Path
            files_dir = Path(__file__).parent / "files"
            # Parse only this EEO's file
            for f in files_dir.glob("*.txt"):
                parsed = builder.parser.parse_file(f)
                if parsed and parsed.kod == eeo_id:
                    for state_name, voltage_states in parsed.uklopna_stanja.items():
                        state_info = {'name': state_name, 'voltages': {}}
                        for vkv, us in voltage_states.items():
                            state_info['voltages'][str(vkv)] = {
                                'gs1': us.polja_gs1,
                                'gs2': us.polja_gs2,
                                'spojno_polje': us.spojno_polje,
                                'dzs_aktivna': us.dzs_aktivna,
                            }
                        available_states.append(state_info)
                    break
        except Exception as e:
            logger.warning(f"[SIM] Could not load uklopna stanja: {e}")
        
        return jsonify({
            'eeo_id': eeo_id,
            'name': eeo_node.get('name', eeo_id),
            'voltage_levels': voltage_levels,
            'busbars': {str(k): v for k, v in busbars.items()},
            'fields': {str(k): v for k, v in fields.items()},
            'transformers': transformers,
            'available_states': available_states,
        })
        
    except Exception as e:
        logger.error(f"[SIM] EEO data error: {e}")
        import traceback; traceback.print_exc()
        return jsonify({"error": str(e)}), 500


@app.route('/api/graph/simulator/toggle/<node_id>', methods=['POST'])
def toggle_element(node_id):
    """Toggle element status (P, SR, IRSU)."""
    try:
        graph, _ = get_knowledge_graph()
        
        node = graph.get_node(node_id)
        if not node:
            return jsonify({"error": f"Node {node_id} not found"}), 404
        
        nt = node.get('node_type', '')
        if nt not in ('P', 'SR', 'IRSU', 'IR', 'OP'):
            return jsonify({"error": f"Cannot toggle {nt} - only P, SR, IRSU, IR, OP"}), 400
        
        # Toggle status
        current = node.get('status', 1)
        new_status = 0 if current == 1 else 1
        graph._graph.nodes[node_id]['status'] = new_status
        
        logger.info(f"[SIM] Toggled {node_id}: {current} -> {new_status}")
        
        # Return updated energization for this EEO
        eeo_id = node.get('eeo_id')
        energized = _compute_energization(graph, eeo_id) if eeo_id else {}
        
        return jsonify({
            'node_id': node_id,
            'old_status': current,
            'new_status': new_status,
            'energized': energized,
        })
        
    except Exception as e:
        logger.error(f"[SIM] Toggle error: {e}")
        return jsonify({"error": str(e)}), 500


@app.route('/api/graph/simulator/set-status/<node_id>/<int:status>', methods=['POST'])
def set_element_status(node_id, status):
    """Set element status explicitly (0 or 1)."""
    try:
        graph, _ = get_knowledge_graph()
        
        node = graph.get_node(node_id)
        if not node:
            return jsonify({"error": f"Node {node_id} not found"}), 404
        
        if status not in (0, 1):
            return jsonify({"error": "Status must be 0 or 1"}), 400
        
        graph._graph.nodes[node_id]['status'] = status
        
        return jsonify({'node_id': node_id, 'status': status})
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/graph/simulator/reset/<eeo_id>', methods=['POST'])
def reset_eeo_state(eeo_id):
    """Reset all switching elements in EEO to normal (all closed)."""
    try:
        graph, _ = get_knowledge_graph()
        
        eeo_nodes = graph._nodes_by_eeo.get(eeo_id, set())
        toggled = 0
        
        for node_id in eeo_nodes:
            node = graph.get_node(node_id)
            if node and node.get('node_type') in ('P', 'SR', 'IRSU', 'IR', 'OP'):
                if node.get('status') != 1:
                    graph._graph.nodes[node_id]['status'] = 1
                    toggled += 1
        
        energized = _compute_energization(graph, eeo_id)
        
        return jsonify({
            'eeo_id': eeo_id,
            'toggled': toggled,
            'message': f'Reset {toggled} elements to closed',
            'energized': energized,
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/graph/simulator/apply-state/<eeo_id>', methods=['POST'])
def apply_uklopno_stanje(eeo_id):
    """Apply predefined uklopno stanje to EEO."""
    try:
        graph, _ = get_knowledge_graph()
        data = request.get_json() or {}
        state_name = data.get('state_name', 'normalno')
        
        # Get uklopno stanje data
        states_data = data.get('states', {})
        
        eeo_nodes = graph._nodes_by_eeo.get(eeo_id, set())
        toggled = 0
        
        # First reset all to closed
        for node_id in eeo_nodes:
            node = graph.get_node(node_id)
            if node and node.get('node_type') in ('P', 'SR', 'IRSU', 'IR', 'OP'):
                graph._graph.nodes[node_id]['status'] = 1
        
        # Apply specific state rules
        # states_data format: {"110": {"gs1": ["DV.."], "gs2": ["DV.."]}}
        for voltage_str, vs in states_data.items():
            gs1_fields = set(vs.get('gs1', []))
            gs2_fields = set(vs.get('gs2', []))
            all_state_fields = gs1_fields | gs2_fields
            
            # Find fields at this voltage that are NOT in the state -> open them
            voltage = int(voltage_str)
            for node_id in eeo_nodes:
                node = graph.get_node(node_id)
                if not node or node.get('node_type') not in ('DVP', 'KBP', 'TRPVN', 'TRPNN', 'GSP', 'PSP'):
                    continue
                if node.get('voltage_kv') != voltage:
                    continue
                    
                field_name = node.get('line_name', '')
                field_name_norm = re.sub(r'\s+', '', field_name).upper()
                
                # Check if field is in state
                in_state = False
                for sf in all_state_fields:
                    sf_norm = re.sub(r'\s+', '', sf).upper()
                    if sf_norm == field_name_norm or sf_norm in field_name_norm or field_name_norm in sf_norm:
                        in_state = True
                        break
                
                if not in_state:
                    # Open all switchgear in this field
                    for neighbor in graph._graph.neighbors(node_id):
                        n = graph.get_node(neighbor)
                        if n and n.get('node_type') in ('P', 'SR', 'IRSU', 'IR', 'OP'):
                            if n.get('status') != 0:
                                graph._graph.nodes[neighbor]['status'] = 0
                                toggled += 1
        
        energized = _compute_energization(graph, eeo_id)
        
        return jsonify({
            'eeo_id': eeo_id,
            'state': state_name,
            'toggled': toggled,
            'energized': energized,
        })
        
    except Exception as e:
        logger.error(f"[SIM] Apply state error: {e}")
        import traceback; traceback.print_exc()
        return jsonify({"error": str(e)}), 500


@app.route('/api/graph/simulator/energized/<eeo_id>', methods=['GET'])
def get_energization(eeo_id):
    """Get energization analysis for EEO."""
    try:
        graph, _ = get_knowledge_graph()
        energized = _compute_energization(graph, eeo_id)
        return jsonify(energized)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def _compute_energization(graph, eeo_id: str) -> dict:
    """Compute energization status for all elements in an EEO.
    
    Only traverses GALVANSKA_VEZA edges (not SADRZI) to correctly
    model electrical connectivity through the breaker chain.
    """
    eeo_nodes = graph._nodes_by_eeo.get(eeo_id, set())
    
    # Source nodes = busbars (GSS) - they are always energized
    source_nodes = set()
    for node_id in eeo_nodes:
        node = graph.get_node(node_id)
        if node and node.get('node_type') == 'GSS':
            source_nodes.add(node_id)
    
    # BFS from each source, only via GALVANSKA_VEZA edges, respecting switch status
    from collections import deque
    
    reachable = set()
    for source in source_nodes:
        visited = set()
        queue = deque([source])
        
        while queue:
            current = queue.popleft()
            if current in visited:
                continue
            visited.add(current)
            reachable.add(current)
            
            # Only follow GALVANSKA_VEZA edges
            for u, v, edge_data in graph._graph.edges(current, data=True):
                neighbor = v if u == current else u
                if neighbor in visited:
                    continue
                
                # Only traverse galvanska veza edges (not SADRZI)
                if edge_data.get('edge_type') not in ('GALVANSKI_VEZAN', 'GALVANSKA_VEZA', 'connected_to'):
                    continue
                
                n_node = graph.get_node(neighbor)
                if n_node:
                    # If it's a switching element and it's open, don't traverse past it
                    if n_node.get('node_type') in ('P', 'SR', 'IRSU', 'IR', 'OP') and n_node.get('status') == 0:
                        # Mark the switch itself but don't continue past
                        continue
                
                queue.append(neighbor)
    
    # Build result: for each node in this EEO, is it reachable from a busbar?
    result = {}
    for node_id in eeo_nodes:
        node = graph.get_node(node_id)
        if node:
            result[node_id] = {
                'energized': node_id in reachable,
                'type': node.get('node_type', ''),
                'status': node.get('status'),
            }
    
    return result


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
