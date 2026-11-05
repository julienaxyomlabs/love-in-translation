# Corrections

Changes that correct or narrow what an earlier version claimed. Each entry quotes the earlier wording, states the correction, lists the affected files and records how deeply the supporting sources were checked: **full text** (read in full), **abstract** (abstract or index record only), **prior knowledge** (formula or claim recalled, metadata verified) or **not accessed**.

The research notes in [`evidence/notes/`](evidence/notes/) are the record of the literature review and are preserved unchanged. Where they contain a statement superseded here, the entry says where.

## v0.3.0 (2026-11-05): audit findings, not yet applied

No paper text changed in this version. An audit compared 24 of the paper's most consequential empirical claims with their primary sources ([`audit/`](audit/README.md)). Its results:

- **Re-grades.** Eight findings are re-graded ([Table A2](audit/corrections.md#tier-3-instrument-tables-design-text-bibliography-and-corrections-log)). Among them, invisible support is re-graded from "Moderate to Established" to *Mixed*, because a larger replication by the same group did not reproduce it.
- **Recommended text changes.** There are 75, listed in [`audit/corrections.md`](audit/corrections.md) with the primary source and verification depth for each.
- **The equations.** None needs changing.

When the corrections are applied, each will be logged here with its earlier wording, the correction, the affected files and how deeply the source was checked. Until then, the statement under v0.2.0 that no empirical finding was re-graded describes v0.2.0 only.

## v0.2.0 (2026-11-04)

Prompted by an external review of v0.1.0. No empirical finding was re-graded and no study result was reinterpreted.

### C1. Response-surface coefficients were over-interpreted

- **Earlier wording.** Chapter 8 §8.7 described $`a_1=b_1+b_2`$ as "the **level or amount** effect" and $`a_4=b_3-b_4+b_5`$ as "the classic **mismatch hurts** term". The README, ADR-0002 and `fit.py` repeated this, and a draft summary called $`b_1+b_2`$ the "effect of the amount of care" and $`b_3-b_4+b_5`$ the "cost of mismatch".
- **Correction.**
  - $`a_1`$ is the slope along the line of congruence *at the centring point only*. The slope at level $`t`$ is $`a_1+2a_2t`$, so $`a_1`$ changes with the centring point whenever $`a_2\neq0`$.
  - $`a_4`$ is the curvature along the line of incongruence. A negative $`a_4`$ is consistent with a mismatch penalty but does not establish one.
  - A congruence effect needs a joint pattern: $`a_4<0`$, $`a_3=0`$, and a ridge on the line of congruence ($`p_{10}=0`$, $`p_{11}=1`$, or $`a_5=0`$ given $`a_3=0`$). It must be tested with confidence intervals and model comparison, on commensurable measures centred at a shared midpoint.
- **Files.**
  - Paper and docs: [`paper/08`](paper/08-mathematical-representation.md) §8.7 and the tables in §8.2, §8.12 and §8.13; README; [ADR-0002](docs/adr/0002-response-surface-for-fit.md).
  - Code: `src/love_translation/fit.py`. It adds $`a_5`$, `stationary_point()`, `principal_axes()` and `congruence_screen()`.
  - Tests: `tests/test_fit.py`, which now reproduces published worked examples.
- **Sources.**
  - Edwards, J. R. (2007), *Polynomial regression and response surface methodology*. **Full text** (author's manuscript). It is the source for:
    - the slope and curvature along $`Y=X`$ and $`Y=-X`$ evaluated at $`(0,0)`$ (eqs. 19–20);
    - the recommendation to centre at scale midpoints;
    - the stationary point and principal axes (eqs. 11–18);
    - the squared-difference constraints (eq. 10).

    The tests reproduce its worked example: a₁ = .196, a₂ = .052, a₃ = .432, a₄ = −.546; stationary point (−.951, −1.973); p₁₀ = −.875, p₁₁ = 1.154.
  - Schönbrodt, F. D., Humberg, S., & Nestler, S. (2018). **Full text** (accepted manuscript), pp. 3–7. It is the source for:
    - $`a_1`$ as the slope of the line of congruence above $`(0,0)`$;
    - $`a_3`$ as the locator of the peak of the line of incongruence;
    - the similarity conditions $`a_4<0`$, $`a_3=0`$ and ridge on the line of congruence ($`a_5=b_3-b_5=0`$);
    - commensurability and measurement invariance;
    - centring.

    The tests reproduce its Figure 1 surface.
  - Humberg, S., Nestler, S., & Back, M. D. (2019). **Not accessed** (the publisher refused automated access). The principal-axis form of the conditions is cited as recorded in the notes from **prior knowledge**, and it agrees with the two full texts above.
  - Shanock et al. (2010): **prior knowledge** for the formulas, which agree with both full texts. Their 2014 erratum ([10.1007/s10869-013-9317-6](https://doi.org/10.1007/s10869-013-9317-6)) was **not accessed**; the paper now tells readers to use it for significance tests. The reference code computes no standard errors.
- **Superseded statements kept in the notes.** [`evidence/notes/07-formal-models-and-methods.md`](evidence/notes/07-formal-models-and-methods.md), under "Response surface analysis (RSA) and successors": the bullet calling $`a_1`$ "the 'level' or 'amount' effect", and the bullet calling $`a_4`$ "the classic 'mismatch hurts' term".

### C2. The two routes read as if they classified kinds of acts

- **Earlier wording.**
  - Chapter 7 defined the substantive route with "(money, practical help, regulatory support)".
  - Chapter 10 and ADR-0004 said "I gave you everything" describes the substantive ledger and "you were never there" describes the symbolic one.
  - A draft summary paired provision with the substantive route and presence with the symbolic route.
- **Correction.** The routes are pathways of effect for any act, not categories of acts. The same act can meet needs (substantive) and be read as regard (symbolic). Money can communicate devotion; presence can meet a need for company, guidance or co-regulation whether or not it is read as love.
- **Files.** Paper chapters [`00`](paper/00-summary.md), [`01`](paper/01-question-and-thesis.md), [`07`](paper/07-revised-model.md), [`08`](paper/08-mathematical-representation.md) §8.8 and [`10`](paper/10-father-daughter-example.md); [ADR-0004](docs/adr/0004-two-routes-of-care.md); README; the at-a-glance figure.
- **Sources.** No empirical claim changed. Chentsova Dutton, Choi & Choi (2020) is now described as classifying kinds of support rather than testing routes. Its coefficients (financial support β = −.01, emotional support β = −.19 on distress) were read from the **full text** by the family-and-culture review ([`evidence/notes/05-family-and-culture.md`](evidence/notes/05-family-and-culture.md)).

### C3. The safety "gate" ranked unsafe options instead of excluding them

- **Earlier wording.** "Evaluate relationship states lexicographically, safety first: $`x\succ y\iff\mathrm{Safe}(x)>\mathrm{Safe}(y)`$ or [$`\mathrm{Safe}(x)=\mathrm{Safe}(y)`$ and $`\mathrm{Care}(x)\succ\mathrm{Care}(y)`$]". This was in chapter 8 §8.10, in ADR-0005 and in `constraints.lexicographic_prefers()`. When every option is unsafe, this rule still selects one.
- **Correction.** Safety is now an admissibility constraint:
  - $`\mathrm{Safe}(x)\in\{0,1\}`$ is decided from safety indicators, never from perceived love or care.
  - $`\mathcal F_{\text{safe}}=\{x\in\mathcal F:\mathrm{Safe}(x)=1\}`$, and outcomes are compared only within it.
  - If $`\mathcal F_{\text{safe}}`$ is empty, the model reports that no admissible arrangement exists and recommends nothing.

  Safety, autonomy and coercion stay analytically distinct from perceived love.
- **Files.**
  - Paper: [`paper/01`](paper/01-question-and-thesis.md), [`07`](paper/07-revised-model.md), [`08`](paper/08-mathematical-representation.md) §8.10 and its tables, [`15`](paper/15-counterexamples.md), [`18`](paper/18-proposed-study.md), [`19`](paper/19-limitations.md).
  - Decision records: [ADR-0005](docs/adr/0005-safety-as-lexicographic-gate.md) is marked superseded and kept unchanged; [ADR-0009](docs/adr/0009-safety-as-admissibility-constraint.md) is new.
  - Code: `constraints.py` gains `admissible()` and `choose()`, and `classify()` now reports `"unsafe"`.
  - Tests: `tests/test_constraints.py`.
  - Figures 1 and the at-a-glance figure.
- **Sources.** This is a modelling and normative change. The evidence cited for keeping safety separate is unchanged: Arriaga, Capezza & Daly (2016) and Lohmann et al. (2024), both checked at **abstract** level in [`evidence/notes/04-safety-coercion-autonomy.md`](evidence/notes/04-safety-coercion-autonomy.md).

### C4. Verification claims overstated what tests and DOI checks show

- **Earlier wording.** The README section "Guarantees and non-guarantees" said: "**Citations are real.**" and "**The math runs.** Every quantitative claim in §8 … is a test."
- **Correction.**
  - Unit tests verify the implementation, mathematical identities and reproduction of published worked examples. They do not validate any psychological mechanism.
  - A DOI that resolves with matching metadata shows bibliographic consistency, not that the study supports the claim attributed to it. Many findings were checked against abstracts only.
- **Files.** README ("What has and has not been checked"); [ADR-0008](docs/adr/0008-stdlib-only-reference-implementation.md); [`CONTRIBUTING.md`](CONTRIBUTING.md).
