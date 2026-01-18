"""Utility modules for RAG system.

Lazy imports to avoid loading dependencies until needed.
"""

from .input_validator import (
    InputValidator,
    ValidationConfig,
    get_validator,
    validate_question,
    validate_session_id
)

# Lazy import for DalekvodChecker (requires rapidfuzz)
def get_dalekovod_checker():
    """Lazy import for DalekvodChecker (requires rapidfuzz)."""
    from .dalekovod_checker import DalekvodChecker
    return DalekvodChecker

__all__ = [
    'InputValidator',
    'ValidationConfig',
    'get_validator',
    'validate_question',
    'validate_session_id',
    'get_dalekovod_checker',
]