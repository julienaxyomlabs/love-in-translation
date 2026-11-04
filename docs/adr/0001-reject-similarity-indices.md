# ADR-0001: Reject similarity indices as measures of fit

- **Status:** accepted
- **Date:** 2026-11-04
- **Paper:** [§8.3 What the mathematics must not do](../../paper/08-mathematical-representation.md)
- **Code:** [`similarity.py`](../../src/love_translation/similarity.py), [`test_similarity.py`](../../tests/test_similarity.py)

## Context

The original brief proposed representing expressed care as a vector $`\mathbf{E}_A(t)`$, needs as $`\mathbf{N}_B(t)`$, and their alignment as a dot product or cosine similarity. The hypothesis under test is precisely whether fit matters *beyond* amount.

## Decision

Do not use cosine similarity, dot products, importance-weighted similarity, difference scores or raw profile correlations as estimators of fit.

- Cosine is scale-invariant, $`\cos(\alpha\mathbf{E},\beta\mathbf{N})=\cos(\mathbf{E},\mathbf{N})`$: a partner giving a quarter of what is needed in the right proportions scores 1. It assumes amount away and so cannot test a claim about amount.
- On rating scales cosine depends on the coding origin (0.959, 0.926 or 0.763 for the same two profiles) and on the units of each channel.
- The profile correlation discards elevation, which is the amount information, and is inflated by shared normative profiles.
- The dot product mixes amount, need intensity and alignment into one number.
- Importance weighting does not improve prediction in the satisfaction literature, and product composites change under permissible rescaling.
- Expressed acts and needs do not live in the same space; a received-supply variable on the need metric is required.

## Consequences

Fit questions are answered with response surfaces ([ADR-0002](0002-response-surface-for-fit.md)). Every number above is a regression test, so a future change that silently reintroduces a similarity index will contradict the suite.
