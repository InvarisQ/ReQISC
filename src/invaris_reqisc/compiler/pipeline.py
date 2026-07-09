"""Sequential compiler-pipeline scaffold."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Iterable

from invaris_reqisc.compiler.passes import CompilerPass, PassOutput


@dataclass(frozen=True)
class PipelineResult:
    """Result from running a compiler pipeline scaffold."""

    final_state: dict[str, Any]
    pass_outputs: tuple[PassOutput, ...] = field(default_factory=tuple)

    def as_dict(self) -> dict[str, Any]:
        """Return a serializable pipeline result."""

        return {
            "final_state": dict(self.final_state),
            "pass_outputs": [output.as_dict() for output in self.pass_outputs],
        }


@dataclass(frozen=True)
class Pipeline:
    """Apply compiler passes sequentially.

    The pipeline records state transitions and pass notes. It is designed as a
    stable integration surface for future synthesis and routing algorithms.
    """

    passes: tuple[CompilerPass, ...]

    def __init__(self, passes: Iterable[CompilerPass]) -> None:
        pass_tuple = tuple(passes)
        if any(not isinstance(pass_obj, CompilerPass) for pass_obj in pass_tuple):
            raise TypeError("all pipeline entries must implement CompilerPass")
        object.__setattr__(self, "passes", pass_tuple)

    def run(self, initial_state: dict[str, Any]) -> PipelineResult:
        """Run each pass on a copy of the current state."""

        state = dict(initial_state)
        outputs: list[PassOutput] = []
        for pass_obj in self.passes:
            result = pass_obj.run(state)
            outputs.append(result)
            state = dict(result.payload)
        return PipelineResult(final_state=state, pass_outputs=tuple(outputs))
