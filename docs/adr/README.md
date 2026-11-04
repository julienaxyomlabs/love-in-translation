# Architecture decision records

Modelling choices that change what the framework claims, recorded with their context, the rejected alternatives and their consequences. Format after Michael Nygard's ADRs.

| ADR | Decision | Status |
|---|---|---|
| [0001](0001-reject-similarity-indices.md) | Reject cosine, dot-product, difference and profile-similarity indices as measures of fit | accepted |
| [0002](0002-response-surface-for-fit.md) | Separate level from mismatch with polynomial regression and response surface analysis | accepted; amended in v0.2.0 |
| [0003](0003-symbolic-parameters-only.md) | Ship symbolic parameters only; never invent coefficients | accepted |
| [0004](0004-two-routes-of-care.md) | Model a substantive and a symbolic route from care to outcomes (pathways, not act types) | accepted (as hypothesis); amended in v0.2.0 |
| [0005](0005-safety-as-lexicographic-gate.md) | Treat safety as a lexicographic gate, not a weighted variable | superseded by 0009 |
| [0006](0006-compatibility-as-feasible-set.md) | Define incompatibility as an empty feasible set of joint life patterns | accepted (as hypothesis) |
| [0007](0007-trust-latent-state-no-bistability-claim.md) | Model trust as a latent state; keep bistability theoretical | accepted |
| [0008](0008-stdlib-only-reference-implementation.md) | Implement the model in standard-library Python with executable claims | accepted; amended in v0.2.0 |
| [0009](0009-safety-as-admissibility-constraint.md) | Treat safety as an admissibility constraint: exclude unsafe arrangements before comparing | accepted |
