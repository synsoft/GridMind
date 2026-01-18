#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chat RAG API - Wrapper klasa za RAG chat funkcionalnost

Koristi interno RAGAgent iz chunks/scripts/rag_agent.py
i LLM za generisanje odgovora.

Može se koristiti kao:
1. Standalone CLI chat
2. Import u druge skripte (npr. evaluacija)
"""

import json
import sys
import requests
from pathlib import Path
from typing import List, Dict, Optional

# Setup paths
ROOT_DIR = Path(__file__).parent
GRIDMIND_ROOT = ROOT_DIR.parent

# Dodaj chunks/scripts u path
sys.path.insert(0, str(GRIDMIND_ROOT / "chunks" / "scripts"))


class OllamaRAGChat:
    """
    RAG Chat klasa koja interno koristi RAGAgent i LLM.
    Kompatibilna sa postojećim kodom koji koristi OllamaRAGChat.
    """
    
    def __init__(self, config_path: str = None):
        """
        Inicijalizuje RAG Chat.
        
        Args:
            config_path: Putanja do config.json fajla
        """
        # Učitaj konfiguraciju
        if config_path is None:
            config_path = ROOT_DIR / "config.json"
        else:
            config_path = Path(config_path)
        
        if config_path.exists():
            with open(config_path, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
        else:
            self.config = self._default_config()
        
        # RAG config putanja
        self.rag_config_path = str(GRIDMIND_ROOT / "chunks" / "config" / "rag_config.json")
        
        # Inicijalizuj komponente
        self._init_rag_agent()
        self._init_llm_client()
        
        # Istorija konverzacije
        self.conversation_history = []
        
        # System prompt
        self.system_prompt = """Ti si stručni AI asistent za elektroenergetski prenosni sistem Srbije.

PRAVILA:
1. Odgovaraj ISKLJUČIVO na osnovu datog konteksta
2. Ako informacija nije u kontekstu, reci "Ne mogu pronaći tu informaciju u dostupnoj dokumentaciji"
3. Budi precizan i koncizan
4. Koristi tehničku terminologiju iz konteksta
5. Navedi iz kog dokumenta/sekcije je informacija kada je relevantno

