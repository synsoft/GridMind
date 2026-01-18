#!/usr/bin/env python3
"""
OpenAI-compatible REST API server za RAG sistem.
Implementira /v1/chat/completions endpoint koji se moze koristiti iz OpenWebUI.
"""

from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import json
import uuid
import time
import hashlib
import re
import logging
from typing import Dict, Any, Generator

from src.core.chat_rag_api import OllamaRAGChat
from src.core.model_manager import get_model_manager, ModelConfig
from src.utils.input_validator import validate_question, validate_session_id

logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)  # Omogućava CORS za sve endpointe

# Globalna instanca RAG chata
rag_chat = None
config_path = "config.json"


def initialize_rag():
    """Inicijalizuje RAG chat."""
    global rag_chat
    if rag_chat is None:
        logger.info("Inicijalizujem RAG sistem...")
        print("Inicijalizujem RAG sistem...")
        
        # silent=True da ne stampa stream u konzolu servera, ali chunk info će se logovati
        rag_chat = OllamaRAGChat(config_path=config_path, silent=True)
        # Forsiraj logovanje chunk-ova
        rag_chat.log_chunks = True
        
        # Učitaj stored knowledge ako je omogućeno u konfiguraciji
        if rag_chat.use_stored_knowledge:
            try:
                # Use ModelManager singleton for reranker
                model_manager = get_model_manager(ModelConfig())
                reranker = model_manager.bge_reranker
                rag_chat.initialize_stored_knowledge(reranker)
                logger.info(f"Stored knowledge ready ({rag_chat.stored_knowledge.count()} entries)")
                print(f"✅ Stored knowledge ready ({rag_chat.stored_knowledge.count()} entries)")
            except Exception as e:
                logger.warning(f"Could not initialize stored knowledge: {e}")
                print(f"⚠️ Could not initialize stored knowledge: {e}")
                print("   Stored knowledge will be disabled")
                rag_chat.use_stored_knowledge = False
        
        logger.info("RAG sistem spreman!")
        print("RAG sistem spreman!")


def ensure_stored_knowledge():
    """Lazy initialization of stored knowledge (samo kada je potrebno)."""
    if rag_chat.stored_knowledge is None:
        try:
            # Use ModelManager singleton - model loaded only once
            model_manager = get_model_manager()
            reranker = model_manager.bge_reranker
            logger.info("Loading stored knowledge with BGE reranker...")
            print("⏳ Loading BGE reranker-v2-m3 for stored knowledge (first use)...")
            rag_chat.initialize_stored_knowledge(reranker)
            logger.info(f"Stored knowledge ready ({rag_chat.stored_knowledge.count()} entries)")
            print(f"✅ Stored knowledge ready with BGE reranker-v2-m3 ({rag_chat.stored_knowledge.count()} entries)")
        except Exception as e:
            logger.error(f"Could not initialize stored knowledge: {e}")
            print(f"⚠️ Could not initialize stored knowledge: {e}")
            print("   Stored knowledge will work without reranker (basic search only)")
            raise


