# ADR-0006: Incompatibility is an empty feasible set

- **Status:** accepted as a hypothesis (formalisation is original)
- **Date:** 2026-11-04
- **Paper:** [§8.10](../../paper/08-mathematical-representation.md), [§15 Case A and Case F](../../paper/15-counterexamples.md)
- **Code:** [`constraints.py`](../../src/love_translation/constraints.py)

## Context

Stress-test Case A (perfect understanding, incompatible lives) breaks any model in which better translation always helps. Goal conflict harms relationship quality regardless of understanding.

## Decision

Let $`x`$ range over joint life patterns (time, money, location, children, careers, care flows) and define

```math
\mathcal{F}=\{x\in\mathcal{C}_A\times\mathcal{C}_B : G_A(x)\ge 0,\ G_B(x)\ge 0,\ W_A(x)\ge w_A^{\min},\ W_B(x)\ge w_B^{\min}\}
```

- **Unmet need:** a gap a reallocation within $`\mathcal{F}`$ could close.
- **Incompatibility:** $`\mathcal{F}=\varnothing`$.
- **Unsustainable need:** $`\mathcal{F}=\varnothing`$ because one person's requirements are met only below the other's sustainability threshold.

## Consequences

Understanding helps partners *find* a point in $`\mathcal{F}`$ but cannot *create* one. Measurement is the weak point: goal-conflict and dealbreaker measures are only partial proxies for the essential requirements $`G`$.
