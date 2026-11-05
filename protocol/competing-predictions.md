[Overview](../audit/README.md) · [Part A: evidence audit](../audit/evidence-audit.md) · **Part B: competing predictions** · [Part C: study protocol](study-protocol.md) · [Corrections](../audit/corrections.md)

# Part B: Competing predictions

This part asks three questions about the translation framework of *Can Love Be Lost in Translation?* (version 0.2.0):

1. Which of its parts predict something that four simpler explanations do not?
2. Which observations would favour one model over another?
3. Where can no realistic design tell them apart?

The framework is treated as frozen. Its chain of distinctions holds that love intended ≠ love expressed ≠ love perceived ≠ love received ≠ relationship compatibility. For care from A to B at occasion $`t`$, the chain is written as ten components (`README.md`, "Model at a glance"; `paper/08-mathematical-representation.md` §8.4–8.10):

```math
\begin{aligned}
&\text{(1) Enactment}     && E_{A\to B}(t) = g\big(I_{A\to B}(t),\ \tilde N_{A\to B}(t)\big), \quad E_{A\to B}(t)\in\mathcal C_A(t)\\
&\text{(2) Detection}     && \Pr\big(D_{B,k}(t)=1\big) = \Phi\big(-c_B + d'_B\,\mathbf 1[E_{A\to B,k}(t)>0] + \gamma\,v_k\big)\\
&\text{(3) Construal}     && Q_B(t)-\mu = \tau\,\big(X_A(t)-\mu\big) + \pi\,\big(O_B(t)-\mu\big) + \delta\big(T_B(t)\big) + u_B(t)\\
&\text{(4) Motive}        && \Pr(w\mid \text{act}) \propto \Pr(w)\,\sigma\big(\beta\,(w\,b-\hat c)\big)\\
&\text{(5) Fit}           && \mathbf S_B(t) = \boldsymbol\Lambda\,\mathbf E_{A\to B}(t), \qquad h(S,N) = b_0+b_1S+b_2N+b_3S^2+b_4SN+b_5N^2\\
&\text{(6) Two routes}    && \mathbf Y_B(t) = \boldsymbol\alpha + \boldsymbol\beta_{\text{sub}}\,h\big(S_B(t),N_B(t)\big) + \boldsymbol\beta_{\text{sym}}\,Q_B(t) + \boldsymbol\Gamma\,\mathbf x(t) + \mathbf e(t)\\
&\text{(7) Trust}         && T_B(t+1) = T_B(t) + \eta\,\big[p\big(Q_B(t),T_B(t)\big)-T_B(t)\big] + \varepsilon(t)\\
&\text{(8) Giver's model} && \tilde N_{A\to B}(t+1) = \tilde N_{A\to B}(t) + \lambda(t)\,\big[N_B(t)-\tilde N_{A\to B}(t)\big] + \xi(t)\\
&\text{(9) Compatibility} && \mathcal F = \big\{x\in\mathcal C_A\times\mathcal C_B : G_A(x)\ge 0,\ G_B(x)\ge 0,\ W_A(x)\ge w_A^{\min},\ W_B(x)\ge w_B^{\min}\big\}\\
&\text{(10) Safety}       && \mathcal F_{\text{safe}} = \{x\in\mathcal F : \mathrm{Safe}(x)=1\}; \ \text{outcomes are compared only within } \mathcal F_{\text{safe}}
\end{aligned}
```

Three rules from v0.2.0 govern everything below:

- **The substantive and symbolic routes are pathways of effect, not kinds of act.** Any act, provision or presence alike, can change B's circumstances and needs through $`h`$ ($`\beta_{\text{sub}}`$) and be read as regard through $`Q`$ ($`\beta_{\text{sym}}`$). $`\beta_{\text{sub}}`$ is defined as the part of an act's effect that does *not* pass through perceived regard (§8.8).
- **Safety is an admissibility constraint**, $`\mathcal F_{\text{safe}}=\{x\in\mathcal F:\mathrm{Safe}(x)=1\}`$, decided from safety indicators and never from perceived love.
- **Autonomy is an independent outcome.**

