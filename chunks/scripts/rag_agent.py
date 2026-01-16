#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RAG Agent za EES dokumentaciju
==============================

Koristi LangChain sa:
- FAISS bazom za pretragu (BGE-M3 embeddings)
- BGE-M3 reranker za re-ranking rezultata
- Konzolni chat interfejs za Q&A
"""

import json
import os
import sys
import warnings
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple, Set
from collections import Counter
import numpy as np

# Suppress tokenizer warnings
os.environ["TOKENIZERS_PARALLELISM"] = "false"
warnings.filterwarnings("ignore", message=".*XLMRobertaTokenizerFast.*")
warnings.filterwarnings("ignore", message=".*incorrect regex pattern.*")
warnings.filterwarnings("ignore", message=".*fix_mistral_regex.*")
warnings.filterwarnings("ignore", category=FutureWarning)

# Mapiranje srpske ćirilice u latinicu
CYRILLIC_TO_LATIN = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Ђ': 'Đ', 'Е': 'E',
    'Ж': 'Ž', 'З': 'Z', 'И': 'I', 'Ј': 'J', 'К': 'K', 'Л': 'L', 'Љ': 'Lj',
    'М': 'M', 'Н': 'N', 'Њ': 'Nj', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S',
    'Т': 'T', 'Ћ': 'Ć', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'C', 'Ч': 'Č',
    'Џ': 'Dž', 'Ш': 'Š',
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'ђ': 'đ', 'е': 'e',
    'ж': 'ž', 'з': 'z', 'и': 'i', 'ј': 'j', 'к': 'k', 'л': 'l', 'љ': 'lj',
    'м': 'm', 'н': 'n', 'њ': 'nj', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's',
    'т': 't', 'ћ': 'ć', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'č',
    'џ': 'dž', 'ш': 'š',
}

def cyrillic_to_latin(text: str) -> str:
    """Konvertuje srpsku ćirilicu u latinicu."""
    if not text:
        return text
    result = []
    for char in text:
        result.append(CYRILLIC_TO_LATIN.get(char, char))
    return ''.join(result)

# Boje za konzolu
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


def load_config(config_path: str) -> dict:
    """Učitava konfiguraciju."""
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_chunks(chunks_path: str) -> List[Dict]:
    """Učitava chunk-ove iz JSONL fajla."""
    chunks = []
    with open(chunks_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                chunks.append(json.loads(line))
    return chunks


class BGEM3Embedder:
    """BGE-M3 Embedding model wrapper."""
    
    def __init__(self, model_name: str = "BAAI/bge-m3", device: str = "cpu", local_files_only: bool = False):
        self.model_name = model_name
        self.device = device
        self.local_files_only = local_files_only
        self.model = None
        
    def load_model(self):
        """Učitava BGE-M3 model."""
        if self.model is not None:
            return self
        
        local_str = " (lokalno)" if self.local_files_only else ""
        print(f"{Colors.CYAN}Učitavanje embedding modela: {self.model_name}{local_str}...{Colors.ENDC}")
        
        try:
            from FlagEmbedding import BGEM3FlagModel
            
            # Postavi environment varijablu za offline mod
            if self.local_files_only:
                import os
                os.environ['HF_HUB_OFFLINE'] = '1'
            
            self.model = BGEM3FlagModel(
                self.model_name,
                use_fp16=False,
                device=self.device
            )
            print(f"{Colors.GREEN}✓ Embedding model učitan{Colors.ENDC}")
        except ImportError as e:
            print(f"{Colors.RED}Greška: FlagEmbedding nije instaliran{Colors.ENDC}")
            print("Instalirajte: pip install FlagEmbedding")
            raise e
            
        return self
    
    def embed_query(self, query: str) -> np.ndarray:
        """Enkodira query u vektor."""
        if self.model is None:
            self.load_model()
            
        result = self.model.encode(
            [query],
            batch_size=1,
            max_length=512,
            return_dense=True,
            return_sparse=False,
            return_colbert_vecs=False
        )
        
        if isinstance(result, dict):
            embedding = result['dense_vecs'][0]
        else:
            embedding = result[0]
            
        return np.array(embedding).astype('float32')


class BGEM3Reranker:
    """BGE-M3 Reranker za re-ranking rezultata."""
    
    def __init__(self, model_name: str = "BAAI/bge-reranker-v2-m3", device: str = "cpu", local_files_only: bool = False):
        self.model_name = model_name
        self.device = device
        self.local_files_only = local_files_only
        self.model = None
        
    def load_model(self):
        """Učitava reranker model."""
        if self.model is not None:
            return self
        
        local_str = " (lokalno)" if self.local_files_only else ""
        print(f"{Colors.CYAN}Učitavanje reranker modela: {self.model_name}{local_str}...{Colors.ENDC}")
        
        try:
            from FlagEmbedding import FlagReranker
            
            # Postavi environment varijablu za offline mod
            if self.local_files_only:
                import os
                os.environ['HF_HUB_OFFLINE'] = '1'
            
            self.model = FlagReranker(
                self.model_name,
                use_fp16=False,
                device=self.device
            )
            print(f"{Colors.GREEN}✓ Reranker model učitan{Colors.ENDC}")
        except ImportError as e:
            print(f"{Colors.RED}Greška: FlagEmbedding nije instaliran{Colors.ENDC}")
            print("Instalirajte: pip install FlagEmbedding")
            raise e
            
        return self
    
    def rerank(self, query: str, documents: List[str], top_k: int = 5) -> List[Tuple[int, float]]:
        """
        Re-rankira dokumente za dati query.
        
        Vraća: Lista (original_index, score) sortirana po score-u
        """
        if self.model is None:
            self.load_model()
        
        if not documents:
            return []
        
        # Kreiraj parove (query, document)
        pairs = [[query, doc] for doc in documents]
        
        # Izračunaj relevance scores - koristimo normalize=False za bolje razdvajanje
        # normalize=True koristi sigmoid koji "saturira" na 1.0 za visoke score-ove
        scores = self.model.compute_score(pairs, normalize=False)
        
        # Ako je samo jedan dokument, scores je float
        if isinstance(scores, float):
            scores = [scores]
        
        # Custom normalizacija: min-max scaling na [0, 1] za bolje razdvajanje
        if len(scores) > 1:
            min_score = min(scores)
            max_score = max(scores)
            if max_score > min_score:
                scores = [(s - min_score) / (max_score - min_score) for s in scores]
            else:
                scores = [1.0 for _ in scores]  # svi jednaki
        
        # Kreiraj listu (index, score)
        indexed_scores = list(enumerate(scores))
        
        # Sortiraj po score-u (descending)
        indexed_scores.sort(key=lambda x: x[1], reverse=True)
        
        # Vrati top_k
        return indexed_scores[:top_k]


class BM25Retriever:
    """
    BM25 retriever za keyword-based pretragu.
    Koristi se zajedno sa FAISS za hibridnu pretragu.
    """
    
    # Srpske stop words
    STOP_WORDS = {
        'i', 'u', 'je', 'se', 'na', 'da', 'su', 'za', 'sa', 'od', 'do', 'ili', 'a',
        'kao', 'koji', 'koja', 'koje', 'ko', 'šta', 'što', 'taj', 'ta', 'to', 'ovo',
        'biti', 'biti', 'ima', 'može', 'treba', 'ako', 'kada', 'dok', 'nego', 'ali',
        'već', 'još', 'samo', 'sve', 'svi', 'sve', 'po', 'iz', 'kroz', 'prema', 'o',
        'li', 'ne', 'ni', 'niti', 'pa', 'te', 'tom', 'tim', 'tog', 'tih', 'taj',
        'onda', 'tako', 'kako', 'ovaj', 'ova', 'ove', 'ovog', 'onih', 'onom',
        'njegov', 'njen', 'njihov', 'moj', 'tvoj', 'naš', 'vaš', 'svoj',
        'jedan', 'jedna', 'jedno', 'dva', 'tri', 'prvi', 'druga', 'drugi',
        'bio', 'bila', 'bilo', 'bili', 'bile', 'bude', 'budu', 'budući',
        'će', 'ću', 'ćeš', 'ćemo', 'ćete', 'bi', 'bih', 'bismo',
        'sam', 'si', 'smo', 'ste', 'jesam', 'jesi', 'jeste', 'jesmo', 'jesu'
    }
    
    def __init__(self, chunks: List[Dict], k1: float = 1.5, b: float = 0.75):
        self.chunks = chunks
        self.k1 = k1
        self.b = b
        self.avg_doc_len = 0
        self.doc_freqs = {}  # term -> number of docs containing term
        self.doc_term_freqs = []  # list of Counter for each doc
        self.N = len(chunks)
        self._build_index()
    
    def _tokenize(self, text: str) -> List[str]:
        """Tokenizuje tekst i uklanja stop words."""
        # Lowercase i split po non-alphanumeric
        import re
        tokens = re.findall(r'\b[a-zA-ZčćžšđČĆŽŠĐ0-9]+\b', text.lower())
        # Filtriraj stop words i kratke tokene
        return [t for t in tokens if t not in self.STOP_WORDS and len(t) > 1]
    
    def _build_index(self):
        """Gradi BM25 indeks."""
        total_len = 0
        
        for chunk in self.chunks:
            content = chunk.get('content', '')
            parent_title = chunk.get('parent_title', '')
            section_title = chunk.get('section_title', '')
            keywords = ' '.join(chunk.get('keywords', []))
            
            # Kombinuj sve tekstualne podatke
            full_text = f"{content} {parent_title} {section_title} {keywords}"
            tokens = self._tokenize(full_text)
            
            term_freq = Counter(tokens)
            self.doc_term_freqs.append(term_freq)
            total_len += len(tokens)
            
            # Update document frequencies
            for term in set(tokens):
                self.doc_freqs[term] = self.doc_freqs.get(term, 0) + 1
        
        self.avg_doc_len = total_len / self.N if self.N > 0 else 0
    
    def search(self, query: str, top_k: int = 100) -> List[Dict]:
        """Pretražuje BM25 indeks i vraća top_k rezultata."""
        query_tokens = self._tokenize(query)
        
        if not query_tokens:
            return []
        
        scores = []
        
        for idx, term_freq in enumerate(self.doc_term_freqs):
            score = 0.0
            doc_len = sum(term_freq.values())
            
            for term in query_tokens:
                if term not in term_freq:
                    continue
                
                tf = term_freq[term]
                df = self.doc_freqs.get(term, 0)
                
                # IDF komponenta
                idf = np.log((self.N - df + 0.5) / (df + 0.5) + 1)
                
                # TF komponenta sa BM25 normalizacijom
                tf_norm = (tf * (self.k1 + 1)) / (tf + self.k1 * (1 - self.b + self.b * doc_len / self.avg_doc_len))
                
                score += idf * tf_norm
            
            scores.append((idx, score))
        
        # Sortiraj po score-u
        scores.sort(key=lambda x: x[1], reverse=True)
        
        # Vrati top_k rezultata
        results = []
        for idx, score in scores[:top_k]:
            if score > 0:
                chunk = self.chunks[idx].copy()
                chunk['bm25_score'] = float(score)
                results.append(chunk)
        
        return results


class FAISSRetriever:
    """FAISS retriever za pretragu chunk-ova."""
    
    def __init__(self, index_path: str, chunks: List[Dict], embedder: BGEM3Embedder):
        self.index_path = index_path
        self.chunks = chunks
        self.embedder = embedder
        self.index = None
        
    def load_index(self):
        """Učitava FAISS indeks."""
        if self.index is not None:
            return self
            
        print(f"{Colors.CYAN}Učitavanje FAISS indeksa...{Colors.ENDC}")
        
        import faiss
        self.index = faiss.read_index(self.index_path)
        print(f"{Colors.GREEN}✓ FAISS indeks učitan ({self.index.ntotal} vektora){Colors.ENDC}")
        
        return self
    
    def search(self, query: str, top_k: int = 100) -> List[Dict]:
        """
        Pretražuje FAISS indeks i vraća top_k rezultata.
        """
        if self.index is None:
            self.load_index()
        
        # Embed query
        query_vector = self.embedder.embed_query(query)
        
        # Normalizuj za inner product
        import faiss
        query_vector = query_vector.reshape(1, -1)
        faiss.normalize_L2(query_vector)
        
        # Pretraži
        scores, indices = self.index.search(query_vector, top_k)
        
        # Kreiraj rezultate
        results = []
        for i, (idx, score) in enumerate(zip(indices[0], scores[0])):
            if idx < 0 or idx >= len(self.chunks):
                continue
                
            chunk = self.chunks[idx].copy()
            chunk['faiss_score'] = float(score)
            chunk['faiss_rank'] = i + 1
            results.append(chunk)
        
        return results


class RAGAgent:
    """
    RAG Agent koji kombinuje:
    - FAISS pretragu (top 100)
    - BGE-M3 reranking (opciono)
    """
    
    def __init__(self, config_path: str):
        self.config = load_config(config_path)
        
        # Rerank opcija iz config-a
        self.use_rerank = self.config.get('retrieval', {}).get('rerank', False)
        self.top_k = self.config.get('retrieval', {}).get('top_k', 3)
        self.embedding_top_k = self.config.get('retrieval', {}).get('embedding_top_k', 100)
        
        # Hibridna pretraga opcije
        self.use_hybrid_search = self.config.get('retrieval', {}).get('use_hybrid_search', True)
        self.hybrid_alpha = self.config.get('retrieval', {}).get('hybrid_alpha', 0.7)  # weight za FAISS
        
        # BM25 boost na reranker nivou
        self.use_rerank_bm25_boost = self.config.get('retrieval', {}).get('use_rerank_bm25_boost', False)
        self.rerank_bm25_weight = self.config.get('retrieval', {}).get('rerank_bm25_weight', 0.15)
        
        # Učitaj chunk-ove
        print(f"\n{Colors.HEADER}{'='*60}{Colors.ENDC}")
        print(f"{Colors.BOLD}RAG AGENT ZA EES DOKUMENTACIJU{Colors.ENDC}")
        print(f"{Colors.HEADER}{'='*60}{Colors.ENDC}\n")
        
        chunks_path = self.config['paths']['chunks_file']
        print(f"{Colors.CYAN}Učitavanje chunk-ova: {chunks_path}{Colors.ENDC}")
        self.chunks = load_chunks(chunks_path)
        print(f"{Colors.GREEN}✓ Učitano {len(self.chunks)} chunk-ova{Colors.ENDC}")
        
        # Inicijalizuj komponente
        device = self.config['embedding'].get('device', 'cpu')
        local_files_only = self.config['embedding'].get('local_files_only', False)
        
        self.embedder = BGEM3Embedder(
            model_name=self.config['embedding']['model_name'],
            device=device,
            local_files_only=local_files_only
        )
        
        self.reranker = None
        if self.use_rerank:
            # Reranker config
            reranker_config = self.config.get('reranker', {})
            use_finetuned = reranker_config.get('use_finetuned', False)
            reranker_device = reranker_config.get('device', device)
            reranker_local = reranker_config.get('local_files_only', True)
            
            if use_finetuned:
                reranker_model = reranker_config.get('model_name_finetuned', 'BAAI/bge-reranker-v2-m3')
                print(f"{Colors.CYAN}Koristi se FINETUNED reranker{Colors.ENDC}")
            else:
                reranker_model = reranker_config.get('model_name', 'BAAI/bge-reranker-v2-m3')
                print(f"{Colors.CYAN}Koristi se ORIGINAL reranker{Colors.ENDC}")
            
            self.reranker = BGEM3Reranker(
                model_name=reranker_model,
                device=reranker_device,
                local_files_only=reranker_local
            )
        
        self.retriever = FAISSRetriever(
            index_path=self.config['paths']['faiss_index'],
            chunks=self.chunks,
            embedder=self.embedder
        )
        
        # BM25 retriever za hibridnu pretragu
        self.bm25_retriever = None
        if self.use_hybrid_search:
            print(f"{Colors.CYAN}Izgradnja BM25 indeksa...{Colors.ENDC}")
            self.bm25_retriever = BM25Retriever(self.chunks)
            print(f"{Colors.GREEN}✓ BM25 indeks izgrađen{Colors.ENDC}")
        
        # Učitaj modele
        print()
        self.embedder.load_model()
        if self.use_rerank:
            self.reranker.load_model()
            print(f"{Colors.CYAN}Reranker: UKLJUČEN{Colors.ENDC}")
        else:
            print(f"{Colors.YELLOW}Reranker: ISKLJUČEN (samo FAISS){Colors.ENDC}")
        
        if self.use_hybrid_search:
            print(f"{Colors.CYAN}Hibridna pretraga: UKLJUČENA (alpha={self.hybrid_alpha}){Colors.ENDC}")
        else:
            print(f"{Colors.YELLOW}Hibridna pretraga: ISKLJUČENA{Colors.ENDC}")
        
        if self.use_rerank_bm25_boost:
            print(f"{Colors.CYAN}Rerank BM25 Boost: UKLJUČEN (weight={self.rerank_bm25_weight}){Colors.ENDC}")
        else:
            print(f"{Colors.YELLOW}Rerank BM25 Boost: ISKLJUČEN{Colors.ENDC}")
        
        self.retriever.load_index()
        
        print(f"\n{Colors.GREEN}✓ RAG Agent spreman!{Colors.ENDC}\n")
    
    def _extract_objects_from_query(self, query: str) -> List[str]:
        """
        Pokušaj da ekstraktuješ imena objekata iz query-ja.
        Vraća listu object_code-ova (npr. ['NI2'] ili ['BG5', 'BG20'] za pitanja o 2 TS).
        """
        query_lower = query.lower()
        
        # Mapiranje imena objekata na kodove
        object_patterns = {
            'niš 2': 'NI2', 'nis 2': 'NI2', 'ni2': 'NI2',
            'niš 1': 'NI1', 'nis 1': 'NI1', 'ni1': 'NI1',
            'niš 3': 'NI3', 'nis 3': 'NI3', 'ni3': 'NI3',
            'novi sad 3': 'NS3', 'ns3': 'NS3',
            'beograd 3': 'BG3', 'bg3': 'BG3',
            'beograd 5': 'BG5', 'bg5': 'BG5',
            'beograd 8': 'BG8', 'bg8': 'BG8',
            'beograd 20': 'BG20', 'bg20': 'BG20',
            'obrenovac': 'OBR', 'obr': 'OBR',
            'srbobran': 'SRB', 'srb': 'SRB',
            'kraljevo 3': 'KR3', 'kr3': 'KR3',
            'kragujevac 2': 'KG2', 'kg2': 'KG2',
            'kruševac 1': 'KR1', 'krusevac 1': 'KR1', 'kr1': 'KR1',
            'leskovac 2': 'LE2', 'le2': 'LE2',
            'vranje 4': 'VR4', 'vr4': 'VR4',
            'jagodina 4': 'JA4', 'ja4': 'JA4',
            'pančevo 2': 'PA2', 'pancevo 2': 'PA2', 'pa2': 'PA2',
            'sremska mitrovica 2': 'SM2', 'sm2': 'SM2',
            'sombor 3': 'SO3', 'so3': 'SO3',
            'subotica 3': 'SU3', 'su3': 'SU3',
            'zrenjanin 2': 'ZR2', 'zr2': 'ZR2',
            'smederevo 3': 'SD3', 'sd3': 'SD3',
            'valjevo 3': 'VA3', 'va3': 'VA3',
            'čačak 3': 'CA3', 'cacak 3': 'CA3', 'ca3': 'CA3',
            'šabac 3': 'SA3', 'sabac 3': 'SA3', 'sa3': 'SA3',
            'požega': 'PO', 'pozega': 'PO',
            'bajina bašta': 'BB', 'bajina basta': 'BB', 'bb': 'BB',
            'bistrica': 'BI',
            'đerdap 1': 'DJE1', 'djerdap 1': 'DJE1', 'dje1': 'DJE1',
            'đerdap 2': 'DJE2', 'djerdap 2': 'DJE2', 'dje2': 'DJE2',
            'drmno': 'DRM', 'drm': 'DRM',
            'mladost': 'ML',
            'čibuk': 'CIB1', 'cibuk': 'CIB1', 'cib1': 'CIB1',
        }
        
        # Pronađi sve objekte u query-ju
        found_objects = []
        found_codes = set()
        for pattern, code in object_patterns.items():
            if pattern in query_lower and code not in found_codes:
                found_objects.append(code)
                found_codes.add(code)
        
        return found_objects
    
    def _hybrid_search(self, query: str, top_k: int) -> List[Dict]:
        """
        Hibridna pretraga koja kombinuje FAISS (semantic) i BM25 (keyword).
        Reciprocal Rank Fusion (RRF) za kombinovanje rezultata.
        """
        # Uzmi više kandidata od oba sistema
        k_each = top_k * 2
        
        # FAISS pretraga
        faiss_results = self.retriever.search(query, top_k=k_each)
        
        # BM25 pretraga
        bm25_results = self.bm25_retriever.search(query, top_k=k_each)
        
        # RRF konstanta (standardna vrednost)
        rrf_k = 60
        
        # Računaj RRF scores
        chunk_scores = {}  # chunk_id -> score
        chunk_data = {}    # chunk_id -> chunk dict
        
        # FAISS rezultati (ponderisano sa alpha)
        for rank, result in enumerate(faiss_results, 1):
            chunk_id = result.get('chunk_id')
            if chunk_id:
                rrf_score = self.hybrid_alpha / (rrf_k + rank)
                chunk_scores[chunk_id] = chunk_scores.get(chunk_id, 0) + rrf_score
                chunk_data[chunk_id] = result
        
        # BM25 rezultati (ponderisano sa 1-alpha)
        for rank, result in enumerate(bm25_results, 1):
            chunk_id = result.get('chunk_id')
            if chunk_id:
                rrf_score = (1 - self.hybrid_alpha) / (rrf_k + rank)
                chunk_scores[chunk_id] = chunk_scores.get(chunk_id, 0) + rrf_score
                if chunk_id not in chunk_data:
                    chunk_data[chunk_id] = result
                else:
                    # Dodaj BM25 score u postojeći rezultat
                    chunk_data[chunk_id]['bm25_score'] = result.get('bm25_score', 0)
        
        # Sortiraj po kombinovanom score-u
        sorted_chunks = sorted(chunk_scores.items(), key=lambda x: x[1], reverse=True)
        
        # Kreiraj finalne rezultate
        results = []
        for chunk_id, hybrid_score in sorted_chunks[:top_k]:
            chunk = chunk_data[chunk_id].copy()
            chunk['hybrid_score'] = hybrid_score
            results.append(chunk)
        
        return results
    
    def _filter_by_document(self, results: List[Dict], target_objects: List[str], 
                            total_count: int, target_ratio: float = 0.7) -> List[Dict]:
        """
        Filtriraj kandidate tako da ~70% bude iz target dokumenta/dokumenata.
        Ostatak popuni sa drugim dokumentima (za generičke informacije).
        
        Args:
            results: Lista rezultata pretrage
            target_objects: Lista object_code-ova koji su target (može biti više za pitanja o 2 TS)
            total_count: Koliko ukupno kandidata treba
            target_ratio: Procenat kandidata koji treba da bude iz target dokumenta
        
        Returns:
            Filtrirana lista rezultata
        """
        if not target_objects:
            return results[:total_count]
        
        # Podeli na target i ostale
        target_results = [r for r in results if r.get('object_code') in target_objects]
        other_results = [r for r in results if r.get('object_code') not in target_objects]
        
        # Izračunaj koliko treba od svakog
        target_count = int(total_count * target_ratio)
        other_count = total_count - target_count
        
        # Uzmi koliko imamo (ali ne više nego što treba)
        final_target = target_results[:target_count]
        final_other = other_results[:other_count]
        
        # Ako nemamo dovoljno target, dopuni sa other
        if len(final_target) < target_count:
            extra_needed = target_count - len(final_target)
            final_other = other_results[:other_count + extra_needed]
        
        # Kombinuj - target prvi (važniji), pa ostali
        return final_target + final_other
    
    def retrieve(self, query: str, initial_k: int = None, final_k: int = None) -> List[Dict]:
        """
        Retrieval pipeline:
        1. Hibridna pretraga (FAISS + BM25) ili samo FAISS - top initial_k
        2. BGE-M3 reranking - top final_k (ako je uključen)
        """
        # Konvertuj query u latinicu (chunkovi su u latinici)
        query = cyrillic_to_latin(query)
        
        if initial_k is None:
            initial_k = self.embedding_top_k
        
        if final_k is None:
            final_k = self.top_k
            
        # Korak 1: Pretraga kandidata
        if self.use_rerank:
            # Ako koristimo reranker, uzmi više kandidata
            if self.use_hybrid_search and self.bm25_retriever:
                initial_results = self._hybrid_search(query, top_k=initial_k)
            else:
                initial_results = self.retriever.search(query, top_k=initial_k)
        else:
            # Bez reranker-a, uzmi samo final_k
            if self.use_hybrid_search and self.bm25_retriever:
                initial_results = self._hybrid_search(query, top_k=final_k)
            else:
                initial_results = self.retriever.search(query, top_k=final_k)
        
        if not initial_results:
            return []
        
        # Ako reranker nije uključen, vrati rezultate direktno
        if not self.use_rerank:
            for i, result in enumerate(initial_results, 1):
                result['final_rank'] = i
                result['rerank_score'] = result.get('hybrid_score', result.get('faiss_score', 0))
            return initial_results
        
        # Detektuj objekte iz query-ja za potencijalni boost i filtriranje
        target_objects = self._extract_objects_from_query(query)
        
        # Korak 1.5: Document-first filtering - prioritizuj kandidate iz target dokumenta
        if target_objects:
            # Filtriraj da 70% bude iz target dokumenata, 30% ostalo
            rerank_candidates_count = min(initial_k, len(initial_results))
            initial_results = self._filter_by_document(
                initial_results, target_objects, rerank_candidates_count, target_ratio=0.7
            )
        
        # Korak 2: Reranking sa metapodacima
        documents_with_metadata = []
        for r in initial_results:
            doc_title = r.get('doc_title', '')
            section_title = r.get('section_title', '')
            section_number = r.get('section_number', '')
            object_code = r.get('object_code', '')
            content = r.get('content', '')
            
            # Formatira tekst sa metapodacima za reranker
            # Koristi object_name za reranker (čitljivije ime objekta)
            object_name = r.get('object_name', '')
            voltage_levels = r.get('voltage_levels', [])
            keywords = r.get('keywords', [])
            parent_title = r.get('parent_title', '')
            
            metadata_prefix = f"[Dokument: {doc_title}"
            if object_name:
                metadata_prefix += f" | Objekat: {object_name}"
            if voltage_levels:
                metadata_prefix += f" | Naponi: {', '.join(voltage_levels)}"
            if parent_title:
                metadata_prefix += f" | Tema: {parent_title}"
            if section_number or section_title:
                sec_label = " ".join([s for s in [str(section_number).strip(), str(section_title).strip()] if s]).strip()
                metadata_prefix += f" | Sekcija: {sec_label}"
            if keywords:
                metadata_prefix += f" | Ključne reči: {', '.join(keywords)}"
            metadata_prefix += "]\n"
            
            enriched_text = metadata_prefix + content
            documents_with_metadata.append(enriched_text)
        
        reranked = self.reranker.rerank(query, documents_with_metadata, top_k=final_k * 3 if target_objects else final_k)
        
        # Kreiraj finalne rezultate sa boost-om za target objekat i BM25
        final_results = []
        OBJECT_BOOST = 0.15  # Boost za rezultate koji se poklapaju sa objektom iz query-ja
        WRONG_OBJECT_PENALTY = 0.10  # Penalizacija za pogrešan objekat sa istom sekcijom
        
        # Ako imamo target objekte, pronađi koje sekcije postoje u tim objektima
        target_sections = set()
        if target_objects:
            for orig_idx, _ in reranked:
                r = initial_results[orig_idx]
                if r.get('object_code') in target_objects:
                    section_num = str(r.get('section_number', '')).strip()
                    if section_num:
                        # Uzmi samo glavni broj sekcije (npr. "3.3" od "3.3.1")
                        main_section = '.'.join(section_num.split('.')[:2])
                        target_sections.add(main_section)
                        target_sections.add(main_section)
        
        for rank, (orig_idx, rerank_score) in enumerate(reranked, 1):
            result = initial_results[orig_idx].copy()
            adjusted_score = float(rerank_score)
            
            # BM25 boost na reranker nivou (ako je uključen)
            bm25_boost = 0.0
            if self.use_rerank_bm25_boost and self.bm25_retriever:
                content = result.get('content', '')
                parent_title = result.get('parent_title', '')
                section_title = result.get('section_title', '')
                keywords = ' '.join(result.get('keywords', []))
                full_text = f"{content} {parent_title} {section_title} {keywords}"
                
                # Računaj BM25 score koristeći već izgrađen BM25 retriever
                query_tokens = self.bm25_retriever._tokenize(query)
                doc_tokens = self.bm25_retriever._tokenize(full_text)
                
                if query_tokens and doc_tokens:
                    from collections import Counter
                    doc_term_freq = Counter(doc_tokens)
                    doc_len = len(doc_tokens)
                    bm25_score = 0.0
                    
                    for term in query_tokens:
                        if term in doc_term_freq:
                            tf = doc_term_freq[term]
                            df = self.bm25_retriever.doc_freqs.get(term, 1)
                            idf = np.log((self.bm25_retriever.N - df + 0.5) / (df + 0.5) + 1)
                            k1, b = 1.5, 0.75
                            avg_dl = self.bm25_retriever.avg_doc_len
                            tf_norm = (tf * (k1 + 1)) / (tf + k1 * (1 - b + b * doc_len / avg_dl))
                            bm25_score += idf * tf_norm
                    
                    # Normalizuj BM25 score na 0-1
                    max_bm25 = len(query_tokens) * 3  # aproksimacija max score-a
                    bm25_normalized = min(1.0, bm25_score / max_bm25) if max_bm25 > 0 else 0
                    bm25_boost = bm25_normalized * self.rerank_bm25_weight
                    result['rerank_bm25_score'] = bm25_normalized
                    result['rerank_bm25_boost'] = bm25_boost
            
            # Ako je detektovan objekat u query-ju i ovaj rezultat je za taj objekat, dodaj boost
            if target_objects and result.get('object_code') in target_objects:
                adjusted_score = min(1.0, adjusted_score + OBJECT_BOOST)
                result['object_boost'] = OBJECT_BOOST
            # Penalizuj SVE rezultate koji nisu iz target objekta
            elif target_objects:
                # Veća penalizacija ako ima istu sekciju kao target (strukturalna sličnost)
                section_num = str(result.get('section_number', '')).strip()
                if section_num and target_sections:
                    main_section = '.'.join(section_num.split('.')[:2])
                    if main_section in target_sections:
                        # Ista sekcija ali pogrešan dokument - jača penalizacija
                        penalty = WRONG_OBJECT_PENALTY * 1.5
                        adjusted_score = max(0.0, adjusted_score - penalty)
                        result['wrong_object_penalty'] = -penalty
                    else:
                        # Različita sekcija, pogrešan dokument - standardna penalizacija
                        adjusted_score = max(0.0, adjusted_score - WRONG_OBJECT_PENALTY)
                        result['wrong_object_penalty'] = -WRONG_OBJECT_PENALTY
                else:
                    # Nema sekcije ili target_sections - standardna penalizacija
                    adjusted_score = max(0.0, adjusted_score - WRONG_OBJECT_PENALTY)
                    result['wrong_object_penalty'] = -WRONG_OBJECT_PENALTY
            
            # Dodaj BM25 boost
            adjusted_score = min(1.0, adjusted_score + bm25_boost)
            
            result['rerank_score'] = adjusted_score
            result['original_rerank_score'] = float(rerank_score)
            final_results.append(result)
        
        # Ponovo sortiraj po adjusted score
        final_results.sort(key=lambda x: x['rerank_score'], reverse=True)
        
        # Ograniči na final_k i dodaj rank
        final_results = final_results[:final_k]
        for i, result in enumerate(final_results, 1):
            result['final_rank'] = i
        
        return final_results
    
    def format_context(self, results: List[Dict]) -> str:
        """Formatira kontekst za prikaz - kompaktni format."""
        if not results:
            return "Nema pronađenih rezultata."
        
        lines = []
        for i, r in enumerate(results, 1):
            doc_title = r.get('doc_title', 'N/A') or 'N/A'
            object_code = r.get('object_code', 'N/A') or 'N/A'
            section_number = str(r.get('section_number', '') or '').strip()
            section_title = str(r.get('section_title', '') or '').strip()
            section_label = " ".join([s for s in [section_number, section_title] if s]).strip()
            section = section_label[:70]
            score = r.get('rerank_score', 0)
            
            line = f"{Colors.YELLOW}[{i:2}]{Colors.ENDC} {doc_title[:20]:20} | Score: {score:.4f} | {Colors.CYAN}{object_code:6}{Colors.ENDC} | {section}"
            lines.append(line)
        
        return "\n".join(lines)
    
    def answer(self, query: str) -> str:
        """
        Odgovara na pitanje.
        Za sada samo vraća pronađeni kontekst.
        Možete dodati LLM za generisanje odgovora.
        """
        print(f"\n{Colors.BLUE}Pretražujem...{Colors.ENDC}")
        
        results = self.retrieve(query)
        
        if self.use_rerank:
            print(f"{Colors.CYAN}FAISS: 100 kandidata → Reranker: {len(results)} rezultata{Colors.ENDC}")
        else:
            print(f"{Colors.CYAN}FAISS: top {len(results)} rezultata (bez reranker-a){Colors.ENDC}")
        
        if not results:
            return f"{Colors.RED}Nije pronađen relevantan sadržaj.{Colors.ENDC}"
        
        # Formatira pronađeni kontekst
        context = self.format_context(results)
        
        # Log tokena za svaki chunk (na kraju)
        token_stats = f"\n{Colors.YELLOW}Token statistika:{Colors.ENDC}\n"
        total_tokens = 0
        for i, r in enumerate(results, 1):
            content = r.get('content', '')
            char_count = len(content)
            token_count = char_count // 4
            total_tokens += token_count
            token_stats += f"  [{i}] {token_count:,} tokena ({char_count:,} karaktera)\n"
        
        token_stats += f"  {Colors.BOLD}Ukupno: {total_tokens:,} tokena{Colors.ENDC}"
        
        response = f"""
{Colors.GREEN}{'='*60}{Colors.ENDC}
{Colors.BOLD}PRONAĐENI KONTEKST ({len(results)} rezultata){Colors.ENDC}
{Colors.GREEN}{'='*60}{Colors.ENDC}
{context}
{Colors.GREEN}{'='*60}{Colors.ENDC}
{token_stats}
"""
        return response


def run_chat():
    """Pokreće konzolni chat interfejs."""
    
    # Putanja do konfiguracije
    base_dir = Path(__file__).parent.parent
    config_path = base_dir / 'config' / 'rag_config.json'
    
    # Inicijalizuj agenta
    try:
        agent = RAGAgent(str(config_path))
    except Exception as e:
        print(f"{Colors.RED}Greška pri inicijalizaciji: {e}{Colors.ENDC}")
        sys.exit(1)
    
    # Chat loop
    print(f"""
{Colors.HEADER}{'='*60}{Colors.ENDC}
{Colors.BOLD}KONZOLNI CHAT - EES RAG SISTEM{Colors.ENDC}
{Colors.HEADER}{'='*60}{Colors.ENDC}

