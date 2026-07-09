# Invaris Quantum ReQISC

Invaris Quantum ReQISC is an open-source research-software workbench for building, testing, and benchmarking reconfigurable quantum instruction-set components across hardware-aware compiler and control workflows.

[![CI](https://github.com/OWNER/invaris-quantum-reqisc/actions/workflows/ci.yml/badge.svg)](https://github.com/OWNER/invaris-quantum-reqisc/actions/workflows/ci.yml)
[![Lint](https://github.com/OWNER/invaris-quantum-reqisc/actions/workflows/lint.yml/badge.svg)](https://github.com/OWNER/invaris-quantum-reqisc/actions/workflows/lint.yml)

> Replace `OWNER` after the public repository is created. The badges point only to workflows included in this repository.

## What this project is

This repository is an early-stage research-software scaffold. It provides typed primitives, package structure, documentation, examples, tests, and contribution pathways for implementing and evaluating reconfigurable quantum instruction-set workflows. It does not yet provide a production compiler, pulse-level control stack, calibrated hardware backend, or validated performance claims.

The project focuses on the implementation layer around reconfigurable quantum instruction-set components: mathematical representations, hardware profiles, compiler-pass interfaces, benchmark manifests, and reproducibility conventions. It is designed to let contributors add carefully reviewed algorithms without forcing heavyweight quantum SDK dependencies into the core package.

## Why this project exists

Quantum compiler research often crosses several boundaries at once: abstract two-qubit operation representation, hardware coupling structure, calibration assumptions, route selection, synthesis templates, and benchmark evidence. Those layers are frequently discussed together but implemented in ways that make it difficult to separate mathematical claims from engineering scaffolds and measured results.

Invaris Quantum ReQISC exists to make that separation explicit. The repository distinguishes between:

- mathematical primitives that can be validated locally;
- compiler and workflow interfaces that define extension points;
- benchmark records that separate manifests from claims;
- documentation and governance that keep scope, evidence, and contribution review visible.

## Current implementation status

The current version is a credible foundation, not a completed quantum compiler. It includes:

- finite-value validation helpers;
- `WeylCoordinate` and `SU4GateRecord` dataclasses;
- `CouplingHamiltonian` and `HardwareProfile` dataclasses;
- gate-mirroring utilities for near-identity coordinate scaffolding;
- a pass-oriented compiler pipeline interface;
- benchmark metric records and manifest loading;
- runnable examples;
- tests for the implemented primitives and scaffolds;
- documentation, governance files, issue templates, CI workflows, and a Netlify-ready website layer.

## What is currently implemented

The package currently implements small, testable components:

```python
from invaris_reqisc.gates import SU4GateRecord, WeylCoordinate
from invaris_reqisc.gates.mirroring import mirrored_gate_record

coord = WeylCoordinate(0.01, 0.0, 0.0)
gate = SU4GateRecord("small-entangler", coord, metadata={"source": "example"})
mirrored = mirrored_gate_record(gate, threshold=0.05)

print(mirrored.as_dict())
```

The compiler pipeline is intentionally structured around explicit passes:

```python
from invaris_reqisc.compiler import (
    HierarchicalSynthesisPass,
    Pipeline,
    ProgramAwareTemplatePass,
    SU4AwareRoutingPass,
)

pipeline = Pipeline([
    ProgramAwareTemplatePass(),
    HierarchicalSynthesisPass(),
    SU4AwareRoutingPass(),
])

result = pipeline.run({"program": "example", "two_qubit_blocks": 2})
print(result.as_dict())
```

## What is intentionally scaffolded

The following areas are intentionally not represented as complete algorithms yet:

- full KAK decomposition and canonical SU(4) solving;
- pulse-level calibration and hardware-control execution;
- full routing, mapping, and gate-scheduling optimization;
- validated comparisons against established compilers;
- backend adapters for Qiskit, BQSKit, TKET, Braket, CUDA-Q, or vendor systems;
- experimental benchmark claims.

Those areas are documented as extension paths and should be added only with tests, references, and clear evidence boundaries.

## Installation

Create a virtual environment, then install the package in editable mode:

```bash
python -m pip install -e ".[dev]"
```

The core package uses the Python standard library. Development tools are optional and installed through the `dev` extra.

## Quick start

Run the test suite:

```bash
pytest
```

Run lint and type checks:

```bash
ruff check .
mypy src
```

Run the examples:

```bash
python examples/minimal_hardware_profile.py
python examples/su4_gate_record.py
python examples/gate_mirroring_demo.py
python examples/compiler_pipeline_demo.py
python examples/benchmark_stub.py
```

## Repository structure

```text
src/invaris_reqisc/       Python package
  gates/                  SU(4), Weyl-coordinate, canonical, and mirroring primitives
  hardware/               Coupling Hamiltonian and hardware profile abstractions
  compiler/               Pass interface, pipeline, synthesis, template, and routing scaffolds
  benchmarks/             Manifest loading, metrics, and report records
  io/                     OpenQASM and JSON-schema placeholders
  validation/             Numerical and invariant validation helpers
examples/                 Runnable examples for implemented components
benchmarks/               Example benchmark and hardware-profile manifests
docs/                     Project documentation and contributor guides
.github/                  Issue templates, PR template, CI, lint, docs, and release dry-run workflows
website/                  Static public website/documentation home for Netlify
```

## Architecture overview

The repository is separated into four layers:

1. **Mathematical primitives.** Typed coordinates, gate records, coupling records, and validation rules.
2. **Compiler/workflow scaffolding.** Pass interfaces, pipeline composition, structured pass notes, and future synthesis/routing extension points.
3. **Benchmark and evidence layer.** Metrics, manifests, reproducibility fields, report records, and examples that avoid fabricated results.
4. **Governance/documentation layer.** Contribution processes, review rules, project scope, conduct, security reporting, and roadmap management.

## Example usage

Create a hardware profile:

```python
from invaris_reqisc.hardware import CouplingHamiltonian, HardwareProfile

profile = HardwareProfile(
    name="xy-example",
    coupling=CouplingHamiltonian(xx=1.0, yy=1.0, zz=0.0),
    native_1q_controls=("rx", "rz"),
    notes="Example XY-like coupling profile for documentation and tests.",
)

print(profile.summary())
```

Compare metric records:

```python
from invaris_reqisc.benchmarks import BenchmarkMetrics, compare_metrics

baseline = BenchmarkMetrics(10, 5, 120.0, 4)
candidate = BenchmarkMetrics(8, 4, 105.0, 3)
print(compare_metrics(baseline, candidate))
```

## Benchmark philosophy

Benchmark files in this repository are manifests and schema examples, not performance evidence. Any future benchmark report must identify the input program, hardware profile, pass configuration, software version, random seeds if applicable, execution environment, and whether results are simulated, analytical, or experimentally calibrated.

No performance claim should be merged unless the supporting data and method are reproducible from repository artifacts or explicitly labeled as external evidence.

## Contribution paths

Contributors can help by:

- adding validation tests for mathematical primitives;
- improving hardware-profile schema examples;
- proposing compiler-pass interfaces before implementing algorithms;
- adding benchmark manifests without inventing results;
- improving documentation and terminology;
- adding optional integration adapters behind extras.

Start with [CONTRIBUTING.md](CONTRIBUTING.md) and [docs/contributor-onboarding.md](docs/contributor-onboarding.md).

## Roadmap summary

The roadmap proceeds from repository foundation to mathematical primitives, hardware profiles, compiler-pass interfaces, benchmark scaffolding, optional ecosystem integrations, reproducibility hardening, and research-extension work. See [ROADMAP.md](ROADMAP.md).

## Governance and conduct

The project uses documented maintainer responsibilities, proposal review, research-integrity checks, and conflict-resolution processes. See [GOVERNANCE.md](GOVERNANCE.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Citation

Use [CITATION.cff](CITATION.cff) to cite the project software. Do not cite this repository as a substitute for citing external research papers, datasets, or tools used in downstream work.

## License

This project is licensed under the Apache License 2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).

## Third-party marks and affiliations

Third-party names, SDKs, compilers, cloud systems, hardware systems, and research platforms mentioned in this repository are descriptive references only. No sponsorship, endorsement, partnership, or affiliation is implied. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
