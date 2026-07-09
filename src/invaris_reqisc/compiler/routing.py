"""Routing extension points."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RoutingPlan:
    """Description of a future SU(4)-aware routing strategy."""

    name: str
    coupling_constraints: tuple[str, ...]
    implemented: bool = False
