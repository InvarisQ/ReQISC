"""Hardware profile records."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from invaris_reqisc.hardware.hamiltonian import CouplingHamiltonian


@dataclass(frozen=True)
class HardwareProfile:
    """Minimal hardware profile used by compiler and benchmark scaffolds."""

    name: str
    coupling: CouplingHamiltonian
    native_1q_controls: tuple[str, ...]
    notes: str = ""

    def __init__(
        self,
        name: str,
        coupling: CouplingHamiltonian,
        native_1q_controls: Iterable[str],
        notes: str = "",
    ) -> None:
        if not name or not name.strip():
            raise ValueError("name must be a non-empty string")
        if not isinstance(coupling, CouplingHamiltonian):
            raise TypeError("coupling must be a CouplingHamiltonian")
        controls = tuple(native_1q_controls)
        if any(not control or not isinstance(control, str) for control in controls):
            raise ValueError("native_1q_controls must contain non-empty strings")
        object.__setattr__(self, "name", name)
        object.__setattr__(self, "coupling", coupling)
        object.__setattr__(self, "native_1q_controls", controls)
        object.__setattr__(self, "notes", notes)

    def summary(self) -> dict[str, object]:
        """Return a JSON-serializable summary."""

        return {
            "name": self.name,
            "coupling": self.coupling.as_tuple(),
            "coupling_strength": self.coupling.strength(),
            "native_1q_controls": self.native_1q_controls,
            "notes": self.notes,
        }

    def supports_control(self, control_name: str) -> bool:
        """Return whether a one-qubit control appears in the profile."""

        return control_name in self.native_1q_controls