@app.route('/v1/chat/completions', methods=['POST'])
def chat_completions():
    """OpenAI-compatible chat completions endpoint."""
    # ⏱️ START: Log vremena prijema zahteva
    request_start_time = time.time()
    print(f"\n{'='*80}")
    print(f"⏱️  REQUEST RECEIVED at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(request_start_time))}.{int((request_start_time % 1) * 1000):03d}")
    print(f"{'='*80}")
    
    try:
        data = request.get_json()
        
        # Validacija
        if 'messages' not in data:
            return jsonify({
                'error': {
                    'message': 'messages field is required',
                    'type': 'invalid_request_error',
                    'code': 'missing_messages'
                }
            }), 400
        
        messages = data['messages']
        stream = data.get('stream', False)
        model = data.get('model', 'rag-model')
        temperature = data.get('temperature', 0.7)
        max_tokens = data.get('max_tokens', 2000)
        
        # DEBUG: Log sve podatke iz requesta
        print(f"\n{'='*80}")
        print("🔍 DEBUG REQUEST INFO:")
        print(f"{'='*80}")
        print(f"📋 Headers: {dict(request.headers)}")
        print(f"📦 Data keys: {list(data.keys())}")
        print(f"💬 Messages count: {len(messages)}")
        
        # Log first user message for debugging session creation
        for msg in messages:
            if msg.get('role') == 'user':
                first_user = msg.get('content', '')[:100]
                print(f"👤 First user msg: '{first_user}'")
                break
        
        # Pokušaj da nađeš session identifikator iz raznih izvora
        # OpenWebUI šalje metadata objekat sa chat_id
        metadata = data.get('metadata', {}) or {}
        print(f"📎 Metadata: {metadata}")
        
        potential_session_ids = {
            'X-Session-ID': request.headers.get('X-Session-ID'),
            'X-Conversation-ID': request.headers.get('X-Conversation-ID'),
            'Authorization': request.headers.get('Authorization'),
            'metadata.chat_id': metadata.get('chat_id'),
            'metadata.conversation_id': metadata.get('conversation_id'),
            'metadata.session_id': metadata.get('session_id'),
            'data.session_id': data.get('session_id'),
            'data.conversation_id': data.get('conversation_id'),
            'data.user_id': data.get('user_id'),
            'data.chat_id': data.get('chat_id'),
            'data.id': data.get('id'),
        }
        
        print(f"🔍 Potential session IDs:")
        for key, value in potential_session_ids.items():
            if value:
                print(f"   {key}: {str(value)[:50]}...")
        
        # Extract session_id (OpenWebUI šalje chat_id u metadata objektu)
        session_id = (
            request.headers.get('X-Session-ID') or
            request.headers.get('X-Conversation-ID') or
            metadata.get('chat_id') or               # OpenWebUI primarni identifikator
            metadata.get('conversation_id') or
            metadata.get('session_id') or
            data.get('session_id') or
            data.get('conversation_id') or
            data.get('chat_id') or
            data.get('id') or
            data.get('user_id')
        )
        
        # Ako nema session_id, kreiraj stabilan ID na osnovu SAMO prve user poruke
        # (bez User-Agent i IP koji se mogu menjati između requestova)
        if not session_id:
            import hashlib
            
            # Pronađi prvu user poruku
            first_user_msg = ""
            for msg in messages:
                if msg.get('role') == 'user':
                    # Normalizuj poruku: lowercase, strip whitespace
                    first_user_msg = msg.get('content', '').strip().lower()[:200]
                    break
            
            if first_user_msg:
                # Hash SAMO prve user poruke (stabilno između requestova)
                session_hash = hashlib.sha256(first_user_msg.encode()).hexdigest()[:16]
                session_id = f"chat_{session_hash}"
                logger.info(f"🔄 Created session from first msg: '{first_user_msg[:30]}...' -> {session_id}")
                print(f"🔄 Session from first msg: '{first_user_msg[:30]}...' -> {session_id}")
            else:
                # Fallback: temporary session
                session_id = f"temp_{uuid.uuid4().hex[:16]}"
                logger.warning(f"⚠️ Temporary session (no user messages): {session_id}")
                print(f"⚠️ Temporary session: {session_id}")
        
        logger.info(f"🔑 Final Session ID: {session_id[:24]}... | Metadata: {metadata}")
        print(f"🔑 Final Session ID: {session_id[:24]}...")
        print(f"{'='*80}\n")
        
        # Izvuci poslednju user poruku
        user_message = None
        for msg in reversed(messages):
            if msg.get('role') == 'user':
                user_message = msg.get('content', '')
                break
        
        if not user_message:
            return jsonify({
                'error': {
                    'message': 'No user message found',
                    'type': 'invalid_request_error',
                    'code': 'no_user_message'
                }
            }), 400
        
        # Validate and sanitize user input
        is_valid, user_message, error_msg = validate_question(user_message)
        if not is_valid:
            logger.warning(f"Invalid user message: {error_msg}")
            return jsonify({
                'error': {
                    'message': error_msg,
                    'type': 'invalid_request_error',
                    'code': 'invalid_message'
                }
            }), 400
        
        # Validate session_id
        _, session_id, _ = validate_session_id(session_id)
        
        # Inicijalizuj RAG ako nije
        initialize_rag()
        
        # Pozovi RAG sistem
        if stream:
            response = Response(
                stream_response(user_message, model, session_id, request_start_time),
                mimetype='text/event-stream'
            )
            # Dodatni headeri za SSE streaming
            response.headers['Cache-Control'] = 'no-cache'
            response.headers['X-Accel-Buffering'] = 'no'
            response.headers['Connection'] = 'keep-alive'
            
            # ⏱️ END: Log vremena slanja response-a (headers sent)
            response_time = time.time()
            elapsed = response_time - request_start_time
            print(f"\n{'='*80}")
            print(f"⏱️  RESPONSE STARTED (stream) at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(response_time))}.{int((response_time % 1) * 1000):03d}")
            print(f"⏱️  TOTAL TIME: {elapsed:.3f}s ({elapsed*1000:.1f}ms)")
            print(f"{'='*80}\n")
            
            return response
        else:
            result = non_stream_response(user_message, model, max_tokens, session_id, request_start_time)
            
            # ⏱️ END: Log vremena slanja response-a
            response_time = time.time()
            elapsed = response_time - request_start_time
            print(f"\n{'='*80}")
            print(f"⏱️  RESPONSE SENT at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(response_time))}.{int((response_time % 1) * 1000):03d}")
            print(f"⏱️  TOTAL TIME: {elapsed:.3f}s ({elapsed*1000:.1f}ms)")
            print(f"{'='*80}\n")
            
            return result
    
    except Exception as e:
        print(f"Error u chat_completions: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({
            'error': {
                'message': str(e),
                'type': 'internal_error',
                'code': 'internal_error'
            }
        }), 500


