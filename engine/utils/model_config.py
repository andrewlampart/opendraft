#!/usr/bin/env python3
"""
ABOUTME: Model pricing data for token cost estimation
ABOUTME: Ported from OpenPaper — sync adaptation for OpenDraft
"""

from dataclasses import dataclass
from typing import Dict, Optional


@dataclass(frozen=True)
class ModelPricing:
    """Pricing per 1M tokens for a given model."""
    input_price: float   # USD per 1M input tokens
    output_price: float  # USD per 1M output tokens
    name: str = ""


# Pricing as of 2025 — update when new models are released
MODEL_PRICING: Dict[str, ModelPricing] = {
    # Gemini 3 family
    "gemini-3-pro-preview": ModelPricing(
        input_price=1.25,
        output_price=10.00,
        name="Gemini 3 Pro Preview",
    ),
    "gemini-3-flash-preview": ModelPricing(
        input_price=0.15,
        output_price=0.60,
        name="Gemini 3 Flash Preview",
    ),
    # Gemini 2.5 family
    "gemini-2.5-pro-preview-05-06": ModelPricing(
        input_price=1.25,
        output_price=10.00,
        name="Gemini 2.5 Pro Preview",
    ),
    "gemini-2.5-flash-preview-04-17": ModelPricing(
        input_price=0.15,
        output_price=0.60,
        name="Gemini 2.5 Flash Preview",
    ),
    # Gemini 2.0 family
    "gemini-2.0-flash": ModelPricing(
        input_price=0.10,
        output_price=0.40,
        name="Gemini 2.0 Flash",
    ),
    "gemini-2.0-flash-lite": ModelPricing(
        input_price=0.075,
        output_price=0.30,
        name="Gemini 2.0 Flash Lite",
    ),
    # Gemini 1.5 family (legacy)
    "gemini-1.5-pro": ModelPricing(
        input_price=1.25,
        output_price=5.00,
        name="Gemini 1.5 Pro",
    ),
    "gemini-1.5-flash": ModelPricing(
        input_price=0.075,
        output_price=0.30,
        name="Gemini 1.5 Flash",
    ),
}


def get_model_pricing(model_name: str) -> Optional[ModelPricing]:
    """
    Look up pricing for a model name.

    Supports partial matching: 'gemini-3-pro' matches 'gemini-3-pro-preview'.
    Returns None if no match found.
    """
    # Exact match first
    if model_name in MODEL_PRICING:
        return MODEL_PRICING[model_name]

    # Partial / prefix match
    for key, pricing in MODEL_PRICING.items():
        if key.startswith(model_name) or model_name.startswith(key):
            return pricing

    return None
