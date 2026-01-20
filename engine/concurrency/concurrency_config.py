#!/usr/bin/env python3
"""
ABOUTME: Concurrency configuration for OpenDraft
ABOUTME: Manages rate limits, batch sizes, and parallel workers
"""

import os
from dataclasses import dataclass
from typing import Optional

@dataclass
class ConcurrencyConfig:
    """Configuration for concurrent operations and rate limiting."""

    # Rate limiting
    rate_limit_delay: float = 0.5  # Delay between API calls in seconds

    # Scout (citation research) settings
    scout_batch_size: int = 10  # Number of topics per batch
    scout_batch_delay: float = 1.0  # Delay between batches
    scout_parallel_workers: int = 4  # Number of parallel workers

    @classmethod
    def from_env(cls) -> 'ConcurrencyConfig':
        """Create configuration from environment variables."""
        return cls(
            rate_limit_delay=float(os.getenv('RATE_LIMIT_DELAY', '0.5')),
            scout_batch_size=int(os.getenv('SCOUT_BATCH_SIZE', '10')),
            scout_batch_delay=float(os.getenv('SCOUT_BATCH_DELAY', '1.0')),
            scout_parallel_workers=int(os.getenv('SCOUT_PARALLEL_WORKERS', '4')),
        )


# Global config instance
_config: Optional[ConcurrencyConfig] = None


def get_concurrency_config(verbose: bool = True) -> ConcurrencyConfig:
    """
    Get the concurrency configuration (lazy loaded from environment).

    Args:
        verbose: Whether to print configuration info (default: True)

    Returns:
        ConcurrencyConfig instance
    """
    global _config
    if _config is None:
        _config = ConcurrencyConfig.from_env()
        if verbose:
            print(f"⚙️  Concurrency config: {_config.scout_parallel_workers} workers, "
                  f"{_config.scout_batch_size} batch size, {_config.rate_limit_delay}s delay")
    return _config
