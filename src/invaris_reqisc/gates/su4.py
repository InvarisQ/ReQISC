"""SU(4)-native gate records."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from invaris_reqisc.gates.weyl import WeylCoordinate
from invaris_reqisc.validation.numerical import ensure_nonnegative_float


@dataclass(frozen=True)
class SU4GateRecord:
    """Record for an SU(4)-native two-qubit operation scaffold.

    The record combines a name, a Weyl-coordinate abstraction, and arbitrary
    metadata. It is meant for structured workflow data, not for storing full
    unitary matrices or calibrated pulse definitions.
    """

    name: str
    weyl_coordinate: WeylCoordinate
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.name or not self.name.strip():
            raise ValueError("name must be a non-empty string")
        if not isinstance(self.weyl_coordinate, WeylCoordinate):
            raise TypeError("weyl_coordinate must be a WeylCoordinate")
        if not isinstance(self.metadata, dict):
            raise TypeError("metadata must be a dictionary")

    def is_near_identity(self, threshold: float) -> bool:
        """Return whether the gate coordinate is near the identity."""

        checked_threshold = ensure_nonnegative_float(threshold, "threshold")
        return self.weyl_coordinate.is_near_identity(checked_threshold)

    def as_dict(self) -> dict[str, Any]:
        """Return a JSON-serializable representation."""

        return {
            "name": self.name,
            "weyl_coordinate": self.weyl_coordinate.as_tuple(),
            "metadata": dict(self.metadata),
        }
