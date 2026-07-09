import math

import pytest

from invaris_reqisc.gates import WeylCoordinate


def test_weyl_coordinate_helpers() -> None:
    coord = WeylCoordinate(0.3, 0.2, 0.1)
    assert coord.as_tuple() == (0.3, 0.2, 0.1)
    assert coord.norm_l1() == pytest.approx(0.6)
    assert coord.norm_l2() == pytest.approx(math.sqrt(0.14))
    assert coord.is_in_simple_canonical_region()


def test_weyl_coordinate_rejects_nonfinite() -> None:
    with pytest.raises(ValueError):
        WeylCoordinate(float("nan"), 0.0, 0.0)


def test_near_identity_threshold_validation() -> None:
    coord = WeylCoordinate(0.01, 0.0, 0.0)
    assert coord.is_near_identity(0.02)
    with pytest.raises(ValueError):
        coord.is_near_identity(-1.0)
