"""Canonical-coordinate extension points.

This module intentionally avoids claiming a full canonical decomposition. It
contains small helpers that make current limitations explicit while preserving a
stable place for future KAK/Weyl-region work.
"""

from __future__ import annotations

from invaris_reqisc.gates.weyl import WeylCoordinate


def is_simple_canonical_coordinate(coord: WeylCoordinate) -> bool:
    """Return whether *coord* satisfies the package's simple ordering check."""

    return coord.is_in_simple_canonical_region()
