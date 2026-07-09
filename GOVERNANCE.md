# Governance

## Maintainer responsibilities

Maintainers are responsible for repository health, scope control, issue triage, pull-request review, release preparation, and research-integrity review. They should keep the project honest about what is implemented, what is planned, and what evidence supports any claim.

## Contributor roles

- **Users** report bugs, request features, and test examples.
- **Documentation contributors** improve guides, terminology, examples, and onboarding.
- **Implementation contributors** add tested code to the package.
- **Research contributors** propose algorithms, benchmark designs, mathematical primitives, or hardware-model extensions.
- **Maintainers** review, merge, release, and resolve scope disputes.

Roles are earned through sustained, high-quality contributions and can be adjusted by maintainer consensus.

## Decision-making

Small fixes may be accepted by one maintainer. Changes affecting architecture, dependencies, benchmark claims, licensing, governance, or public positioning require broader maintainer review. When consensus is not immediate, maintainers should document the decision rationale in the issue or pull request.

## Issue triage

Issues are triaged by layer: mathematical primitive, compiler pass, hardware profile, calibration model, benchmark, documentation, governance, or infrastructure. Maintainers may request a narrower scope before accepting implementation work.

## Design proposal process

A design proposal is required for:

- new compiler passes that claim optimization behavior;
- benchmark result formats;
- optional integration adapters;
- new dependencies;
- major changes to public data models;
- features that might imply hardware or institutional claims.

A proposal should state the problem, interface, alternatives considered, validation plan, documentation plan, and expected limitations.

## Research-integrity review

Maintainers should verify that contributions do not fabricate benchmark results, overclaim implementation maturity, copy external prose, imply false affiliations, or blur the difference between scaffold and evidence. Claims about algorithmic performance must be supported by reproducible artifacts or clearly labeled as future work.

## Release process

Releases should include:

1. passing tests, lint, and type checks;
2. updated changelog;
3. reviewed documentation;
4. version update in package metadata and `CITATION.cff`;
5. release notes distinguishing implemented features from planned work;
6. a dry-run package build before publishing.

## Conflict resolution

Technical disputes should be resolved with tests, references, reduced examples, and explicit scope boundaries. Conduct disputes follow `CODE_OF_CONDUCT.md`. Maintainers may pause a discussion if it becomes unproductive or unsafe.

## Scope control

The project should remain a research-software workbench. It should not become a marketing site, a repository of copied papers, a claim vehicle for unsupported benchmarks, or a wrapper that requires heavyweight quantum SDKs in the core package.
