#!/usr/bin/env python3
"""
Session Manager - upravljanje LangChain memorijom po sesijama.
Koristi ConversationSummaryBufferMemory za efikasno čuvanje konteksta:
- Poslednjih 5 poruka se čuva u celosti
- Starije poruke se automatski sumarizuju
"""

import time
import threading
from typing import Dict, Optional, Callable
from datetime import datetime, timedelta

# Import from langchain_classic (langchain v2.x)
from langchain_classic.memory import ConversationSummaryBufferMemory
from langchain_classic.llms.base import LLM
from langchain_classic.prompts import PromptTemplate


# Serbian summary prompt for conversation summarization
SERBIAN_SUMMARY_PROMPT = PromptTemplate(
    input_variables=["summary", "new_lines"],
    template="""Progresivno sumiraj razgovor, dodajući na prethodni rezime i vraćajući novi rezime.
Rezime treba da bude na SRPSKOM jeziku (latinica).
Fokusiraj se na ključne tehničke informacije: nazive trafostanica (TS), dalekovoda (DV), naponske nivoe (kV), uklopna stanja.

Trenutni rezime:
{summary}

Nove linije razgovora:
{new_lines}

Novi rezime (na srpskom, latinica):"""
)


def _default_llm_call(prompt: str) -> str:
    """Default LLM call that returns a placeholder (used when no LLM is configured)."""
    return "Summary not available"


class SimpleLLMWrapper(LLM):
    """Simple LLM wrapper for LangChain that uses our existing LLM client."""
    
    llm_call: Callable[[str], str] = _default_llm_call
    
    @property
    def _llm_type(self) -> str:
        return "custom"
    
    def _call(self, prompt: str, stop=None, run_manager=None, **kwargs) -> str:
        """Call the LLM with the given prompt."""
        try:
            return self.llm_call(prompt)
        except Exception as e:
            print(f"⚠️ LLM call for summarization failed: {e}")
            return "Summary not available"
    
    @property
    def _identifying_params(self) -> dict:
        return {}