Neither safety nor autonomy appears below as a term that could be traded against satisfaction, and no rival is credited with explaining a safety or autonomy result by appeal to care.

The four rivals are:

1. the total amount of support received predicts outcomes;
2. perceived support alone predicts outcomes;
3. need fulfilment predicts outcomes;
4. existing trust or attachment explains the apparent translation effect.

Evidence is cited with the verification depth a primary-source audit reached in November 2026: full text, abstract, or secondary (press or practitioner summaries). No new theoretical equation is introduced. Where a prediction needs a statistical statement, it is written as a restriction on the parameters of equations (1)–(10).

## Two definitional points decide what can be tested at all

**First, "not through perceived regard" is not the same as "unperceived".** The substantive route does not require the receiver to miss the act. It requires only that some of the act's effect does not run through $`Q`$. A receiver who notices that a partner cooked dinner and is less exhausted as a result shows a substantive effect, whether or not the meal also reads as love. Evidence that benefit occurs without the receiver noticing would therefore be sufficient for $`\beta_{\text{sub}}\neq0`$, but it is not necessary.

The converse matters more. Evidence that invisible support works by sparing the receiver a negative reading is evidence about construal, which is the symbolic route. That is what the best experiment shows: in Bolger & Amarel's (2007) Study 3, about 45% of the distress caused by support that signalled inefficacy ran through reflected appraisal of inefficacy ([Bolger & Amarel 2007](http://www.columbia.edu/~nb2229/docs/bolger-amarel-support-experiments-2006.pdf); full text). The paper's phrase "a non-perceptual route exists" (`paper/08-mathematical-representation.md:231`) conflates the two definitions.

**Second, the meaning of the route split depends on what $`S`$ is made of.** In equation (5), supply on the need metric is produced by enacted care through the translation matrix, $`\mathbf S_B=\boldsymbol\Lambda\,\mathbf E_{A\to B}`$. The v0.2.0 glossary (§8.2), however, measures $`S`$ by the receiver's report: "How much $`k`$ did you want / receive?" If $`S`$ is the receiver's report, two things follow:

- $`h(S,N)`$ and $`Q`$ come from the same reporter, so equation (6) separates two of the receiver's perceptions, of supply and of regard. It does not separate perceived effects from unperceived ones.
- The substantive term becomes nearly indistinguishable from rivals 1 and 3.

The split can be read as "effects carried by what the giver actually did, not through the receiver's regard" only under one of three conditions:

- $`S`$ is built from giver-logged or observer-coded $`E`$ through equation (5), with a pooled and structured $`\boldsymbol\Lambda`$ (§8.11 notes that $`\boldsymbol\Lambda`$ cannot be estimated for a single dyad);
- $`E`$ is randomised;
- both versions are estimated and reported.

This is a choice about identification, not a change to the equations. It recurs below because it decides two of the four comparisons.

## What each route predicts

Table B1 derives eight falsifiable predictions from the two routes, states the observation that would count against each, and summarises the audited evidence so far.

