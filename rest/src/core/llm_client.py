#!/usr/bin/env python3
"""
LLM Client - Unified interface for Ollama and OpenAI-compatible APIs.
Eliminates code duplication across the codebase.
"""

import json
import logging
import requests
from typing import Dict, List, Optional, Generator, Any
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class LLMConfig:
    """Configuration for LLM client."""
    provider: str = "ollama"  # "ollama" or "openai"
    url: str = "http://localhost:11434/api/chat"
    model: str = "gemma3:27b"
    small_model: str = "gemma3:4b"
    temperature: float = 0.3
    small_temperature: float = 0.1
    timeout: int = 120
    max_retries: int = 2
    
    @classmethod
    def from_config(cls, cfg: Dict) -> "LLMConfig":
        """Create LLMConfig from config dictionary."""
        llm_cfg = cfg.get("llm", {})
        provider = llm_cfg.get("provider", "ollama")
        
        if provider == "openai":
            host = llm_cfg.get("openai_host", "192.168.30.61")
            port = llm_cfg.get("openai_port", 8080)
            url = f"http://{host}:{port}/v1/chat/completions"
        else:
            host = llm_cfg.get("ollama_host", "192.168.30.61")
            port = llm_cfg.get("ollama_port", 11434)
            url = f"http://{host}:{port}/api/chat"
        
        return cls(
            provider=provider,
            url=url,
            model=llm_cfg.get("model", "gemma3:27b"),
            small_model=llm_cfg.get("small_model", "gemma3:4b"),
            temperature=llm_cfg.get("temperature", 0.3),
            small_temperature=llm_cfg.get("small_temperature", 0.1),
            timeout=llm_cfg.get("timeout", 120),
            max_retries=llm_cfg.get("max_retries", 2)
        )