FORMAT ODGOVORA:
- Koristi kratke, jasne rečenice
- Za liste koristi bullet points
- Za procedure koristi numerisane korake
"""
    
    def _default_config(self) -> dict:
        """Vraća default konfiguraciju."""
        return {
            "search": {
                "faiss": {
                    "initial_top_k": 80,
                    "rerank_top_k": 10,
                    "default_top_k": 10
                }
            },
            "llm": {
                "provider": "openai",
                "model": "gemma3:27b",
                "ollama_host": "192.168.30.61",
                "ollama_port": 11434,
                "openai_host": "192.168.30.62",
                "openai_port": 8080,
                "temperature": 0.3,
                "timeout": 120
            }
        }
    
    def _init_rag_agent(self):
        """Inicijalizuje RAG Agent."""
        print("🔍 Učitavanje RAG Agent-a...")
        
        try:
            from rag_agent import RAGAgent
            self.rag_agent = RAGAgent(self.rag_config_path)
            print("✓ RAG Agent učitan")
        except Exception as e:
            print(f"❌ Greška pri učitavanju RAG Agent-a: {e}")
            raise
    
    def _init_llm_client(self):
        """Inicijalizuje LLM klijenta."""
        llm_config = self.config.get('llm', {})
        
        self.llm_provider = llm_config.get('provider', 'ollama')
        self.llm_model = llm_config.get('model', 'gemma3:27b')
        self.temperature = llm_config.get('temperature', 0.3)
        self.timeout = llm_config.get('timeout', 120)
        
        if self.llm_provider == 'ollama':
            host = llm_config.get('ollama_host', 'localhost')
            port = llm_config.get('ollama_port', 11434)
            self.llm_base_url = f"http://{host}:{port}"
        else:
            host = llm_config.get('openai_host', 'localhost')
            port = llm_config.get('openai_port', 8080)
            self.llm_base_url = f"http://{host}:{port}"
        
        self.api_key = llm_config.get('openai_api_key', '')
        
        print(f"✓ LLM konfigurisan: {self.llm_provider} / {self.llm_model}")
    
    def retrieve(self, query: str, top_k: int = None) -> List[Dict]:
        """
        Pretražuje dokumente za dati query.
        
        Args:
            query: Tekst upita
            top_k: Broj rezultata za vraćanje
            
        Returns:
            Lista rezultata pretrage
        """
        search_cfg = self.config.get('search', {}).get('faiss', {})
        
        if top_k is None:
            top_k = search_cfg.get('rerank_top_k', 10)
        
        initial_k = search_cfg.get('initial_top_k', 80)
        
        results = self.rag_agent.retrieve(
            query=query,
            initial_k=initial_k,
            final_k=top_k
        )
        
        return results
    
    def _build_context(self, results: List[Dict]) -> str:
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
    
    def _call_llm(self, messages: List[Dict]) -> str:
        """Poziva LLM i vraća odgovor."""
        if self.llm_provider == 'ollama':
            return self._call_ollama(messages)
        else:
            return self._call_openai(messages)
    
    def _call_ollama(self, messages: List[Dict]) -> str:
        """Poziva Ollama API."""
        url = f"{self.llm_base_url}/api/chat"
        
        payload = {
            "model": self.llm_model,
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
            print(f"❌ Ollama greška: {e}")
            raise
    
    def _call_openai(self, messages: List[Dict]) -> str:
        """Poziva OpenAI-compatible API."""
        url = f"{self.llm_base_url}/v1/chat/completions"
        
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        
        payload = {
            "model": self.llm_model,
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
            print(f"❌ OpenAI greška: {e}")
            raise
    
    def chat(self, question: str, include_sources: bool = False) -> str:
        """
        Odgovara na pitanje koristeći RAG.
        
        Args:
            question: Pitanje korisnika
            include_sources: Da li uključiti izvore u odgovor
            
        Returns:
            Odgovor LLM-a
        """
        # Retrieval
        results = self.retrieve(question)
        
        # Gradi kontekst
        context = self._build_context(results)
        
        if not context:
            return "Nisam pronašao relevantne informacije za vaše pitanje u dostupnoj dokumentaciji."
        
        # Gradi poruke za LLM
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": f"KONTEKST:\n{context}\n\nPITANJE: {question}"}
        ]
        
        # Pozovi LLM
        response = self._call_llm(messages)
        
        # Dodaj izvore ako je potrebno
        if include_sources and results:
            sources = []
            for i, r in enumerate(results, 1):
                doc_title = r.get('doc_title', 'Nepoznat')
                section_num = r.get('section_number', '')
                section_title = r.get('section_title', '')
                score = r.get('rerank_score', 0)
                
                section_str = f"{section_num}: {section_title}" if section_num else section_title
                sources.append(f"[{i}] {doc_title} ({section_str}) - relevantnost: {score:.3f}")
            
            response += "\n\n**Izvori:**\n" + "\n".join(f"- {s}" for s in sources)
        
        # Dodaj u istoriju
        self.conversation_history.append({"role": "user", "content": question})
        self.conversation_history.append({"role": "assistant", "content": response})
        
        return response
    
    def reset_conversation(self):
        """Resetuje istoriju konverzacije."""
        self.conversation_history = []
    
    def get_conversation_history(self) -> List[Dict]:
        """Vraća istoriju konverzacije."""
        return self.conversation_history


def main():
    """CLI chat interfejs."""
    import argparse
    
    parser = argparse.ArgumentParser(description='RAG Chat CLI')
    parser.add_argument('--config', type=str, default=None, help='Putanja do config.json')
    parser.add_argument('--sources', action='store_true', help='Prikaži izvore')
    args = parser.parse_args()
    
    print("\n" + "=" * 60)
    print("GRIDMIND RAG CHAT")
    print("=" * 60)
    print("Upišite 'quit' ili 'exit' za izlaz")
    print("Upišite 'reset' za novu konverzaciju")
    print("=" * 60 + "\n")
    
    # Inicijalizuj chat
    chat = OllamaRAGChat(config_path=args.config)
    
    while True:
        try:
            question = input("\n❓ Pitanje: ").strip()
            
            if not question:
                continue
            
            if question.lower() in ['quit', 'exit', 'q']:
                print("\n👋 Doviđenja!")
                break
            
            if question.lower() == 'reset':
                chat.reset_conversation()
                print("🔄 Konverzacija resetovana")
                continue
            
            print("\n⏳ Tražim odgovor...\n")
            
            response = chat.chat(question, include_sources=args.sources)
            
            print("=" * 60)
            print("💡 ODGOVOR:")
            print("=" * 60)
            print(response)
            
        except KeyboardInterrupt:
            print("\n\n👋 Prekinuto od strane korisnika")
            break
        except Exception as e:
            print(f"\n❌ Greška: {e}")


if __name__ == "__main__":
    main()