| ID | Route | Prediction, in v0.2.0 terms | Observation that would count against it | Design that can make the observation | Audited evidence so far |
|---|---|---|---|---|---|
| P1 | Substantive | With $`E`$ logged by the giver or randomised, part of $`E`$'s effect on substantive outcomes remains once $`Q`$ is held fixed: $`\beta_{\text{sub}}\neq0`$ in (6) | The direct effect falls inside a pre-registered smallest effect size of interest (SESOI), and a sensitivity analysis shows that no plausible confounding could be hiding one | Giver logs or a micro-randomised trial (MRT) for the total effect; mediation with sensitivity analysis for the split | **No audited study shows it.** The invisible-support diary pattern did not replicate (see below). The laboratory benefit ran through a perception. The income studies measured no perception. One unaudited study reports invisible emotional support predicting goal achievement over a year without raising perceived support ([Girme, Overall & Simpson 2013](https://doi.org/10.1177/0146167213497802); abstract) |
| P2 | Substantive | A substantive benefit does not require detection. On days a giver-logged act goes unregistered (a miss in equation 2), need-relevant outcomes in that channel exceed those on days with no act | Miss days do not differ from no-act days on need-relief outcomes | Paired diaries with signal-detection coding (observational) | Untested. The diary evidence measured gratitude only |
| P3 | Substantive | Supply helps according to need: the surface in (5) shows the joint congruence pattern ($`a_4<0`$, $`a_3=0`$, ridge on $`S=N`$) or a directional variant, not a plain rise along $`S`$ | An equivalence test places every mismatch term inside the SESOI while the level term is clear | Multilevel response surface analysis on commensurate $`N`$ and $`S`$ | No care-channel surface has been published. The closest study measured a perceived direction of discrepancy, not commensurate need and supply ([Brock & Lawrence 2009](https://pmc.ncbi.nlm.nih.gov/articles/PMC2776033/); full text) |
| P4 | Both [Our hypothesis, §8.8] | $`\beta_{\text{sub}}`$ loads on material, behavioural and educational outcomes; $`\beta_{\text{sym}}`$ on emotional and relational outcomes | No difference in outcome signatures | Models with several outcomes, some of them not self-reported | Consistent but weak. Casino income reduced conduct symptoms but not anxiety or depression ([Costello et al. 2003](https://pubmed.ncbi.nlm.nih.gov/14559956/); abstract). The authors attribute part of the education and arrest effects to better parenting ([Akee et al. 2010](https://pmc.ncbi.nlm.nih.gov/articles/PMC2891175/); full text) |
| P5 | Symbolic | $`Q`$ predicts emotional and relational outcomes within persons and with a lag, beyond the amount received and need fulfilment | The within-person, lagged increment of $`Q`$ falls inside the SESOI | Dynamic structural equation models on diaries | Associational and mostly same-reporter: own perceptions explained 45% of baseline satisfaction ([Joel et al. 2020](https://escholarship.org/content/qt8mc5n2c3/qt8mc5n2c3.pdf); full text); perceived acceptance correlated r = .51 with adjustment ([Khaleque & Rohner 2002](https://api.crossref.org/works/10.1111/j.1741-3737.2002.00054.x); abstract) |
| P6 | Symbolic | $`Q`$ depends on features of the act, not only on the perceiver: visibility shifts $`d'`$ in (2); cost information raises inferred regard for an identical act in (4); a matched channel at fixed intensity raises $`Q`$ through (3) and (5) | None of these effects lies outside the SESOI | Signal-detection diaries, a vignette experiment and an MRT | Partly. Clearly supportive notes were appraised alike regardless of attachment ([Collins & Feeney 2004](https://doi.org/10.1037/0022-3514.87.3.363); full text). Daily counts of benefits received tracked the partner's reported giving (.36) as much as one's own (.34) ([Lemay, Clark & Feeney 2007](https://doi.org/10.1037/0022-3514.92.5.834); full text) |
| P7 | Symbolic | The same act can carry opposite regard: support that signals the receiver's inefficacy lowers construal and raises distress at constant content | Framing has no effect at constant content | Laboratory experiments; visibility codes in diaries | Supported in a laboratory analogue with strangers: the inefficacy message raised distress by 1.09 units against no support (d = 0.66), while content alone had no effect ([Bolger & Amarel 2007](http://www.columbia.edu/~nb2229/docs/bolger-amarel-support-experiments-2006.pdf); full text) |
| P8 | Symbolic | Acts that go unregistered bring no regard: gratitude and $`Q`$ do not rise on miss days | Misses raise gratitude as hits do | Paired diaries | Supported in two short diaries. Same-day gratitude rose on hit days (b = .19, .38) and false-alarm days (b = .18, .41), but not on miss days (b = −.11, p = .159; b = .03, p = .671) ([Visserman et al. 2019](https://doi.org/10.1177/1948550618757599); full text) |

**The asymmetry in this table is the main empirical finding of Part B.** The symbolic route has direct, if mostly associational or laboratory, support (P5–P8). The substantive route's defining prediction (P1) has none that survives audit. The original invisible-support diary pattern was not reproduced by the same group in a replication with 312 examinees and 310 partners, more than three times the original sample. In that replication, provider-reported emotional support was often associated with *more* anger, anxiety, depressed mood and fatigue ([Shrout et al. 2010](https://psychology.columbia.edu/sites/psychology.columbia.edu/files/2016-11/shrout-2009-support%20transaction%20chapter_0.pdf); author manuscript, full text).

## Rival 1: the total amount of support received predicts outcomes

**The rival.** Outcomes depend on how much care arrives, summed over channels. It has two variants:
- **1a**, total support as the receiver reports it;
- **1b**, total care as the giver enacts it.

In v0.2.0 terms the rival makes three claims:
- the surface in (5) reduces to a rise along $`S`$, with no congruence pattern;
- the identity of a channel carries no information at a fixed total, so $`\boldsymbol\Lambda`$ adds nothing beyond scale;
- $`Q`$ adds nothing once the total is known.

| Observation | Translation framework predicts | Rival 1 predicts | Audited evidence so far |
|---|---|---|---|
| Response surface over commensurate need and supply (5) | Joint congruence pattern, or a directional variant ($`a_3\neq0`$, cubic terms) where deficit and excess differ | Outcomes rise with $`S`$; mismatch terms inside the SESOI | None for care channels. The closest study cannot test this: its "over-provision" was the share of behaviours the recipient wanted less of ([Brock & Lawrence 2009](https://pmc.ncbi.nlm.nih.gov/articles/PMC2776033/); full text) |
| Randomised prompts at fixed intensity, in the receiver's highest-need channel versus another channel | Matched prompts raise same-evening $`Q`$ and need relief more | Only intensity matters | No study. This is hypothesis H8 of the v0.2.0 design (`paper/18-proposed-study.md:24`) |
| Same content, different framing | Framing that signals inefficacy lowers benefit at a constant amount | Framing is irrelevant at a constant amount | Against rival 1, in a laboratory analogue: framing changed distress while content did not ([Bolger & Amarel 2007](http://www.columbia.edu/~nb2229/docs/bolger-amarel-support-experiments-2006.pdf); full text) |
| What predicts same-day gratitude: acts the receiver perceives, or acts the giver reports? | Gratitude follows detection | Under 1b, gratitude follows enacted acts | Against 1b for gratitude: false alarms raised gratitude and misses did not ([Visserman et al. 2019](https://doi.org/10.1177/1948550618757599); full text). The criterion is the partner's self-report |
| One's own love versus love received | Silent: one's own love feeds intention in (1) | Silent | Own love and commitment predict whether non-marital relationships last ([Le et al. 2010](https://api.openalex.org/works/doi:10.1111/j.1475-6811.2010.01285.x); abstract). This fits both models, because love received was not measured |
| Extra weight of a "primary love language" | Not a v0.2.0 prediction: fit is defined on needs | No extra weight | No extra weight, and relationship quality tracked satisfaction with many behaviours ([Flicker et al. 2025](https://pubmed.ncbi.nlm.nih.gov/40977357/); abstract). This also fits both models |

**What would decide it.**
- **Favours the framework:** congruence curvature whose confidence intervals exclude the SESOI, together with a match effect at fixed intensity in the MRT.
- **Favours rival 1:** a two one-sided equivalence test (TOST) places every mismatch term inside the SESOI while the level term is clear, and the match effect is null while the intensity effect is clear. These are v0.2.0's own falsification criteria for H2 and H8 (`paper/18-proposed-study.md:18`, `:24`).

**Where the two cannot be told apart.**
- **When need and supply rarely diverge.** The surface is then extrapolated into regions with few observations.
- **When quadratic and interaction terms are underpowered.** The median power to detect a typical interaction in 159 published studies was .18 ([Sommet et al. 2023](https://doi.org/10.1177/25152459231178728); abstract).
- **When "the preferred channel" is undefined.** Fewer than half of one US sample had an identifiable primary love language (Flicker et al.). The MRT's match contrast should therefore be defined from the receiver's own report of need on the previous evening, not from a trait-like preference.
- **When the substantive term is built from receiver reports.** Against variant 1b, the substantive route makes the same prediction (enacted care helps) unless need matters. Without fit curvature, $`\beta_{\text{sub}}\,h`$ collapses into "amount".

## Rival 2: perceived support alone predicts outcomes

**The rival.** Enacted care matters only through the receiver's perception, so $`\beta_{\text{sub}}=0`$ in (6). A strong variant, **2b**, adds that perception is mostly generated by the perceiver: $`\pi`$ dominates and $`\tau\approx0`$ in (3).

**The symbolic-route-only version of the framework is observationally identical to rival 2 for outcomes.** The framework claims more in only two places:
- a non-zero $`\beta_{\text{sub}}`$;
- the claim that $`Q`$ is formed by features of the act, as described in (2)–(4).

| Observation | Translation framework predicts | Rival 2 predicts | Audited evidence so far |
|---|---|---|---|
| Direct path from giver-logged or randomised $`E`$ to substantive outcomes, with $`Q`$ held fixed | $`\beta_{\text{sub}}\neq0`$ | $`\beta_{\text{sub}}=0`$ | None that survives audit (P1 above) |
| How $`E`$'s effects scale across several outcomes | Effects depart from proportionality, mostly in material, behavioural and educational outcomes | If every effect passes through the single mediator $`Q`$, $`E`$'s effects across outcomes scale with $`Q`$'s effects on them | Untested. The test assumes the effects of $`Q`$ on outcomes are unconfounded, which is a strong assumption |
| Need relief on miss days versus days with no act | Higher on miss days | Equal | Untested |
| Perceived supportiveness versus benefit | Can diverge | Equivalent by definition | Diverged in the laboratory: visible support was rated more supportive (5.2 versus 2.6 on a 0–10 scale), even in the condition that raised distress (4.6) (Bolger & Amarel 2007; full text) |
| Does $`Q`$ track acts net of projection? | $`\tau>0`$, and randomised acts move $`Q`$ | Under 2b, $`\tau\approx0`$ | Against 2b. Global perceived responsiveness was dominated by projection (own path β .47–.60 versus the partner's .17–.22), but daily benefits tracked the partner's giving ([Lemay, Clark & Feeney 2007](https://doi.org/10.1037/0022-3514.92.5.834); full text). Tracking accuracy for judgments of a partner's love was r = .40 ([Fletcher & Kerr 2010](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.471.1954&rep=rep1&type=pdf); full text) |
| Incremental prediction from partner reports | Some increment, at least for change | None | For rival 2 at the level of prediction: partner reports added 0.0–1.9% at baseline and 0.9–3.5% at follow-up, and change was predicted no better than 5% ([Joel et al. 2020](https://escholarship.org/content/qt8mc5n2c3/qt8mc5n2c3.pdf); full text) |

**What would decide it.** Only three kinds of evidence separate the framework from rival 2:
- a direct effect of independently measured or randomised enactment on outcomes the receiver does not report, such as behavioural, educational or task records, that survives a pre-registered sensitivity analysis;
- benefit on miss days in substantive outcomes;
- outcome signatures that are not proportional.

Strong variant 2b fails already on the evidence above. Randomised prompts that move same-evening $`Q`$ would refute it causally.

**Where they cannot be told apart.**
- **For emotional and relational outcomes reported by the same person on the same evening as $`Q`$**, any analysis favours rival 2 mechanically through shared method.
- **Randomising $`E`$ identifies only its total effect.** The split between routes then rests on sequential ignorability of the mediator, which data cannot verify ([Imai, Keele & Yamamoto 2010](https://doi.org/10.1214/10-STS321); abstract).
- **Randomising $`Q`$ itself in real dyads** would mean deceptive messages attributed to a partner, which the v0.2.0 design rules out (`paper/18-proposed-study.md:90`).

## Rival 3: need fulfilment predicts outcomes

**The rival.** Outcomes depend on how far the receiver's needs are met, whether measured globally or within the relationship. It does not matter which act met them, or whether the act was read as regard. Translation (detection, channel, construal) matters only through need fulfilment, and $`Q`$ adds nothing once fulfilment is known.

**How it relates to the framework.** The substantive route in (6) is itself a need-fulfilment term, $`h(S,N)`$. If $`S`$ is reported by the receiver, rival 3 is close to "the substantive route only". The framework then differs from rival 3 in two places:
- it claims that regard adds to need fulfilment ($`\beta_{\text{sym}}>0`$ given $`h`$);
- it describes how acts become fulfilment ($`\boldsymbol\Lambda`$ and detection).

| Observation | Translation framework predicts | Rival 3 predicts | Evidence so far |
|---|---|---|---|
| $`Q`$'s increment over relationship-specific need satisfaction, for relational outcomes, within persons and lagged | Positive | Zero | Untested. Need fulfilment predicted relationship functioning for both partners ([Patrick et al. 2007](https://doi.org/10.1037/0022-3514.92.3.434); abstract, not audited as a claim) |
| Latent correlation between $`Q`$ and relatedness need satisfaction | Distinct constructs (correlation below 1) | Possibly one construct | Untested. No Korean validation of the Perceived Responsiveness and Insensitivity scale (PRI) was found. The Korean need-satisfaction scale is validated only in cancer survivors ([Yeom & Lee 2024](https://doi.org/10.3390/healthcare12242535); full text) |
| Channel-level fit beyond global need satisfaction | Adds | Adds nothing | Untested |
| Fulfilment from the partner versus from any source | The partner's regard matters for outcomes specific to that relationship | Fulfilment from any source substitutes | Need fulfilment varies across partners and predicts attachment security in each relationship ([La Guardia et al. 2000](https://doi.org/10.1037/0022-3514.79.3.367); abstract) |
| Randomised matched prompts | Raise $`Q`$ even when need relief does not change | Act only through need relief | Untested |

**What would decide it.** The framework is favoured only if two conditions hold together:
- in a measurement phase, $`Q`$ and relatedness need satisfaction prove distinct latent constructs;
- $`Q`$ then predicts relational outcomes within persons and with a lag, beyond relationship-specific need satisfaction.

**Rival 3 is favoured** if $`Q`$'s increment falls inside the SESOI once discriminant validity is established.

**Where they cannot be told apart.**
- **If the two constructs are one.** In self-determination theory, relatedness satisfaction includes feeling cared for. If the latent correlation approaches 1, no analysis of outcomes can separate the symbolic route from rival 3.
- **If need fulfilment is the receiver's report of supply adequacy.** It is then $`h(S,N)`$ under another name.

## Rival 4: existing trust or attachment explains the apparent translation effect

**The rival.** Stable trust, or attachment insecurity, lowers both perceived regard and outcomes. "Translation failures" such as misses, or regard that falls short of the care enacted, are symptoms of the perceiver's disposition. Features of the act add nothing.

**How it relates to the framework.** The framework already places trust inside construal ($`\delta(T)`$ in (3)) and lets regard update trust in (7). Attachment effects on bias are expected to depend on how ambiguous a signal is (§8.6). A loss driven by trust is therefore translation in the framework's own terms. Rival 4's distinctive claim is that translation *reduces to* a trait of the perceiver: visibility, channel, cost information and fit specific to the pair add nothing, and influence runs from trust to perception only.

| Observation | Translation framework predicts | Rival 4 predicts | Evidence so far |
|---|---|---|---|
| Effects of translation indices after person-mean centring and lagged state trust | Persist within persons | Vanish (if purely a trait) | Untested in this form |
| Signal-detection decomposition | Visibility shifts sensitivity $`d'`$ | Misses are shifts in criterion $`c`$, tied to trust or sentiment | Untested. This is hypothesis H1 (`paper/18-proposed-study.md:17`) |
| Clear versus ambiguous acts | Attachment effects depend on ambiguity | Attachment colours the reading of every act | Against the strong rival. Appraisal of clearly supportive notes was driven by their content (β = .66), with no attachment effect. Attachment effects on hurtful appraisals of low-support notes were small (sr² ≈ .06), weaker for moderately supportive genuine notes and absent for very supportive ones ([Collins & Feeney 2004](https://labs.psych.ucsb.edu/collins/nancy/UCSB_Close_Relationships_Lab/Publications_files/Collins%20and%20Feeney,%202004.pdf); full text) |
| Variance in a family round robin | A non-negligible variance specific to each relationship, even after trust and attachment specific to that relationship | Variance from perceivers dominates | Indirect. The perceiver × supporter pairing was the largest variance component ([Lakey et al. 1996](https://pubmed.ncbi.nlm.nih.gov/8667167/); abstract). Family studies find perceiver and relationship effects most important ([Eichelsheim et al. 2009](https://doi.org/10.1111/j.1741-3737.2009.00652.x); abstract) |
| Randomised prompts | Affect $`Q`$ at a given level of stable trust | Can moderate an effect, never explain it away | Untested |
| Direction of influence over time | Trust shapes regard ($`\delta(T)`$) and regard updates trust (7) | Trust shapes regard only | Lower-trust people's perceived relationship quality varied more from day to day ([Campbell et al. 2010](https://doi.org/10.1037/a0019714); abstract) |
| Apparent misfit | Fit in (5) | Attachment produces apparent over-provision | Attachment was among the predictors of over-provision ([Brock & Lawrence 2014](https://doi.org/10.1037/a0035280); abstract) |

**What would decide it.**
- **Favours the framework:**
  - translation indices that predict outcomes within persons after centring and after lagged state trust;
  - visibility effects on $`d'`$ net of criterion;
  - relationship-specific variance that remains after relationship-specific attachment and trust are measured;
  - an MRT effect of match on $`Q`$, which stable trust cannot confound.
- **Favours rival 4:** misses explained by the criterion alone, and variance dominated by perceivers.

**Where they cannot be told apart.**
- **Trust measured on the same evening as $`Q`$.** The order within a day is then unknown.
- **Relationship-specific variance, $`\gamma_{ij}`$, if trust specific to that relationship is unmeasured.** Translation and relationship-specific trust then predict the same pattern.
- **Feedback loops slower than the study.** Loops that run $`Q\to T\to Q`$ over months or years are beyond the study's window. The reading function $`p(\cdot)`$ and any bistability are practically unidentifiable, as v0.2.0 itself says (§8.13).

## Where realistic designs cannot separate the models

Seven boundaries hold for any study a research group could realistically run.

1. **The route split is never fully identified.** Randomising enactment identifies its total effect. Dividing that effect into $`\beta_{\text{sub}}`$ and $`\beta_{\text{sym}}`$ needs no unmeasured same-day confounding of $`Q`$ and the outcome, for example by mood, stress or trust. That assumption can be bounded by sensitivity analysis but not tested. Manipulating $`Q`$ in real dyads would require deception.
2. **At the level of outcomes, the symbolic route is rival 2.** Only the formation of $`Q`$ (equations 2–4) separates them.
3. **The substantive route is close to rivals 1 and 3 whenever supply is the receiver's report.** It can be distinguished only if supply is built from giver logs or observer codes, through a pooled $`\boldsymbol\Lambda`$, or if enactment is randomised.
4. **Regard and relatedness need satisfaction may be one construct.** If so, no outcome analysis can separate the symbolic route from rival 3.
5. **Rival 4 is partly nested in the framework.** A principled line between "trust-driven translation" and "trust instead of translation" has to be drawn in advance, as a test of whether features of the act add anything beyond the perceiver.
6. **Large provision cannot be randomised.** Large transfers between parent and child, such as money, housing or tuition, can vary exogenously only through natural experiments. The audited natural experiments measured no perception ([Costello et al. 2003](https://pubmed.ncbi.nlm.nih.gov/14559956/); abstract; [Akee et al. 2010](https://pmc.ncbi.nlm.nih.gov/articles/PMC2891175/); full text). For provision, the route split remains unidentifiable.
7. **Change may be too small to detect.** Change in relationship quality was predicted no better than 5% (Joel et al. 2020). Lagged communication effects at 9-month intervals were weak and inconsistent ([Lavner, Karney & Bradbury 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC4852543/); full text). Detection did not predict gratitude at follow-ups of three months and one year (Visserman et al. 2019). A null result on long-run prediction counts against the framework only if the study was powered for a pre-registered SESOI.

## Distinguishability, by part of the theory

The codes in the table are:
- **C:** separable causally, by randomisation;
- **A:** separable associationally;
- **S:** separable only under sequential ignorability, with sensitivity analysis;
- **N:** not separable with realistic designs;
- **—:** the rival makes no competing claim.

| Part of the theory | vs rival 1 (amount) | vs rival 2 (perception alone) | vs rival 3 (need fulfilment) | vs rival 4 (trust or attachment) |
|---|---|---|---|---|
| Detection (2) | A (paired diaries) | C (prompts as a known signal) | — | A ($`d'`$ versus $`c`$) |
| Construal $`\tau,\pi,\delta`$ (3) | — | A; C for $`\tau`$ in an MRT | — | A (bias moderated by ambiguity, within persons) |
| Inferring regard from cost (4) | C (vignettes) | C (vignettes) | — | C (vignettes involve no relationship trust) |
| Fit surface (5) | A (response surface analysis); C for same-evening outcomes (MRT) | — | A, only if the constructs are distinct | A |
| Symbolic route, $`\beta_{\text{sym}}`$ (6) | A | **N** at the outcome level | A, only if discriminant validity holds | A (within persons, lagged) |
| Substantive route, $`\beta_{\text{sub}}`$ (6) | S; N against variant 1b if there is no fit curvature | **S** | S if $`S`$ comes from giver logs; N if it comes from the receiver | S |
| Relationship-specific misperception (§8.11) | — | — | — | A, conditional on measured relationship-specific trust |
| Trust dynamics (7) | — | — | — | A (dynamic structural equation models); direction only partly |
| Giver's learning rate $`\lambda`$ (8) | — | — | — | N in practice |
| Intended ≠ expressed (1) | N (intention unmeasured) | — | — | — |
| Compatibility (9) | N | N | N | N |

## Open problems for external critics

**The proportionality test.** It is the cleanest outcome-level contrast with rival 2, but it assumes that the effects of $`Q`$ on outcomes are unconfounded. Same-day sentiment inflates $`Q`$'s association with emotional outcomes more than with behavioural ones, which could mimic a substantive signature.

**What $`S`$ is made of.** Whether $`S`$ in (6) should mean supply as the receiver reports it, or supply implied by enacted care through $`\boldsymbol\Lambda`$, is a choice the v0.2.0 text leaves implicit. That choice decides whether the route split is about perception at all.

**Where trust stops being translation.** Rival 4 needs a pre-registered criterion for when a loss driven by trust counts as translation. Otherwise the framework can absorb any result about trust.

**The matching criterion.** Matching on stated preferences is undermined by unstable love-language classifications. Matching on day-level need reports raises confidentiality questions, discussed in [Part C](study-protocol.md#safety-autonomy-and-ethics-procedures).

**Generalisation beyond the Korean case.** A Korean study is a case study. Its estimates describe the sampled population, channels and timescale, and cannot license claims about "Korean families" or about other cultures without tests of invariance across countries.
