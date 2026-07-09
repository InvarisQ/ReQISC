"""Small JSON-schema helpers for manifests."""

from __future__ import annotations

from typing import Any


def minimal_benchmark_manifest_schema() -> dict[str, Any]:
    """Return a minimal JSON-schema-like benchmark manifest description."""

    return {
        "type": "object",
        "required": ["name", "version", "workload", "hardware_profile", "metrics"],
        "properties": {
            "name": {"type": "string"},
            "version": {"type": "string"},
            "workload": {"type": "object"},
            "hardware_profile": {"type": "object"},
            "metrics": {"type": "array", "items": {"type": "string"}},
        },
    }
