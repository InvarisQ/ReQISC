"""Numerical validation helpers used by public data records."""

from __future__ import annotations

import math
from numbers import Real


def ensure_finite_real(value: Real, name: str) -> float:
    """Return *value* as a float if it is a finite real number.

    Booleans are rejected even though they are subclasses of ``int`` because
    accepting them would make configuration errors difficult to see.
    """

    if isinstance(value, bool) or not isinstance(value, Real):
        raise TypeError(f"{name} must be a finite real number")
    converted = float(value)
    if not math.isfinite(converted):
        raise ValueError(f"{name} must be finite")
    return converted


def ensure_nonnegative_float(value: Real, name: str) -> float:
    """Return *value* as a nonnegative finite float."""

    converted = ensure_finite_real(value, name)
    if converted < 0:
        raise ValueError(f"{name} must be nonnegative")
    return converted


def ensure_nonnegative_int(value: int, name: str) -> int:
    """Return *value* if it is a nonnegative integer."""

    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if value < 0:
        raise ValueError(f"{name} must be nonnegative")
    return value
