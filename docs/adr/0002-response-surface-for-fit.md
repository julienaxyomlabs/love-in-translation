# ADR-0002: Separate level from mismatch with response surface analysis

- **Status:** accepted; amended 2026-11-04 (v0.2.0, see [Amendment](#amendment-v020))
- **Date:** 2026-11-04
- **Paper:** [§8.7 Need fulfilment and fit](../../paper/08-mathematical-representation.md#87-component-4-need-fulfilment-and-fit)
- **Code:** [`fit.py`](../../src/love_translation/fit.py), [`test_fit.py`](../../tests/test_fit.py)

## Context

"Translation versus amount" is a claim about the *shape* of the relation between received supply $`S`$, need $`N`$ and outcome $`Y`$. Difference scores impose equal and opposite coefficients without testing them.

## Decision

Model $`Y=b_0+b_1S+b_2N+b_3S^2+b_4SN+b_5N^2+e`$ with $`S`$ and $`N`$ commensurable and centred on a shared zero (the scale midpoint), and read the surface through quantities defined at that centring point:

- $`a_1=b_1+b_2`$: slope along the line of congruence $`S=N`$ **at the centring point**; along that line the slope at level $`t`$ is $`a_1+2a_2t`$;
- $`a_2=b_3+b_4+b_5`$: curvature along the line of congruence;
- $`a_3=b_1-b_2`$: slope along the line of incongruence $`S=-N`$ at the centring point; with $`a_4\ne0`$ it locates the peak or trough of that line;
- $`a_4=b_3-b_4+b_5`$: curvature along the line of incongruence;
- $`a_5=b_3-b_5`$, the stationary point and the principal axes (Edwards 2007, eqs. 11–18).

A congruence claim needs the joint pattern $`a_4<0`$, $`a_3=0`$ and a first principal axis on the congruence line ($`p_{10}=0`$, $`p_{11}=1`$, or $`a_5=0`$ given $`a_3=0`$), each with confidence intervals, plus comparison with constrained models such as the squared-difference model ($`b_1=b_2=0`$, $`b_3=b_5`$, $`b_4=-2b_3`$). Asymmetric deficiency/excess losses are estimated with cubic RSA or splines, never assumed.

## Consequences

The translation hypothesis predicts the joint congruence pattern, or a directional variant where deficiency and excess differ; the amount hypothesis predicts outcomes that rise with supply without that pattern. The base rate is sobering (fit terms add ΔR² ≈ .008 in person–environment fit research), and no dyadic RSA of care channels has been published, so this is the first test to run, not a known result.

## Amendment (v0.2.0)

Version 0.1.0 of this record called $`a_1`$ "the amount effect" and $`a_4`$ "mismatch hurts". Both overstated the coefficients: $`a_1`$ is a slope at one point, and a negative $`a_4`$ is one part of a joint pattern. The corrected reading follows the full texts of Edwards (2007) and Schönbrodt, Humberg & Nestler (2018); details and sources are in [`CORRECTIONS.md`](../../CORRECTIONS.md) (C1).
