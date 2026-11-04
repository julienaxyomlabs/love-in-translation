# ADR-0005: Safety is a lexicographic gate, not a weighted variable

> **Superseded.** A lexicographic order ranks unsafe options instead of excluding them: when every option is unsafe it still picks one. [ADR-0009](0009-safety-as-admissibility-constraint.md) replaces it with an admissibility constraint. This record is kept unchanged below as the decision that was made in v0.1.0.

- **Status:** superseded by [ADR-0009](0009-safety-as-admissibility-constraint.md) on 2026-11-04 (v0.2.0)
- **Date:** 2026-11-04
- **Paper:** [§8.10 Constraints that are not weights](../../paper/08-mathematical-representation.md), [§15 Counterexamples](../../paper/15-counterexamples.md)
- **Code:** [`constraints.py`](../../src/love_translation/constraints.py), [`test_constraints.py`](../../tests/test_constraints.py)

## Context

In abusive relationships, felt love and commitment can stay high or rise as safety falls; committed partners re-label aggression as tolerable. A care score with a safety term would partly cancel the danger signal.

## Decision

Evaluate relationship states lexicographically, safety first, care only among equally safe states. Autonomy (psychological control, intrusion) is a separate outcome, never netted against care.

## Consequences

- No finite safety weight in a weighted sum reproduces the gate: for every weight there is an unsafe-but-caring state the sum prefers. The test suite constructs that counterexample for weights up to $`10^9`$.
- The empirical signature of a gate is that below a safety threshold outcomes become insensitive to care in other channels, testable with threshold models and necessary condition analysis against additive alternatives.
- Treating safety this way is partly a normative choice; the data inform it but do not settle it.