def non_stream_response(question: str, model: str, max_tokens: int, session_id: str = None, request_start_time: float = None) -> Dict[str, Any]:
    """Generiše non-streaming odgovor."""
    try:
        processing_start = time.time()
        print(f"\n{'='*80}")
        print(f"📥 NON-STREAM REQUEST")
        print(f"{'='*80}")
        print(f"❓ Question: {question}")
        print(f"🔑 Session: {session_id[:16] if session_id else 'N/A'}...")
        if request_start_time:
            prep_time = processing_start - request_start_time
            print(f"⏱️  Preparation time: {prep_time:.3f}s ({prep_time*1000:.1f}ms)")
        print(f"{'='*80}\n")
        
        # ⏱️ Počni merenje RAG obrade
        rag_start = time.time()
        
        # Pozovi RAG chat sa session_id (already saves to session memory internally)
        answer = rag_chat.chat(question, session_id=session_id)
        
        # ⏱️ Završi merenje RAG obrade
        rag_end = time.time()
        rag_time = rag_end - rag_start
        
        print(f"\n{'='*80}")
        print(f"📤 NON-STREAM RESPONSE")
        print(f"{'='*80}")
        print(f"✅ Answer length: {len(answer)} characters")
        print(f"Preview: {answer[:200]}...")
        print(f"⏱️  RAG processing time: {rag_time:.3f}s ({rag_time*1000:.1f}ms)")
        if request_start_time:
            total_so_far = time.time() - request_start_time
            print(f"⏱️  Total time so far: {total_so_far:.3f}s ({total_so_far*1000:.1f}ms)")
        print(f"{'='*80}\n")
        
        # Kreiraj OpenAI format odgovora
        response = {
            'id': f'chatcmpl-{uuid.uuid4().hex[:24]}',
            'object': 'chat.completion',
            'created': int(time.time()),
            'model': model,
            'choices': [
                {
                    'index': 0,
                    'message': {
                        'role': 'assistant',
                        'content': answer
                    },
                    'finish_reason': 'stop'
                }
            ],
            'usage': {
                'prompt_tokens': len(question.split()),
                'completion_tokens': len(answer.split()),
                'total_tokens': len(question.split()) + len(answer.split())
            }
        }
        
        return jsonify(response)
    
    except Exception as e:
        print(f"Error u non_stream_response: {e}")
        import traceback
        traceback.print_exc()
        raise


