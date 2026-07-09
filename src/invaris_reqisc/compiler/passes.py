"""Compiler-pass interfaces and placeholder passes."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class PassOutput:
    """Structured output emitted by a compiler pass scaffold."""

    pass_name: str
    payload: dict[str, Any]
    notes: tuple[str, ...] = field(default_factory=tuple)

    def as_dict(self) -> dict[str, Any]:
        """Return a serializable pass output."""

        return {
            "pass_name": self.pass_name,
            "payload": dict(self.payload),
            "notes": list(self.notes),
        }


class CompilerPass(ABC):
    """Base interface for compiler workflow passes."""

    name: str

    @abstractmethod
    def run(self, state: dict[str, Any]) -> PassOutput:
        """Run the pass and return a structured output."""


class ProgramAwareTemplatePass(CompilerPass):
    """Placeholder for program-aware template synthesis.

    The pass records that template synthesis would inspect program structure. It
    does not perform optimization or template replacement yet.
    """

    name = "program-aware-template"

    def run(self, state: dict[str, Any]) -> PassOutput:
        output = dict(state)
        output.setdefault("template_candidates", [])
        output["program_aware_template_scaffold"] = True
        return PassOutput(
            self.name,
            output,
            ("Template synthesis interface only; no optimization performed.",),
        )


class HierarchicalSynthesisPass(CompilerPass):
    """Placeholder for program-agnostic hierarchical synthesis."""

    name = "hierarchical-synthesis"

    def run(self, state: dict[str, Any]) -> PassOutput:
        output = dict(state)
        output["hierarchical_synthesis_scaffold"] = True
        return PassOutput(
            self.name,
            output,
            ("Hierarchical synthesis scaffold only; no KAK solver is implemented.",),
        )


class SU4AwareRoutingPass(CompilerPass):
    """Placeholder for SU(4)-aware routing and mapping."""

    name = "su4-aware-routing"

    def run(self, state: dict[str, Any]) -> PassOutput:
        output = dict(state)
        output["su4_aware_routing_scaffold"] = True
        return PassOutput(
            self.name,
            output,
            ("Routing scaffold only; no hardware mapping optimizer is implemented.",),
        )
