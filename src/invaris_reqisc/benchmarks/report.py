"""Benchmark report records."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from invaris_reqisc.benchmarks.metrics import BenchmarkMetrics


@dataclass(frozen=True)
class BenchmarkReport:
    """Report container that distinguishes metrics from evidence notes."""

    manifest_name: str
    metrics: BenchmarkMetrics | None = None
    reproducibility: dict[str, Any] = field(default_factory=dict)
    notes: tuple[str, ...] = field(default_factory=tuple)

    def as_dict(self) -> dict[str, Any]:
        """Return a serializable report."""

        return {
            "manifest_name": self.manifest_name,
            "metrics": None if self.metrics is None else self.metrics.as_dict(),
            "reproducibility": dict(self.reproducibility),
            "notes": list(self.notes),
        }
