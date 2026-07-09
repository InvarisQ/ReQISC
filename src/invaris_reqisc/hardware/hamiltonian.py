"""Coupling Hamiltonian records."""

from __future__ import annotations

import math
from dataclasses import dataclass
from numbers import Real

from invaris_reqisc.validation.numerical import ensure_finite_real


@dataclass(frozen=True)
class CouplingHamiltonian:
    """Simple ``XX``, ``YY``, and ``ZZ`` coupling-strength record.

    The record stores normalized abstractions used by hardware-profile examples.
    It does not represent a calibrated device Hamiltonian.
    """

    xx: Real
    yy: Real
    zz: Real

    def __post_init__(self) -> None:
        object.__setattr__(self, "xx", ensure_finite_real(self.xx, "xx"))
        object.__setattr__(self, "yy", ensure_finite_real(self.yy, "yy"))
        object.__setattr__(self, "zz", ensure_finite_real(self.zz, "zz"))

    def strength(self) -> float:
        """Return Euclidean coupling strength."""

        return math.sqrt(float(self.xx) ** 2 + float(self.yy) ** 2 + float(self.zz) ** 2)

    def as_tuple(self) -> tuple[float, float, float]:
        """Return ``(xx, yy, zz)``."""

        return (float(self.xx), float(self.yy), float(self.zz))

    def normalized(self) -> "CouplingHamiltonian":
        """Return a unit-strength coupling profile.

        A zero-strength profile cannot be normalized because its direction is
        undefined.
        """

        magnitude = self.strength()
        if magnitude == 0.0:
            raise ValueError("cannot normalize a zero-strength coupling")
        return CouplingHamiltonian(
            float(self.xx) / magnitude,
            float(self.yy) / magnitude,
            float(self.zz) / magnitude,
        )
