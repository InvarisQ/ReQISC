"""Benchmark metric records."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from invaris_reqisc.validation.numerical import ensure_nonnegative_float, ensure_nonnegative_int


@dataclass(frozen=True)
class BenchmarkMetrics:
    """Small metric record for benchmark scaffolds."""

    two_qubit_gate_count: int
    depth_2q: int
    pulse_duration_estimate: float
    distinct_su4_count: int

    def __post_init__(self) -> None:
        self.validate_nonnegative()

    def validate_nonnegative(self) -> None:
        """Validate that all metric fields are nonnegative."""

        ensure_nonnegative_int(self.two_qubit_gate_count, "two_qubit_gate_count")
        ensure_nonnegative_int(self.depth_2q, "depth_2q")
        ensure_nonnegative_float(self.pulse_duration_estimate, "pulse_duration_estimate")
        ensure_nonnegative_int(self.distinct_su4_count, "distinct_su4_count")

    def as_dict(self) -> dict[str, Any]:
        """Return a serializable metrics dictionary."""

        return {
            "two_qubit_gate_count": self.two_qubit_gate_count,
            "depth_2q": self.depth_2q,
            "pulse_duration_estimate": self.pulse_duration_estimate,
            "distinct_su4_count": self.distinct_su4_count,
        }


def compare_metrics(
    baseline: BenchmarkMetrics | None,
    candidate: BenchmarkMetrics | None,
) -> dict[str, float] | None:
    """Return candidate-minus-baseline deltas when both records exist."""

    if baseline is None or candidate is None:
        return None
    return {
        "two_qubit_gate_count_delta": float(
            candidate.two_qubit_gate_count - baseline.two_qubit_gate_count
        ),
        "depth_2q_delta": float(candidate.depth_2q - baseline.depth_2q),
        "pulse_duration_estimate_delta": float(
            candidate.pulse_duration_estimate - baseline.pulse_duration_estimate
        ),
        "distinct_su4_count_delta": float(candidate.distinct_su4_count - baseline.distinct_su4_count),
    }
