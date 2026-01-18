"""Core modules for RAG system.

Lazy imports to avoid loading heavy dependencies until needed.
"""

# Light modules - always available
from .llm_client import LLMClient, LLMConfig, get_llm_client
from .model_manager import ModelManager, ModelConfig, get_model_manager, get_reranker, get_embedder

# Heavy modules - imported on demand
def get_session_manager():
    """Lazy import for SessionMemoryManager (requires langchain)."""
    from .session_manager import SessionMemoryManager
    return SessionMemoryManager

def get_stored_knowledge_manager():
    """Lazy import for StoredKnowledgeManager."""
    from .stored_knowledge import StoredKnowledgeManager
    return StoredKnowledgeManager

def get_rag_chat():
    """Lazy import for OllamaRAGChat."""
    from .chat_rag_api import OllamaRAGChat
    return OllamaRAGChat

__all__ = [
    'LLMClient',
    'LLMConfig', 
    'get_llm_client',
    'ModelManager',
    'ModelConfig',
    'get_model_manager',
    'get_reranker',
    'get_embedder',
    'get_session_manager',
    'get_stored_knowledge_manager',
    'get_rag_chat',
]