# Roadmap

This roadmap is intentionally explicit about what is implemented versus planned. The project should grow by adding validated layers, not by presenting future algorithms as complete.

## Phase 0: Repository foundation

- Community files: README, conduct, contributing, governance, support, security, citation, notices.
- Package skeleton with typed modules.
- Documentation structure and website layer.
- Runnable examples.
- CI, lint, docs validation, and release dry-run workflows.
- Initial tests for implemented dataclasses and scaffolds.

Status: initial implementation present.

## Phase 1: Mathematical primitives

- `WeylCoordinate` validation and tuple/norm helpers.
- `SU4GateRecord` representation and metadata export.
- Coordinate validation helpers and canonical-region checks.
- Mirror coordinate utilities.
- Basic invariant checks.

Status: partial implementation present; full KAK/canonical decomposition is not implemented.

## Phase 2: Hardware profile abstractions

- Coupling Hamiltonian profiles.
- Basic native-control descriptions.
- JSON/YAML profile schema examples.
- Validation for finite coupling parameters.
- Contributor guide for new profile examples.

Status: dataclasses and example manifests present; no calibrated hardware backend exists.

## Phase 3: Compiler pass interfaces

- Base pass interface.
- Pipeline object.
- Program-aware template synthesis interface.
- Hierarchical synthesis interface.
- SU(4)-aware routing interface.
- Structured pass notes and output records.

Status: scaffold present; optimization algorithms are future work.

## Phase 4: Benchmark scaffolding

- Benchmark manifest format.
- Metrics model.
- Report model.
- Example circuit placeholders.
- Reproducibility metadata.

Status: metrics and manifest loading present; no benchmark result claims are included.

## Phase 5: Optional ecosystem integrations

- OpenQASM import/export expansion.
- Optional Qiskit adapter.
- Optional BQSKit adapter.
- Optional TKET adapter.
- Braket and CUDA-Q exploration.
- Hardware backend adapter proposals.

Status: planned only. Core package should remain lightweight.

## Phase 6: Reproducibility hardening

- Versioned fixtures.
- Deterministic example workflows.
- Benchmark report generation.
- Versioned benchmark artifacts.
- Documentation publishing and link validation.

Status: planned.

## Phase 7: Research-extension program

- Curated good-first issues.
- Contributor proposals for algorithmic extensions.
- Validation tasks for mathematical invariants.
- Comparison studies with clearly bounded claims.
- Calibration-model improvements.

Status: planned.
