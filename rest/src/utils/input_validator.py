#!/usr/bin/env python3
"""
Input Validator - Validation and sanitization for user inputs.
Provides security and data integrity checks.
"""

import re
import logging
from typing import Optional, Tuple
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class ValidationConfig:
    """Configuration for input validation."""
    max_question_length: int = 4000
    min_question_length: int = 2
    max_session_id_length: int = 128
    max_stored_knowledge_length: int = 10000
    allowed_commands: Tuple[str, ...] = ("/store", "/recall", "/help", "/history", "/reset")
    

class InputValidator:
    """Validates and sanitizes user inputs."""
    
    def __init__(self, config: ValidationConfig = None):
        """Initialize validator.
        
        Args:
            config: ValidationConfig instance
        """
        self.config = config or ValidationConfig()
        
        # Patterns for detecting potential issues
        self._sql_injection_pattern = re.compile(
            r"(\b(SELECT|INSERT|UPDATE|DELETE|DROP|UNION|ALTER|CREATE|TRUNCATE)\b)",
            re.IGNORECASE
        )
        self._script_pattern = re.compile(
            r"<\s*script[^>]*>|javascript\s*:|on\w+\s*=",
            re.IGNORECASE
        )
    
    def validate_question(self, question: str) -> Tuple[bool, str, Optional[str]]:
        """Validate user question.
        
        Args:
            question: User's question text
            
        Returns:
            Tuple of (is_valid, sanitized_question, error_message)
        """
        if not question:
            return False, "", "Pitanje ne može biti prazno"
        
        # Strip whitespace
        question = question.strip()
        
        # Check length
        if len(question) < self.config.min_question_length:
            return False, question, f"Pitanje je prekratko (min {self.config.min_question_length} karaktera)"
        
        if len(question) > self.config.max_question_length:
            logger.warning(f"Question truncated from {len(question)} to {self.config.max_question_length} chars")
            question = question[:self.config.max_question_length]
        
        # Check for potential script injection (just log, don't block)
        if self._script_pattern.search(question):
            logger.warning(f"Potential script injection detected in question")
        
        return True, question, None
    
    def validate_session_id(self, session_id: str) -> Tuple[bool, str, Optional[str]]:
        """Validate session ID.
        
        Args:
            session_id: Session identifier
            
        Returns:
            Tuple of (is_valid, sanitized_id, error_message)
        """
        if not session_id:
            return True, "", None  # Empty session ID is allowed
        
        # Strip and limit length
        session_id = session_id.strip()
        
        if len(session_id) > self.config.max_session_id_length:
            session_id = session_id[:self.config.max_session_id_length]
        
        # Allow only alphanumeric, hyphen, underscore
        sanitized = re.sub(r'[^a-zA-Z0-9_\-]', '', session_id)
        
        if sanitized != session_id:
            logger.warning(f"Session ID sanitized: '{session_id[:20]}...' -> '{sanitized[:20]}...'")
        
        return True, sanitized, None
    
    def validate_stored_knowledge(self, content: str) -> Tuple[bool, str, Optional[str]]:
        """Validate content for stored knowledge.
        
        Args:
            content: Knowledge content to store
            
        Returns:
            Tuple of (is_valid, sanitized_content, error_message)
        """
        if not content:
            return False, "", "Sadržaj ne može biti prazan"
        
        content = content.strip()
        
        if len(content) < 10:
            return False, content, "Sadržaj je prekratak (min 10 karaktera)"
        
        if len(content) > self.config.max_stored_knowledge_length:
            logger.warning(f"Stored knowledge truncated from {len(content)} to {self.config.max_stored_knowledge_length}")
            content = content[:self.config.max_stored_knowledge_length]
        
        return True, content, None
    
    def extract_command(self, message: str) -> Tuple[Optional[str], str]:
        """Extract command from message if present.
        
        Args:
            message: User message
            
        Returns:
            Tuple of (command, remaining_message)
            command is None if no valid command found
        """
        message = message.strip()
        
        for cmd in self.config.allowed_commands:
            if message.lower().startswith(cmd):
                remaining = message[len(cmd):].strip()
                return cmd, remaining
        
        return None, message
    
    def sanitize_for_logging(self, text: str, max_length: int = 200) -> str:
        """Sanitize text for safe logging.
        
        Args:
            text: Text to sanitize
            max_length: Maximum length for log output
            
        Returns:
            Sanitized text safe for logging
        """
        if not text:
            return ""
        
        # Remove potential log injection characters
        sanitized = text.replace('\n', ' ').replace('\r', ' ')
        
        # Truncate
        if len(sanitized) > max_length:
            sanitized = sanitized[:max_length] + "..."
        
        return sanitized


# Singleton instance
_validator_instance: Optional[InputValidator] = None


def get_validator(config: ValidationConfig = None) -> InputValidator:
    """Get or create singleton validator instance."""
    global _validator_instance
    
    if _validator_instance is None:
        _validator_instance = InputValidator(config)
    
    return _validator_instance


def validate_question(question: str) -> Tuple[bool, str, Optional[str]]:
    """Convenience function for question validation."""
    return get_validator().validate_question(question)


def validate_session_id(session_id: str) -> Tuple[bool, str, Optional[str]]:
    """Convenience function for session ID validation."""
    return get_validator().validate_session_id(session_id)
