import pytest

from invaris_reqisc.hardware import CouplingHamiltonian, HardwareProfile


def test_coupling_hamiltonian_strength_and_normalized() -> None:
    coupling = CouplingHamiltonian(3.0, 4.0, 0.0)
    assert coupling.strength() == pytest.approx(5.0)
    assert coupling.normalized().as_tuple() == pytest.approx((0.6, 0.8, 0.0))


def test_zero_coupling_cannot_normalize() -> None:
    with pytest.raises(ValueError):
        CouplingHamiltonian(0.0, 0.0, 0.0).normalized()


def test_hardware_profile_summary_and_control_lookup() -> None:
    profile = HardwareProfile("xy", CouplingHamiltonian(1.0, 1.0, 0.0), ("rx", "rz"), "demo")
    assert profile.supports_control("rx")
    assert not profile.supports_control("ry")
    assert profile.summary()["name"] == "xy"