Postavljajte pitanja o elektroenergetskom sistemu.
Komande:
  {Colors.CYAN}/quit{Colors.ENDC} ili {Colors.CYAN}/exit{Colors.ENDC} - Izlaz iz programa
  {Colors.CYAN}/help{Colors.ENDC} - Pomoć
  {Colors.CYAN}/clear{Colors.ENDC} - Obriši ekran

{Colors.GREEN}Spreman za pitanja!{Colors.ENDC}
""")
    
    while True:
        try:
            # Prompt
            print(f"\n{Colors.BOLD}{Colors.BLUE}Vi:{Colors.ENDC} ", end="")
            user_input = input().strip()
            
            # Proveri komande
            if not user_input:
                continue
                
            if user_input.lower() in ['/quit', '/exit', 'quit', 'exit']:
                print(f"\n{Colors.YELLOW}Doviđenja!{Colors.ENDC}\n")
                break
                
            if user_input.lower() == '/help':
                print(f"""
{Colors.CYAN}Pomoć:{Colors.ENDC}
- Postavite pitanje na srpskom jeziku
- Sistem pretražuje dokumentaciju EES-a
- Vraća top 5 najrelevantnijih odlomaka

{Colors.CYAN}Primeri pitanja:{Colors.ENDC}
- Šta je balansna grupa?
- Objasni postupak uklapanja transformatora
- Koje su zaštite na transformatoru?
- Pravila za priključenje na prenosni sistem
""")
                continue
                
            if user_input.lower() == '/clear':
                os.system('clear' if os.name != 'nt' else 'cls')
                continue
            
            # Dobij odgovor
            print(f"\n{Colors.BOLD}{Colors.GREEN}Agent:{Colors.ENDC}")
            response = agent.answer(user_input)
            print(response)
            
        except KeyboardInterrupt:
            print(f"\n\n{Colors.YELLOW}Prekinuto. Doviđenja!{Colors.ENDC}\n")
            break
        except Exception as e:
            print(f"{Colors.RED}Greška: {e}{Colors.ENDC}")


if __name__ == '__main__':
    run_chat()
