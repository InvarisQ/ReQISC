# Architecture

## Layer 1: Mathematical primitives

Mathematical primitives include Weyl coordinates, SU(4) gate records, coupling vectors, finite-value validation, and simple invariant checks. These are small enough to test directly.

## Layer 2: Compiler workflow

The compiler layer defines pass interfaces and a sequential pipeline. Current passes return structured scaffold outputs and notes. They do not perform full optimization.

## Layer 3: Hardware profiles

Hardware profiles capture coupling Hamiltonian abstractions and native one-qubit controls. They are not calibrated backend models.

## Layer 4: Benchmark and evidence

Benchmark records distinguish manifests, metrics, reports, and evidence. A manifest is not a result.

## Layer 5: Governance and documentation

Governance documents define how contributors propose work, how maintainers review claims, and how scope is controlled.
