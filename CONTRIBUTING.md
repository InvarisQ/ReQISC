# Contributing

Thank you for considering a contribution to Invaris Quantum ReQISC. The project is intentionally early, so contributions should make the scaffold more useful without overstating what has been validated.

## Set up the environment

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -e ".[dev]"
pytest
ruff check .
mypy src
```

On Windows, activate the virtual environment with `.venv\\Scripts\\activate`.

## Choose an issue

Good first contributions usually affect one layer:

- mathematical primitives: validation, invariants, coordinate utilities;
- hardware profiles: schemas, examples, validation rules;
- compiler scaffold: pass interfaces, structured notes, tests;
- benchmark layer: manifests, metrics, report records;
- documentation: terminology, examples, contributor onboarding.

Avoid starting with a large compiler algorithm unless there is already an accepted design proposal.

## Add code

Code should be small, typed, and directly tested. Prefer dataclasses and explicit return records over unstructured dictionaries where stable structure matters. New modules should include:

- a docstring explaining scope and limitations;
- type hints for public functions;
- validation for user-facing data records;
- tests that cover both valid and invalid inputs;
- documentation updates if contributors need to understand the feature.

## Add documentation

Documentation should identify the current status of an idea. Use language such as "implemented", "scaffolded", "planned", or "out of scope". Do not turn the README into a paper summary. Do not copy large passages from external papers or documentation.

## Add benchmarks

Benchmark contributions must separate manifests from results. A manifest may describe an input, hardware profile, and metric plan without claiming performance. A result file must identify the exact software version, configuration, environment, random seeds if relevant, and whether the result is simulated, analytical, or experimental.

Do not submit invented benchmark values, placeholder wins, or comparative claims without reproducible support.

## Propose research features

For nontrivial research features, open a research-task issue before implementation. The proposal should include:

- affected layer;
- technical claim;
- references or prior art;
- expected inputs and outputs;
- validation strategy;
- benchmark impact;
- dependency impact.

## Cite external sources

Cite external papers, documentation, algorithms, data, and tools when they materially influence a contribution. Keep citations close to the relevant explanation. Do not list external researchers as project authors unless they have contributed to this repository and agreed to be listed.

## Review expectations

Maintainers may request changes for tests, documentation, scope control, dependency policy, citation quality, or claim language. A technically interesting change may still be declined if it makes the project appear more mature than it is.
