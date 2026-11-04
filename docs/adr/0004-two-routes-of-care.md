# ADR-0004: Two routes from care to outcomes

- **Status:** accepted as a hypothesis (untested); amended 2026-11-04 (v0.2.0, see [Amendment](#amendment-v020))
- **Date:** 2026-11-04
- **Paper:** [§7 Two routes by which care acts](../../paper/07-revised-model.md), [§8.8](../../paper/08-mathematical-representation.md#88-component-5-the-two-routes-our-hypothesis)

## Context

The candidate chain ran behaviour → signal → perception → interpretation → outcome, so care that is never perceived could have no effect. Evidence contradicts that: unnoticed (invisible) support aids adjustment, and household income improves children's outcomes whether or not it is read as love.

## Decision

Split the effect of enacted care into two **pathways**:

- a **substantive route**: the act changes circumstances, capacities or need states, and acts whether or not it is perceived;
- a **symbolic route**: the act is read as information about how much the giver values the receiver, and acts through perceived regard.

The routes classify pathways of effect, **not kinds of acts**. Every act can travel both: money can change circumstances and communicate devotion; presence can meet a real need for company or co-regulation whatever it signals, and can also signal regard.

```math
\mathbf{Y}_j=\boldsymbol\alpha+\boldsymbol\beta_{\text{sub}}\,h(E_{i\to j},N_j)+\boldsymbol\beta_{\text{sym}}\,Q_j+\boldsymbol\Gamma\mathbf{x}+\mathbf{e}
```

Both terms are functions of the same enacted care $`E`$.

## Consequences

- In the father–daughter case, both sincere statements can be true at once: "I gave you everything" counts what was provided, and "you were never there" reports needs and regard that the provision did not reach. Provision can still carry regard if its costs and motive are visible, and missing presence can leave needs unmet on both routes.
- The proposition predicts different outcome signatures (material and educational versus emotional and relational) and needs enactment measured independently of the receiver, ideally randomised, to estimate. Studies that classify kinds of support (financial versus emotional) are consistent with it but cannot test it.
- The routes interact in reality (income can improve emotional health through parents' relationships; visible help can signal inefficacy), so the decomposition is an analytic device, not a claim of independence.

## Amendment (v0.2.0)

Version 0.1.0 said the father's statement "describes the substantive ledger" and the daughter's "the symbolic one", and the paper listed money among substantive acts. That read as if provision were substantive and presence symbolic. The routes now explicitly describe how an act affects someone, not which category it belongs to. See [`CORRECTIONS.md`](../../CORRECTIONS.md) (C2).