def stream_response(question: str, model: str, session_id: str = None, request_start_time: float = None) -> Generator[str, None, None]:
    """Generiše streaming odgovor u OpenAI formatu."""
    try:
        processing_start = time.time()
        print(f"\n{'='*80}")
        print(f"📥 STREAM REQUEST")
        print(f"{'='*80}")
        print(f"❓ Question: {question}")
        print(f"🔑 Session: {session_id[:16] if session_id else 'N/A'}...")
        print(f"🆔 Chat ID: chatcmpl-{uuid.uuid4().hex[:24]}")
        if request_start_time:
            prep_time = processing_start - request_start_time
            print(f"⏱️  Preparation time: {prep_time:.3f}s ({prep_time*1000:.1f}ms)")
        print(f"{'='*80}\n")
        
        chat_id = f'chatcmpl-{uuid.uuid4().hex[:24]}'
        created = int(time.time())
        
        # Inicijalni chunk
        initial_chunk = {
            'id': chat_id,
            'object': 'chat.completion.chunk',
            'created': created,
            'model': model,
            'choices': [
                {
                    'index': 0,
                    'delta': {'role': 'assistant', 'content': ''},
                    'finish_reason': None
                }
            ]
        }
        yield f"data: {json.dumps(initial_chunk)}\n\n"
        
        # ⏱️ Počni merenje RAG obrade
        rag_start = time.time()
        
        # Za sada koristi non-streaming i simuliraj streaming
        # (RAG chat nema direktan streaming API, već čuva u session memory interno)
        answer = rag_chat.chat(question, session_id=session_id)
        
        # ⏱️ Završi merenje RAG obrade
        rag_end = time.time()
        rag_time = rag_end - rag_start
        
        print(f"\n{'='*80}")
        print(f"📤 STREAM RESPONSE READY")
        print(f"{'='*80}")
        print(f"✅ Answer length: {len(answer)} characters")
        print(f"Preview: {answer[:200]}...")
        print(f"⏱️  RAG processing time: {rag_time:.3f}s ({rag_time*1000:.1f}ms)")
        if request_start_time:
            total_so_far = time.time() - request_start_time
            print(f"⏱️  Total time so far: {total_so_far:.3f}s ({total_so_far*1000:.1f}ms)")
        print(f"{'='*80}\n")
        
        # Simuliraj streaming po tokenima ali ČUVAJ nove redove i formatiranje
        # Deli tekst na delove tako da čuva strukturu
        import re
        import time as time_module
        # Split on whitespace but keep newlines
        tokens = re.findall(r'\S+|\n+', answer)
        
        print(f"🔄 Streaming {len(tokens)} tokens...")
        
        # ⏱️ Počni merenje streaming faze
        streaming_start = time.time()
        
        for i, token in enumerate(tokens):
            # Preserve formatting characters
            chunk_text = token
            if i < len(tokens) - 1 and not token.endswith('\n') and not tokens[i+1].startswith('\n'):
                chunk_text += ' '
            
            stream_chunk = {
                'id': chat_id,
                'object': 'chat.completion.chunk',
                'created': created,
                'model': model,
                'choices': [
                    {
                        'index': 0,
                        'delta': {'content': chunk_text},
                        'finish_reason': None
                    }
                ]
            }
            yield f"data: {json.dumps(stream_chunk)}\n\n"
            
            # Minimal delay for natural streaming (reduced from 20ms to 5ms)
            time.sleep(0.005)
        
        # ⏱️ Završi merenje streaming faze
        streaming_end = time.time()
        streaming_time = streaming_end - streaming_start
        
        print(f"✅ Streaming completed: {len(tokens)} tokens sent")
        print(f"⏱️  Streaming time: {streaming_time:.3f}s ({streaming_time*1000:.1f}ms)")
        if request_start_time:
            total_time = streaming_end - request_start_time
            print(f"⏱️  TOTAL REQUEST TIME: {total_time:.3f}s ({total_time*1000:.1f}ms)")
        print()
        
        # Finalni chunk
        final_chunk = {
            'id': chat_id,
            'object': 'chat.completion.chunk',
            'created': created,
            'model': model,
            'choices': [
                {
                    'index': 0,
                    'delta': {},
                    'finish_reason': 'stop'
                }
            ]
        }
        yield f"data: {json.dumps(final_chunk)}\n\n"
        yield "data: [DONE]\n\n"
    
    except Exception as e:
        print(f"Error u stream_response: {e}")
        import traceback
        traceback.print_exc()
        error_chunk = {
            'error': {
                'message': str(e),
                'type': 'internal_error',
                'code': 'stream_error'
            }
        }
        yield f"data: {json.dumps(error_chunk)}\n\n"


