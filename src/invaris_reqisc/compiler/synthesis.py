"""Synthesis extension points."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SynthesisPlan:
    """Description of a proposed synthesis strategy."""

    name: str
    scope: str
    implemented: bool = False

    def require_implemented(self) -> None:
        """Raise when a plan is not implemented."""

        if not self.implemented:
            raise NotImplementedError(f"Synthesis plan '{self.name}' is not implemented")
