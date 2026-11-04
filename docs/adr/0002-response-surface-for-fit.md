# ADR-0002: Separate level from mismatch with response surface analysis

- **Status:** accepted
- **Date:** 2026-11-04
- **Paper:** [§8.7 Need fulfilment and fit](../../paper/08-mathematical-representation.md)
- **Code:** [`fit.py`](../../src/love_translation/fit.py), [`test_fit.py`](../../tests/test_fit.py)

## Context

"Translation versus amount" is a claim about the *shape* of the relation between received supply $`S`$, need $`N`$ and outcome $`Y`$. Difference scores impose equal and opposite coefficients without testing them.

## Decision

Model $`Y=b_0+b_1S+b_2N+b_3S^2+b_4SN+b_5N^2+e`$ with $`S`$ and $`N`$ on one metric, and interpret the surface quantities

- $`a_1=b_1+b_2`$: level along the line of congruence (the amount effect);
- $`a_3=b_1-b_2`$: directional misfit (over- versus under-supply);
- $`a_4=b_3-b_4+b_5`$: curvature across the line of incongruence (mismatch hurts).

A congruence claim needs the joint pattern $`a_4<0`$, $`a_3\approx 0`$ and a principal axis on the congruence line. Asymmetric deficiency/excess losses are estimated with cubic RSA or splines, never assumed.

## Consequences

The translation hypothesis predicts a substantial $`a_4`$; the amount hypothesis predicts a dominant $`a_1`$ with incongruence terms near zero. The base rate is sobering (fit terms add ΔR² ≈ .008 in person–environment fit research), and no dyadic RSA of care channels has been published, so this is the first test to run, not a known result.
