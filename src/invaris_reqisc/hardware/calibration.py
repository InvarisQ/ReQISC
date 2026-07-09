"""Calibration-aware modeling placeholders."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class CalibrationAssumption:
    """Named calibration assumption for benchmark manifests and reports."""

    name: str
    value: Any
    source: str = "unvalidated-assumption"
    notes: str = ""

    def as_dict(self) -> dict[str, Any]:
        """Return a JSON-serializable dictionary."""

        return {
            "name": self.name,
            "value": self.value,
            "source": self.source,
            "notes": self.notes,
        }


@dataclass(frozen=True)
class CalibrationModel:
    """Container for calibration assumptions.

    This is a metadata scaffold, not a fitted hardware calibration model.
    """

    assumptions: tuple[CalibrationAssumption, ...] = field(default_factory=tuple)

    def as_dict(self) -> dict[str, list[dict[str, Any]]]:
        """Return assumptions in serializable form."""

        return {"assumptions": [assumption.as_dict() for assumption in self.assumptions]}
