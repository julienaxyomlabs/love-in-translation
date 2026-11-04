# ADR-0008: A standard-library reference implementation with executable claims

- **Status:** accepted
- **Date:** 2026-11-04

## Context

A formal framework is only as checkable as its arithmetic. Readers should be able to verify every quantitative statement in the paper without trusting the prose, on any machine, years from now.

## Decision

- Implement each formal component as a small Python module using only the standard library (`statistics.NormalDist`, a 6×6 least-squares solver, bisection root-finding). No NumPy, no SciPy, no runtime dependencies.
- Express every mathematical claim in the paper as a unit test that names the section it implements.
- Treat the paper as source code too: CI lints its Markdown (links, math delimiters, no raw HTML), fails if the evidence ledger is stale, and re-resolves all DOIs monthly.
- Support Python 3.9 to 3.13 in CI.

## Consequences

- The implementation favours clarity over speed; it is a reference, not an estimation library. Fitting real dyadic data belongs in established tools (multilevel and dynamic SEM software) using the specifications in the paper.
- Contributors adding a component must add the test that pins its claim.
- **Tests are not validation** (added in v0.2.0). Passing tests shows that the code implements the stated equations, that mathematical identities hold, and that the RSA code reproduces published worked examples (Edwards 2007; Schönbrodt, Humberg & Nestler 2018). It does not show that any psychological mechanism is true. Likewise, a DOI that resolves with matching metadata shows that a citation points to the right work, not that the work supports every claim attributed to it.