class LLMClient:
    """Unified LLM client for Ollama and OpenAI-compatible APIs."""
    
    def __init__(self, config: LLMConfig):
        """Initialize LLM client.
        
        Args:
            config: LLMConfig instance
        """
        self.config = config
        logger.info(f"LLM Client initialized: provider={config.provider}, model={config.model}")
    
    def _build_payload(self, messages: List[Dict], model: str = None, 
                       temperature: float = None, stream: bool = False) -> Dict:
        """Build request payload based on provider."""
        model = model or self.config.model
        temperature = temperature if temperature is not None else self.config.temperature
        
        if self.config.provider == "openai":
            return {
                "model": model,
                "messages": messages,
                "stream": stream,
                "temperature": temperature
            }
        else:
            return {
                "model": model,
                "messages": messages,
                "stream": stream,
                "options": {"temperature": temperature}
            }
    
    def _parse_response(self, response_json: Dict) -> str:
        """Parse response content based on provider format."""
        if self.config.provider == "openai":
            return response_json["choices"][0]["message"]["content"]
        else:
            return response_json["message"]["content"]
    
    def chat(self, messages: List[Dict], model: str = None, 
             temperature: float = None, timeout: int = None) -> Optional[str]:
        """Send chat request and get response.
        
        Args:
            messages: List of message dicts with 'role' and 'content'
            model: Model to use (defaults to config.model)
            temperature: Temperature for generation
            timeout: Request timeout in seconds
            
        Returns:
            Response content string or None on error
        """
        payload = self._build_payload(messages, model, temperature, stream=False)
        timeout = timeout or self.config.timeout
        
        for attempt in range(self.config.max_retries + 1):
            try:
                response = requests.post(
                    self.config.url,
                    json=payload,
                    timeout=timeout
                )
                response.raise_for_status()
                return self._parse_response(response.json())
                
            except requests.exceptions.Timeout:
                logger.warning(f"LLM request timeout (attempt {attempt + 1}/{self.config.max_retries + 1})")
                if attempt == self.config.max_retries:
                    logger.error("LLM request failed after all retries (timeout)")
                    return None
                    
            except requests.exceptions.RequestException as e:
                logger.error(f"LLM request error: {e}")
                if attempt == self.config.max_retries:
                    return None
                    
            except (KeyError, IndexError) as e:
                logger.error(f"Error parsing LLM response: {e}")
                return None
        
        return None
    
    def chat_small(self, messages: List[Dict], timeout: int = 15) -> Optional[str]:
        """Send chat request using small model (for classification, etc.).
        
        Args:
            messages: List of message dicts
            timeout: Request timeout (default 15s for small model)
            
        Returns:
            Response content string or None on error
        """
        return self.chat(
            messages, 
            model=self.config.small_model,
            temperature=self.config.small_temperature,
            timeout=timeout
        )
    
    def chat_stream(self, messages: List[Dict], model: str = None,
                    temperature: float = None) -> Generator[str, None, None]:
        """Stream chat response token by token.
        
        Args:
            messages: List of message dicts
            model: Model to use
            temperature: Temperature for generation
            
        Yields:
            Response tokens as they arrive
        """
        payload = self._build_payload(messages, model, temperature, stream=True)
        
        try:
            response = requests.post(
                self.config.url,
                json=payload,
                stream=True,
                timeout=self.config.timeout
            )
            response.raise_for_status()
            
            for line in response.iter_lines():
                if not line:
                    continue
                    
                try:
                    if self.config.provider == "openai":
                        # OpenAI format: data: {json}
                        line_str = line.decode('utf-8')
                        if line_str.startswith('data: '):
                            data_str = line_str[6:]
                            if data_str.strip() == '[DONE]':
                                break
                            chunk = json.loads(data_str)
                            token = chunk.get("choices", [{}])[0].get("delta", {}).get("content", "")
                    else:
                        # Ollama format
                        chunk = json.loads(line)
                        token = chunk.get("message", {}).get("content", "")
                        
                        if chunk.get("done", False):
                            break
                    
                    if token:
                        yield token
                        
                except json.JSONDecodeError:
                    continue
                    
        except requests.exceptions.RequestException as e:
            logger.error(f"Streaming error: {e}")
            yield ""
    
    def classify(self, prompt: str, options: List[str], default: str = None) -> str:
        """Use small model to classify input into one of the options.
        
        Args:
            prompt: Classification prompt
            options: List of valid options (e.g., ["NEW", "FOLLOWUP"])
            default: Default option if classification fails
            
        Returns:
            One of the options or default
        """
        messages = [{"role": "user", "content": prompt}]
        response = self.chat_small(messages)
        
        if response:
            response_upper = response.strip().upper()
            for option in options:
                if option.upper() in response_upper:
                    return option
        
        logger.warning(f"Classification unclear, using default: {default}")
        return default or options[0]
    
    def generate_title(self, content: str, max_words: int = 10) -> str:
        """Generate a short title for content using small model.
        
        Args:
            content: Content to generate title for
            max_words: Maximum words in title
            
        Returns:
            Generated title
        """
        prompt = f"""Kreiraj **kratak i precizan naslov** (maksimalno {max_words} reči) za sledeći stručni tekst.

Tekst:
{content[:500]}

Naslov treba da:
- Bude na srpskom jeziku
- Sadrži ključne tehničke termine
- NE sadrži znakove navoda

Odgovori SAMO sa naslovom, bez dodatnog teksta."""

        messages = [{"role": "user", "content": prompt}]
        title = self.chat_small(messages)
        
        if title:
            # Clean up title
            title = title.strip('"\'\'').strip()
            if len(title) > 100:
                title = title[:97] + '...'
            return title
        
        # Fallback: simple truncation
        import re
        clean_content = re.sub(r'[^\w\s\u0400-\u04FF]', ' ', content)
        words = clean_content.split()[:8]
        return ' '.join(words) or 'Stored Knowledge Entry'


# Singleton instance holder
_llm_client_instance: Optional[LLMClient] = None


def get_llm_client(config: LLMConfig = None) -> LLMClient:
    """Get or create singleton LLM client instance.
    
    Args:
        config: LLMConfig (required on first call)
        
    Returns:
        LLMClient singleton instance
    """
    global _llm_client_instance
    
    if _llm_client_instance is None:
        if config is None:
            raise ValueError("Config required for first LLM client initialization")
        _llm_client_instance = LLMClient(config)
    
    return _llm_client_instance


def reset_llm_client():
    """Reset singleton instance (useful for testing)."""
    global _llm_client_instance
    _llm_client_instance = None
