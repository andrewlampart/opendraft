"""
Opcjonalny zapis zużycia tokenów LLM (callback przez contextvar).
Używane z Celery/Django — gdy brak sinka, wywołania są no-op (CLI, testy).
"""

from __future__ import annotations

import logging
from contextvars import ContextVar
from typing import Any, Callable, Dict, Optional

logger = logging.getLogger(__name__)

Sink = Callable[[Dict[str, Any]], None]

_llm_usage_sink: ContextVar[Optional[Sink]] = ContextVar(
    "opendraft_llm_usage_sink", default=None
)


def set_llm_usage_sink(sink: Optional[Sink]):
    """Zwraca token do reset_llm_usage_sink."""
    return _llm_usage_sink.set(sink)


def reset_llm_usage_sink(token) -> None:
    _llm_usage_sink.reset(token)


def _safe_int(val) -> Optional[int]:
    if isinstance(val, int) and not isinstance(val, bool) and val >= 0:
        return val
    return None


def _emit_tokens(
    model_name: str,
    component: str,
    prompt_tokens: Optional[int],
    candidates_tokens: Optional[int],
    total_tokens: Optional[int],
) -> None:
    fn = _llm_usage_sink.get()
    if not fn:
        return
    try:
        fn(
            {
                "model_name": (model_name or "")[:128],
                "component": (component or "")[:64],
                "prompt_tokens": prompt_tokens,
                "candidates_tokens": candidates_tokens,
                "total_tokens": total_tokens,
            }
        )
    except Exception:
        logger.exception("LLM usage sink failed (component=%s)", component)


def emit_llm_usage_sdk(
    model_name: str, response: Any, component: str = ""
) -> None:
    """Odpowiedź google.genai / GroqResponse z atrybutem usage_metadata."""
    pt = ct = tt = None
    um = getattr(response, "usage_metadata", None)
    if um is not None:
        pt = _safe_int(getattr(um, "prompt_token_count", None))
        ct = _safe_int(getattr(um, "candidates_token_count", None))
        tt = _safe_int(getattr(um, "total_token_count", None))
    _emit_tokens(model_name, component, pt, ct, tt)


def emit_llm_usage_rest(
    model_name: str, data: Dict[str, Any], component: str = ""
) -> None:
    """Odpowiedź REST generateContent (JSON) — usageMetadata w camelCase."""
    um = data.get("usageMetadata") or {}
    pt = _safe_int(um.get("promptTokenCount"))
    ct = _safe_int(um.get("candidatesTokenCount"))
    tt = _safe_int(um.get("totalTokenCount"))
    _emit_tokens(model_name, component, pt, ct, tt)
