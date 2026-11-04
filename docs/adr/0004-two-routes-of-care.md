# ADR-0004: Two routes from care to outcomes

- **Status:** accepted as a hypothesis (untested)
- **Date:** 2026-11-04
- **Paper:** [§7 Two routes by which care acts](../../paper/07-revised-model.md), [§8.8](../../paper/08-mathematical-representation.md)

## Context

The candidate chain ran behaviour → signal → perception → interpretation → outcome, so care that is never perceived could have no effect. Evidence contradicts that: unnoticed (invisible) support aids adjustment, and household income improves children's outcomes whether or not it is read as love.

## Decision

Split the effect of enacted care into

- a **substantive route**: care changes circumstances or capacities and acts whether or not it is perceived;
- a **symbolic route**: care is read as information about how much the giver values the receiver, and acts through perceived regard.

```math
\mathbf{Y}_j=\boldsymbol\alpha+\boldsymbol\beta_{\text{sub}}\,h(E_{i\to j},N_j)+\boldsymbol\beta_{\text{sym}}\,Q_j+\boldsymbol\Gamma\mathbf{x}+\mathbf{e}
```

## Consequences

- The father–daughter statements can both be sincere: "I gave you everything" describes the substantive ledger, "you were never there" the symbolic one.
- The proposition predicts different outcome signatures (material and educational versus emotional and relational) and needs enactment measured independently of the receiver, ideally randomised, to estimate.
- The routes interact in reality (income can improve emotional health through parents' relationships; visible help can signal inefficacy), so the decomposition is an analytic device, not a claim of independence.
