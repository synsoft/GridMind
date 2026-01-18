import faiss
import numpy as np
import json
import pickle
import logging
from pathlib import Path
from src.core.model_manager import get_model_manager, ModelConfig

logger = logging.getLogger(__name__)


class FAISSSearcher:
    def __init__(self, faiss_dir="data/faiss_db", use_shared_models=True):
        """Initialize FAISS searcher.
        
        Args:
            faiss_dir: Path to FAISS index directory
            use_shared_models: If True, use ModelManager singleton for models
        """
        self.faiss_dir = Path(faiss_dir)
        self.use_shared_models = use_shared_models
        
        # Load FAISS index
        logger.info("Loading FAISS index...")
        print("Loading FAISS index...")
        self.index = faiss.read_index(str(self.faiss_dir / "index.faiss"))
        
        # Load metadata
        with open(self.faiss_dir / "index_info.json", "r") as f:
            self.metadata = json.load(f)
        
        # Get models from ModelManager singleton (shared across application)
        if use_shared_models:
            self._model_manager = get_model_manager(ModelConfig())
            logger.info("Using shared models from ModelManager")
        else:
            # Create dedicated instances (legacy behavior)
            self._model_manager = None
            from FlagEmbedding import BGEM3FlagModel, FlagReranker
            logger.info("Loading BGE-M3 embedding model...")
            print("Loading BGE-M3 embedding model...")
            self._bge_m3 = BGEM3FlagModel('BAAI/bge-m3', use_fp16=True)
            logger.info("Loading BGE reranker-v2-m3...")
            print("Loading BGE reranker-v2-m3...")
            self._reranker = FlagReranker('BAAI/bge-reranker-v2-m3', use_fp16=True)
        
        # Load docstore from pickle
        logger.info("Loading document store...")
        print("Loading document store...")
        self.docstore, self.index_to_id = self._load_docstore()
        
        logger.info(f"Loaded {self.metadata['num_documents']} documents")
        print(f"Loaded {self.metadata['num_documents']} documents")
        print("Ready for search!\n")
    
    @property
    def model(self):
        """Get BGE-M3 embedding model (lazy loaded via ModelManager)."""
        if self._model_manager:
            return self._model_manager.bge_m3
        return self._bge_m3
    
    @property
    def reranker(self):
        """Get BGE Reranker model (lazy loaded via ModelManager)."""
        if self._model_manager:
            return self._model_manager.bge_reranker
        return self._reranker
    
    def _load_docstore(self):
        """Load docstore and index mapping from pickle file."""
        pkl_file = self.faiss_dir / "index.pkl"
        if pkl_file.exists():
            with open(pkl_file, "rb") as f:
                docstore, index_to_id = pickle.load(f)
            return docstore, index_to_id
        return None, None
    
    def search(self, query, top_k=100):
        """Search for top_k similar documents."""
        # Generate embedding for query
        query_embedding = self.model.encode([query], 
                                           batch_size=1, 
                                           max_length=8192)['dense_vecs']
        
        # Search in FAISS
        distances, indices = self.index.search(query_embedding, top_k)
        
        # Prepare results
        results = []
        for idx, (distance, doc_idx) in enumerate(zip(distances[0], indices[0])):
            if doc_idx == -1:  # FAISS returns -1 for empty slots
                continue
            
            result = {
                'rank': idx + 1,
                'doc_idx': int(doc_idx),
                'distance': float(distance),
                'score': float(1 / (1 + distance))  # Convert distance to similarity score
            }
            
            # Get document from docstore
            if self.docstore and doc_idx in self.index_to_id:
                doc_id = self.index_to_id[doc_idx]
                doc = self.docstore.get(doc_id)
                if doc:
                    # Handle both dict and langchain Document formats
                    if isinstance(doc, dict):
                        result['filename'] = doc.get('filename', 'Unknown')
                        result['section'] = doc.get('section', 'N/A')
                        result['item_number'] = doc.get('item_number', 'N/A')
                        result['chunk_type'] = doc.get('chunk_type', 'N/A')
                        result['text'] = doc.get('text', '')
                        result['source'] = doc.get('filename', 'N/A')
                    else:
                        # Legacy langchain Document format
                        result['filename'] = doc.metadata.get('filename', 'Unknown')
                        result['section'] = doc.metadata.get('section', 'N/A')
                        result['item_number'] = doc.metadata.get('item_number', 'N/A')
                        result['chunk_type'] = doc.metadata.get('chunk_type', 'N/A')
                        result['text'] = doc.page_content
                        result['source'] = doc.metadata.get('source', 'N/A')
            else:
                result['filename'] = f"doc_{doc_idx}"
                result['text'] = ""
                result['section'] = 'N/A'
                result['item_number'] = 'N/A'
                result['chunk_type'] = 'N/A'
                result['source'] = 'N/A'
            
            results.append(result)
        
        return results
    
    def rerank(self, query, results, top_k=5):
        """Rerank results using BAAI/bge-reranker-v2-m3."""
        if not results:
            return []
        
        # Prepare query-document pairs for reranking
        pairs = [[query, r['text']] for r in results]
        
        # Compute reranking scores using bge-reranker-v2-m3
        scores = self.reranker.compute_score(pairs, batch_size=32)
        
        # Add rerank scores to results
        for result, score in zip(results, scores):
            result['rerank_score'] = float(score)
        
        # Sort by rerank score and return top_k
        reranked = sorted(results, key=lambda x: x['rerank_score'], reverse=True)
        return reranked[:top_k]
    
    def display_results(self, results):
        """Display search results in console."""
        print("\n" + "="*100)
        print(f"TOP {len(results)} RESULTS")
        print("="*100 + "\n")
        
        for i, result in enumerate(results, 1):
            print(f"🏆 Rank: {i}")
            print(f"📄 Filename: {result.get('filename', 'N/A')}")
            print(f"📍 Section: {result.get('section', 'N/A')} | Item: {result.get('item_number', 'N/A')}")
            print(f"🏷️  Chunk Type: {result.get('chunk_type', 'N/A')}")
            print(f"⭐ Rerank Score: {result.get('rerank_score', 0):.4f}")
            print(f"📊 Original Score: {result.get('score', 0):.4f}")
            print(f"\n📝 Content:")
            text = result.get('text', '')
            print(f"{text[:500]}{'...' if len(text) > 500 else ''}")
            print("\n" + "-" * 100 + "\n")


def main():
    """Main function for interactive search."""
    # Initialize searcher
    searcher = FAISSSearcher()
    
    print("=" * 80)
    print("FAISS SEARCH WITH BGE-M3")
    print("=" * 80)
    print("Type your query (or 'quit' to exit)\n")
    
    while True:
        # Get query from user
        query = input("Enter your search query: ").strip()
        
        if query.lower() in ['quit', 'exit', 'q']:
            print("Exiting...")
            break
        
        if not query:
            print("Please enter a valid query.\n")
            continue
        
        print(f"\nSearching for: '{query}'")
        
        # Step 1: Search top 100
        print("Retrieving top 100 results...")
        top_100 = searcher.search(query, top_k=400)
        print(f"Found {len(top_100)} results")
        
        # Step 2: Rerank to get top 3
        print("Reranking to get top 3...")
        top_5 = searcher.rerank(query, top_100, top_k=5)
        
        # Step 3: Display results
        searcher.display_results(top_5)


if __name__ == "__main__":
    main()
