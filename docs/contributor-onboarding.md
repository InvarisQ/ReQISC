# Contributor Onboarding

## First good issues

Good first issues include documentation cleanup, validation tests, manifest examples, and small helper functions with clear scope.

## Run tests

Use `python -m pip install -e ".[dev]"`, then run `pytest`, `ruff check .`, and `mypy src`.

## Add examples

Examples should be short, runnable, and honest about scaffold limitations.

## Propose a pass

Open a research-task issue before adding a nontrivial pass. Include inputs, outputs, references, validation, and benchmark impact.

## Add hardware profiles

Add a manifest and state what is represented, what is omitted, and whether values are illustrative or calibrated.

## Improve docs

Prefer precise terminology and scope boundaries over hype.