@app.route('/v1/models', methods=['GET'])
def list_models():
    """Lista dostupnih modela (OpenAI compatible)."""
    return jsonify({
        'object': 'list',
        'data': [
            {
                'id': 'Gridmind v0.8',
                'object': 'model',
                'created': int(time.time()),
                'owned_by': 'gridmind'
            }
        ]
    })


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint."""
    try:
        initialize_rag()
        return jsonify({
            'status': 'healthy',
            'rag_initialized': rag_chat is not None
        })
    except Exception as e:
        return jsonify({
            'status': 'unhealthy',
            'error': str(e)
        }), 500


@app.route('/admin/stored-knowledge', methods=['GET'])
def list_stored_knowledge():
    """Admin endpoint - lista stored knowledge."""
    try:
        initialize_rag()
        ensure_stored_knowledge()  # Lazy load stored knowledge
        
        entries = rag_chat.stored_knowledge.list_all()
        return jsonify({
            'count': len(entries),
            'entries': entries
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/admin/sessions', methods=['GET'])
def list_sessions():
    """Admin endpoint - lista aktivnih sesija."""
    try:
        initialize_rag()
        sessions = rag_chat.session_manager.list_active_sessions()
        session_info = []
        
        for session_id in sessions:
            info = rag_chat.session_manager.get_session_info(session_id)
            if info:
                session_info.append(info)
        
        return jsonify({
            'active_sessions': len(sessions),
            'sessions': session_info
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/', methods=['GET'])
def root():
    """Root endpoint sa informacijama."""
    return jsonify({
        'name': 'RAG OpenAI-compatible API',
        'version': '1.1.0',
        'features': [
            'LangChain ConversationBufferWindowMemory (window=10)',
            'Session-based memory isolation',
            '/store command for persistent expert knowledge',
            'BGE-M3 semantic search for stored knowledge'
        ],
        'endpoints': {
            '/v1/chat/completions': 'POST - Chat completions (OpenAI compatible)',
            '/v1/models': 'GET - List available models',
            '/health': 'GET - Health check',
            '/admin/stored-knowledge': 'GET - List stored knowledge entries',
            '/admin/sessions': 'GET - List active sessions'
        }
    })


if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='RAG OpenAI API Server')
    parser.add_argument('--host', default='0.0.0.0', help='Host to bind to')
    parser.add_argument('--port', type=int, default=5000, help='Port to listen on')
    parser.add_argument('--config', default='config.json', help='Config file path')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    
    args = parser.parse_args()
    config_path = args.config
    
    print(f"""
╔════════════════════════════════════════════════════════════╗
║         RAG OpenAI-Compatible API Server v1.1             ║
╠════════════════════════════════════════════════════════════╣
║  Host: {args.host:48s} ║
║  Port: {args.port:48d} ║
║  Config: {args.config:46s} ║
╠════════════════════════════════════════════════════════════╣
║  Features:                                                 ║
║    ✓ LangChain Session Memory (window=10)                 ║
║    ✓ /store command for expert knowledge                  ║
║    ✓ BGE-M3 semantic search                               ║
╠════════════════════════════════════════════════════════════╣
║  Endpoints:                                                ║
║    POST http://{args.host}:{args.port}/v1/chat/completions       ║
║    GET  http://{args.host}:{args.port}/v1/models                 ║
║    GET  http://{args.host}:{args.port}/health                    ║
║    GET  http://{args.host}:{args.port}/admin/stored-knowledge    ║
║    GET  http://{args.host}:{args.port}/admin/sessions            ║
╚════════════════════════════════════════════════════════════╝
    """)
    
    # Inicijalizuj RAG pre pokretanja servera
    try:
        initialize_rag()
        print("\n💡 USAGE:")
        print("   • Regular chat - ask questions normally")
        print("   • Store knowledge - start message with: /store <content>")
        print("   • Example: /store Trafo T1 u TS Beograd 5 ima snagu 300 MVA\n")
    except Exception as e:
        print(f"⚠️  Warning: Could not initialize RAG: {e}")
        print("Server will start but RAG will be initialized on first request.")
    
    app.run(host=args.host, port=args.port, debug=args.debug, threaded=True)
