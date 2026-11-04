# ADR-0003: Ship symbolic parameters only

- **Status:** accepted
- **Date:** 2026-11-04
- **Paper:** [§8.1 Design rules](../../paper/08-mathematical-representation.md)

## Context

The brief forbids inventing numerical coefficients "to make the equation look scientific". Code invites defaults, and defaults read as estimates.

## Decision

- Every behavioural parameter ($`\tau,\pi,\delta,d',c,\beta,w,\eta,\lambda`$, loss weights) is a required argument or an explicit test fixture; no module ships a default that could be mistaken for an estimate.
- Numbers in tests and the CLI are arithmetic illustrations, labelled as such where they appear.
- Each component states its evidence status (established method, theoretical, or this project's hypothesis) in its module docstring and in the README table.

## Consequences

The package cannot "score" a relationship and is not a diagnostic tool. Turning a component into a predictive model requires estimating its parameters from data designed for it ([Section 17](../../paper/17-what-testing-requires.md), [Section 18](../../paper/18-proposed-study.md)).
