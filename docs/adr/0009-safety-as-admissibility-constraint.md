# ADR-0009: Safety is an admissibility constraint

- **Status:** accepted
- **Date:** 2026-11-04 (v0.2.0)
- **Supersedes:** [ADR-0005](0005-safety-as-lexicographic-gate.md)
- **Paper:** [§8.10 Constraints that are not weights](../../paper/08-mathematical-representation.md#810-component-7-constraints-that-are-not-weights), [§15 Counterexamples](../../paper/15-counterexamples.md)
- **Code:** [`constraints.py`](../../src/love_translation/constraints.py), [`test_constraints.py`](../../tests/test_constraints.py)

## Context

ADR-0005 ordered relationship states lexicographically: safety first, then care. That is a ranking. When every available option is unsafe, a lexicographic order still selects one, the least unsafe or the more caring of two equally unsafe options, and the model would then appear to recommend it. A hard safety requirement has to exclude, not rank.

## Decision

Restrict the feasible set before anything is compared:

```math
\mathcal F_{\text{safe}}=\{x\in\mathcal F:\ \mathrm{Safe}(x)=1\},\qquad x^\star=\arg\max_{x\in\mathcal F_{\text{safe}}}\mathrm{Outcome}(x)\ \text{ only if }\mathcal F_{\text{safe}}\neq\varnothing .
```

- $`\mathrm{Safe}(x)\in\{0,1\}`$ is decided from safety indicators (violence, threats, coercive control, fear-based compliance) against a threshold, never from perceived love or from care.
- If $`\mathcal F_{\text{safe}}=\varnothing`$, the model reports that no admissible arrangement exists and recommends nothing.
- Safety, autonomy and coercion stay analytically distinct from perceived love. Autonomy remains a separate outcome, never netted against care.

## Consequences

- `constraints.choose()` returns `None` when no option is safe, and `classify()` reports `"unsafe"` when the only arrangements meeting both people's requirements fail the safety criterion. Tests pin both behaviours and show that the lexicographic ranking would still have picked an unsafe option.
- The weighted-sum argument still stands: no finite safety weight excludes unsafe options.
- Where the threshold sits, and the decision to exclude, are normative. Data can show whether care compensates for danger (a non-compensability test with threshold models or necessary condition analysis), not where the line must be.
