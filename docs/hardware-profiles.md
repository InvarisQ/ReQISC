# Hardware Profiles

Hardware profiles describe simplified coupling and native-control assumptions.

## XY, XX, and generic coupling examples

The benchmark directory includes XY-like, XX-like, and generic examples. These are profile examples for tests and documentation, not calibrated device records.

## What is represented

A profile currently represents a name, three coupling components, native one-qubit controls, and notes.

## What is not represented yet

The project does not yet represent drift, pulse constraints, connectivity graphs, crosstalk, calibrated error models, or vendor-specific hardware behavior.

## Adding profiles

Contributors should add a manifest, tests if validation logic changes, and documentation explaining what the profile assumes and what it omits.
