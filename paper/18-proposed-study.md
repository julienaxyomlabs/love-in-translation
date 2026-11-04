# 18. A proposed empirical research design

## The Care Transmission Study: overview

The proposed study is designed to let the hypothesis lose. It combines a multi-informant observational component with two experiments, so that associations, predictions and causal effects are each tested by the design suited to them. Its primary arm studies **families in the Seoul metropolitan area with an emerging-adult child aged 19–29 and at least one parent**. A subsample of four-member families (both parents and two children aged 15 or older) supports round-robin analysis. Running the same protocol in one Western comparison country tests whether Korea differs in *levels* or in *rules*. A secondary arm applies the protocol to cohabiting romantic couples.

Sampling is stratified on four variables:
- household income, because care through provision is steeply class-graded;
- co-residence, because 54.4% of Koreans aged 19–34 live with parents ([Newsis, 11 Mar 2025](https://www.newsis.com/view/NISX20250311_0003094021));
- parents' working hours;
- **child gender**, because father–daughter versus father–son differences are almost undocumented.

## Hypotheses, rivals and falsification criteria

| Hypothesis (from this paper) | Competing hypothesis | Pre-registered result that would falsify ours |
|---|---|---|
| **H1 Detection.** Parent-logged care acts are missed more often in low-visibility channels (financial, practical) than in high-visibility ones (verbal, physical), beyond any effect of the child's sentiment | Misses reflect the child's sentiment (a criterion shift), not visibility | Visibility does not predict sensitivity or misses once the criterion is modelled; sentiment explains them |
| **H2 Level versus fit.** In response surfaces of need fulfilment and perceived regard, mismatch terms ($`a_3`$, $`a_4`$, cubic) add to the level term ($`a_1`$) | Amount: the level term dominates, and mismatch terms fall inside the smallest effect of interest | An equivalence test places all mismatch terms inside the pre-registered smallest effect of interest |
| **H3 Two routes.** Parent-enacted care predicts the child's material and educational outcomes beyond perceived regard, and perceived regard predicts emotional outcomes | All effects run through perception, or all through overall level | No direct path from enactment once perception is modelled; no difference in outcome signatures |
| **H4 Visibility asymmetry.** In vignette experiments, giving information about costs and constraints raises inferred regard for an *identical* provision act and softens judgments of absence | Regard is read from the act alone | The effect of cost information falls inside the smallest effect of interest |
| **H5 Developmental lag.** Parents' tracking of the child's needs is weaker, and biased toward an earlier developmental stage, when contact and disclosure are low, especially for autonomy needs | Gaps reflect projection or general accuracy, unrelated to contact | Contact and disclosure do not moderate tracking or directional bias |
| **H6 Relationship-specific misperception.** In round-robin families, relationship-specific variance in perceived care is non-negligible relative to perceiver variance | Misperception is a property of the perceiver | Relationship variance is negligible relative to perceiver variance |
| **H7 Filial-piety marker.** Low perceived regard from a parent predicts lower reciprocal but not authoritarian filial piety toward that parent | Both forms track general relationship quality | Both forms decline equally |
| **H8 Causal match versus amount (micro-randomized trial).** Prompts in the child's stated preferred channel raise evening perceived care more than equally intense prompts in other channels | Only intensity (amount) matters | The match effect falls inside the smallest effect of interest while the intensity effect is clear |

A further exploratory aim tests the **safety gate**. Below a safety threshold, care measures should stop predicting well-being. It is exploratory because of the ethical constraints below.

## Measures and observations

**Baseline measures** come in four groups:
- *Love and the relationship:* love components ([Sprecher & Fehr 2005](https://doi.org/10.1177/0265407505056439); [Mills et al. 2004](https://doi.org/10.1111/j.1475-6811.2004.00079.x)); the Korean short-form ECR-R ([Lee, Kim & Shin 2023](https://doi.org/10.1007/s10447-023-09503-6)); trust; relationship quality (the CSI for couples, with parallel items for parent–child dyads).
- *Parenting and family obligation:* parent and child versions of the PARQ; Korean psychological-control scales ([Choe et al. 2026](https://doi.org/10.1177/10731911261440140)); Sung's filial piety measure and the dual filial piety scale, after Korean validation; perceived parental sacrifice; basic need satisfaction.
- *Structure:* power (couples); work hours, income, stress, co-residence and contact.
- *Safety:* a confidential screen covering acts, control and fear ([Ford-Gilboe et al. 2016](https://doi.org/10.1136/bmjopen-2016-012824)).

**A 28-day dyadic diary** asks both members each evening, by channel:
- acts of care they performed, the care they intended, and the cost to them;
- acts of care they noticed from the other;
- the care they wanted and the care they received, on the same scale;
- perceived regard, and the motive they inferred behind the other's acts;
- felt closeness, mood, stress, trust and satisfaction;
- a prediction of the other's needs and ratings.

**Calibration** uses non-care vignettes to measure scale use. Standardized care-act vignettes, including provision acts with and without cost and constraint information, serve as outcome data rather than calibration.

**A laboratory session** records a support conversation and a disagreement. Both people then rate the recording segment by segment, and independent coders apply support and responsiveness codes ([Cutrona & Suhr 1992](https://doi.org/10.1177/009365092019002002); [Maisel, Gable & Strachman 2008](https://doi.org/10.1111/j.1475-6811.2008.00201.x)).

**End-of-period global ratings** ("how much care did you give or receive this month?") allow the memory decomposition in [Section 12](12-asymmetry-and-misperception.md). A **12-month follow-up** measures relationship quality, well-being, depressive symptoms, filial piety and, for couples, dissolution.

## The two experiments

**The micro-randomized trial** runs in diary weeks 3–4 with consenting dyads. Each day the parent is randomized either to no prompt or to a prompt to express care, in the child's stated preferred channel or in another channel. Prompt intensity is randomized separately. Because both members consent to the scheme, there is no deception. Causal excursion effects of channel match and of intensity are estimated on the child's same-evening perceived care, with trust and stated importance as moderators ([Qian et al. 2022](https://doi.org/10.1037/met0000283)).

**The vignette experiment** recruits unrelated adults and family members in separate samples. It holds a provision act constant while varying information about its cost and the giver's constraints, testing H4 without involving any participant's own family.

## Statistical methods

| Hypothesis | Primary analysis |
|---|---|
| H1 | Mixed-effects probit signal detection, with visibility and sentiment predicting sensitivity and criterion ([DeCarlo 1998](https://doi.org/10.1037/1082-989X.3.2.186)) |
| H2 | Dyadic and multilevel cubic response surfaces ([Nestler, Humberg & Schönbrodt 2019](https://doi.org/10.1037/met0000199); [Humberg et al. 2022](https://doi.org/10.1037/met0000352)); latent congruence models; equivalence tests ([Lakens, Scheel & Isager 2018](https://doi.org/10.1177/2515245918770963)) |
| H3 | Actor–partner models with mediation and sensitivity analyses; short-run causal estimates from the micro-randomized trial |
| H4 | Between-subjects experiment with equivalence testing |
| H5 | Truth-and-bias models over time; dynamic structural equation models ([Savord et al. 2023](https://doi.org/10.1080/10705511.2022.2065279)) |
| H6 | Social Relations Model on round-robin families ([Cook 1994](https://doi.org/10.1037/0022-006X.62.3.500)) |
| H7 | Structural models with reciprocal and authoritarian filial piety as separate outcomes |
| H8 | Causal excursion effects ([Klasnja et al. 2015](https://doi.org/10.1037/hea0000305)) |

Across all hypotheses:
- **Invariance.** Measurement invariance between Korea and the comparison country is tested before any mean comparison, by alignment if exact invariance fails.
- **Predictive benchmark.** Out-of-sample prediction of 12-month *change* is benchmarked against perceived partner commitment, appreciation and satisfaction ([Joel et al. 2020](https://doi.org/10.1073/pnas.1917036117)).
- **Sample size.** Numbers of dyads, families and days are set by simulation-based power analysis against pre-registered smallest effects of interest ([Lafit et al. 2021](https://doi.org/10.1177/2515245920978738)). Quadratic and interaction terms are notoriously underpowered ([Sommet et al. 2023](https://doi.org/10.1177/25152459231178728)), so planning should budget for several hundred dyads per country. No sample size is fixed here because it would be arbitrary without those simulations.

## Confounders and the causal graph

A pre-registered causal graph specifies the following confounders:
- **Global sentiment and love**, which colour both partners' reports and are measured and modelled explicitly.
- **The receiver's own giving**, the projection variable.
- **Stress and economic conditions**, which affect both capacity and perception.
- **Mental health of child and parent**, including child effects.
- **Contact and co-residence; socioeconomic status; prior relationship history; scale use; social desirability.**
- **Time-varying life events**, logged daily.

Perceived care is treated as a possible collider, so it is not adjusted for when estimating the effect of enacted care. Taking part in the study is itself treated as a possible intervention. A one-session awareness intervention cut break-up as much as skills programmes did ([Rogge et al. 2013](https://doi.org/10.1037/a0034209)), so an assessment-only control group with minimal diary burden estimates reactivity.

## Ethical constraints

Couple and family research raises issues that standard regulations address poorly: confidentiality among members, consent with several members (including minors), shared data, harms to the family unit, and abuse reporting ([Margolin et al. 2005](https://doi.org/10.1037/0893-3200.19.1.157)) [Established]. The protocol therefore commits to six safeguards:
1. **Confidentiality.** No member's responses are ever shown to another member. Each uses a separate device and account.
2. **No deception.** No deceptive manipulation of messages attributed to real family members, because deceptive standard-note paradigms with real partners can do relational harm ([Collins & Feeney 2004](https://doi.org/10.1037/0022-3514.87.3.363)).
3. **Consent and assent.** Assent from minors and parental consent for them.
4. **Safety first.** Safety screening, distress protocols, referral resources and disclosed reporting obligations. Any indicator of coercion or violence triggers safety procedures that override research aims.
5. **Non-blaming framing.** Feedback and materials never frame abuse or control as a mutual "translation" problem.
6. **Proportionate burden.** Compensation for diary burden and an unconditional right to withdraw.

## What results would weaken or disprove the framework

The framework would be **substantially disproved** for this population by any of four results:
- mismatch terms falling inside the smallest effect of interest while the level term dominates (H2);
- negligible relationship-specific variance relative to perceiver variance (H6);
- a null match effect alongside a clear intensity effect in the micro-randomized trial (H8);
- translation constructs adding no out-of-sample prediction of change beyond perceived commitment and appreciation.

It would be **partly disproved** by any of four further results:
- no direct substantive route (H3);
- no effect of cost information on inferred regard (H4);
- misses explained entirely by the receiver's sentiment (H1);
- global "90 versus 40" gaps that vanish after the memory and scale-use steps of the decomposition.

Conversely, clear mismatch curvature, non-trivial relationship-specific variance, a match effect at fixed intensity and incremental prediction of change would support the revised hypothesis. Each would hold only for the population, channels and timescale studied.

---

**Navigation:** [← What testing requires](17-what-testing-requires.md) · [Contents](README.md) · [Limitations →](19-limitations.md)
