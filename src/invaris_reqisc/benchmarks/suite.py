"""Benchmark manifest loading."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_manifest(path: str | Path) -> dict[str, Any]:
    """Load a benchmark manifest from JSON or YAML.

    JSON is always supported. YAML is supported when PyYAML is installed. The
    loader returns the parsed mapping and performs only minimal shape checks.
    """

    manifest_path = Path(path)
    if not manifest_path.exists():
        raise FileNotFoundError(manifest_path)
    suffix = manifest_path.suffix.lower()
    text = manifest_path.read_text(encoding="utf-8")
    if suffix == ".json":
        data = json.loads(text)
    elif suffix in {".yml", ".yaml"}:
        try:
            import yaml  # type: ignore[import-untyped]
        except Exception as exc:  # pragma: no cover - depends on optional package
            raise RuntimeError("YAML manifests require the optional 'yaml' extra") from exc
        data = yaml.safe_load(text)
    else:
        raise ValueError("manifest path must end in .json, .yml, or .yaml")
    if not isinstance(data, dict):
        raise ValueError("manifest root must be a mapping")
    return data
