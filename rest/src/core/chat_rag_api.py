import json
import logging
import sys
import requests
from pathlib import Path
from cyrtranslit import to_latin
from src.core.stored_knowledge import StoredKnowledgeManager
from src.core.session_manager import SessionMemoryManager
from src.core.llm_client import LLMClient, LLMConfig
from src.utils.dalekovod_checker import DalekvodChecker

logger = logging.getLogger(__name__)

# Dodaj chunks/scripts u path za RAGAgent
REST_DIR = Path(__file__).parent.parent.parent
GRIDMIND_ROOT = REST_DIR.parent
sys.path.insert(0, str(GRIDMIND_ROOT / "chunks" / "scripts"))


class OllamaRAGChat:
    def __init__(self, config_path="config.json", silent=False, use_internal_rag=True):
        """Initialize Ollama RAG Chat with internal RAGAgent or REST API retrieval.
        
        Args:
            config_path: Path to config file
            silent: If True, suppress console output (for REST API usage)
            use_internal_rag: If True, use internal RAGAgent; if False, use REST API
        """
        self.silent = silent
        self.log_chunks = False  # Can be enabled externally for chunk logging
        self.use_internal_rag = use_internal_rag
        self.rag_agent = None
        
        # Load config
        try:
            with open(config_path, "r") as f:
                cfg = json.load(f)
        except Exception as e:
            if not silent:
                print(f"⚠️ Could not load config from {config_path}: {e}")
            cfg = {}
        
        # Internal RAG configuration
        if use_internal_rag:
            rag_config_path = str(GRIDMIND_ROOT / "chunks" / "config" / "rag_config.json")
            self._print(f"🔧 Initializing internal RAG Agent from: {rag_config_path}")
            try:
                from rag_agent import RAGAgent
                self.rag_agent = RAGAgent(rag_config_path)
                self._print(f"✅ Internal RAG Agent loaded ({len(self.rag_agent.chunks)} chunks)")
            except Exception as e:
                self._print(f"❌ Failed to load RAG Agent: {e}")
                raise
        
        # Search API configuration (fallback or alternative)
        api_cfg = cfg.get("search", {}).get("api", {})
        self.rag_api_url = api_cfg.get("base_url", "http://192.168.30.61:8888")
        
        # Initialize DalekvodChecker
        self.dv_checker = DalekvodChecker()
        self.default_top_k = api_cfg.get("default_top_k", 5)
        self.api_timeout = api_cfg.get("timeout_seconds", 30)
        
        # Stored knowledge configuration
        stored_cfg = cfg.get("stored_knowledge", {})
        self.use_stored_knowledge = stored_cfg.get("enabled", True)
        self.stored_knowledge_min_score = stored_cfg.get("min_score_threshold", -1.0)
        
        # Follow-up search configuration
        followup_cfg = cfg.get("search", {}).get("followup", {})
        self.followup_search_both = followup_cfg.get("search_with_both_questions", True)
        self.followup_separator = followup_cfg.get("combine_questions_separator", " | ")
        
        # LLM configuration
        llm_cfg = cfg.get("llm", {})
        provider = llm_cfg.get("provider", "ollama")
        
        if provider == "openai":
            openai_host = llm_cfg.get("openai_host", "192.168.30.61")
            openai_port = llm_cfg.get("openai_port", 8080)
            self.ollama_url = f"http://{openai_host}:{openai_port}/v1/chat/completions"
            self.model = llm_cfg.get("model", "gpt-oss:latest")
            self.provider = "openai"
        else:
            ollama_host = llm_cfg.get("ollama_host", "192.168.30.61")
            ollama_port = llm_cfg.get("ollama_port", 11434)
            self.ollama_url = f"http://{ollama_host}:{ollama_port}/api/chat"
            self.model = llm_cfg.get("model", "gemma3:27b")
            self.provider = "ollama"
        
        self.small_model = llm_cfg.get("small_model", "gemma3:4b")
        self.small_temperature = llm_cfg.get("small_temperature", 0.1)
        self.stream_tokens = llm_cfg.get("stream_tokens", False)
        self.use_markdown = llm_cfg.get("use_markdown", True)
        
        # Initialize unified LLM client
        llm_config = LLMConfig(
            provider=self.provider,
            url=self.ollama_url,
            model=self.model,
            small_model=self.small_model,
            temperature=0.3,
            small_temperature=self.small_temperature
        )
        self.llm_client = LLMClient(llm_config)
        
        # Check if RAG API is available
        self._print("Checking RAG API connection...")
        try:
            response = requests.get(f"{self.rag_api_url}/health", timeout=5)
            if response.ok:
                self._print(f"✅ Connected to RAG API at {self.rag_api_url}")
            else:
                self._print(f"⚠️ RAG API returned status: {response.status_code}")
        except Exception as e:
            self._print(f"❌ Could not connect to RAG API: {e}")
            self._print(f"   Make sure the server is running at {self.rag_api_url}")
        
        # Print LLM configuration
        if self.provider == "openai":
            self._print(f"\nConnected to OpenAI-compatible server at {self.ollama_url}")
        else:
            self._print(f"\nConnected to Ollama at {self.ollama_url}")
        self._print(f"Using model: {self.model}")
        self._print(f"Small model for classification: {self.small_model}\n")
        
        # System prompt
        if self.use_markdown:
            self.system_prompt = """Ti si ekspert dispečer u prenosnom sistemu električne energije. Tvoja uloga je da odgovaraš na pitanja isključivo na osnovu dokumenata iz baze znanja.

## KRITIČNA PRAVILA (OBAVEZNA):
1. Odgovaraj SAMO na osnovu informacija iz priloženih dokumenata - NIKADA ne koristi svoje opšte znanje
2. ODGOVORI KONCIZNO - tipično 4-8 rečenica, osim ako pitanje zahteva kraći ili detaljniji odgovor
3. NIKADA ne dodaj informacije koje NISU eksplicitno navedene u dokumentima - bolje je reći "Ne mogu pronaći tu informaciju" nego izmisliti
4. Ako nisi 100% siguran u informaciju iz dokumenta, NAZNAČI to u odgovoru (npr. "Prema dokumentu...", "Nije potpuno jasno, ali...")
5. Ako informacija nije u dokumentima, JASNO reci: "Ne mogu pronaći tu informaciju u dostupnim dokumentima"
6. NE navodi izvore/dokumente na kraju odgovora - oni se dodaju automatski

## OBAVEZNO FORMATIRANJE U MARKDOWN:
- **UVEK** koristi Markdown sintaksu u svom odgovoru
- Koristi **bold** za ključne termine i važne pojmove
- Koristi *italic* za naglašavanje
- Koristi numerisane liste (`1. 2. 3.`) za sekvencijalne korake ili procedure
- Koristi bullet liste (`- ` ili `* `) za nabrajanje stavki bez redosleda
- Koristi `> ` za citate iz dokumenata
- Strukturiraj odgovor logično sa jasnim sekcijama
- Odgovore piši na srpskom jeziku ekavica latiničnog pisma
"""
        else:
            self.system_prompt = """Ti si ekspert dispečer u prenosnom sistemu električne energije. Tvoja uloga je da odgovaraš na pitanja isključivo na osnovu dokumenata iz baze znanja.

KRITIČNA PRAVILA (OBAVEZNA):
1. Odgovaraj SAMO na osnovu informacija iz priloženih dokumenata - NIKADA ne koristi svoje opšte znanje
2. ODGOVORI KONCIZNO - tipično 4-8 rečenica, osim ako pitanje zahteva kraći ili detaljniji odgovor
3. NIKADA ne dodaj informacije koje NISU eksplicitno navedene u dokumentima - bolje je reći "Ne mogu pronaći tu informaciju" nego izmisliti
4. Ako nisi 100% siguran u informaciju iz dokumenta, NAZNAČI to u odgovoru
5. Ako informacija nije u dokumentima, JASNO reci: "Ne mogu pronaći tu informaciju u dostupnim dokumentima"
6. NE navodi izvore/dokumente na kraju odgovora - oni se dodaju automatski

FORMATIRANJE ODGOVORA:
- Koristi numerisane liste (1. 2. 3.) za sekvencijalne korake ili procedure
- Koristi bullet liste (- ili *) za nabrajanje stavki
- Strukturiraj odgovor logično
- Odgovore piši na srpskom jeziku ekavica
"""
        
        # Conversation history (legacy - kept for backward compatibility)
        self.messages = [{
            "role": "system",
            "content": self.system_prompt
        }]
        
        # Stored knowledge manager (for /store command)
        self.stored_knowledge = None
        
        # Session memory manager (LangChain)
        self.session_manager = SessionMemoryManager(window_size=10, session_timeout_minutes=30)
    
    def _print(self, *args, **kwargs):
        """Print only if not in silent mode."""
        if not self.silent:
            print(*args, **kwargs)
    
    def initialize_stored_knowledge(self, reranker):
        """Initialize stored knowledge manager with BGE reranker-v2-m3 model.
        
        This is called explicitly (e.g., from openai_api_server.py) to load
        the reranker model and stored knowledge database.
        """
        if self.stored_knowledge is None:
            # Prepare LLM config for title generation
            llm_config = {
                'url': self.ollama_url,
                'model': self.small_model,
                'provider': self.provider
            }
            
            # Use absolute path based on this module's location
            import os
            module_dir = os.path.dirname(os.path.abspath(__file__))
            storage_path = os.path.join(module_dir, "..", "..", "data", "stored_knowledge_data", "stored_knowledge.json")
            storage_path = os.path.normpath(storage_path)
            
            self.stored_knowledge = StoredKnowledgeManager(
                storage_file=storage_path,
                reranker=reranker,
                llm_config=llm_config
            )
            print(f"✅ Stored knowledge initialized ({self.stored_knowledge.count()} entries)")
    
    def ensure_stored_knowledge_lazy(self):
        """Lazy initialization of stored knowledge when needed.
        
        This is called automatically when /store or /recall commands are used.
        It only loads the reranker model if not already loaded.
        """
        if self.stored_knowledge is None:
            self._print("⏳ Loading BGE reranker-v2-m3 for stored knowledge (first use)...")
            try:
                from FlagEmbedding import FlagReranker
                reranker = FlagReranker('BAAI/bge-reranker-v2-m3', use_fp16=True)
                self.initialize_stored_knowledge(reranker)
                self._print(f"✅ Stored knowledge ready ({self.stored_knowledge.count()} entries)")
            except Exception as e:
                self._print(f"❌ Could not load stored knowledge: {e}")
                raise Exception(f"Failed to initialize stored knowledge: {e}")
    
    def search_documents(self, query, top_k=None):
        """Search documents using internal RAGAgent or REST API."""
        if top_k is None:
            top_k = self.default_top_k
        
        # Use internal RAG if enabled and available
        if self.use_internal_rag and self.rag_agent:
            return self._search_documents_internal(query, top_k)
        else:
            return self._search_documents_api(query, top_k)
    
    def _search_documents_internal(self, query, top_k):
        """Search documents using internal RAGAgent."""
        self._print(f"\n🔍 Searching documents via internal RAG for: '{query}'")
        
        try:
            # Call internal RAG agent
            self._print(f"➡️ Internal RAGAgent.retrieve with final_k={top_k}")
            results = self.rag_agent.retrieve(query, final_k=top_k)
            self._print(f"✅ RAGAgent returned {len(results)} results")
            
            # Format results for the model
            formatted_results = []
            
            # Log chunks header
            if self.log_chunks:
                print(f"\n{'='*100}")
                print(f"📦 CHUNKS FROM INTERNAL RAG (Top {len(results)}):")
                print(f"{'='*100}\n")
            else:
                self._print(f"\n{'='*100}")
                self._print(f"📦 CHUNKS FROM INTERNAL RAG (Top {len(results)}):")
                self._print(f"{'='*100}\n")
            
            for i, result in enumerate(results, 1):
                # Map RAGAgent result fields to expected format
                doc_title = result.get('doc_title', 'N/A')
                section_number = result.get('section_number', '')
                section_title = result.get('section_title', '')
                section_label = f"{section_number} {section_title}".strip() if section_number or section_title else 'N/A'
                
                chunk_data = {
                    "rank": i,
                    "filename": doc_title,
                    "section": section_label,
                    "item_number": result.get('object_code', 'N/A'),
                    "score": result.get('rerank_score', result.get('faiss_score', 0)),
                    "content": result.get('content', '')
                }
                formatted_results.append(chunk_data)
                
                # Log chunk details
                if self.log_chunks:
                    print(f"📄 Chunk #{i}:")
                    print(f"   File: {chunk_data['filename']}")
                    print(f"   Section: {chunk_data['section']} | Item: {chunk_data['item_number']}")
                    print(f"   Score: {chunk_data['score']:.4f}")
                    print(f"   Content: {chunk_data['content'][:150]}...")
                    print(f"{'-'*100}\n")
                else:
                    self._print(f"📄 Chunk #{i}:")
                    self._print(f"   File: {chunk_data['filename']}")
                    self._print(f"   Section: {chunk_data['section']} | Item: {chunk_data['item_number']}")
                    self._print(f"   Score: {chunk_data['score']:.4f}")
                    self._print(f"   Content preview: {chunk_data['content'][:200]}...")
                    self._print(f"{'-'*100}\n")
            
            if self.log_chunks:
                print(f"✅ Total {len(formatted_results)} chunks from internal RAG\n")
            else:
                self._print(f"✅ Total {len(formatted_results)} chunks from internal RAG\n")
            
            # Also search stored knowledge (if enabled)
            if self.use_stored_knowledge:
                stored_results = self._search_stored_knowledge(query, top_k=2, min_score=self.stored_knowledge_min_score)
                
                if stored_results:
                    combined_results = stored_results + formatted_results
                    self._print(f"📚 Combined {len(stored_results)} stored + {len(formatted_results)} documents = {len(combined_results)} total\n")
                    return combined_results
            
            return formatted_results
            
        except Exception as e:
            print(f"❌ Error with internal RAG: {e}")
            return []
    
    def _search_documents_api(self, query, top_k):
        """Search documents using REST API (fallback)."""
        self._print(f"\n🔍 Searching documents via API for: '{query}'")
        
        try:
            # Call RAG API
            self._print(f"➡️ POST {self.rag_api_url}/retrieve with top_k={top_k}")
            response = requests.post(
                f"{self.rag_api_url}/retrieve",
                json={"question": query, "top_k": top_k},
                timeout=self.api_timeout
            )
            if not response.ok:
                self._print(f"❌ RAG API HTTP {response.status_code}")
                try:
                    self._print(f"🧾 Response body: {response.text[:500]}")
                except Exception:
                    pass
                response.raise_for_status()
            else:
                self._print("✅ RAG API responded OK")
            
            api_response = response.json()
            # Debug: show raw keys and sample
            self._print(f"🧾 RAG API keys: {list(api_response.keys())}")
            results = api_response.get("results", [])
            if not isinstance(results, list):
                self._print("⚠️ 'results' is not a list. Full response:")
                self._print(json.dumps(api_response, ensure_ascii=False)[:1000])
                results = []
            
            # Format results for the model
            formatted_results = []
            
            # Always log chunks if log_chunks is enabled, regardless of silent mode
            if self.log_chunks:
                print(f"\n{'='*100}")
                print(f"📦 CHUNKS RECEIVED FROM API (Top {len(results)}):")
                print(f"{'='*100}\n")
            else:
                self._print(f"\n{'='*100}")
                self._print(f"📦 CHUNKS RECEIVED FROM API (Top {len(results)}):")
                self._print(f"{'='*100}\n")
            
            # Server already honors top_k; do not slice again unnecessarily
            for i, result in enumerate(results, 1):
                metadata = result.get("metadata", {})
                chunk_data = {
                    "rank": i,
                    "filename": metadata.get("filename", "N/A"),
                    "section": metadata.get("section", "N/A"),
                    "item_number": metadata.get("item_number", "N/A"),
                    "score": result.get("score", 0),
                    "content": result.get("text", "")
                }
                formatted_results.append(chunk_data)
                
                # Log chunk details - always if log_chunks enabled
                if self.log_chunks:
                    print(f"📄 Chunk #{i}:")
                    print(f"   File: {chunk_data['filename']}")
                    print(f"   Section: {chunk_data['section']} | Item: {chunk_data['item_number']}")
                    print(f"   Score: {chunk_data['score']:.4f}")
                    print(f"   Content: {chunk_data['content'][:150]}...")
                    print(f"{'-'*100}\n")
                else:
                    self._print(f"📄 Chunk #{i}:")
                    self._print(f"   File: {chunk_data['filename']}")
                    self._print(f"   Section: {chunk_data['section']} | Item: {chunk_data['item_number']}")
                    self._print(f"   Score: {chunk_data['score']:.4f}")
                    self._print(f"   Content preview: {chunk_data['content']}")
                    self._print(f"{'-'*100}\n")
            
            if self.log_chunks:
                print(f"✅ Total {len(formatted_results)} chunks received from API\n")
            else:
                self._print(f"✅ Total {len(formatted_results)} chunks received from API\n")
            
            # Also search stored knowledge (if enabled)
            if self.use_stored_knowledge:
                stored_results = self._search_stored_knowledge(query, top_k=2, min_score=self.stored_knowledge_min_score)
                
                if stored_results:
                    # Combine stored knowledge with document search (stored knowledge first)
                    combined_results = stored_results + formatted_results
                    self._print(f"📚 Combined {len(stored_results)} stored + {len(formatted_results)} documents = {len(combined_results)} total\n")
                    return combined_results
            
            return formatted_results
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Error calling RAG API: {e}")
            return []
    
    def format_markdown_response(self, text):
        """Format response text to proper Markdown with double newlines."""
        if not self.use_markdown:
            return text
        
        import re
        
        # Split text into lines
        lines = text.split('\n')
        formatted_lines = []
        prev_line_empty = False
        
        for i, line in enumerate(lines):
            stripped = line.strip()
            
            # Check if this is a special line that needs spacing
            is_header = stripped.startswith('#')
            is_list_item = bool(re.match(r'^[\d\-\*][\.\)]?\s', stripped))
            is_separator = stripped.startswith('---')
            is_bold_start = stripped.startswith('**') and ':' in stripped[:20]
            
            # Check next line type
            next_line_special = False
            if i < len(lines) - 1:
                next_stripped = lines[i + 1].strip()
                next_line_special = (
                    next_stripped.startswith('#') or
                    bool(re.match(r'^[\d\-\*][\.\)]?\s', next_stripped)) or
                    next_stripped.startswith('---') or
                    (next_stripped.startswith('**') and ':' in next_stripped[:20])
                )
            
            # Add current line
            formatted_lines.append(line)
            
            # Decide if we need extra newline
            current_empty = not stripped
            
            if not current_empty and not prev_line_empty:
                # Add extra newline after:
                # - Headers
                # - Before/after separators
                # - After list items if next line is not a list
                # - After bold labels
                # - Before special formatting
                if is_header or is_separator or is_bold_start:
                    formatted_lines.append('')
                elif is_list_item and i < len(lines) - 1:
                    next_is_list = bool(re.match(r'^[\d\-\*][\.\)]?\s', lines[i + 1].strip()))
                    if not next_is_list:
                        formatted_lines.append('')
                elif next_line_special:
                    formatted_lines.append('')
            
            prev_line_empty = current_empty
        
        return '\n'.join(formatted_lines)
    
    def _is_followup_question(self, current_question):
        """Use a small LLM to detect if this is a follow-up question."""
        
        # Need at least one previous exchange to determine follow-up
        if len(self.messages) <= 2:  # Only system prompt
            return False
        
        # Get last user question and assistant answer
        previous_question = ""
        previous_answer = ""
        
        for msg in reversed(self.messages[-4:]):  # Last 2 exchanges
            if msg["role"] == "user" and not previous_question:
                # Extract just the question, not the whole context
                content = msg["content"]
                if "Korisničko pitanje:" in content:
                    previous_question = content.split("Korisničko pitanje:")[1].split("\n")[0].strip()
            elif msg["role"] == "assistant" and not previous_answer:
                # Get short summary of answer
                previous_answer = msg["content"][:400]
        
        # Prompt for classification with entity awareness
        classification_prompt = f"""Tvoj zadatak je da odlučiš da li je novo pitanje NASTAVAK razgovora o ISTOM objektu/temi ili je NOVA tema.

KLJUČNO: Ako se promenio naziv objekta (trafostanica, dalekovod, TS, postrojenje), to je NOVA tema!

PRETHODNI RAZGOVOR:
Pitanje: {previous_question}
Odgovor: {previous_answer}

NOVO PITANJE: {current_question}

PRAVILA:
1. FOLLOW-UP - ako se pitanje odnosi na IST objekat:
   - "Zašto?" nakon odgovora o TS Pančevo
   - "Objasni detaljnije" o istoj trafostanici
   - "Kako to radi?" za isti sistem
   - "Šta još?" o istom objektu

2. NEW TOPIC - ako se promenio objekat ili tema:
   - Prethodno: "TS Pančevo" → Sada: "TS Beograd" = NEW!
   - Prethodno: "DV 400kV" → Sada: "DV 220kV" = NEW!
   - Prethodno: "DV 123" → Sada: "DV 124" = NEW!
   - Prethodno: "Trafo T1" → Sada: "Trafo T2" = NEW!
   - Potpuno druga tema = NEW!

ODGOVORI SAMO SA JEDNOM REČJU:
- Ako je nastavak o ISTOM objektu → FOLLOWUP
- Ako se promenio objekat ili je nova tema → NEW

Tvoj odgovor:"""

        # Use LLMClient for classification (cleaner, unified approach)
        try:
            result = self.llm_client.classify(
                classification_prompt, 
                options=["NEW", "FOLLOWUP"], 
                default="NEW"
            )
            is_followup = result == "FOLLOWUP"
            logger.info(f"Classification: {'FOLLOW-UP' if is_followup else 'NEW TOPIC'}")
            print(f"🔍 Classification: {'FOLLOW-UP' if is_followup else 'NEW TOPIC'}")
            return is_followup
        except Exception as e:
            logger.warning(f"Classification failed, assuming new topic: {e}")
            self._print(f"⚠️ Classification failed, assuming new topic: {e}")
        
        return False  # Default to new search if classification fails
    
    def _contextualize_question(self, user_message, conversation_history):
        """Reformulate a follow-up question into a standalone question using LLM.
        
        If the question is short or seems to reference previous context,
        use the main LLM to create a complete, standalone question for better retrieval.
        
        Args:
            user_message: Current user question (possibly short like "a 220kV?")
            conversation_history: Formatted string of previous conversation
            
        Returns:
            Standalone question suitable for document retrieval
        """
        # Skip if no history or question is already long enough
        if not conversation_history:
            return user_message
        
        # Heuristic: short questions (< 6 words) or questions starting with
        # conjunctions/pronouns likely need contextualization
        words = user_message.strip().split()
        followup_indicators = ['a', 'i', 'ali', 'što', 'šta', 'kako', 'zašto', 'koliko', 
                               'da', 'li', 'taj', 'ta', 'to', 'isti', 'ista', 'isto',
                               'prethodni', 'prethodna', 'gornji', 'donji', 'ovaj', 'ova']
        
        is_short = len(words) < 6
        starts_with_followup = words[0].lower().rstrip('?.,!') in followup_indicators if words else False
        
        if not (is_short or starts_with_followup):
            # Question seems complete enough
            return user_message
        
        print(f"🔄 Contextualizing follow-up question: '{user_message}'")
        
        # Build contextualization prompt
        contextualize_prompt = f"""Na osnovu prethodne konverzacije i novog pitanja, napravi JEDNO samostalno pitanje koje se može razumeti bez prethodnog konteksta.

**Prethodna konverzacija:**
{conversation_history}

**Novo pitanje:** {user_message}

**INSTRUKCIJE:**
- Ako novo pitanje referencira nešto iz prethodne konverzacije (npr. "a 220kV?" umesto punog pitanja), napravi kompletno pitanje
- Ako je novo pitanje već samostalno i potpuno, samo ga vrati bez izmena
- Vrati SAMO reformulisano pitanje, bez objašnjenja
- Koristi isti jezik kao u originalnom pitanju (srpski)

**Samostalno pitanje:**"""

        messages = [
            {"role": "system", "content": "Ti si asistent koji reformuliše kratka follow-up pitanja u samostalna pitanja. Odgovaraj SAMO sa reformulisanim pitanjem, bez dodatnih objašnjenja."},
            {"role": "user", "content": contextualize_prompt}
        ]
        
        # Log what is being sent to LLM for contextualization
        print("=" * 60)
        print("CONTEXTUALIZATION REQUEST TO LLM")
        print("=" * 60)
        logger.info("=" * 60)
        logger.info("CONTEXTUALIZATION REQUEST TO LLM")
        logger.info("=" * 60)
        for msg in messages:
            print(f"[{msg['role'].upper()}]:")
            print(msg['content'])
            print("-" * 40)
            logger.info(f"[{msg['role'].upper()}]:")
            logger.info(msg['content'])
            logger.info("-" * 40)
        print("=" * 60)
        logger.info("=" * 60)
        
        try:
            # Use the main LLM (via llm_client.chat)
            standalone_question = self.llm_client.chat(messages)
            
            if standalone_question and len(standalone_question.strip()) > len(user_message):
                standalone_question = standalone_question.strip().strip('"').strip("'")
                print(f"✅ Contextualized to: '{standalone_question}'")
                logger.info(f"Contextualized '{user_message}' -> '{standalone_question}'")
                return standalone_question
            else:
                print(f"ℹ️ Keeping original question (no improvement)")
                return user_message
                
        except Exception as e:
            logger.warning(f"Contextualization failed: {e}")
            print(f"⚠️ Contextualization failed: {e}, using original question")
            return user_message

    def call_ollama_stream(self, messages):
        """Call Ollama/OpenAI with streaming enabled using LLMClient."""
        try:
            full_response = ""
            if not self.silent:
                print("\n🤖 Assistant: ", end="", flush=True)
            
            for token in self.llm_client.chat_stream(messages):
                if token:
                    if not self.silent:
                        print(token, end="", flush=True)
                    full_response += token
            
            if not self.silent:
                print("\n")  # New line after streaming
            return {"message": {"content": full_response, "role": "assistant"}}
            
        except Exception as e:
            logger.error(f"Streaming error: {e}")
            print(f"❌ Streaming error: {e}")
            return None
    
    def _get_limited_history(self, max_exchanges=3):
        """Get limited conversation history to reduce token count."""
        # Always keep system prompt
        limited = [self.messages[0]]
        
        # Get last N exchanges (user + assistant pairs)
        recent_messages = []
        for msg in reversed(self.messages[1:]):
            recent_messages.insert(0, msg)
            if len(recent_messages) >= max_exchanges * 2:
                break
        
        limited.extend(recent_messages)
        return limited
    
    def call_ollama(self, messages, tools=None):
        """Call LLM API using unified LLMClient."""
        try:
            # Note: tools parameter is kept for API compatibility but not used by LLMClient
            if tools:
                logger.warning("Tools parameter is deprecated, use LLMClient directly")
            
            content = self.llm_client.chat(messages)
            if content:
                return {"message": {"role": "assistant", "content": content}}
            return None
        except Exception as e:
            logger.error(f"Error calling LLM: {e}")
            print(f"❌ Error calling LLM: {e}")
            return None
    
    def _check_if_found_in_chunks(self, answer):
        """Check if LLM found information in the provided chunks using LLMClient."""
        check_prompt = f"""Analiziraj sledeći odgovor i odluči da li je LLM uspeo da pronađe relevantne informacije u dostupnim dokumentima ili nije.

Odgovor: {answer}

PRAVILA:
- DA = LLM je pronašao konkretne informacije, naveo detalje iz dokumenata, citirao izvore
- NE = LLM kaže da nema informacija, da ne može da pronađe, odgovor je generičan bez konkretnih podataka

Odgovori SAMO sa jednom rečju: DA ili NE"""

        try:
            result = self.llm_client.classify(check_prompt, options=["DA", "NE"], default="DA")
            found = result == "DA"
            logger.info(f"Informacije pronađene u chunkovima: {'DA' if found else 'NE'}")
            print(f"🔍 Informacije pronađene u chunkovima: {'✅ DA' if found else '❌ NE'}")
            return found
        except Exception as e:
            logger.warning(f"Provera neuspela: {e}")
            self._print(f"⚠️ Provera neuspela: {e}")
        
        return True  # Default to True if check fails (assume answer is good)

    def chat(self, user_message, session_id=None):
        """Simplified chat with LangChain memory support.
        
        Args:
            user_message: User's question/message
            session_id: Optional session ID for LangChain memory management.
        
        Returns:
            AI's response as string
        """
        # Check for /store command
        if user_message.strip().startswith("/store"):
            return self._handle_store_command(user_message)
        
        # Get conversation history from LangChain if session exists
        conversation_history = ""
        if session_id:
            conversation_history = self.session_manager.get_conversation_history(session_id)
            if conversation_history:
                print(f"📜 Using LangChain conversation history ({len(conversation_history)} chars)")
        
        # Contextualize follow-up questions for better retrieval
        search_query = user_message
        if conversation_history:
            search_query = self._contextualize_question(user_message, conversation_history)
        
        # Check for dalekovod info FIRST (before retrieval)
        print(f"\n{'='*80}")
        print(f"🔍 CHECKING FOR DALEKOVOD INFO")
        print(f"{'='*80}")
        dv_info = self.dv_checker.check_question(search_query)
        
        # Prepare additional context (dalekovod info)
        additional_context = ""
        enhanced_query = search_query
        
        if dv_info:
            additional_context = f"\n**Informacije o dalekovodima:**\n{dv_info}\n"
            print(f"✅ Pronađene informacije o dalekovodima:")
            print(f"{dv_info}")
            
            # Extract dalekovod numbers from the info to enhance retrieval query
            import re
            dv_numbers = re.findall(r'DV\s*(\d+[АБаб]?(?:/\d+)?)', dv_info)
            if dv_numbers:
                # Add DV numbers to query for better retrieval
                dv_terms = ' '.join([f"DV {num}" for num in dv_numbers[:5]])  # Limit to 5 to avoid too long query
                enhanced_query = f"{user_message} {dv_terms}"
                print(f"📡 Enhanced query with DV numbers: {dv_terms}")
            
            print(f"{'='*80}\n")
        else:
            print(f"❌ Nisu pronađene informacije o dalekovodima")
            print(f"{'='*80}\n")
        
        # ALWAYS search documents (LangChain handles context automatically)
        # Use enhanced query if we found dalekovod info
        print(f"🔍 Searching documents for: '{enhanced_query}'")
        search_results = self.search_documents(enhanced_query, top_k=self.default_top_k)
        
        # Build simple prompt with history + question + documents
        if conversation_history:
            # With history
            prompt = f"""**Prethodna konverzacija:**
{conversation_history}

**Novo pitanje:** {user_message}
{additional_context}
**Relevantni dokumenti iz baze znanja:**
{json.dumps(search_results, ensure_ascii=False, indent=2)}

**INSTRUKCIJE:**
1. Odgovori KONCIZNO (4-8 rečenica) - bez nepotrebnih detalja
2. Koristi SAMO činjenice koje su EKSPLICITNO navedene u dokumentima iznad
3. Ako tražena informacija NIJE u dokumentima, reci "Ne mogu pronaći tu informaciju u dostupnim dokumentima"
4. NE SMEŠ dodavati informacije koje nisu u dokumentima - čak i ako "znaš" nešto, ignoriši to
5. NE navodi izvore na kraju - oni se dodaju automatski"""
        else:
            # Without history
            prompt = f"""**Korisničko pitanje:** {user_message}
{additional_context}
**Relevantni dokumenti iz baze znanja:**
{json.dumps(search_results, ensure_ascii=False, indent=2)}

**INSTRUKCIJE:**
1. Odgovori KONCIZNO (4-8 rečenica) - bez nepotrebnih detalja
2. Koristi SAMO činjenice koje su EKSPLICITNO navedene u dokumentima iznad
3. Ako tražena informacija NIJE u dokumentima, reci "Ne mogu pronaći tu informaciju u dostupnim dokumentima"
4. NE SMEŠ dodavati informacije koje nisu u dokumentima - čak i ako "znaš" nešto, ignoriši to
5. NE navodi izvore na kraju - oni se dodaju automatski"""
        
        # Simple messages list for LLM
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": prompt}
        ]
        
        # Log context size
        total_chars = len(prompt) + len(self.system_prompt)
        estimated_tokens = total_chars // 4
        print(f"📊 Context size: ~{estimated_tokens:,} tokens (~{total_chars:,} characters)")
        
        # Call LLM
        print("💭 Generating answer...")
        if self.stream_tokens:
            response = self.call_ollama_stream(messages)
        else:
            response = self.call_ollama(messages, tools=None)
        
        if not response:
            return "Error: Could not connect to Ollama"
        
        answer = response["message"]["content"]
        
        # Save to LangChain session memory
        if session_id:
            self.session_manager.add_interaction(session_id, user_message, answer)
            print(f"💾 Saved interaction to session")
        
        # Convert answer from Cyrillic to Latin using cyrtranslit
        answer_latin = to_latin(answer, 'sr')
        
        # Format and add sources
        formatted_answer = self.format_markdown_response(answer_latin)
        sources_text = self._build_sources_text(search_results)
        
        if sources_text:
            formatted_answer += "\n\n" + sources_text
        
        return formatted_answer
    
    def _build_sources_text(self, results):
        """Build sources text from search results."""
        if not results:
            return ""
        
        sources = []
        for r in results:
            # Skip stored knowledge entries (they have different format)
            if r.get('type') == 'stored_knowledge':
                continue
                
            filename = r.get('filename', 'Nepoznat')
            section = r.get('section', '')
            
            # Extract only section number (e.g., "5.1" from "5.1 Postrojenje 400 kV")
            if section:
                section_num = section.split()[0] if section else ''
                sources.append(f"{filename} - Sekcija: {section_num}")
            else:
                sources.append(filename)
        
        # Remove duplicates while preserving order
        unique_sources = list(dict.fromkeys(sources))
        
        if not unique_sources:
            return ""
        
        return "\n📚 **Izvori:**\n" + "\n".join(f"- {s}" for s in unique_sources)
    
    def _handle_store_command(self, message):
        """Handle /store command to save persistent knowledge.
        
        Args:
            message: Full message starting with /store
            
        Returns:
            Confirmation message
        """
        # Lazy load stored knowledge if needed
        try:
            self.ensure_stored_knowledge_lazy()
        except Exception as e:
            return f"❌ Stored knowledge nije inicijalizovan: {str(e)}"
        
        # Extract content after /store
        content = message[6:].strip()  # Remove "/store"
        
        if not content:
            return "❌ Morate uneti sadržaj nakon /store komande.\n\nPrimer: /store Trafo T1 u TS Beograd 5 ima snagu 300 MVA"
        
        try:
            # Store the knowledge
            entry = self.stored_knowledge.add_entry(content, stored_by="expert")
            
            return f"""✅ **Informacija uspešno sačuvana!**

**ID:** `{entry['id'][:8]}...`

**Sadržaj:** {content}

**Vreme:** {entry['timestamp']}

Ova informacija će sada biti dostupna svim korisnicima u svim budućim sesijama."""
            
        except Exception as e:
            return f"❌ Greška pri čuvanju informacije: {str(e)}"
    
    def _search_stored_knowledge(self, query, top_k=3, min_score=-1.0):
        """Search stored knowledge and format results.
        
        Args:
            query: Search query
            top_k: Number of results to return
            min_score: Minimum rerank score threshold (BGE logit scores, typically -5 to +5)
            
        Returns:
            List of formatted results (only those above min_score)
        """
        # Try to lazy load stored knowledge if needed
        if self.stored_knowledge is None:
            try:
                self.ensure_stored_knowledge_lazy()
            except:
                # If loading fails, just return empty results (stored knowledge not critical for search)
                return []
        
        if self.stored_knowledge.count() == 0:
            return []
        
        try:
            results = self.stored_knowledge.search(query, top_k=top_k)
            
            # Format as document chunks for consistency
            formatted = []
            filtered_count = 0
            for i, result in enumerate(results, 1):
                # Stored knowledge uses 'rerank_score' from BGE reranker
                score = result.get('rerank_score', result.get('similarity_score', 0.0))
                
                # Use title if available, otherwise fallback to truncated content
                display_title = result.get('title', result['content'][:50] + '...')
                
                # Filter by minimum score threshold
                if score < min_score:
                    filtered_count += 1
                    print(f"  ⚠️ Filtered out: '{display_title}' (score={score:.3f} < threshold={min_score})")
                    continue
                formatted.append({
                    "rank": i,
                    "filename": "STORED_KNOWLEDGE",
                    "section": display_title,  # Use title as section
                    "item_number": "Expert Knowledge",  # User-friendly label
                    "score": score,
                    "content": result['content']
                })
            
            if formatted:
                print(f"📚 Found {len(formatted)} stored knowledge entries above threshold {min_score} (top score: {formatted[0]['score']:.3f})")
                if filtered_count > 0:
                    print(f"   Filtered out {filtered_count} entries below threshold")
            else:
                print(f"📚 No stored knowledge entries found above threshold {min_score}")
                if filtered_count > 0:
                    print(f"   All {filtered_count} candidates were below threshold")
            
            return formatted
            
        except Exception as e:
            print(f"⚠️ Error searching stored knowledge: {e}")
            return []
    
    def display_history(self):
        """Display conversation history."""
        print("\n" + "="*100)
        print("CONVERSATION HISTORY")
        print("="*100 + "\n")
        
        for msg in self.messages:
            role = msg["role"].upper()
            content = msg.get("content", "")
            
            if role == "USER":
                print(f"👤 USER:\n{content}\n")
            elif role == "ASSISTANT":
                if "tool_calls" in msg:
                    print(f"🤖 ASSISTANT: [Calling tools...]\n")
                else:
                    print(f"🤖 ASSISTANT:\n{content}\n")
            elif role == "TOOL":
                print(f"🔧 TOOL RESULT: [Document search completed]\n")
            
            print("-" * 100 + "\n")
    
    def reset_conversation(self):
        """Clear conversation history."""
        self.messages = [{
            "role": "system",
            "content": self.system_prompt
        }]
        print("✅ Conversation history cleared\n")


def main():
    """Main chat loop."""
    print("="*100)
    print("OLLAMA RAG CHAT WITH REST API RETRIEVAL")
    print("="*100)
    print("Commands:")
    print("  - Type your question to chat")
    print("  - 'history' - Show conversation history")
    print("  - 'reset' - Clear conversation")
    print("  - 'quit' - Exit\n")
    
    # Initialize chat with REST API (reads config.json internally)
    chat = OllamaRAGChat()
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
            
            if user_input.lower() == 'history':
                chat.display_history()
                continue
            
            if user_input.lower() == 'reset':
                chat.reset_conversation()
                continue
            
            # Get response
            response = chat.chat(user_input)
            
            # Only print if not streaming (streaming already prints during generation)
            if not chat.stream_tokens:
                print(f"\n🤖 Assistant: {response}\n")
            print("="*100 + "\n")
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}\n")


if __name__ == "__main__":
    main()
