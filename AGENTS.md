# Instructions for Coding Agents

## Mission

Invaris Quantum ReQISC is an open-source research-software workbench for reconfigurable quantum instruction-set components. The repository should remain technically serious, contributor-ready, and honest about implementation status.

## Current implementation status

The repository contains tested scaffolding for mathematical primitives, hardware profiles, compiler pipeline interfaces, benchmark metrics, documentation, examples, and governance. It does not contain a production compiler, pulse-level solver, calibrated backend, validated routing optimizer, or benchmark performance evidence.

## Commands

Run these before proposing changes:

```bash
python -m pip install -e ".[dev]"
pytest
ruff check .
mypy src
```

## Repository map

- `src/invaris_reqisc/gates/`: SU(4), Weyl-coordinate, canonical, and mirroring primitives.
- `src/invaris_reqisc/hardware/`: coupling Hamiltonian and hardware profile abstractions.
- `src/invaris_reqisc/compiler/`: pass interface, pipeline, template, synthesis, and routing scaffolds.
- `src/invaris_reqisc/benchmarks/`: metrics, manifest loading, and report records.
- `src/invaris_reqisc/io/`: OpenQASM and JSON-schema extension points.
- `src/invaris_reqisc/validation/`: numerical and invariant validation helpers.
- `docs/`: user and contributor documentation.
- `examples/`: short runnable examples.
- `benchmarks/`: manifests and fixtures, not claims.
- `website/`: public static website layer.

## Coding style

Use type hints, dataclasses for stable records, clear exceptions for invalid inputs, small functions, and tests that cover edge cases. Keep core dependencies minimal. Do not add heavyweight quantum SDKs to runtime dependencies without an accepted proposal.

## Documentation style

Use sober technical language. Mark each feature as implemented, scaffolded, planned, or out of scope. Do not write marketing copy. Do not copy large passages from papers or external documentation.

## Testing expectations

New public behavior requires tests. Tests should check successful use and invalid inputs. Example scripts should remain runnable after changes.

## Honesty rules

Do not add false partnerships, false sponsorships, false institutional affiliations, invented benchmark results, copied paper text, private development notes, or claims that a scaffold is a completed algorithm.

## Adding a module

1. Place the module in the appropriate layer.
2. Add docstrings and type hints.
3. Export stable public names from the package or subpackage `__init__.py` only when the interface is intended for users.
4. Add tests.
5. Update docs if contributors need to understand the new module.

## Adding an example

Examples should run with the installed package and standard-library dependencies only unless clearly documented otherwise. Keep examples short and avoid implying measured performance.

## Adding a benchmark manifest

A manifest describes what to run; it is not a result. Include input name, hardware profile, metric plan, reproducibility fields, and notes. Do not include unsupported comparative claims.

## Modifying website docs

The website is the public documentation and project-home layer. It should link to docs and contribution paths. It should not include fake affiliations, private development notes, copied paper text, or unverified results.

## Updating the roadmap

When adding implemented behavior, update the roadmap status and changelog. Keep planned work separate from completed work.

## Citations

Add citations when a contribution depends on external research, datasets, algorithms, specifications, or documentation. Do not cite external authors as project maintainers unless they directly contribute and agree.

## Protected areas

Do not modify license, governance, security reporting, benchmark-claim language, dependency policy, or public project positioning without maintainer review.
