from invaris_reqisc.gates import (
    SU4GateRecord,
    WeylCoordinate,
    mirror_weyl_coordinate,
    mirrored_gate_record,
    should_mirror,
)


def test_mirror_coordinate() -> None:
    coord = WeylCoordinate(0.1, -0.2, 0.3)
    assert mirror_weyl_coordinate(coord).as_tuple() == (-0.1, 0.2, -0.3)


def test_should_mirror_near_identity() -> None:
    assert should_mirror(WeylCoordinate(0.01, 0.0, 0.0), 0.05)


def test_mirrored_gate_record_updates_metadata() -> None:
    gate = SU4GateRecord("g", WeylCoordinate(0.01, 0.0, 0.0), {"a": 1})
    mirrored = mirrored_gate_record(gate, 0.05)
    assert mirrored.name == "g.mirrored"
    assert mirrored.metadata["mirroring_scaffold_applied"] is True
    assert mirrored.metadata["original_weyl_coordinate"] == (0.01, 0.0, 0.0)
