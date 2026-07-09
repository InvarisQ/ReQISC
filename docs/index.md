# Invaris Quantum ReQISC Documentation

Invaris Quantum ReQISC is an early-stage research-software workbench for reconfigurable quantum instruction-set components.

## Repository map

- `src/invaris_reqisc/gates/`: Weyl coordinates, SU(4) gate records, canonical-region helpers, and mirroring utilities.
- `src/invaris_reqisc/hardware/`: coupling Hamiltonians and hardware profiles.
- `src/invaris_reqisc/compiler/`: compiler-pass interfaces and sequential pipeline scaffold.
- `src/invaris_reqisc/benchmarks/`: metric records, manifest loading, and report structures.
- `examples/`: runnable examples for current scaffolds.
- `benchmarks/`: manifest and hardware-profile examples.

## How to start

Install with `python -m pip install -e ".[dev]"`, run `pytest`, and read `docs/contributor-onboarding.md` before opening a larger proposal.
