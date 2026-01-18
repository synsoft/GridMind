#!/usr/bin/env python3
"""
Model Manager - Singleton management for ML models.
Ensures models are loaded only once and shared across the application.
"""

import logging
import threading
from typing import Optional
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class ModelConfig:
    """Configuration for model loading."""
    bge_m3_model: str = "BAAI/bge-m3"
    bge_reranker_model: str = "BAAI/bge-reranker-v2-m3"
    use_fp16: bool = True
    device: str = "cuda"  # or "cpu"


class ModelManager:
    """Singleton manager for ML models.
    
    Ensures expensive models like BGE-M3 and BGE Reranker are loaded
    only once and shared across all components.
    """
    
    _instance: Optional["ModelManager"] = None
    _lock = threading.Lock()
    
    def __new__(cls, *args, **kwargs):
        """Ensure only one instance exists."""
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance
    
    def __init__(self, config: ModelConfig = None):
        """Initialize model manager.
        
        Args:
            config: ModelConfig instance (only used on first init)
        """
        if self._initialized:
            return
            
        self.config = config or ModelConfig()
        self._bge_m3 = None
        self._bge_reranker = None
        self._models_lock = threading.Lock()
        self._initialized = True
        
        logger.info("ModelManager singleton initialized")
    
    @property
    def bge_m3(self):
        """Lazy-load and return BGE-M3 embedding model."""
        if self._bge_m3 is None:
            with self._models_lock:
                if self._bge_m3 is None:
                    logger.info(f"Loading BGE-M3 model: {self.config.bge_m3_model}")
                    try:
                        from FlagEmbedding import BGEM3FlagModel
                        self._bge_m3 = BGEM3FlagModel(
                            self.config.bge_m3_model, 
                            use_fp16=self.config.use_fp16
                        )
                        logger.info("✅ BGE-M3 model loaded successfully")
                    except Exception as e:
                        logger.error(f"❌ Failed to load BGE-M3: {e}")
                        raise
        return self._bge_m3
    
    @property
    def bge_reranker(self):
        """Lazy-load and return BGE Reranker model."""
        if self._bge_reranker is None:
            with self._models_lock:
                if self._bge_reranker is None:
                    logger.info(f"Loading BGE Reranker: {self.config.bge_reranker_model}")
                    try:
                        from FlagEmbedding import FlagReranker
                        self._bge_reranker = FlagReranker(
                            self.config.bge_reranker_model,
                            use_fp16=self.config.use_fp16
                        )
                        logger.info("✅ BGE Reranker loaded successfully")
                    except Exception as e:
                        logger.error(f"❌ Failed to load BGE Reranker: {e}")
                        raise
        return self._bge_reranker
    
    def preload_all(self):
        """Preload all models (useful at startup)."""
        logger.info("Preloading all models...")
        _ = self.bge_m3
        _ = self.bge_reranker
        logger.info("✅ All models preloaded")
    
    def is_loaded(self, model_name: str) -> bool:
        """Check if a specific model is loaded.
        
        Args:
            model_name: 'bge_m3' or 'bge_reranker'
            
        Returns:
            True if model is loaded
        """
        if model_name == "bge_m3":
            return self._bge_m3 is not None
        elif model_name == "bge_reranker":
            return self._bge_reranker is not None
        return False
    
    def get_status(self) -> dict:
        """Get status of all models."""
        return {
            "bge_m3": {
                "loaded": self._bge_m3 is not None,
                "model": self.config.bge_m3_model
            },
            "bge_reranker": {
                "loaded": self._bge_reranker is not None,
                "model": self.config.bge_reranker_model
            },
            "config": {
                "use_fp16": self.config.use_fp16,
                "device": self.config.device
            }
        }
    
    def unload(self, model_name: str = None):
        """Unload model(s) to free memory.
        
        Args:
            model_name: Specific model to unload, or None for all
        """
        with self._models_lock:
            if model_name is None or model_name == "bge_m3":
                if self._bge_m3 is not None:
                    del self._bge_m3
                    self._bge_m3 = None
                    logger.info("Unloaded BGE-M3 model")
                    
            if model_name is None or model_name == "bge_reranker":
                if self._bge_reranker is not None:
                    del self._bge_reranker
                    self._bge_reranker = None
                    logger.info("Unloaded BGE Reranker model")
        
        # Trigger garbage collection
        import gc
        gc.collect()
        
        try:
            import torch
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
                logger.info("Cleared CUDA cache")
        except ImportError:
            pass


# Convenience function for getting singleton
def get_model_manager(config: ModelConfig = None) -> ModelManager:
    """Get ModelManager singleton instance.
    
    Args:
        config: ModelConfig (only used on first call)
        
    Returns:
        ModelManager singleton
    """
    return ModelManager(config)


def get_reranker():
    """Convenience function to get BGE Reranker."""
    return get_model_manager().bge_reranker


def get_embedder():
    """Convenience function to get BGE-M3 embedder."""
    return get_model_manager().bge_m3
