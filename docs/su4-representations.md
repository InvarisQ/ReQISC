# SU(4) Representations

The package stores `SU4GateRecord` objects that connect a gate name, a Weyl-coordinate abstraction, and metadata.

## Why coordinate abstractions are useful

Coordinate records make it possible to discuss two-qubit operation families, mirroring scaffolds, compiler-pass interfaces, and benchmark metrics without forcing every example to include a matrix decomposition.

## Limitations

The current package does not compute SU(4) matrix decompositions, canonicalize arbitrary unitaries, or verify equivalence classes beyond simple validation helpers.
