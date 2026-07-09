"""Template-synthesis extension records."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TemplateCandidate:
    """Describes a future template-synthesis candidate without claiming use."""

    name: str
    description: str
    required_evidence: str = "tests, references, and benchmark manifest"
