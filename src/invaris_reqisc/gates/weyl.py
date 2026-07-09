"""Weyl-coordinate representation for SU(4)-native two-qubit operations."""

from __future__ import annotations

import math
from dataclasses import dataclass
from numbers import Real

from invaris_reqisc.validation.invariants import validate_weyl_ordering
from invaris_reqisc.validation.numerical import ensure_finite_real, ensure_nonnegative_float


@dataclass(frozen=True)
class WeylCoordinate:
    """Three-coordinate scaffold for representing two-qubit operation classes.

    The class stores finite real coordinates and provides lightweight helpers
    used by examples, mirroring utilities, and benchmark scaffolds. It does not
    compute a KAK decomposition and does not claim to canonicalize arbitrary
    unitary matrices.
    """

    x: Real
    y: Real
    z: Real

    def __post_init__(self) -> None:
        object.__setattr__(self, "x", ensure_finite_real(self.x, "x"))
        object.__setattr__(self, "y", ensure_finite_real(self.y, "y"))
        object.__setattr__(self, "z", ensure_finite_real(self.z, "z"))

    def as_tuple(self) -> tuple[float, float, float]:
        """Return coordinates as ``(x, y, z)``."""

        return (float(self.x), float(self.y), float(self.z))

    def norm_l1(self) -> float:
        """Return the L1 norm of the coordinate tuple."""

        return abs(float(self.x)) + abs(float(self.y)) + abs(float(self.z))

    def norm_l2(self) -> float:
        """Return the Euclidean norm of the coordinate tuple."""

        return math.sqrt(float(self.x) ** 2 + float(self.y) ** 2 + float(self.z) ** 2)

    def is_near_identity(self, threshold: Real) -> bool:
        """Return whether the coordinate is near the identity by L2 norm."""

        checked_threshold = ensure_nonnegative_float(threshold, "threshold")
        return self.norm_l2() <= checked_threshold

    def is_in_simple_canonical_region(self) -> bool:
        """Return whether the tuple matches the project's simple Weyl ordering.

        This is a validation helper for examples and tests, not a complete
        canonical-region proof for every coordinate convention.
        """

        return validate_weyl_ordering(float(self.x), float(self.y), float(self.z))