class SessionMemoryManager:
    def __init__(self, 
                 max_token_limit: int = 2000,
                 session_timeout_minutes: int = 30,
                 llm_call: Callable[[str], str] = None):
        """
        Initialize session memory manager with summary buffer.
        
        Args:
            max_token_limit: Approximate token limit before summarization kicks in (default 2000)
            session_timeout_minutes: Minutes of inactivity before session expires (default 30)
            llm_call: Function to call LLM for summarization (receives prompt, returns response)
        """
        self.max_token_limit = max_token_limit
        self.session_timeout = timedelta(minutes=session_timeout_minutes)
        
        # Create LLM wrapper for summarization (use default if not provided)
        effective_llm_call = llm_call if llm_call is not None else _default_llm_call
        self.llm_wrapper = SimpleLLMWrapper(llm_call=effective_llm_call)
        self.llm_call = llm_call
        
        # Dictionary: session_id -> {'memory': ConversationSummaryBufferMemory, 'last_access': datetime}
        self.sessions: Dict[str, Dict] = {}
        
        # Lock for thread-safe access
        self.lock = threading.Lock()
        
        # Start cleanup thread
        self.cleanup_thread = threading.Thread(target=self._cleanup_loop, daemon=True)
        self.cleanup_thread.start()
        
        print(f"✅ Session Memory Manager initialized (max_tokens={max_token_limit}, timeout={session_timeout_minutes}min, with summarization)")
    
    def set_llm_call(self, llm_call: Callable[[str], str]):
        """Set or update the LLM call function for summarization."""
        self.llm_call = llm_call
        self.llm_wrapper = SimpleLLMWrapper(llm_call=llm_call)
        # Update existing sessions
        with self.lock:
            for session_data in self.sessions.values():
                session_data['memory'].llm = self.llm_wrapper
    
    def get_or_create_memory(self, session_id: str) -> ConversationSummaryBufferMemory:
        """
        Get existing memory for session or create new one.
        
        Args:
            session_id: Unique session identifier
            
        Returns:
            ConversationSummaryBufferMemory instance for this session
        """
        with self.lock:
            current_time = datetime.now()
            
            # Check if session exists and is not expired
            if session_id in self.sessions:
                session_data = self.sessions[session_id]
                last_access = session_data['last_access']
                
                # Check if expired
                if current_time - last_access > self.session_timeout:
                    print(f"⏰ Session {session_id[:8]}... expired, creating new")
                    del self.sessions[session_id]
                else:
                    # Update last access time
                    session_data['last_access'] = current_time
                    print(f"♻️  Reusing existing session memory: {session_id[:8]}...")
                    return session_data['memory']
            
            # Create new session with summary buffer memory and Serbian prompt
            memory = ConversationSummaryBufferMemory(
                llm=self.llm_wrapper,
                max_token_limit=self.max_token_limit,
                memory_key="chat_history",
                return_messages=True,
                prompt=SERBIAN_SUMMARY_PROMPT
            )
            
            self.sessions[session_id] = {
                'memory': memory,
                'last_access': current_time,
                'created': current_time
            }
            
            print(f"✨ Created new session memory: {session_id[:8]}... (total sessions: {len(self.sessions)})")
            return memory
    
    def add_interaction(self, session_id: str, user_input: str, ai_output: str):
        """
        Add user-AI interaction to session memory.
        
        Args:
            session_id: Session identifier
            user_input: User's message
            ai_output: AI's response
        """
        memory = self.get_or_create_memory(session_id)
        memory.save_context(
            {"input": user_input},
            {"output": ai_output}
        )
        
        # Log buffer status
        try:
            buffer = memory.load_memory_variables({})
            msg_count = len(buffer.get('chat_history', []))
            has_summary = bool(memory.moving_summary_buffer)
            print(f"💾 Saved interaction to session {session_id[:8]}... (msgs: {msg_count}, has_summary: {has_summary})")
            if has_summary:
                print(f"📝 Full Summary:")
                print(f"{'='*60}")
                print(memory.moving_summary_buffer)
                print(f"{'='*60}")
        except Exception as e:
            print(f"💾 Saved interaction to session {session_id[:8]}...")
    
    def get_conversation_history(self, session_id: str) -> str:
        """
        Get formatted conversation history for session.
        Includes both the summary of older messages and recent messages.
        
        Args:
            session_id: Session identifier
            
        Returns:
            Formatted conversation history as string
        """
        memory = self.get_or_create_memory(session_id)
        
        try:
            # Get buffer content (includes summary + recent messages)
            buffer = memory.load_memory_variables({})
            messages = buffer.get('chat_history', [])
            
            if not messages and not memory.moving_summary_buffer:
                return ""
            
            formatted_parts = []
            
            # Add summary if exists
            if memory.moving_summary_buffer:
                formatted_parts.append(f"[Rezime prethodnog razgovora]: {memory.moving_summary_buffer}")
            
            # Format recent messages
            for msg in messages:
                if hasattr(msg, 'type'):
                    role = "User" if msg.type == "human" else "Assistant"
                    content = msg.content
                else:
                    # Fallback for dict format
                    role = "User" if msg.get('type') == 'human' else "Assistant"
                    content = msg.get('content', '')
                
                # Truncate long responses for context
                if role == "Assistant" and len(content) > 500:
                    content = content[:500] + "..."
                
                formatted_parts.append(f"{role}: {content}")
            
            history = "\n".join(formatted_parts)
            msg_count = len(messages)
            has_summary = bool(memory.moving_summary_buffer)
            print(f"📜 Retrieved history for {session_id[:8]}... ({msg_count} recent msgs, summary: {has_summary})")
            return history
            
        except Exception as e:
            print(f"⚠️ Error getting conversation history: {e}")
            return ""
    
    def clear_session(self, session_id: str) -> bool:
        """
        Clear/delete specific session.
        
        Args:
            session_id: Session to clear
            
        Returns:
            True if session existed and was cleared
        """
        with self.lock:
            if session_id in self.sessions:
                del self.sessions[session_id]
                print(f"🗑️ Cleared session: {session_id[:8]}...")
                return True
            return False
    
    def get_session_info(self, session_id: str) -> Optional[Dict]:
        """Get information about session."""
        with self.lock:
            if session_id in self.sessions:
                session_data = self.sessions[session_id]
                memory = session_data['memory']
                
                try:
                    messages = memory.load_memory_variables({}).get('chat_history', [])
                    has_summary = bool(memory.moving_summary_buffer)
                except:
                    messages = []
                    has_summary = False
                
                return {
                    'session_id': session_id,
                    'created': session_data['created'].isoformat(),
                    'last_access': session_data['last_access'].isoformat(),
                    'message_count': len(messages),
                    'has_summary': has_summary,
                    'max_token_limit': self.max_token_limit
                }
            return None
    
    def list_active_sessions(self) -> list:
        """List all active sessions."""
        with self.lock:
            return list(self.sessions.keys())
    
    def get_active_session_count(self) -> int:
        """Get number of active sessions."""
        with self.lock:
            return len(self.sessions)
    
    def _cleanup_loop(self):
        """Background thread that periodically cleans up expired sessions."""
        while True:
            try:
                time.sleep(60)  # Check every minute
                self._cleanup_expired_sessions()
            except Exception as e:
                print(f"⚠️ Error in session cleanup: {e}")
    
    def _cleanup_expired_sessions(self):
        """Remove expired sessions."""
        with self.lock:
            current_time = datetime.now()
            expired_sessions = []
            
            for session_id, session_data in self.sessions.items():
                last_access = session_data['last_access']
                if current_time - last_access > self.session_timeout:
                    expired_sessions.append(session_id)
            
            for session_id in expired_sessions:
                del self.sessions[session_id]
            
            if expired_sessions:
                print(f"🧹 Cleaned up {len(expired_sessions)} expired sessions (active: {len(self.sessions)})")
