#!/usr/bin/env python3
"""
Stored Knowledge Manager - upravljanje persistent znanjem koje eksperti dodaju.
Koristi BGE reranker-v2-m3 za semantic search.
"""

import json
import uuid
import logging
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional

logger = logging.getLogger(__name__)


class StoredKnowledgeManager:
    def __init__(self, storage_file="data/stored_knowledge_data/stored_knowledge.json", reranker=None, llm_client=None, llm_config=None):
        """
        Initialize stored knowledge manager.
        
        Args:
            storage_file: Path to JSON file for persistent storage
            reranker: FlagReranker model instance for semantic search
            llm_client: LLMClient instance for title generation (preferred)
            llm_config: Dict with LLM configuration (deprecated, use llm_client)
        """
        self.storage_file = Path(storage_file)
        self.reranker = reranker
        self.llm_client = llm_client
        self.llm_config = llm_config or {}  # Keep for backward compatibility
        self.knowledge_base = []
        
        # Load existing knowledge
        self._load()
    
    def _load(self):
        """Load stored knowledge from JSON file."""
        if self.storage_file.exists():
            try:
                with open(self.storage_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.knowledge_base = data.get('entries', [])
                    
                logger.info(f"Loaded {len(self.knowledge_base)} stored knowledge entries")
                print(f"✅ Loaded {len(self.knowledge_base)} stored knowledge entries")
            except Exception as e:
                logger.error(f"Error loading stored knowledge: {e}")
                print(f"⚠️ Error loading stored knowledge: {e}")
                self.knowledge_base = []
        else:
            logger.info("No existing stored knowledge file found")
            print("ℹ️  No existing stored knowledge file found")
            self.knowledge_base = []
    
    def _save(self):
        """Save stored knowledge to JSON file."""
        try:
            # Ensure directory exists
            self.storage_file.parent.mkdir(parents=True, exist_ok=True)
            
            data = {
                'entries': self.knowledge_base,
                'last_updated': datetime.now().isoformat()
            }
            
            with open(self.storage_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            logger.info(f"Saved {len(self.knowledge_base)} stored knowledge entries")
            print(f"✅ Saved {len(self.knowledge_base)} stored knowledge entries")
        except Exception as e:
            logger.error(f"Error saving stored knowledge: {e}")
            print(f"❌ Error saving stored knowledge: {e}")
            raise
    
    def add_entry(self, content: str, stored_by: str = "unknown", title: str = None) -> Dict[str, Any]:
        """
        Add new knowledge entry.
        
        Args:
            content: The knowledge content to store
            stored_by: Identifier of who stored this (email, username, etc.)
            title: Optional title/summary (will be auto-generated if None)
            
        Returns:
            The created entry with metadata
        """
        entry_id = str(uuid.uuid4())
        timestamp = datetime.now().isoformat()
        
        # Auto-generate title if not provided
        if not title:
            title = self._generate_title(content)
        
        entry = {
            'id': entry_id,
            'content': content,
            'title': title,
            'stored_by': stored_by,
            'timestamp': timestamp
        }
        
        self.knowledge_base.append(entry)
        self._save()
        
        print(f"📝 Stored new knowledge entry: {content[:100]}...")
        return entry
    
    def search(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        """
        Search stored knowledge using BGE reranker-v2-m3.
        
        Two-stage approach:
        1. Get all entries as candidates (or filtered set if too large)
        2. Rerank using BGE reranker-v2-m3 for precise ranking
        
        Args:
            query: Search query
            top_k: Number of top results to return
            
        Returns:
            List of matching entries with rerank scores
        """
        if not self.knowledge_base:
            return []
        
        if not self.reranker:
            print("⚠️ No reranker available, returning all stored knowledge")
            return self.knowledge_base[:top_k]
        
        try:
            # Stage 1: Get candidates (all entries for now, could add filtering later)
            candidates = self.knowledge_base
            
            # Stage 2: Rerank using BGE reranker-v2-m3
            # Prepare query-document pairs
            # Combine title + content for better matching
            pairs = []
            for entry in candidates:
                # Use title and content for comprehensive matching
                text = f"{entry['title']}. {entry['content']}"
                pairs.append([query, text])
            
            # Compute reranking scores
            scores = self.reranker.compute_score(pairs, batch_size=32)
            
            # Combine entries with scores
            results = []
            for entry, score in zip(candidates, scores):
                result = entry.copy()
                result['rerank_score'] = float(score)
                results.append(result)
            
            # Sort by rerank score and return top_k
            results.sort(key=lambda x: x['rerank_score'], reverse=True)
            results = results[:top_k]
            
            # No logging here - will be logged in chat_rag_api after filtering
            
            return results
            
        except Exception as e:
            print(f"❌ Error searching stored knowledge: {e}")
            import traceback
            traceback.print_exc()
            return []
    
    def list_all(self) -> List[Dict[str, Any]]:
        """List all stored knowledge entries."""
        return self.knowledge_base
    
    def get_entry(self, entry_id: str) -> Optional[Dict[str, Any]]:
        """Get specific entry by ID."""
        for entry in self.knowledge_base:
            if entry['id'] == entry_id:
                return entry
        return None
    
    def delete_entry(self, entry_id: str) -> bool:
        """
        Delete entry by ID.
        
        Args:
            entry_id: ID of entry to delete
            
        Returns:
            True if deleted, False if not found
        """
        for i, entry in enumerate(self.knowledge_base):
            if entry['id'] == entry_id:
                self.knowledge_base.pop(i)
                self._save()
                print(f"🗑️ Deleted stored knowledge entry: {entry_id}")
                return True
        return False
    
    def count(self) -> int:
        """Get total number of stored entries."""
        return len(self.knowledge_base)
    
    def _generate_title(self, content: str) -> str:
        """Generate a short descriptive title using LLMClient.
        
        Args:
            content: The knowledge content
            
        Returns:
            A short title (max 10 words)
        """
        import re
        
        # Use LLMClient if available (preferred method)
        if self.llm_client:
            try:
                title = self.llm_client.generate_title(content, max_words=10)
                logger.info(f"Generated title: {title}")
                print(f"✨ Generated title: {title}")
                return title
            except Exception as e:
                logger.warning(f"LLMClient title generation failed: {e}")
        
        # Fallback to legacy llm_config method
        if self.llm_config and self.llm_config.get('url'):
            try:
                import requests
                
                prompt = f"""Kreiraj **kratak i precizan naslov** (maksimalno 10 reči) za sledeći stručni tekst.

Tekst:
{content[:500]}

Naslov treba da:
- Bude na srpskom jeziku
- Sadrži ključne tehničke termine
- NE sadrži znakove navoda

Odgovori SAMO sa naslovom, bez dodatnog teksta."""

                url = self.llm_config.get('url')
                model = self.llm_config.get('model', 'gemma3:4b')
                provider = self.llm_config.get('provider', 'ollama')
                
                if provider == 'openai':
                    response = requests.post(
                        url,
                        json={
                            "model": model,
                            "messages": [{"role": "user", "content": prompt}],
                            "stream": False,
                            "temperature": 0.3
                        },
                        timeout=15
                    )
                    if response.ok:
                        title = response.json()["choices"][0]["message"]["content"].strip()
                else:
                    response = requests.post(
                        url,
                        json={
                            "model": model,
                            "messages": [{"role": "user", "content": prompt}],
                            "stream": False,
                            "options": {"temperature": 0.3}
                        },
                        timeout=15
                    )
                    if response.ok:
                        title = response.json()["message"]["content"].strip()
                
                # Clean up title
                title = title.strip('"\'\'').strip()
                if len(title) > 100:
                    title = title[:97] + '...'
                
                logger.info(f"Generated title (legacy): {title}")
                print(f"✨ Generated title: {title}")
                return title
                
            except Exception as e:
                logger.warning(f"Legacy title generation failed: {e}")
        
        # Final fallback: simple truncation
        clean_content = re.sub(r'[^\w\s\u0400-\u04FF]', ' ', content)
        words = clean_content.split()[:8]
        return ' '.join(words) or 'Stored Knowledge Entry'
