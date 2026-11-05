# 8. A mathematically rigorous representation, with explicit assumptions

## Model at a glance

> **Status: a structural hypothesis, not a validated model.** Every parameter below is unknown and nothing has been estimated. The unit tests check that the code implements these equations and reproduces published worked examples; they do not show that any mechanism is true. Resolving all cited DOIs shows the references point to the right works, not that each work supports every claim attributed to it.

![The model at a glance: ten components, two routes, compatibility and safety](figures/model-at-a-glance.png)

The model runs in both directions at once (swap A and B). For care from A to B at occasion $`t`$:

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

### What each equation says, and how well it is supported

The columns keep three things apart: the statistical method (is the tool standard?), the psychological evidence (is the mechanism observed?), and what is original to this project (untested).

| # | In words | Statistical method | Psychological evidence | Original to this project | Details |
|---|---|---|---|---|---|
| 1 | A acts on intention and on A's picture of B's needs, but only within what A can actually do. | none needed: a constraint | Stress dampened husbands' provider-reported support for perceived needs on high-stress days, slope .81 against .72 ([Neff, Nguyen & Williamson 2021](https://doi.org/10.1177/0146167220974490)) [Preliminary] | Constraint form [Assumption] | [§8.4](#84-component-1-enactment-under-capacity) |
| 2 | Whether B registers an act depends on B's sensitivity and threshold, and on how visible the act is. | Signal detection as a mixed-effects probit ([DeCarlo 1998](https://doi.org/10.1037/1082-989X.3.2.186)) [Established method] | About half of partner-reported sacrifices went undetected, 46–47% of sacrifice days in two short diaries ([Visserman et al. 2019](https://doi.org/10.1177/1948550618757599)) [Moderate/mixed] | Visibility term $`\gamma v_k`$ [Our hypothesis] | [§8.5](#85-component-2-detection) |
| 3 | Perceived care tracks what A did ($`\tau`$), projects B's own care ($`\pi`$) and is shifted by a level bias ($`\delta`$). | Truth-and-bias model ([West & Kenny 2011](https://doi.org/10.1037/a0022936)) [Established method] | Projection ([Lemay, Clark & Feeney 2007](https://doi.org/10.1037/0022-3514.92.5.834)) [Moderate]; partners track each other moderately well (r ≈ .40 for judgments of the partner's love), with a small mean-level bias that is positive overall (r = .09) but slightly negative for perceived love (r = −.11, k = 7) ([Fletcher & Kerr 2010](https://doi.org/10.1037/a0019792)) [Established; love-specific sign Moderate/Preliminary] | Bias that depends on trust, $`\delta(T)`$ [Our hypothesis] | [§8.6](#86-component-3-construal-and-motive-inference) |
| 4 | B infers how much A values B from what B believes the act cost A. | Bayesian inverse planning ([Jara-Ettinger et al. 2016](https://doi.org/10.1016/j.tics.2016.05.011)) [Established in laboratory cognition] | Value inferred from cost in laboratory tasks, including infants ([Liu et al. 2017](https://doi.org/10.1126/science.aag2132)) [Moderate, laboratory only] | Application to care; visibility of cost [Our hypothesis] | [§8.6](#86-component-3-construal-and-motive-inference) |
| 5 | Acts become supply on the need's own scale; the outcome is a surface over supply and need, read along $`S=N`$ and $`S=-N`$ around a shared centring point. | Polynomial regression with response surface analysis ([Edwards 2007](https://tarheels.live/jeffreyedwardswebsite/wp-content/uploads/sites/5503/2024/03/Edwards2007.pdf); [Schönbrodt, Humberg & Nestler 2018](https://doi.org/10.1002/per.2169)) [Established method] | Both under- and over-provision co-varied with lower satisfaction within spouses ([Brock & Lawrence 2009](https://doi.org/10.1037/a0015402)) [Moderate]; whether excess is worse than deficit is unresolved [Preliminary]. That measure was a perceived direction of discrepancy, not commensurate need and supply; no care-channel surface has been published | Translation matrix $`\boldsymbol\Lambda`$ [Assumption] | [§8.7](#87-component-4-need-fulfilment-and-fit) |
| 6 | Every act can work through two routes at once: changing B's circumstances and needs (substantive) and being read as regard (symbolic). | Mediation decomposition; needs independent or randomised enactment ([Rohrer et al. 2022](https://doi.org/10.1177/25152459221095827)) [Established method, strong assumptions] | Invisible support: the original diary benefit ([Bolger, Zuckerman & Kessler 2000](https://doi.org/10.1037/0022-3514.79.6.953)) was not reproduced in the same group's replication with more than three times the sample ([Shrout et al. 2010](https://doi.org/10.1093/acprof:oso/9780195380170.003.0007)) [Moderate/mixed; not replicated]; income improves some children's outcomes, but no study measured whether they read it as care ([Cooper & Stewart 2021](https://doi.org/10.1007/s12187-020-09782-0)) [Moderate to Established, for income effects]. No audited study shows a benefit that bypasses perceived regard; the mechanism is unproven, not refuted | Route split and outcome signatures [Our hypothesis] | [§8.8](#88-component-5-the-two-routes-our-hypothesis) |
| 7 | Trust moves toward what B currently perceives, and colours how the next act is read. | Latent state-space model ([Song & Ferrer 2009](https://doi.org/10.1080/10705510902751432)) [Established method] | Trust acts as outcome, mediator and moderator ([Wieselquist et al. 1999](https://doi.org/10.1037/0022-3514.77.5.942); [Campbell et al. 2010](https://doi.org/10.1037/a0019714)) [Moderate/mixed] | Reading function $`p(\cdot)`$; any bistability [Theoretical] | [§8.9](#89-component-6-dynamics) |
| 8 | A's picture of B's needs catches up at a rate $`\lambda`$ set by contact and disclosure; under steady change it lags by $`e^*=r/\lambda`$. | Error-correction learning [Established mathematics] | Fast change in adolescent autonomy needs ([Hadiwijaya et al. 2017](https://doi.org/10.1007/s10964-016-0627-7)) [indirect] | The lag model [Our hypothesis] | [§8.9](#89-component-6-dynamics) |
| 9 | A shared life is possible only if some arrangement meets both people's essentials without pushing either below a sustainability threshold. | Set definition | Goal conflict lowers quality regardless of understanding ([Gere & Schimmack 2013](https://doi.org/10.1007/s10902-011-9314-2)) [Moderate/mixed] | Feasibility formalisation [Our hypothesis] | [§8.10](#810-component-7-constraints-that-are-not-weights) |
| 10 | Unsafe arrangements are excluded before anything is compared; if none is safe, the model recommends nothing. Perceived love never enters $`\mathrm{Safe}(x)`$. | Constrained choice over $`\mathcal F_{\text{safe}}`$; no weighted sum can exclude ([Fishburn 1974](https://doi.org/10.1287/mnsc.20.11.1442)) [Established mathematics] | Once a partner's aggression begins, highly committed people adopt more tolerant standards for it (longitudinal n = 52; experiment n = 73), so the receiver's own judgments cannot define safety ([Arriaga, Capezza & Daly 2016](https://doi.org/10.1037/pspi0000035)) [Moderate/mixed]; harms appear on dimensions separate from love ratings ([Lohmann et al. 2024](https://doi.org/10.1177/15248380231162972)) [Moderate/mixed; not audited] | Admissibility rule and its threshold [Our hypothesis; partly normative] | [§8.10](#810-component-7-constraints-that-are-not-weights) |

Reading the fit surface (5) needs care: $`a_1=b_1+b_2`$ is the slope along $`S=N`$ **at the centring point only**, and a negative $`a_4=b_3-b_4+b_5`$ is **not by itself** a mismatch penalty. A congruence effect needs the joint pattern $`a_4<0`$, $`a_3=0`$ and a first principal axis on $`S=N`$, with confidence intervals and model comparison ([§8.7](#87-component-4-need-fulfilment-and-fit)).

### Variables: definitions, units and domains

| Symbol | Meaning | Unit or scale | Domain |
|---|---|---|---|
| $`t`$; $`k`$ | occasion (diary day or panel wave); care channel (presence, talk, touch, practical help, money, …) | time step; index | $`t\in\mathbb N`$; $`k=1,\dots,K`$ |
| $`I_{A\to B}`$ | A's intention to care, by channel | self-report rating | latent, $`\ge 0`$ |
| $`\mathcal C_A(t)`$ | what A can feasibly enact (time, money, energy, stress) | channel units | subset of $`\mathbb R_{\ge0}^K`$ |
| $`E_{A\to B,k}(t)`$ | care A enacts in channel $`k`$ | minutes, currency, counts | $`\ge 0`$ |
| $`D_{B,k}(t)`$ | B registers that an act occurred | indicator | $`\{0,1\}`$ |
| $`d'_B,\ c_B`$ | B's detection sensitivity and criterion | z units | $`\mathbb R`$ |
| $`v_k,\ \gamma`$ | visibility of an act and of its cost; its effect on detection | proportion or design indicator; z units per unit of $`v`$ | $`v_k\in[0,1]`$; $`\gamma\in\mathbb R`$ |
| $`Q_B(t)`$ | B's perceived regard: feeling understood, valued, cared for | rating-scale score | bounded scale, treated as interval |
| $`X_A(t),\ O_B(t),\ \mu`$ | criterion for A's care (A's report or observer coding); B's own care given; criterion mean | same scale as $`Q`$ | same as $`Q`$ |
| $`\tau,\ \pi`$ | truth force and projection force | dimensionless weights | $`\mathbb R`$, typically 0 to 1 |
| $`\delta(T)`$ | directional (level) bias, possibly dependent on trust | scale units of $`Q`$ | $`\mathbb R`$ |
| $`w`$ | the weight A places on B's welfare, as B infers it | utility weight | $`[0,1]`$ in the reference code |
| $`b,\ \hat c,\ \beta`$ | benefit of the act to B; cost B believes A paid; choice precision in B's model of A | utility units; 1/utility units for $`\beta`$ | $`b,\hat c\ge 0`$; $`\beta>0`$ |
| $`N_{B,k}(t),\ S_{B,k}(t)`$ | B's need and the supply B received in channel $`k`$ | one shared need metric, centred at the scale midpoint | bounded scale |
| $`\boldsymbol\Lambda`$ | translation from acts (channel units) to supply (need metric) | need units per channel unit | $`K\times K`$ matrix |
| $`b_0,\dots,b_5`$; $`a_1,\dots,a_5`$; $`p_{10},p_{11}`$ | polynomial coefficients; surface quantities at the centring point; first principal axis | outcome units per centred scale unit (and squares) | $`\mathbb R`$ |
| $`\mathbf Y_B(t)`$ | B's outcomes (well-being, satisfaction, …), each on its own instrument | instrument units | $`\mathbb R^m`$ |
| $`\boldsymbol\beta_{\text{sub}},\ \boldsymbol\beta_{\text{sym}},\ \boldsymbol\Gamma,\ \mathbf x(t)`$ | effects of the two routes on each outcome; covariates and their coefficients | outcome units per unit of $`h`$ or $`Q`$ | $`\mathbb R^m`$ |
| $`T_B(t),\ \eta,\ p(\cdot)`$ | B's trust in A, normalised; updating rate; trust-dependent reading of perceived regard | proportion of scale range; per step | $`T\in[0,1]`$; $`\eta\in(0,1]`$; $`p:[0,1]\to[0,1]`$ |
| $`\tilde N_{A\to B}(t),\ \lambda(t),\ r`$ | A's model of B's need; its learning rate; drift rate of B's need | need units; per step; need units per step | bounded scale; $`\lambda\in(0,1]`$; $`r\in\mathbb R`$ |
| $`G_A(x),\ G_B(x)`$ | margins on each person's essential requirements under arrangement $`x`$ | requirement-specific | $`\ge 0`$ means met |
| $`W_A(x),\ W_B(x);\ w^{\min}`$ | each person's well-being under $`x`$; sustainability thresholds | well-being scale units | $`\mathbb R`$ |
| $`\mathrm{Safe}(x)`$ | $`x`$ passes the safety criterion on validated indicators (violence, threats, coercive control, fear-based compliance) | indicator | $`\{0,1\}`$ |
| $`\mathcal F,\ \mathcal F_{\text{safe}}`$ | feasible joint arrangements; the safe subset | sets of arrangements | possibly empty |

### Assumptions and what can be identified

- $`S`$ and $`N`$ must be commensurable and centred on a shared zero; otherwise the surface quantities in (5) say nothing about fit.
- $`X`$ is another report, not the truth. $`\tau`$, $`\pi`$ and $`\delta`$ need repeated judgments plus a criterion on the same metric.
- $`d'`$ and $`c`$ describe disagreement between two reports unless an observer or an experiment supplies the criterion.
- $`\boldsymbol\beta_{\text{sub}}`$ and $`\boldsymbol\beta_{\text{sym}}`$ need enactment measured independently of the receiver, ideally randomised; observational mediation also needs no unmeasured mediator–outcome confounding.
- $`\boldsymbol\Lambda`$ has $`K^2`$ parameters and cannot be identified for a single dyad; it needs pooling with structure or randomised channels.
- $`\lambda`$ needs long paired series of A's predictions against B's reports. No such study exists.
- $`p(\cdot)`$ and any bistability are practically unidentifiable, and no study has shown bistability in relationships.
- $`\mathrm{Safe}(x)`$ uses a normative threshold. Data can show whether care compensates for danger, not where the line must be.
- The equations are explanatory hypotheses. Predictive value would have to be shown out of sample, beyond the perceptions that already predict relationship quality.

## 8.1 Design rules

The mathematics below obeys six rules:
1. **No numerical coefficient is invented.** Every parameter is a symbol to be estimated, and every numerical value that appears is either a published estimate or labelled illustrative arithmetic.
2. **Nothing measures love directly.** Love enters only as latent components that influence observable quantities.
3. **Need and supply are compared only on commensurate scales.**
4. **Each component states six things:** the construct it represents, its measurement, why the operation fits, its assumptions, its empirical support, and what remains speculative.
5. **Explanatory equations are distinguished from predictive models.**
6. **Each parameter's identifiability is stated.** A parameter that cannot be estimated from any feasible data is labelled as such.

The equations are hypotheses about structure. They are not validated psychological laws.

## 8.2 Notation glossary

| Symbol | Meaning | Observed or latent | Measurement route | Status |
|---|---|---|---|---|
| $`i, j \in \{A, B\}`$; $`i \to j`$ | Persons; direction of care (both directions run at once) | — | — | — |
| $`k = 1, \dots, K`$; $`t`$ | Care channel (time and presence, verbal affection, physical affection, practical help, financial provision, informational support, and so on); occasion | — | — | — |
| $`\mathbf{L}_i(t)`$ | Vector of love components of person $`i`$ | Latent | Component scales (triangular, compassionate love, communal strength) | Validated scales exist |
| $`I_{i\to j,k}(t)`$ | Intended care in channel $`k`$ | Latent | Giver diary proxy | No validated measure [Theoretical] |
| $`\mathcal{C}_i(t) \subset \mathbb{R}^K_{+}`$ | Feasible set of enactable care (capacity) | Latent | Proxies: hours, money, stress, skill | [Assumption] |
| $`E_{i\to j,k}(t)`$ | Enacted care (counts, durations) | Observed | Giver event log; observer coding | Partially validated (support coding) |
| $`c_{i,k}(t)`$ | Cost of the act to the giver | Observed (giver) | Giver report | No validated measure |
| $`v_k`$ | Visibility of the act and of its cost | Partly observed | Design (visible or invisible) and receiver report | [Assumption] |
| $`D_{j,k}(t)`$ | Receiver registers that the act occurred | Observed | Receiver checklist | Quasi-signal-detection practice |
| $`Q_j(t)`$ | Perceived regard (symbolic route) | Observed | PRI or PPRS; regard items | Validated scales; strong sentiment overlap |
| $`N_{j,k}(t)`$, $`S_{j,k}(t)`$ | Needed (desired) and received amount of $`k`$, on one metric | Observed | "How much $`k`$ did you want / receive?" | Support desire and receipt items |
| $`\tilde N_{i\to j,k}(t)`$ | Giver's model of the receiver's need | Observed | Giver's prediction of the receiver's report | Paired-prediction paradigms |
| $`T_j(t)`$ | Trust of $`j`$ in $`i`$ | Latent | Multi-indicator trust items | Validated at trait level |
| $`\mathbf{Y}_j(t)`$, $`W_i(t)`$ | Receiver's outcome vector; giver's well-being | Observed | Satisfaction (CSI), well-being scales | Validated |
| $`\mathbf{Z}(t)`$, $`U_j(t)`$ | Safety indicators (acts, control, fear); autonomy frustration or psychological control | Observed | CTS2, CAS, PMWI; psychological-control scales | Validated (mostly WEIRD) |
| $`\mathcal{F}`$ | Set of joint life patterns meeting both people's essential requirements | Latent | Goal conflict, dealbreakers | [Our hypothesis] |
| $`\tau, \pi, \delta`$ | Truth force, projection force, directional bias | Parameters | Truth-and-bias model | Established method |
| $`d'_j, c_j`$ | Detection sensitivity and criterion | Parameters | Mixed-effects probit | Established method |
| $`b_0,\dots,b_5`$; $`a_1,\dots,a_5`$; $`p_{10}, p_{11}`$ | Polynomial coefficients; response-surface quantities relative to the centring point; first principal axis | Parameters | Response surface analysis (RSA) | Established method |
| $`\beta_{\text{sub}}, \beta_{\text{sym}}`$ | Weights of the substantive and symbolic routes | Parameters | Requires independent or randomized enactment | [Our hypothesis] |
| $`\lambda`$, $`\eta`$, $`p(\cdot)`$ | Learning rate of the giver's need model; trust updating rate; trust-dependent interpretation function | Parameters | Long paired series | [Our hypothesis] / [Theoretical] |

## 8.3 What the mathematics must not do

**Cosine similarity cannot adjudicate "translation versus amount."** For expressed care $`\mathbf{E}`$ and needs $`\mathbf{N}`$, $`\cos(\mathbf{E},\mathbf{N}) = \mathbf{E}\cdot\mathbf{N} / (\lVert\mathbf{E}\rVert\,\lVert\mathbf{N}\rVert)`$. For any $`\alpha, \beta > 0`$,

```math
\cos(\alpha\mathbf{E}, \beta\mathbf{N}) = \frac{\alpha\beta\,\mathbf{E}\cdot\mathbf{N}}{\alpha\lVert\mathbf{E}\rVert\,\beta\lVert\mathbf{N}\rVert} = \cos(\mathbf{E},\mathbf{N}).
```

A partner who gives a quarter of what is needed in the right proportions scores a perfect 1. Cosine assumes amount away, so it cannot test a claim about amount [Established mathematics]. Cosine is also undefined in meaning on rating scales, which have no true zero. Take the illustrative profiles $`\mathbf{E} = (5,3,1,2,4)`$ and $`\mathbf{N} = (4,4,2,1,5)`$. The cosine is .959 when coded 1–5, .926 when coded 0–4 and .763 when coded −2 to +2, while the profile correlation is .770 under all three codings. These values were verified by direct computation and are arithmetic, not data. Cosine also changes with the units of each channel: $`\cos((1, .5), (.5, 1)) = .80`$, but it becomes about .86 if channel 1 is measured in half-size units. And it presumes orthogonal, equally scaled channels, which self-report channel scales never are.

The Pearson profile correlation is the cosine of mean-centred profiles. It escapes the origin problem only by discarding *elevation*, which is exactly the "amount" information ([Cronbach & Gleser 1953](https://doi.org/10.1037/h0057173)). Profile similarity is also inflated by **normativeness**: if most people value being listened to and few value gifts, any two profiles correlate because both are typical. Correlates of overall similarity indices are therefore "often misleadingly positive" ([Wood & Furr 2016](https://doi.org/10.1177/1088868315581119); [Furr 2008](https://doi.org/10.1111/j.1467-6494.2008.00521.x)) [Established]. The dot product $`\mathbf{E}\cdot\mathbf{N} = \lVert\mathbf{E}\rVert\,\lVert\mathbf{N}\rVert\cos\theta`$ mixes the giver's amount, the receiver's need intensity and their alignment into one number, so it cannot separate them.

**Importance-weighted similarity, $`\sum_k w_k E_k N_k`$, is rejected.** Locke's range-of-affect hypothesis, with empirical support, holds that importance is already embedded in domain satisfaction. In a study of 12 job facets, importance moderated how facet amount related to facet satisfaction, but not how facet satisfaction aggregated into overall satisfaction ([Rice, Gentile & McFarlin 1991](https://doi.org/10.1037/0021-9010.76.1.31)). In life-satisfaction data, importance weighting was "unnecessary" ([Wu & Yao 2006](https://doi.org/10.1007/s11205-005-5666-5)), and weighted scores did no better than unweighted ones ([Wu 2008](https://doi.org/10.1007/s11205-007-9180-9); [Trauer & Mackinnon 2001](https://doi.org/10.1023/A:1013159414364)) [Moderate to Established]. Product composites of interval-scale ratings have correlations that change under permissible rescaling of the components ([Evans 1991](https://doi.org/10.1037/0003-066X.46.1.6)) [Established].

**Expressed care and need do not live in the same space.** Needs are motivational states of the receiver, and acts are behaviours of the giver. Person–environment fit theory requires the two sides of a comparison to be measured on *commensurate* dimensions ([Edwards, Caplan & Harrison 1998](https://doi.org/10.1093/oso/9780198522799.003.0003)) [Theoretical]. The formalism therefore needs a received-supply variable $`S_{j,k}`$ on the need metric, plus an explicit translation step from acts to supply. A cosine between $`\mathbf{E}_A`$ and $`\mathbf{N}_B`$ collapses that step, which is the hypothesis itself, into one unjustified operation.

**Difference scores and single relationship scores are rejected.** Difference scores impose untested equal-and-opposite coefficients and confound their components ([Edwards 1994](https://doi.org/10.1006/obhd.1994.1029); [Edwards 2001](https://doi.org/10.1177/109442810143005)) [Established]. A single relationship score would net trade-offs and danger signals that must be kept apart ([Section 2](02-definitions-and-distinctions.md)).

## 8.4 Component 1: enactment under capacity

```math
E_{i\to j}(t) = g\big(I_{i\to j}(t)\big) \quad \text{subject to} \quad E_{i\to j}(t) \in \mathcal{C}_i(t). \qquad \text{[Assumption]}
```

The construct is the translation of intention into acts, bounded by what is feasible. No validated measure of intention exists, so $`I`$ is approximated by giver diaries ("today I meant to show care by…"). Enactment is measured by event logs or observers. Capacity proxies include stress, working hours, money and skill.

The constraint form is a modelling assumption: the evidence cannot tell a feasibility bound from a trade-off weight. On higher-stress days, husbands who perceived that their wives needed support reported giving somewhat less, a graded weakening rather than a hard bound ([Neff, Nguyen & Williamson 2021](https://doi.org/10.1177/0146167220974490)) [Preliminary], and market work hours predicted less paternal childcare in every wave of Korean time-use data ([Lee & Seo 2021](https://doi.org/10.22626/jkfrma.2021.25.3.007)) [Moderate/mixed]. The model assumes that intention exists independently of enactment and can be reported without excessive self-presentation; it does not assume the shape of $`g`$. The testable implication is that, conditional on reported intention, enactment falls when capacity proxies tighten. The functional form of $`g`$ and the content of $`\mathcal{C}`$ remain speculative.

## 8.5 Component 2: detection

```math
\Pr\big(D_{j,k,t}=1 \mid E_{i\to j,k,t}\big) = \Phi\big(-c_j + d'_j\,\mathbb{1}[E_{i\to j,k,t}>0] + \gamma\, v_k\big), \qquad c_j, d'_j \ \text{random over persons.}
```

The construct is whether the receiver registers that an act occurred. The *signal* is the giver's report of the act, and the *response* is the receiver's report, giving hits, misses, false alarms and correct rejections ([Gable, Reis & Downey 2003](https://doi.org/10.1111/1467-9280.t01-1-01426); [Visserman et al. 2019](https://doi.org/10.1177/1948550618757599)). Signal detection theory can be written as a generalized linear model ([DeCarlo 1998](https://doi.org/10.1037/1082-989X.3.2.186)), and a mixed-effects probit yields person-specific sensitivity $`d'_j`$ and criterion $`c_j`$ [Established as a method]. A lenient criterion means a generous perceiver who "sees" care that the giver did not report.

The key assumption is that the giver's report stands in for ground truth. It does not: self-presentation, forgetting and invisible intentions all intervene. Misses and false alarms are therefore *disagreements*, not errors, unless an observer or an experimental manipulation provides the criterion. The design needs enough signal-present and signal-absent days per person. Speculative extensions are channel-specific sensitivities and moderation of $`c_j`$ by trust and sentiment.

## 8.6 Component 3: construal and motive inference

**Truth and bias.** Let $`X_{i,t}`$ be a criterion for A's care (A's report or observer coding), $`O_{j,t}`$ the receiver's own care given (the projection variable), and $`\mu`$ the criterion mean. Following [West & Kenny 2011](https://doi.org/10.1037/a0022936),

```math
Q_{j,t} - \mu = \tau\,(X_{i,t} - \mu) + \pi\,(O_{j,t} - \mu) + \delta + u_{j,t}.
```

Here $`\tau`$ is the truth force (tracking), $`\pi`$ is projection and $`\delta`$ is directional bias. The construct is the receiver's perceived regard. It is measured with responsiveness scales (the PRI or PPRS) or regard items, alongside giver reports or observer codes. The additive form is the standard truth-and-bias specification, and it separates the "B reads A" force from the "B projects B" force ([Lemay, Clark & Feeney 2007](https://doi.org/10.1037/0022-3514.92.5.834)) [Established method; Moderate evidence for $`\pi > 0`$ in couples].

The specification assumes that both variables share a metric and that the criterion is another report, not truth. Context-dependence enters as moderation of $`(\tau, \pi, \delta)`$. For example, attachment insecurity raised negative appraisal mainly for low-support or ambiguous messages, less for moderately supportive ones and not for very supportive ones ([Collins & Feeney 2004](https://doi.org/10.1037/0022-3514.87.3.363)), so the attachment effect on $`\delta`$ should depend on signal ambiguity [Moderate]. A "90 versus 40" gap corresponds to a large $`\delta`$ (a level shift) and is fully compatible with high $`\tau`$: B can track *which* days A gave more while placing the whole series lower.

**Motive inference through the naïve utility calculus** [Theoretical mechanism; application is Our hypothesis]. Observers infer what agents value by inverting a model in which agents choose actions that maximize rewards minus costs ([Jara-Ettinger et al. 2016](https://doi.org/10.1016/j.tics.2016.05.011)). Even ten-month-old infants infer that an agent who pays a higher cost values a goal more ([Liu et al. 2017](https://doi.org/10.1126/science.aag2132)) [Moderate/mixed for laboratory stimuli]. In a relationship, suppose A chooses between a caring act $`a_1`$, which has benefit $`b`$ to B and cost $`c`$ to A, and an alternative $`a_0`$. A softmax-rational giver chooses $`a_1`$ with probability

```math
\Pr(a_1 \mid w) = \sigma\big(\beta (w\,b - c)\big),
```

where $`w`$ is the weight A places on B's welfare, $`\beta`$ is choice precision and $`\sigma`$ is the logistic function. B infers $`w`$ by Bayes' rule, using B's *believed* cost $`\hat c`$. For two candidate weights $`w_2 > w_1`$, write $`x_m = \beta w_m b`$. The log-likelihood ratio after observing the caring act has derivative

```math
\frac{\partial}{\partial \hat c}\log\frac{\sigma(x_2 - \beta\hat c)}{\sigma(x_1 - \beta\hat c)} = \beta\big[\sigma(x_2 - \beta\hat c) - \sigma(x_1 - \beta\hat c)\big] > 0,
```

and the same sign holds after observing *absence* ($`a_0`$), with $`1 - \sigma`$ in place of $`\sigma`$. Two predictions follow under these assumptions [Our hypothesis]:
- The posterior belief about $`w`$ increases with the believed cost of the act. A receiver who underestimates what care cost the giver will underestimate how much the giver values them.
- Absence is read more harshly the cheaper the receiver believes presence would have been.

This gives a principled version of the **visibility asymmetry**. When the costs of provision (long hours, forgone opportunities) are invisible but its by-product (absence) is visible, inferred regard falls even if the giver's true $`w`$ is high. If B also attributes A's working to A's own preferences rather than to the goal of providing for B, the provision act is "explained away" and carries no information about $`w`$ at all. This rests on the theoretical position that "providing" is a form of involvement families tend not to see ([Christiansen & Palkovitz 2001](https://doi.org/10.1177/019251301022001004)) [Theoretical].

The component assumes approximately rational choice, a known option set and a stable $`w`$, none of which holds exactly in families. The model has never been estimated on close-relationship data ([Baker, Saxe & Tenenbaum 2009](https://doi.org/10.1016/j.cognition.2009.07.005)). It can be tested with vignettes that hold the act constant while manipulating cost information, or with diaries in which A reports costs and B estimates them.

## 8.7 Component 4: need fulfilment and fit

For each channel, or for a justified aggregate, model the receiver's outcome with polynomial regression on received supply $`S`$ and need $`N`$, measured on the same metric:

```math
Y = b_0 + b_1 S + b_2 N + b_3 S^2 + b_4 S N + b_5 N^2 + e.
```

**Preconditions.** $`S`$ and $`N`$ must be *commensurable*: the same construct on the same metric, with measurement invariance wherever groups or partners are compared ([Schönbrodt, Humberg & Nestler 2018](https://doi.org/10.1002/per.2169)). Both are centred on the same meaningful zero, conventionally the scale midpoint; only under that common centring does the line $`S = -N`$ represent misfit ([Edwards 2007](https://tarheels.live/jeffreyedwardswebsite/wp-content/uploads/sites/5503/2024/03/Edwards2007.pdf)) [Established method].

**Surface quantities**, all defined relative to the centring point $`(0, 0)`$ ([Edwards 2007](https://tarheels.live/jeffreyedwardswebsite/wp-content/uploads/sites/5503/2024/03/Edwards2007.pdf); [Shanock et al. 2010](https://doi.org/10.1007/s10869-010-9183-4); [Schönbrodt, Humberg & Nestler 2018](https://doi.org/10.1002/per.2169)):
- $`a_1 = b_1 + b_2`$ is the slope along the line of congruence ($`S = N`$) **at the centring point only**. Substituting $`S = N = t`$ gives $`Y = b_0 + a_1 t + a_2 t^2`$, so the slope at level $`t`$ is $`a_1 + 2a_2 t`$. It is the linear component of the agreement line, not the effect of the amount of care everywhere, and it changes with the centring point whenever $`a_2 \ne 0`$;
- $`a_2 = b_3 + b_4 + b_5`$ is the curvature along the line of congruence;
- $`a_3 = b_1 - b_2`$ is the slope along the line of incongruence ($`S = -N`$) at the centring point; when $`a_4 \ne 0`$ it locates the highest or lowest point of that line away from $`(0, 0)`$, so $`a_3 \ne 0`$ puts the best outcome at a margin of over- or under-supply;
- $`a_4 = b_3 - b_4 + b_5`$ is the curvature along the line of incongruence;
- $`a_5 = b_3 - b_5`$ is zero when the ridge (or trough) can run along the line of congruence.

**A negative $`a_4`$ is not, by itself, a mismatch penalty.** It shows an inverted U along one line through the centring point. A congruence (similarity) effect requires a *joint* pattern, each part estimated with its uncertainty: $`a_4 < 0`$; $`a_3 = 0`$; and the ridge on the line of congruence, that is a first principal axis with intercept $`p_{10} = 0`$ and slope $`p_{11} = 1`$ (equivalently $`a_5 = 0`$ given $`a_3 = 0`$) ([Schönbrodt, Humberg & Nestler 2018](https://doi.org/10.1002/per.2169); [Humberg, Nestler & Back 2019](https://doi.org/10.1177/1948550618757600)) [Established method]. A flat ridge ($`a_1 = a_2 = 0`$) makes it the prototypical pattern; $`a_1 \ne 0`$ or $`a_2 \ne 0`$ means outcomes also depend on the level at which supply and need agree. The stationary point and principal axes follow from $`b_1, \dots, b_5`$ ([Edwards 2007](https://tarheels.live/jeffreyedwardswebsite/wp-content/uploads/sites/5503/2024/03/Edwards2007.pdf), eqs. 11–18).

**Empirical tests.** Point estimates are not enough. The required evidence is confidence intervals (for example bootstrap) for $`a_3`$, $`a_4`$, $`p_{10}`$ and $`p_{11}`$; comparison of the full quadratic model with constrained models such as the squared-difference model, which imposes $`b_1 = b_2 = 0`$, $`b_3 = b_5`$ and $`b_4 = -2b_3`$ ([Edwards 2007](https://tarheels.live/jeffreyedwardswebsite/wp-content/uploads/sites/5503/2024/03/Edwards2007.pdf)); enough observations in incongruent regions that the surface is not extrapolated; and adequate power for quadratic terms. Moderated regression with main effects and a single interaction cannot represent a congruence effect ([Schönbrodt, Humberg & Nestler 2018](https://doi.org/10.1002/per.2169)). Significance tests for the surface quantities should use the corrected formulas published in an erratum to Shanock et al. ([2014](https://doi.org/10.1007/s10869-013-9317-6); not accessed for this paper) [Preliminary].

**Translation-as-fit predicts** the joint congruence pattern, or a directional variant ($`a_3 \ne 0`$ or cubic terms) where deficiency and excess differ. **Amount predicts** outcomes that rise with supply, along and across the agreement line, without that pattern. Cubic RSA ([Humberg et al. 2022](https://doi.org/10.1037/met0000352)) or spline regression ([Edwards & Parry 2018](https://doi.org/10.1177/1094428117715067)) estimate an asymmetric loss without assuming its shape. That matters because the evidence on excess is unresolved. In newlyweds' concurrent covariation over five years, over-provision had the larger slope per behaviour flagged, but under-provision had the larger reported effect size and was far more common ([Brock & Lawrence 2009](https://doi.org/10.1037/a0015402)); daily data found minimal effects of excess ([Bar-Kalifa & Rafaeli 2013](https://doi.org/10.1037/a0034905)), and the two studies differ in measurement and design as well as timescale [Preliminary].

The answer to "is more care always better?" is therefore an empirical $`a_3`$ and cubic question, not an assumption. Intrusive or autonomy-violating "care" is better modelled as a separate outcome (Section 8.10) than as positive supply. Multilevel and dyadic versions handle diaries and couples ([Nestler, Humberg & Schönbrodt 2019](https://doi.org/10.1037/met0000199); [Schönbrodt, Humberg & Nestler 2018](https://doi.org/10.1002/per.2169)). A latent congruence model controls measurement error ([Cheung 2009](https://doi.org/10.1177/1094428107308914)).

Across channels, balanced need satisfaction predicts well-being beyond its sum ([Sheldon & Niemiec 2006](https://doi.org/10.1037/0022-3514.91.2.331)), which justifies an imbalance term such as the dispersion of channel deficits [Assumption]. The approach assumes commensurate measures, adequate sample size (interaction terms are typically underpowered, [Sommet et al. 2023](https://doi.org/10.1177/25152459231178728), and quadratic terms need their own power simulation) and no strong ceiling effects. Partner-support research has measured received frequency plus a perceived direction of discrepancy, more, less or the same ([Brock & Lawrence 2009](https://doi.org/10.1037/a0015402)). That is not commensurate need and supply and cannot support response surface analysis, and **no dyadic or multilevel RSA of care channels has been published**. Base rates from other domains are sobering: nonlinear fit terms add ΔR² ≈ .008 ([Yang et al. 2008](https://doi.org/10.1016/j.hrmr.2008.07.014)).

## 8.8 Component 5: the two routes [Our hypothesis]

```math
\mathbf{Y}_j(t) = \boldsymbol{\alpha} + \boldsymbol{\beta}_{\text{sub}}\; h\big(E_{i\to j}(t), N_j(t)\big) + \boldsymbol{\beta}_{\text{sym}}\; Q_j(t) + \boldsymbol{\Gamma}\mathbf{x}_t + \mathbf{e}_t, \qquad Q_j(t) = f\big(E_{i\to j}(t), \text{priors}_j(t)\big).
```

**The routes are pathways of effect, not kinds of acts.** Both terms are functions of the same enacted care $`E`$: one act can change circumstances or needs (through $`h`$) and be read as regard (through $`Q`$). Money can communicate devotion; presence can meet a need for company, co-regulation or being known whether or not it is read as love. $`\boldsymbol{\beta}_{\text{sub}}`$ is the part of an act's effect that does not pass through perceived regard, and $`\boldsymbol{\beta}_{\text{sym}}`$ the part that does.

The construct is the decomposition of care's total effect into a part that does not pass through perceived regard and a part that does. $`E`$ must be measured independently of the receiver (giver logs, observers) or randomized ([Section 18](18-proposed-study.md)), and $`Q`$ comes from the receiver. Mediation decomposition is the appropriate operation, but only under strong assumptions, notably no unmeasured confounding of the mediator–outcome relation. Path models with reversed arrows or compared fit indices cannot decide between causal structures ([Rohrer et al. 2022](https://doi.org/10.1177/25152459221095827); [Bullock, Green & Ha 2010](https://doi.org/10.1037/a0018933)) [Established].

No audited study shows a benefit that bypasses perceived regard. The invisible-support diary pattern did not replicate in the same group's larger study ([Shrout et al. 2010](https://doi.org/10.1093/acprof:oso/9780195380170.003.0007)), the laboratory benefit of invisible support ran through a perception, a reflected appraisal of inefficacy ([Bolger & Amarel 2007](https://doi.org/10.1037/0022-3514.92.3.458)), and the income studies measured no perception; a failed replication of one result removes the main evidence for the route without refuting it [Moderate/mixed]. That $`\boldsymbol{\beta}_{\text{sub}} \neq 0`$ in close relationships is therefore [Our hypothesis]. Note that a route not passing through perceived regard does not require the receiver to miss the act, so evidence of benefit from unnoticed care would be sufficient for it but is not necessary. The prediction that $`\boldsymbol{\beta}_{\text{sub}}`$ loads on material, behavioural and educational outcomes while $`\boldsymbol{\beta}_{\text{sym}}`$ loads on emotional and relational outcomes is speculative [Our hypothesis]. It concerns routes, not act types, so evidence that classifies acts, such as perceived financial versus emotional support ([Chentsova Dutton, Choi & Choi 2020](https://doi.org/10.3389/fpsyg.2020.00353)), is consistent with it but cannot test it.

## 8.9 Component 6: dynamics

**Trust as a latent state.** In discrete time,

```math
T_j(t+1) = T_j(t) + \eta\,\big[p\big(Q_j(t), T_j(t)\big) - T_j(t)\big] + \varepsilon_t, \qquad y_{m,t} = \omega_m T_j(t) + e_{m,t}.
```

Trust is measured by several indicators per occasion (indicator $`y_{m,t}`$ with loading $`\omega_m`$), which a state-space model separates from state noise; short series bias the state-noise estimates ([Song & Ferrer 2009](https://doi.org/10.1080/10705510902751432)) [Established method]. Trust appears in the evidence as an *outcome* (enthusiastic responses build it; [Reis et al. 2010](https://doi.org/10.1037/a0018344)), a *mediator* (mutual cyclical growth; [Wieselquist et al. 1999](https://doi.org/10.1037/0022-3514.77.5.942)) and a *moderator* (low-trust people's perceived relationship quality varies more day to day; [Campbell et al. 2010](https://doi.org/10.1037/a0019714)) [Moderate/mixed]. A static choice among these roles is therefore misspecified. In the model, trust shifts the construal parameters, is updated by perceived regard, and carries acts into commitment.

**Tipping points are theoretical only.** Simplify to $`dT/dt = \eta\,[p(T) - T]`$ with $`p:[0,1]\to(0,1)`$ continuous and increasing. At least one equilibrium exists, because $`p(0) > 0`$ and $`p(1) < 1`$. An equilibrium $`T^*`$ is stable if and only if $`p'(T^*) < 1`$, and $`\eta`$ only rescales time. Multiple stable equilibria (bistability) require $`p' > 1`$ somewhere, by the mean value theorem, but this condition is **not sufficient**. With a logistic $`p`$ of slope $`k`$ and midpoint $`\theta`$, maximum $`p' = k/4`$. For $`k = 10, \theta = .3`$, $`p'`$ reaches 2.5 yet there is one equilibrium. For $`k = 4.5, \theta = .5`$, there are three. The steep region must straddle the diagonal. These are illustrative values verified by computation, not estimates.

No study has shown bistability, hysteresis or critical slowing down in relationship trust or satisfaction, and early-warning signals have little support even in psychopathology ([Helmich et al. 2024](https://doi.org/10.1038/s44159-024-00369-y)) [Moderate/mixed]. Accelerating declines in satisfaction before separation are real ([Bühler & Orth 2025](https://doi.org/10.1037/pspp0000551)), but they are not diagnostic of a tipping point. Selecting on a threshold crossing can produce an accelerating terminal decline even in a driftless random walk whose dynamics never change. When trajectories are aligned on the moment they first cross a fixed threshold, the average path appears to fall faster and faster toward that moment, because the alignment selects runs of chance downward steps. Bistable trust is therefore a [Theoretical] proposition that is currently very hard to falsify. A cheaper testable implication is asymmetric updating: larger belief changes after negative evidence when trust is already low ([Siegel et al. 2018](https://doi.org/10.1038/s41562-018-0425-1), shown only with strangers) [Theoretical for couples].

**Developmental lag in the giver's model** [Our hypothesis]. Let the giver's model of a need update as

```math
\tilde N(t+1) = \tilde N(t) + \lambda(t)\,\big[N(t) - \tilde N(t)\big] + \xi_t, \qquad 0 < \lambda(t) \le 1,
```

with $`\lambda(t)`$ increasing in contact and disclosure. If the need drifts linearly at rate $`r`$ (so $`N(t+1) = N(t) + r`$), the error $`e(t) = N(t) - \tilde N(t)`$ obeys $`e(t+1) = (1-\lambda)\,e(t) + r`$. Its steady state is therefore

```math
e^* = \frac{r}{\lambda}.
```

The model predicts that **the lag grows with the speed of developmental change and shrinks with contact and disclosure**. A parent with little contact during adolescence, a period of rapid change in autonomy needs ([Hadiwijaya et al. 2017](https://doi.org/10.1007/s10964-016-0627-7)), is predicted to be calibrated to an earlier child. The parameter $`\lambda`$ is identifiable from repeated paired reports, the giver's prediction of the receiver's need against the receiver's own report, analysed with truth-and-bias models over time. No such study exists.

**Strategy adaptation** [Our hypothesis]. If a giver reallocates effort across channels in proportion to the feedback each produces (thanks, complaints, visible relief), then care that goes unregistered, such as sacrifices the partner misses, which bring no same-day gratitude ([Visserman et al. 2019](https://doi.org/10.1177/1948550618757599); detection showed no evident effect on gratitude at follow-ups of three months and one year), receives no reinforcement. The giver is predicted either to abandon unregistered care, whatever its substantive value, or to escalate visible care whose meaning may be costly, such as visible help that signals inefficacy.

**Repair.** Apology and reduced perceived malicious intent are the strongest correlates of forgiveness ([Fehr, Gelfand & Nag 2010](https://doi.org/10.1037/a0019993)) [Established, associational]. In the model, repair acts update construal and trust. If updating is asymmetric, repair can reverse some damage but not all, without any bistability [Theoretical].

## 8.10 Component 7: constraints that are not weights

**Compatibility as feasibility** [Our hypothesis]. Let $`x`$ range over joint life patterns: allocations of time and money, location, children, careers and care flows. Let $`G_A(x) \ge 0`$ and $`G_B(x) \ge 0`$ be each person's essential requirements, and $`W_i(x) \ge w_i^{\min}`$ each person's sustainability threshold. Define

```math
\mathcal{F} = \big\{x \in \mathcal{C}_A \times \mathcal{C}_B : G_A(x) \ge 0,\ G_B(x) \ge 0,\ W_A(x) \ge w_A^{\min},\ W_B(x) \ge w_B^{\min}\big\}.
```

This definition separates three cases:
- An **unmet** need is a gap that a reallocation within $`\mathcal{F}`$ could close.
- **Incompatibility** is $`\mathcal{F} = \varnothing`$.
- **Unsustainable need** is the special case where $`\mathcal{F}`$ is empty because $`G_B`$ can be satisfied only with $`W_A < w_A^{\min}`$.

Understanding, meaning accurate models of each other's $`G`$, helps partners *find* a point in $`\mathcal{F}`$ but cannot *create* one. That is the formal content of "perfect understanding, incompatible lives." Measurement is the weak point here. Goal-conflict measures ([Gere & Schimmack 2013](https://doi.org/10.1007/s10902-011-9314-2)) and research on dealbreakers ([Jonason et al. 2015](https://doi.org/10.1177/0146167215609064)) are partial proxies.

**Safety as an admissibility constraint** [Our hypothesis in formalisation; partly normative]. Unsafe arrangements are removed before anything is compared:

```math
\mathcal{F}_{\text{safe}} = \{x \in \mathcal{F} : \mathrm{Safe}(x) = 1\}, \qquad x^{\star} = \arg\max_{x \in \mathcal{F}_{\text{safe}}} \mathrm{Outcome}(x) \ \text{ only if } \mathcal{F}_{\text{safe}} \ne \varnothing.
```

$`\mathrm{Safe}(x) \in \{0, 1\}`$ is decided from safety indicators $`\mathbf{Z}`$ (violence, threats, coercive control, fear-based compliance) against a threshold, never from perceived love $`Q`$ or from care. If $`\mathcal{F}_{\text{safe}} = \varnothing`$, the model reports that no admissible arrangement exists and recommends nothing.

Two weaker formalisations fail. A weighted sum cannot exclude anything: lexicographic preferences cannot in general be represented by a real-valued utility ([Fishburn 1974](https://doi.org/10.1287/mnsc.20.11.1442)) [Established mathematics], and for every finite safety weight there is an unsafe but caring arrangement that the sum prefers to a safe one. A lexicographic order (safety first, then care) ranks rather than excludes: when every option is unsafe it still selects the least unsafe one, or the more caring of two equally unsafe ones. Version 0.1.0 of this paper used that order; it is corrected here (see [`CORRECTIONS.md`](../CORRECTIONS.md), C3).

The case for keeping safety outside the care calculus rests on normative and design grounds and on a narrower empirical finding. Harm from violence and coercion appears on dimensions (fear, PTSD, injury) separate from love ratings ([Lohmann et al. 2024](https://doi.org/10.1177/15248380231162972); not examined in the audit). Once a partner's aggression begins, highly committed people adopt more tolerant standards for it ([Arriaga, Capezza & Daly 2016](https://doi.org/10.1037/pspi0000035)), so a committed receiver's own judgments cannot define safety; whether love ratings themselves move in the wrong direction as safety falls needs another source. A weighted sum would partly cancel the danger signal. One empirical question remains: below a safety threshold, do outcomes become insensitive to care in other channels? Threshold or hurdle models and necessary condition analysis can test that non-compensability ([Dul 2016](https://doi.org/10.1177/1094428115584005)). Where to set the threshold, and the decision to exclude, are normative choices that the data inform but do not settle.

**Autonomy as a separate outcome.** Psychological control and autonomy support have *distinct* associations with outcomes even when each controls for the other ([Bradshaw et al. 2025](https://doi.org/10.1037/amp0001389)) [Established, associational]. So $`U_j`$ is modelled as its own outcome, with the legitimacy of the domain as a moderator ([Smetana & Daddis 2002](https://doi.org/10.1111/1467-8624.00424)). It is not subtracted from "care."


**Multiplicative bottleneck or additive?** Whether care in the wrong channel is worthless (multiplicative) or a partial substitute (additive) cannot be decided from ordinal outcomes. $`Y = A \cdot B`$ becomes additive after a log transform, so non-crossover interactions are scale-dependent ([Wagenmakers et al. 2012](https://doi.org/10.3758/s13421-011-0158-0); [Rohrer & Arslan 2021](https://doi.org/10.1177/25152459211007368)) [Established]. Only crossover predictions, factorial experiments or necessary-condition analysis can decide it.

## 8.11 Asymmetry and dyadic structure

Each person's outcomes depend on both people. For distinguishable roles (parent and child; giver-role on a given day), the actor–partner interdependence model writes $`Y_A = a_A X_A + p_A X_B + e_A`$ and $`Y_B = a_B X_B + p_B X_A + e_B`$ with correlated errors ([Cook & Kenny 2005](https://doi.org/10.1080/01650250444000405)) [Established].

The component of misperception that best matches "translation" is the **relationship effect** of the Social Relations Model. In $`X_{ij} = \mu + \alpha_i + \beta_j + \gamma_{ij} + \varepsilon_{ij}`$, $`\alpha_i`$ is the perceiver's general tendency, $`\beta_j`$ the target's general expressiveness, and $`\gamma_{ij}`$ the pair-specific residual ([Kenny & La Voie 1984](https://doi.org/10.1016/S0065-2601(08)60144-6)). This **cannot be identified within a single couple**, because with two people the relationship effect is confounded with perceiver and target effects. It requires round-robin family designs, in which each member rates each other member, or people rating several partners, with at least two indicators ([Cook 1994](https://doi.org/10.1037/0022-006X.62.3.500)) [Established]. Family studies find that perceiver and relationship effects dominate ([Eichelsheim et al. 2009](https://doi.org/10.1111/j.1741-3737.2009.00652.x)).

**Channels are not independent, and their weights may change.** Care channels co-vary: time together enables talk and touch, and money can buy time. A model that treats channels as orthogonal axes misstates their structure, so channel-level analyses need a measured covariance or latent-factor structure. Network models of how channels co-vary within couples are exploratory at best, given replicability concerns about such networks ([Forbes et al. 2017](https://doi.org/10.1037/abn0000276)). Whether a channel's importance changes over time can be estimated with time-varying effect models ([Tan et al. 2012](https://doi.org/10.1037/a0025814); [Bringmann et al. 2017](https://doi.org/10.1037/met0000085)). Money might matter more during education, for example, and presence more during a crisis. Such models need long series and a prior theory of why weights should change, such as a developmental transition. Without both, time-varying weights simply overfit [Established method; no relationship application located].

The cross-channel translation matrix $`\boldsymbol{\Lambda}`$ in $`\mathbf{S}_B = \boldsymbol{\Lambda}\,\mathbf{E}_A`$ would capture how much each act counts toward each need, for example how far money "counts" as time. It has $`K^2`$ parameters per dyad, 25 for five channels, and cannot be estimated per dyad from weeks of diaries. It needs pooling with structure (diagonal plus a few theorized off-diagonal terms) or within-dyad randomization of channels [Assumption].

## 8.12 Component audit

| Component | Construct | Validated measure? | Why this operation | Key assumptions | Empirical support | Still speculative |
|---|---|---|---|---|---|---|
| Enactment under capacity | Intention converted to acts within feasible limits | Acts: partly (support coding); intention: no | A constraint form is assumed; the evidence cannot tell a bound from a trade-off | Intention reportable; capacity proxies valid | Stress dampens provider-reported enactment ([Neff, Nguyen & Williamson 2021](https://doi.org/10.1177/0146167220974490)) [Preliminary] | Form of $`g`$; content of $`\mathcal{C}`$ |
| Detection (probit signal detection) | Registering that care occurred | Diary checklists (practice, not validated scales) | Binary occurrence calls for a probit or logit model | Giver report as signal | Misses and false alarms ([Visserman et al. 2019](https://doi.org/10.1177/1948550618757599)) | Channel-specific $`d'`$ |
| Truth and bias | Accuracy, projection, level bias in perceived care | Responsiveness scales; criterion reports | Standard decomposition of judgment | Common metric; criterion is a report | Projection ([Lemay, Clark & Feeney 2007](https://doi.org/10.1037/0022-3514.92.5.834)); accuracy and bias ([Fletcher & Kerr 2010](https://doi.org/10.1037/a0019792)) | Size of $`\delta`$ for care adequacy |
| Motive inference (naïve utility calculus) | Inferred value of the receiver to the giver | None in couples | Bayesian inversion of cost-sensitive choice | Near-rational choice; known options | Laboratory and infants only | All relationship applications |
| Need fulfilment (RSA) | Fit versus level of care | Support desire and receipt items | Separates the agreement-line level ($`a_1, a_2`$) from the joint congruence pattern ($`a_3, a_4`$, principal axis) | Commensurate, commonly centred $`N, S`$; data in incongruent regions; power | Over- and under-provision as a perceived direction of discrepancy, not commensurate need and supply ([Brock & Lawrence 2009](https://doi.org/10.1037/a0015402)) | Care-channel surfaces |
| Two routes | Effects of the same acts with and without perceived regard | Requires independent $`E`$ | Mediation decomposition | Sequential ignorability or randomization | None that survives audit: invisible support did not replicate, and the income studies measured no perception | Whether the route exists; distinct outcome signatures |
| Trust state-space | Trust dynamics and roles | Trait trust scales; daily items | Latent state with feedback | Indicator validity; stationarity | Trust as outcome, mediator and moderator | Bistability; shape of $`p(\cdot)`$ |
| Developmental lag | Giver's need model tracking change | Paired predictions | Error-correction learning | Linear drift; constant $`\lambda`$ | Indirect (normative adolescent change) | Entire component |
| Safety admissibility | Exclusion of unsafe arrangements | CTS2, CAS, PMWI, fear items | Constrained choice over $`\mathcal{F}_{\text{safe}}`$ | Threshold measurable; decided without $`Q`$ | Tolerance standards drift among the highly committed ([Arriaga, Capezza & Daly 2016](https://doi.org/10.1037/pspi0000035)) | Threshold location; normative weight |
| Compatibility set $`\mathcal{F}`$ | Joint feasibility | Goal-conflict and dealbreaker proxies | Set-theoretic emptiness | Essential requirements identifiable | Goal conflict harms ([Gere & Schimmack 2013](https://doi.org/10.1007/s10902-011-9314-2)) | Measurement of $`G`$ |

## 8.13 What can be identified from what data

| Parameter | Data required | Identifiable with existing designs? |
|---|---|---|
| Actor and partner associations ($`a, p`$) | Both partners' $`X`$ and $`Y`$, many dyads | Yes (associational) |
| Truth, projection, directional bias ($`\tau, \pi, \delta`$) | Repeated judgments plus a criterion on the same metric | Yes; "truth" is only another report |
| Detection ($`d', c`$) | Both partners' daily act reports; enough signal-present and signal-absent days | Yes, descriptively; firmer with observers or experiments |
| Agreement-line level versus congruence pattern ($`a_1, a_2`$ versus $`a_3, a_4, p_{10}, p_{11}`$) | Commensurate $`N`$ and $`S`$, large samples | Yes, associational; not yet done for care channels |
| Relationship-specific misperception ($`\gamma_{ij}`$) | Round-robin families or multi-partner designs | Not from couples; yes from families of four or more |
| Route weights ($`\beta_{\text{sub}}, \beta_{\text{sym}}`$) | Enactment independent of perception, ideally randomized | Only with experiments or micro-randomized trials |
| Learning rate $`\lambda`$ | Long paired series of predicted versus reported needs | In principle; no study |
| Translation matrix $`\boldsymbol{\Lambda}`$ | Channel randomization or pooled structure | Not per dyad |
| Trust interpretation function $`p(\cdot)`$ and bistability | Long series spanning low and high trust; within-dyad multimodality; slowly varied inputs | Practically no; ethical limits on manipulating partners downward |

## 8.14 Alternative model formulations compared

| Formulation | Represents | Verdict | Reason |
|---|---|---|---|
| Difference score $`N - E`$ | Mismatch | **Reject** | Imposes untested constraints; confounds components ([Edwards 1994](https://doi.org/10.1006/obhd.1994.1029)) |
| Cosine or profile correlation between $`\mathbf{E}`$ and $`\mathbf{N}`$ | Pattern match | **Reject** | Scale-invariant (ignores amount), origin- and unit-dependent, inflated by normativeness ([Wood & Furr 2016](https://doi.org/10.1177/1088868315581119)) |
| Dot product $`\mathbf{E}\cdot\mathbf{N}`$ | "Aligned amount" | **Reject** | Mixes amount, need intensity and alignment |
| Weighted similarity $`\sum_k w_k E_k N_k`$ | Importance-weighted match | **Reject** | Weighting adds nothing; origin-dependent ([Trauer & Mackinnon 2001](https://doi.org/10.1023/A:1013159414364)) |
| Polynomial regression with RSA (dyadic, multilevel, cubic, spline) | Level versus fit | **Use (primary)** | Separates amount from mismatch; congruence increments usually small ([Yang et al. 2008](https://doi.org/10.1016/j.hrmr.2008.07.014)) |
| Latent congruence model | Fit with measurement error | **Use** | Controls error; tests equivalence ([Cheung 2009](https://doi.org/10.1177/1094428107308914)) |
| Actor–partner interdependence model, cross-sectional or dynamic | Mutual influence | **Use** | Standard; associational ([Cook & Kenny 2005](https://doi.org/10.1080/01650250444000405)) |
| Social Relations Model (family round robin) | Perceiver, target and relationship variance | **Use for the "translation variance" claim** | Only design that identifies $`\gamma_{ij}`$ ([Eichelsheim et al. 2009](https://doi.org/10.1111/j.1741-3737.2009.00652.x)) |
| Truth and bias | Accuracy versus bias per link | **Use** | Mature in couples ([West & Kenny 2011](https://doi.org/10.1037/a0022936)) |
| Quasi-signal detection (mixed probit) | Noticing acts | **Use** | With observer or experimental criterion where possible |
| Naïve utility calculus or inverse planning | Inferred regard from costs | **Theoretical; test with stimuli** | Strong in the laboratory, absent in couples |
| Bayesian or reinforcement-learning trust updating | Trust learning | **Speculative for couples** | Shown with strangers ([Siegel et al. 2018](https://doi.org/10.1038/s41562-018-0425-1)) |
| Love differential equations ([Strogatz 1988](https://doi.org/10.1080/0025570X.1988.11977342); [Rinaldi 1998](https://doi.org/10.1137/S003613999630592X)) | Mutual feelings over time | **Reject as empirical model** | Never estimated on relationship data; calibrated on literature |
| Threshold autoregression for coded interaction ([Hamaker, Zhang & van der Maas 2009](https://doi.org/10.1007/s11336-009-9113-4)) | Affect influence in conflict | **Use for interaction data** | Estimable; the related divorce prediction shrinks under cross-validation ([Heyman & Slep 2001](https://doi.org/10.1111/j.1741-3737.2001.00473.x)) |
| Dynamic structural equation modelling or multilevel vector autoregression | Within-dyad lagged dynamics | **Use (workhorse)** | ([Asparouhov, Hamaker & Muthén 2018](https://doi.org/10.1080/10705511.2017.1406803)) |
| Classic cross-lagged panel model | "Reciprocal effects" | **Reject** | Confounds stable differences with within-person effects ([Hamaker, Kuiper & Grasman 2015](https://doi.org/10.1037/a0038889); [Lucas 2023](https://doi.org/10.1177/25152459231158378)) |
| Random-intercept cross-lagged panel model | Within-person reciprocal association | **Use cautiously** | Depends on parametric assumptions ([Lüdtke & Robitzsch 2022](https://doi.org/10.1080/10705511.2022.2065278)) |
| Regime-switching or hidden Markov models | Discrete relational states | **Use** | Sudden shifts without assuming bistability ([Hamaker & Grasman 2012](https://doi.org/10.1007/s11336-012-9254-8)) |
| Bistable feedback $`dT/dt = \eta[p(T) - T]`$ | Self-reinforcing trust | **Theoretical only** | No relationship evidence |
| Early-warning signals | Approaching transitions | **Do not rely on** | Weak support ([Helmich et al. 2024](https://doi.org/10.1038/s44159-024-00369-y)) |
| Network models | Co-variation of channels | **Exploratory only** | Replicability concerns ([Forbes et al. 2017](https://doi.org/10.1037/abn0000276)) |
| Necessary condition analysis | Bottlenecks and gates | **Use for gate claims** | Built for necessity claims ([Dul 2016](https://doi.org/10.1177/1094428115584005)) |
| Machine-learning prediction | Predictability | **Use as benchmark** | [Joel et al. 2020](https://doi.org/10.1073/pnas.1917036117) |
| Factorial experiments and within-couple micro-randomized trials | Causal effect of channel match versus amount | **Use (strongest test)** | Randomization within persons ([Qian et al. 2022](https://doi.org/10.1037/met0000283)) |

## 8.15 Explanation versus prediction

The equations above are **explanatory**: they state hypothesized structure and say what would have to be true for each part to hold. Explanatory adequacy does not imply predictive power, and conflating the two is a common error ([Shmueli 2010](https://doi.org/10.1214/10-STS330); [Yarkoni & Westfall 2017](https://doi.org/10.1177/1745691617693393)) [Established].

The relevant predictive benchmark is sobering. In 43 Western datasets, self-reported relationship-specific variables predicted up to 45% of baseline relationship quality and up to 18% of its level at follow-up, but at most 5% (mean about 2.2–2.5%) of its change, measured as slopes over typically one to two years ([Joel et al. 2020](https://doi.org/10.1073/pnas.1917036117)). A translation model earns predictive standing only if its constructs improve **out-of-sample** prediction of *change* beyond perceived partner commitment, appreciation and similar perceptions, in pre-registered tests. If they do not, that failure counts against the comparative claim, whatever the model's explanatory appeal.

---

**Navigation:** [← Revised model](07-revised-model.md) · [Contents](README.md) · [The model without math →](09-model-without-math.md)
