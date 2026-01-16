#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FAISS Indexer za EES RAG sistem
===============================

Kreira FAISS indeks od chunk-ova koristeći BGE-M3 embedding model.
"""

import json
import os
import numpy as np
from pathlib import Path
from typing import List, Dict, Tuple
from tqdm import tqdm
import time


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


class BGEEmbedder:
    """Wrapper za BGE-M3 embedding model."""
    
    def __init__(self, model_name: str, device: str = "cpu", 
                 max_length: int = 512, batch_size: int = 32):
        self.model_name = model_name
        self.device = device
        self.max_length = max_length
        self.batch_size = batch_size
        self.model = None
        self.dimension = None
        
    def load_model(self):
        """Učitava model."""
        print(f"Učitavanje modela: {self.model_name}")
        print(f"Ovo može potrajati pri prvom pokretanju...")
        
        try:
            # Pokušaj sa FlagEmbedding (preporučeno za BGE-M3)
            from FlagEmbedding import BGEM3FlagModel
            self.model = BGEM3FlagModel(
                self.model_name, 
                use_fp16=False,
                device=self.device
            )
            self.model_type = "flag"
            # BGE-M3 ima 1024 dimenzija za dense embeddings
            self.dimension = 1024
            print(f"Model učitan (FlagEmbedding): {self.model_name}")
            
        except ImportError:
            # Fallback na sentence-transformers
            from sentence_transformers import SentenceTransformer
            self.model = SentenceTransformer(self.model_name, device=self.device)
            self.model_type = "sentence_transformer"
            self.dimension = self.model.get_sentence_embedding_dimension()
            print(f"Model učitan (sentence-transformers): {self.model_name}")
        
        print(f"Dimenzija embedding-a: {self.dimension}")
        return self
    
    def encode(self, texts: List[str], show_progress: bool = True) -> np.ndarray:
        """Enkodira tekstove u embedding vektore."""
        if self.model is None:
            self.load_model()
        
        if self.model_type == "flag":
            # FlagEmbedding BGE-M3
            embeddings = self.model.encode(
                texts,
                batch_size=self.batch_size,
                max_length=self.max_length,
                return_dense=True,
                return_sparse=False,
                return_colbert_vecs=False
            )
            # BGE-M3 vraća dict sa 'dense_vecs'
            if isinstance(embeddings, dict):
                embeddings = embeddings['dense_vecs']
        else:
            # Sentence Transformers
            embeddings = self.model.encode(
                texts,
                batch_size=self.batch_size,
                show_progress_bar=show_progress,
                normalize_embeddings=True
            )
        
        return np.array(embeddings).astype('float32')


def create_faiss_index(embeddings: np.ndarray, index_type: str = "IndexFlatIP"):
    """Kreira FAISS indeks."""
    import faiss
    
    dimension = embeddings.shape[1]
    
    if index_type == "IndexFlatIP":
        # Inner Product (koristi se za cosine similarity sa normalizovanim vektorima)
        index = faiss.IndexFlatIP(dimension)
    elif index_type == "IndexFlatL2":
        # L2 distance
        index = faiss.IndexFlatL2(dimension)
    elif index_type == "IndexIVFFlat":
        # IVF za brže pretraživanje velikih dataseta
        quantizer = faiss.IndexFlatIP(dimension)
        index = faiss.IndexIVFFlat(quantizer, dimension, 100)
        index.train(embeddings)
    else:
        raise ValueError(f"Nepoznat tip indeksa: {index_type}")
    
    # Normalizuj vektore za Inner Product
    if index_type == "IndexFlatIP":
        faiss.normalize_L2(embeddings)
    
    index.add(embeddings)
    return index


def save_index(index, index_path: str):
    """Čuva FAISS indeks na disk."""
    import faiss
    os.makedirs(os.path.dirname(index_path), exist_ok=True)
    faiss.write_index(index, index_path)
    print(f"Indeks sačuvan: {index_path}")


def save_chunk_mapping(chunks: List[Dict], mapping_path: str):
    """Čuva mapiranje indeksa na chunk-ove."""
    mapping = {
        "total_chunks": len(chunks),
        "chunks": []
    }
    
    for i, chunk in enumerate(chunks):
        mapping["chunks"].append({
            "index": i,
            "chunk_id": chunk.get("chunk_id"),
            "doc_id": chunk.get("doc_id"),
            "object_code": chunk.get("object_code"),
            "section_type": chunk.get("section_type"),
            "chunk_type": chunk.get("chunk_type")
        })
    
    os.makedirs(os.path.dirname(mapping_path), exist_ok=True)
    with open(mapping_path, 'w', encoding='utf-8') as f:
        json.dump(mapping, f, ensure_ascii=False, indent=2)
    
    print(f"Mapiranje sačuvano: {mapping_path}")


def main():
    """Glavna funkcija za indeksiranje."""
    
    # Putanje
    base_dir = Path(__file__).parent.parent
    config_path = base_dir / 'config' / 'rag_config.json'
    
    # Učitaj konfiguraciju
    print("=" * 60)
    print("FAISS INDEXER ZA EES RAG")
    print("=" * 60)
    
    config = load_config(str(config_path))
    print(f"\nKonfiguracija učitana: {config_path}")
    
    # Učitaj chunk-ove
    chunks_path = config['paths']['chunks_file']
    print(f"\nUčitavanje chunk-ova: {chunks_path}")
    chunks = load_chunks(chunks_path)
    print(f"Učitano {len(chunks)} chunk-ova")
    
    # Pripremi tekstove za embedding
    texts = [chunk['content'] for chunk in chunks]
    
    # Kreiraj embedder
    emb_config = config['embedding']
    embedder = BGEEmbedder(
        model_name=emb_config['model_name'],
        device=emb_config['device'],
        max_length=emb_config['max_length'],
        batch_size=emb_config['batch_size']
    )
    
    # Generiši embeddings
    print(f"\nGenerisanje embedding-a...")
    start_time = time.time()
    embeddings = embedder.encode(texts, show_progress=True)
    elapsed = time.time() - start_time
    print(f"Embedding završen za {elapsed:.2f}s")
    print(f"Oblik embedding matrice: {embeddings.shape}")
    
    # Kreiraj FAISS indeks
    print(f"\nKreiranje FAISS indeksa...")
    faiss_config = config['faiss']
    index = create_faiss_index(embeddings, faiss_config['index_type'])
    print(f"Indeks kreiran: {index.ntotal} vektora")
    
    # Sačuvaj indeks
    index_path = config['paths']['faiss_index']
    save_index(index, index_path)
    
    # Sačuvaj mapiranje
    mapping_path = config['paths']['chunk_mapping']
    save_chunk_mapping(chunks, mapping_path)
    
    # Statistike
    print("\n" + "=" * 60)
    print("ZAVRŠENO")
    print("=" * 60)
    print(f"  Broj chunk-ova: {len(chunks)}")
    print(f"  Dimenzija embedding-a: {embeddings.shape[1]}")
    print(f"  Veličina indeksa: {os.path.getsize(index_path) / 1024 / 1024:.2f} MB")
    print(f"  Vreme procesiranja: {elapsed:.2f}s")


if __name__ == '__main__':
    main()
