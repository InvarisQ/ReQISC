"""Small invariant checks for coordinate scaffolds."""

from __future__ import annotations

from invaris_reqisc.constants import CANONICAL_REGION_UPPER_BOUND


def validate_weyl_ordering(x: float, y: float, z: float) -> bool:
    """Return whether coordinates fit a simple closed Weyl-chamber scaffold.

    This helper is deliberately conservative and should not be interpreted as a
    full canonicalization algorithm. It checks the common ordering
    ``0 <= z <= y <= x <= 1/2`` used by project examples.
    """

    return 0.0 <= z <= y <= x <= CANONICAL_REGION_UPPER_BOUND
