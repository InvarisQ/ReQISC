"""Gate-mirroring utilities for near-identity coordinate scaffolds."""

from __future__ import annotations

from dataclasses import replace
from numbers import Real

from invaris_reqisc.gates.su4 import SU4GateRecord
from invaris_reqisc.gates.weyl import WeylCoordinate
from invaris_reqisc.validation.numerical import ensure_nonnegative_float


def should_mirror(coord: WeylCoordinate, threshold: Real) -> bool:
    """Return whether a coordinate should be considered for mirroring.

    This scaffold treats near-identity coordinates as candidates. A complete
    hardware compiler would also update mappings, schedules, calibration costs,
    and native operation choices.
    """

    checked_threshold = ensure_nonnegative_float(threshold, "threshold")
    return coord.is_near_identity(checked_threshold)


def mirror_weyl_coordinate(coord: WeylCoordinate) -> WeylCoordinate:
    """Return a simple mirrored coordinate scaffold.

    The transformation negates the coordinate tuple. This is a local coordinate
    transformation placeholder for testing pass plumbing and metadata handling;
    it is not a full hardware-aware mirroring algorithm.
    """

    return WeylCoordinate(-float(coord.x), -float(coord.y), -float(coord.z))


def mirrored_gate_record(gate: SU4GateRecord, threshold: Real) -> SU4GateRecord:
    """Return a gate record with mirrored coordinates when the threshold matches.

    Metadata records whether the scaffold changed the coordinate. Full mapping
    updates, pulse changes, and routing interactions are future compiler work.
    """

    mirrored = should_mirror(gate.weyl_coordinate, threshold)
    metadata = dict(gate.metadata)
    metadata["mirroring_scaffold_applied"] = mirrored
    if not mirrored:
        return replace(gate, metadata=metadata)
    metadata["original_weyl_coordinate"] = gate.weyl_coordinate.as_tuple()
    return SU4GateRecord(
        name=f"{gate.name}.mirrored",
        weyl_coordinate=mirror_weyl_coordinate(gate.weyl_coordinate),
        metadata=metadata,
    )
