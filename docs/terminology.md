# Terminology

## Reconfigurable instruction-set component

A reusable abstraction for a two-qubit or workflow-level operation whose representation may be adapted to hardware, compiler, or calibration constraints.

## Two-qubit operation

An operation acting on two qubits. This repository currently models such operations through coordinate records rather than full matrices.

## SU(4)-native representation

A representation centered on the two-qubit unitary group SU(4), usually after separating local one-qubit controls from nonlocal structure.

## Weyl coordinate

A three-coordinate abstraction used to describe nonlocal equivalence classes of two-qubit operations under a chosen convention.

## Coupling Hamiltonian

A simplified record of `XX`, `YY`, and `ZZ` coupling strengths used for hardware-profile scaffolding.

## Calibration-aware workflow

A workflow that explicitly tracks assumptions about hardware calibration, cost, duration, or reliability. The current repository stores assumptions but does not fit calibrations.

## Routing overhead

Additional operations, depth, or duration introduced by mapping logical interactions onto hardware connectivity.

## Benchmark manifest

A reproducibility-first description of what should be run, with which profile and metrics. It is not a result.

## Compiler pass

A transformation or analysis stage with explicit input state, output state, and notes.

## Hardware profile

A named abstraction describing coupling and native controls for compiler or benchmark planning.
