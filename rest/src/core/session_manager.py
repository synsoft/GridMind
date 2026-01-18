#!/usr/bin/env python3
"""
Session Manager - upravljanje LangChain memorijom po sesijama.
Svaka sesija ima izolovanu ConversationBufferWindowMemory.
"""

import time
import threading
from typing import Dict, Optional
from datetime import datetime, timedelta

# Import from langchain_classic (langchain v2.x)
from langchain_classic.memory import ConversationBufferWindowMemory


class SessionMemoryManager:
    def __init__(self, window_size: int = 10, session_timeout_minutes: int = 30):
        """
        Initialize session memory manager.
        
        Args:
            window_size: Number of conversation turns to keep in memory (default 10)
            session_timeout_minutes: Minutes of inactivity before session expires (default 30)
        """
        self.window_size = window_size
        self.session_timeout = timedelta(minutes=session_timeout_minutes)
        
        # Dictionary: session_id -> {'memory': ConversationBufferWindowMemory, 'last_access': datetime}
        self.sessions: Dict[str, Dict] = {}
        
        # Lock for thread-safe access
        self.lock = threading.Lock()
        
        # Start cleanup thread
        self.cleanup_thread = threading.Thread(target=self._cleanup_loop, daemon=True)
        self.cleanup_thread.start()
        
        print(f"✅ Session Memory Manager initialized (window={window_size}, timeout={session_timeout_minutes}min)")
    
    def get_or_create_memory(self, session_id: str) -> ConversationBufferWindowMemory:
        """
        Get existing memory for session or create new one.
        
        Args:
            session_id: Unique session identifier
            
        Returns:
            ConversationBufferWindowMemory instance for this session
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
            
            # Create new session
            memory = ConversationBufferWindowMemory(
                k=self.window_size,
                memory_key="chat_history",
                return_messages=True
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
        print(f"💾 Saved interaction to session {session_id[:8]}...")
    
    def get_conversation_history(self, session_id: str) -> str:
        """
        Get formatted conversation history for session.
        
        Args:
            session_id: Session identifier
            
        Returns:
            Formatted conversation history as string
        """
        memory = self.get_or_create_memory(session_id)
        
        try:
            # Get messages from memory
            messages = memory.load_memory_variables({}).get('chat_history', [])
            
            if not messages:
                return ""
            
            # Format as conversation
            formatted = []
            for msg in messages:
                if hasattr(msg, 'type'):
                    role = "User" if msg.type == "human" else "Assistant"
                    content = msg.content
                else:
                    # Fallback for dict format
                    role = "User" if msg.get('type') == 'human' else "Assistant"
                    content = msg.get('content', '')
                
                formatted.append(f"{role}: {content}")
            
            history = "\n".join(formatted)
            print(f"📜 Retrieved conversation history for {session_id[:8]}... ({len(messages)} messages)")
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
                messages = memory.load_memory_variables({}).get('chat_history', [])
                
                return {
                    'session_id': session_id,
                    'created': session_data['created'].isoformat(),
                    'last_access': session_data['last_access'].isoformat(),
                    'message_count': len(messages),
                    'window_size': self.window_size
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
