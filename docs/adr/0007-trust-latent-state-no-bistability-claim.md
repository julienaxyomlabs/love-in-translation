# ADR-0007: Trust is a latent state; bistability stays theoretical

- **Status:** accepted
- **Date:** 2026-11-04
- **Paper:** [§8.9 Dynamics](../../paper/08-mathematical-representation.md), [§14 Time and feedback](../../paper/14-time-and-feedback.md)
- **Code:** [`trust.py`](../../src/love_translation/trust.py), [`test_dynamics.py`](../../tests/test_dynamics.py)

## Context

Trust appears in the evidence as an outcome, a mediator and a moderator, so a static choice among those roles is misspecified. A self-reinforcing loop between trust and the reading of ambiguous acts is plausible and would explain why repair can reverse some damage but not all.

## Decision

Model trust as a latent state measured by several indicators, $`T(t+1)=T(t)+\eta\,[p(Q(t),T(t))-T(t)]+\varepsilon`$, and treat tipping points as theoretical only.

For $`\dot T=\eta\,[p(T)-T]`$ with continuous increasing $`p`$, an equilibrium is stable iff $`p'(T^*)<1`$. Bistability requires $`p'>1`$ somewhere, but this is **not sufficient**: logistic $`p`$ with slope 10 and midpoint 0.3 has $`\max p'=2.5`$ and one equilibrium, while slope 4.5 and midpoint 0.5 gives three. Both cases are tests.

## Consequences

- No study shows bistability, hysteresis or critical slowing down in relationship trust or satisfaction, and early-warning signals have weak support even in psychopathology. Accelerating declines before separation are not diagnostic: aligning random walks on a threshold crossing produces the same shape.
- Partial, irreversible-looking repair is also explained by asymmetric updating without any bistability, which is the cheaper hypothesis to test first.
- Love differential equations (Strogatz; Rinaldi) are rejected as empirical models: never estimated on relationship data.
