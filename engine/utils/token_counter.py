#!/usr/bin/env python3
"""
ABOUTME: Provider-specific token counting utilities
ABOUTME: Ported from OpenPaper — Gemini native / tiktoken / fallback
"""

import logging
from typing import Optional

logger = logging.getLogger(__name__)


def count_tokens_gemini(text: str, model_name: str = "gemini-3-pro-preview") -> Optional[int]:
    """
    Count tokens using Gemini's native count_tokens API.

    Returns None if the API call fails (e.g., not configured).
    """
    try:
        import google.generativeai as genai
        model = genai.GenerativeModel(model_name)
        result = model.count_tokens(text)
        return result.total_tokens
    except Exception as e:
        logger.debug(f"Gemini token counting failed: {e}")
        return None


def count_tokens_tiktoken(text: str, encoding_name: str = "cl100k_base") -> Optional[int]:
    """
    Count tokens using tiktoken (OpenAI tokenizer).

    Works as a reasonable approximation for Gemini models.
    Returns None if tiktoken is not installed.
    """
    try:
        import tiktoken
        enc = tiktoken.get_encoding(encoding_name)
        return len(enc.encode(text))
    except ImportError:
        logger.debug("tiktoken not installed — skipping tiktoken counting")
        return None
    except Exception as e:
        logger.debug(f"tiktoken counting failed: {e}")
        return None


def count_tokens_fallback(text: str) -> int:
    """
    Rough fallback: ~4 characters per token (GPT/Gemini average).

    Always succeeds.
    """
    return max(1, len(text) // 4)


def count_tokens(text: str, model_name: str = "gemini-3-pro-preview") -> int:
    """
    Count tokens using best available method.

    Priority: Gemini native -> tiktoken -> character fallback.
    """
    # Try Gemini native
    result = count_tokens_gemini(text, model_name)
    if result is not None:
        return result

    # Try tiktoken
    result = count_tokens_tiktoken(text)
    if result is not None:
        return result

    # Fallback
    return count_tokens_fallback(text)
