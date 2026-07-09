"""OpenQASM extension placeholder."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class OpenQASMProgram:
    """Stores OpenQASM text for future adapter work."""

    source: str

    def __post_init__(self) -> None:
        if not self.source.strip():
            raise ValueError("source must not be empty")
