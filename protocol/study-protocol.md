[Overview](../audit/README.md) · [Part A: evidence audit](../audit/evidence-audit.md) · [Part B: competing predictions](competing-predictions.md) · **Part C: study protocol** · [Corrections](../audit/corrections.md)

# Part C: Study protocol

> **Status: design document only.** No participant data have been collected, no one has been recruited and no ethics application has been filed. Every sample size, interval and threshold below is a proposal. Each is to be fixed by simulation, piloting, ethics review and a Stage 1 Registered Report before any data exist.

The protocol tests the frozen framework of *Can Love Be Lost in Translation?* (version 0.2.0) against four rivals:

1. the total amount of support received predicts outcomes;
2. perceived support alone predicts outcomes;
3. need fulfilment predicts outcomes;
4. existing trust or attachment explains the apparent translation effect.

The framework distinguishes love intended, expressed, perceived and received from relationship compatibility. It writes these links as ten components (`README.md`, "Model at a glance"; `paper/08-mathematical-representation.md` §8.4–8.10). The protocol refers to them by number:

| No. | Component | Content |
|---|---|---|
| (1) | Enactment under capacity | — |
| (2) | Detection | A probit with sensitivity $`d'`$, criterion $`c`$ and visibility $`\gamma v_k`$ |
| (3) | Construal | Tracking $`\tau`$, projection $`\pi`$ and a level bias $`\delta(T)`$ |
| (4) | Inference of regard from believed cost | — |
| (5) | Fit | Supply $`\mathbf S=\boldsymbol\Lambda\mathbf E`$ and a polynomial surface $`h(S,N)`$ over commensurate supply and need |
| (6) | Two routes | $`\mathbf Y=\boldsymbol\alpha+\boldsymbol\beta_{\text{sub}}h(S,N)+\boldsymbol\beta_{\text{sym}}Q+\boldsymbol\Gamma\mathbf x+\mathbf e`$ |
| (7) | Trust updating | — |
| (8) | The giver's learning of the receiver's needs | — |
| (9) | The compatibility set $`\mathcal F`$ | — |
| (10) | The safety admissibility constraint | $`\mathcal F_{\text{safe}}=\{x\in\mathcal F:\mathrm{Safe}(x)=1\}`$ |

The routes are pathways of effect, not kinds of act. Safety is a constraint decided from safety indicators, never from perceived love, and autonomy is a separate outcome. **Neither enters any model as a coefficient to be traded against satisfaction.** No new theoretical equation is introduced.

## Aims and scope: a Korean case study with two separate kinds of dyad

**Aim.** The study asks which parts of the framework can be told apart from the four rivals in one population, measured over one year. Its confirmatory targets are:
- detection (2);
- construal (3);
- inference of regard from cost (4);
- fit against level (5);
- the causal effect of channel match against intensity, via (2), (3) and (5);
- the incremental, within-person validity of perceived regard (6).

The split between the substantive and symbolic routes is estimated with pre-registered sensitivity analysis, but it is never called identified. The giver's learning rate (8), trust dynamics (7) and compatibility (9) are exploratory. Intention to care, compatibility and channel preferences are classed in v0.2.0 as "not reliably operationalizable" (`paper/17-what-testing-requires.md`). They are pre-registered as exploratory only.

**Korea is a case study, not grounds for generalisation.** The study samples residents of the Seoul metropolitan area, following the v0.2.0 design (`paper/18-proposed-study.md:5`), and stratifies on household income, co-residence, working hours and, in the parent–child arm, child gender.
- Estimates describe the sampled strata, the channels measured and the timescale observed.
- National averages are never used to describe individuals or families.
- A comparison country is optional. It is added only if cross-national measurement invariance can be tested first, and no cross-national contrast is confirmatory in this protocol.

**Two arms are analysed separately and never pooled into one reciprocity model.**

| Arm | Dyads | Status |
|---|---|---|
| **Arm R** (romantic) | Married or cohabiting couples, both members adults | **Confirmatory core.** Validated couple measures exist for the main outcome, and the audited evidence comes overwhelmingly from couples |
| **Arm P** (parent–child) | One parent and one emerging-adult child aged 19–29, the population of the v0.2.0 primary arm | Confirmatory **only for hypotheses whose measures pass the Phase 0 tests of role invariance.** Otherwise exploratory, because no validated parent–child analogues were found for the couple satisfaction, responsiveness and trust scales |
| **Module F** (optional) | Four-member families in which every member is an adult | Needed only for relationship-specific misperception, which requires round-robin groups of at least four ([Kenny, SOREMO](https://davidakenny.net/srm/soremo.htm); author's site). Restricting it to adults avoids involving minors in the first study |

The age floor of 19 rests on Korea's age of majority, which is **PRIOR KNOWLEDGE / UNVERIFIED** in the notes and must be confirmed against the Civil Act before submission.

**Parental responsibility is kept distinct from romantic reciprocity.** This follows the framework's own position (`paper/02-definitions-and-distinctions.md:50–58`; `paper/10-father-daughter-example.md:60–62`) and is applied through five rules:

1. **Couples (Arm R).** Reciprocity is a legitimate standard, so both directions of care are modelled symmetrically, and asymmetries in care exchanged are an admissible outcome.
2. **Parents and children (Arm P).** The primary estimand is care from parent to child. The child's own giving is measured because equation (3) needs it as the projection term $`O_B`$. It is **never** entered as a "return leg", repayment or balance score, and no hypothesis treats a child's lower giving as a translation failure on the child's side.
3. **Filial piety** (hypothesis H7) is analysed as the child's attitude: an outcome and a marker of the symbolic route, not an obligation the child fails to meet.
4. **A parent's expectation of repayment,** if measured, is analysed as a risk marker, not as a standard. The paper cites Korean adolescent evidence linking repayment expectation to psychological control (`paper/02-definitions-and-distinctions.md:58`) [Preliminary].
5. **Materials and feedback** never suggest that a child owes care back.

## Phase 0 comes first: Korean measurement work before any substantive test

The audit of instruments found that **the core translation constructs lack Korean validation**: perceived responsiveness, desired versus received support, trust, relationship-specific attachment, commitment, autonomy support and the brief screens for intimate partner violence. Validated Korean versions exist for couple satisfaction, depressive symptoms, perceived stress, a short-form adult attachment measure and a state attachment measure (Table C2). Phase 0 is therefore a separate, pre-registered psychometric study with its own sample and four tasks.

**1. Adaptation.** Forward translation, back-translation, expert review and cognitive interviews, for each new or untranslated instrument.

**2. Validation.** Confirmatory factor analysis followed by three kinds of invariance testing:
- *across partners and roles*, using fully dyadic invariance models ([Sakaluk, Fisher & Kilshaw 2021](https://doi.org/10.1111/pere.12341); abstract);
- *between parent and child*, for the Arm P wordings;
- *over time*, inside dynamic measurement models, which can test whether scales are "invariant across time and across people" ([McNeish et al. 2021](https://doi.org/10.1080/10705511.2021.1915788); abstract).

**3. Three tests that the hypotheses depend on.**
- **Discriminant validity between perceived regard and relatedness need satisfaction.** Rival 3 can be tested only if they are distinct.
- **Commensurability of need and supply.** They need the same stem, the same response scale and a shared midpoint, plus invariance between partners. Without these, the response-surface quantities say nothing about fit (§8.7).
- **Anchor items** to estimate the minimum subjectively experienced difference on each outcome, for setting smallest effect sizes of interest ([Anvari & Lakens 2021](https://doi.org/10.1016/j.jesp.2021.104159); abstract).

**4. Pilots.** A pilot of diary burden and compliance, and a pilot of the safety procedures.

**Phase 0 can fail.** If a measure fails its pre-registered criteria, every hypothesis that depends on it becomes exploratory. It is not tested with an unvalidated measure.

## Observable variables and latent constructs

**Table C1. Observable variables and latent constructs**

| v0.2.0 term | Construct | Observed indicators | Reporter and timescale | Status |
|---|---|---|---|---|
| $`I_{A\to B,k}`$ (1) | Intention to care, by channel | "Today I meant to show care by…", for each channel | Giver; evenings | Latent; no validated measure; **exploratory only** |
| $`\mathcal C_A(t)`$ (1) | Capacity | Daily stress item; hours worked; money spent; Perceived Stress Scale (PSS) at each wave; log of daily stressors | Giver; daily and waves | Latent proxies [Assumption] |
| $`E_{A\to B,k}`$ (1) | Enacted care, by channel (presence, talk, touch, practical help, money) | Act checklist: did it happen, and how much (minutes, won, count); observer codes in the laboratory module | Giver; observers; evenings | Observed; established practice, not a validated scale |
| $`c`$ | Cost of the act to the giver | Rated cost for each act | Giver; evenings | Observed; no validated measure |
| $`D_{B,k}`$ (2) | Detection | "Did [the other] do X for you today?", for each channel, paired with the giver's log | Receiver; evenings | Observed; coded as hits, misses, false alarms and correct rejections |
| $`v_k`$ (2) | Visibility of the act and of its cost | Channel coded by design; giver reports whether the act and its cost were visible | Design and giver; evenings | Partly observed |
| $`Q_B`$ (3) | Perceived regard | Short daily regard items; brief PRI at each wave | Receiver; evenings and waves | Latent; daily items to be validated in Phase 0 |
| $`X_A`$, $`O_B`$ (3) | Criterion for A's care; B's own care given (projection term) | The giver's own report; the receiver's own giver log | Both; evenings | Observed. **In Arm P, the child's giving serves only as the projection term** |
| $`T_B`$ (3, 7) | Trust | Multi-item state trust module each week; Trust Scale at baseline | Receiver; weekly | Latent state; no validated daily short form exists |
| $`\hat c`$, inferred $`w`$ (4) | Believed cost; regard inferred from cost | Receiver's estimate of the cost and the inferred motive; vignette experiment | Receiver; evenings; separate vignette samples | Latent; Theoretical |
| $`N_{B,k}`$, $`S_{B,k}`$ (5) | Need and supply on one metric | "How much X did you want today?" and "How much X did you receive today?", with the same stem and scale, centred at the midpoint | Receiver; evenings | Observed; commensurate by design, subject to the Phase 0 tests |
| $`\boldsymbol\Lambda\mathbf E`$ (5) | Supply implied by enacted acts | Estimated with a pooled, structured $`\boldsymbol\Lambda`$: diagonal plus a few theorised off-diagonal terms | Derived | Not estimable for a single dyad |
| $`\mathbf Y_B`$ (6) | Outcomes | Relational: four-item Couples Satisfaction Index (CSI-4) weekly and K-CSI-16 at waves; gratitude. Emotional: PHQ-9 at waves; daily mood. Substantive: need relief in each channel; completion of tasks; in Arm P, changes in education and employment | Receiver; partner; evenings, weeks and waves | Mixed. Includes outcomes not reported by the receiver |
| $`\tilde N_{A\to B}`$ (8) | The giver's model of the receiver's need | The giver's evening prediction of the receiver's need in each channel | Giver; evenings | Observed; exploratory |
| $`G`$, $`W`$, $`\mathcal F`$ (9) | Compatibility | Goal-conflict items | Both; waves | Not reliably operationalizable; descriptive only |
| $`\mathbf Z`$, $`\mathrm{Safe}(x)`$ (10) | Safety | Victimisation-only screen items; fear and control items | Each member, privately; baseline, every burst, monthly | An indicator against a normative threshold |
| $`U_B`$ | Autonomy | Autonomy satisfaction and frustration; psychological control and autonomy support (Arm P) | Receiver; weekly and waves | Latent; **a separate outcome** |
| Rival 1 | Total amount | Sum over channels of the giver-logged $`E_k`$; sum of received $`S_k`$; SIRRS frequency | Giver; receiver | Observed |
| Rival 3 | Need fulfilment | Basic Psychological Need Satisfaction and Frustration Scale (BPNSFS); need fulfilment within the relationship | Receiver; weekly and waves | Latent |
| Rival 4 | Prior trust and attachment | Trust Scale and relationship-specific attachment (ECR-RS) at baseline; State Adult Attachment Measure (SAAM) weekly; lagged state trust | Receiver; baseline, weekly | Latent |

## Instruments and their Korean validation status

Table C2 lists the best-established measure for each construct and its Korean validation status. Lengths are given only where the notes verified them. Every other item count is **UNVERIFIED** (prior knowledge) and must be checked against the original publication.

**Table C2. Instruments and Korean validation status**

| Construct | Instrument and source | What is verified | Korean validation | Role in the protocol |
|---|---|---|---|---|
| Relationship satisfaction | Couples Satisfaction Index, CSI-32, -16 and -4 ([Funk & Rogge 2007](https://doi.org/10.1037/0893-3200.21.4.572); abstract) | Developed with item response theory in 5,315 people; more precise than older scales | **Yes.** K-CSI tested in 218 couples; one-factor structure for all three forms; distress cut-offs 105.5, 50.25 and 13.25 ([Kim et al. 2022](https://doi.org/10.4040/jkan.21177); abstract) | Arm R outcome. Parallel wording in Arm P needs Phase 0 role invariance |
| Perceived regard | Perceived Responsiveness and Insensitivity scale, PRI ([Crasta et al. 2021](https://doi.org/10.1037/pas0000986); abstract) | Two 8-item subscales; sensitive to change when given every other week for 8 weeks (n = 173); dyadic validity in 161 couples | **None found** | $`Q`$ at each wave; daily items derived in Phase 0 |
| Perceived regard (alternative) | Perceived Partner Responsiveness Scale, PPRS ([Reis et al. 2017](https://doi.org/10.1002/9781119102991.ch57); abstract) | Item count UNVERIFIED | **None found** | Alternative to the PRI |
| Daily responsiveness | Daily diary items ([Laurenceau, Barrett & Rovine 2005](https://doi.org/10.1037/0893-3200.19.2.314); [Maisel & Gable 2009](https://doi.org/10.1111/j.1467-9280.2009.02388.x); abstracts) | Used in dyadic diaries of 42 days (96 couples) and with 67 couples; exact wording unverified | None | Template for the daily $`Q`$ items |
| Support adequacy | SIRRS ([Dehle, Larsen & Landers 2001](https://doi.org/10.1080/01926180126500); [Barry et al. 2009](https://doi.org/10.1037/a0014174); abstracts) | Adequacy rated daily for 7 days by 177 married people; four types of support received | None located (no targeted search) | Cross-check; SIRRS frequency for rival 1 |
| Desired versus received support | Ratings of desired and experienced support ([Xu & Burleson 2001](https://doi.org/10.1111/j.1468-2958.2001.tb00792.x); abstract) | 100 US and 102 Chinese newlyweds; five types of support | None | Template for commensurate $`N`$ and $`S`$. The new channel items **cannot be called validated** |
| Need satisfaction and frustration | BPNSFS ([Chen et al. 2015](https://doi.org/10.1007/s11031-014-9450-1); metadata) | 24 items in six subscales of four | **Partly.** K-BPNSFS validated in 367 cancer survivors ([Yeom & Lee 2024](https://doi.org/10.3390/healthcare12242535); full text). A workplace study record ([Kyobo](https://scholar.kyobobook.co.kr/article/detail/4050027792125); secondary) has not been reconciled with it | Rival 3; autonomy subscales for $`U`$ |
| Need fulfilment within a relationship | [La Guardia et al. 2000](https://doi.org/10.1037/0022-3514.79.3.367); [Patrick et al. 2007](https://doi.org/10.1037/0022-3514.92.3.434) (abstracts) | Fulfilment rated for each partner; diary use in Patrick et al.'s Study 3 | None | Rival 3, specific to the relationship |
| Trust | Trust Scale ([Rempel, Holmes & Zanna 1985](https://doi.org/10.1037/0022-3514.49.1.95)); Dyadic Trust Scale ([Larzelere & Huston 1980](https://doi.org/10.2307/351903)) | Three dimensions in the Trust Scale; item counts UNVERIFIED | **None found** | Baseline measure for rival 4; a weekly state module is new |
| Relationship-specific attachment | ECR-RS ([Fraley et al. 2011](https://doi.org/10.1037/a0022898); abstract) | Attachment rated separately for each target; item count UNVERIFIED | **None found.** One 2015 Korean study used it with 317 students (secondary) | Rival 4, one rating per target; covariate for relationship-specific variance |
| Global and state attachment | K-ECRR-SF, 12 items ([Lee, Kim & Shin 2023](https://doi.org/10.1007/s10447-023-09503-6)); Korean ECR-R ([Lee, Grossman & Krishnan 2008](https://doi.org/10.1177/0013164407313367)); Korean SAAM ([Park et al. 2012](https://doi.org/10.4306/jknpa.2012.51.4.147)) (abstracts) | Rasch analysis warns that items at high anxiety and avoidance may not suit Korean students | **Yes** | Global and weekly state attachment |
| Commitment | Investment Model Scale ([Rusbult, Martz & Agnew 1998](https://doi.org/10.1111/j.1475-6811.1998.tb00177.x); abstract) | Four factors; predicted later adjustment and break-up | **None found.** A Korean Commitment Inventory record exists ([Kyobo](https://scholar.kyobobook.co.kr/article/detail/4050026794191); secondary) | Confounder and moderator |
| Perceived parental acceptance | PARQ ([Rohner, Khaleque & Cournoyer 2005](https://doi.org/10.1525/eth.2005.33.3.299); metadata) | Reliable in a 51-study meta-analysis ([Khaleque & Rohner 2002](https://doi.org/10.1177/0022022102033001006); abstract) | Used in 1985; **no validation verified, none for emerging adults** | Arm P |
| Psychological control | Psychological Control Scale ([Barber 1996](https://doi.org/10.2307/1131780); abstract) | Predicted internalising problems in youth | **Adolescents only** ([Soenens et al. 2012](https://doi.org/10.1016/j.adolescence.2011.05.001); [Choe et al. 2026](https://doi.org/10.1177/10731911261440140); abstracts) | Arm P autonomy outcome. Phase 0 must validate it for adults aged 19–29 |
| Autonomy support | P-PASS ([Mageau et al. 2015](https://doi.org/10.1037/a0039325); metadata) | Item count UNVERIFIED | **None found.** Nearest is a helicopter-parenting scale (secondary; DOI not verified) | Arm P autonomy outcome |
| Safety screen | Composite Abuse Scale short form, CAS-R-SF ([Ford-Gilboe et al. 2016](https://doi.org/10.1136/bmjopen-2016-012824)); HARK ([Sohal, Eldridge & Feder 2007](https://doi.org/10.1186/1471-2296-8-49)) (abstracts) | 15 items and 4 questions; victimisation only | **None found** | Private screen for $`\mathrm{Safe}(x)`$ |
| Partner violence, full scale | Revised Conflict Tactics Scales, CTS2 ([Straus et al. 1996](https://doi.org/10.1177/019251396017003001)), and its short form CTS2S ([Straus & Douglas 2004](https://doi.org/10.1891/vivi.19.5.507.63686)) (abstracts) | Asks about the respondent's own acts and the partner's | Korean CTS2: a study record only, with α .64–.94 (secondary; UNVERIFIED). No CTS2S | **Not used for the dyadic screen** (see the safety section) |
| Controlling behaviour | Checklist of Controlling Behaviors ([Lehmann, Simmons & Pillai 2012](https://doi.org/10.1177/1077801212456522); abstract) | 84 items; validated in shelter samples | None found | Not used; too long and validated only in shelters |
| Korean violence measures | Korean Dating Violence Questionnaire–Revised; Korean Index of Spouse Abuse; Korean Validation and Invalidation Response Scale (all secondary; no DOIs verified) | — | Korean-developed | To be reviewed in Phase 0 |
| Depressive symptoms | PHQ-9 ([Kroenke, Spitzer & Williams 2001](https://doi.org/10.1046/j.1525-1497.2001.016009606.x); abstract) | Score ≥ 10: sensitivity 88%, specificity 88% | **Yes**, in older adults ([Han et al. 2008](https://doi.org/10.1016/j.comppsych.2007.08.006)) and psychiatric outpatients ([Shin et al. 2019](https://doi.org/10.30773/pi.2019.02.01)) | Confounder and outcome; sensitive data under Korean law |
| Perceived stress | PSS ([Cohen, Kamarck & Mermelstein 1983](https://doi.org/10.2307/2136404); abstract) | 14 items | **Yes.** Korean PSS-14, -10 and -4 ([Lee et al. 2015](https://doi.org/10.1111/scs.12131); abstract) | Proxy for capacity; confounder |
| Daily stressors | Daily Inventory of Stressful Events ([Almeida, Wethington & Kessler 2002](https://doi.org/10.1177/1073191102091006); abstract) | A stressor occurred on 40% of days in 1,031 US adults | No Korean version searched | Time-varying confounder |

**The Korean validation populations rarely match the study population.** The validations were done in cancer survivors, older adults, psychiatric outpatients, people with chronic disease, students and adolescents. Only the K-CSI was validated in couples. **Even the validated Korean instruments therefore need checks in the target population during Phase 0.**

## Time intervals: daily for fast processes, weekly for slow states, bursts for change

The timescales follow the processes the model describes:
- detection, construal and daily acts are fast;
- trust, need fulfilment, relationship quality and commitment are slow.

Theory about the timescale of a process should set the interval ([Hamaker 2023](https://doi.org/10.1037/met0000600); abstract). Optimal lags for panel designs are "usually quite short" ([Dormann & Griffin 2015](https://doi.org/10.1037/met0000041); abstract). Bursts separate short-term variation from long-term change ([Sliwinski 2008](https://doi.org/10.1111/j.1751-9004.2007.00043.x); abstract). Continuous-time models absorb unequal spacing between waves ([Voelkle et al. 2012](https://doi.org/10.1037/a0027543); abstract).

**Table C3. Timeline (proposal)**

| When | Full protocol (Arms R and P, Module F) | Assessment-only control |
|---|---|---|
| **Phase 0**, before the main study, with a separate sample | Adaptation, psychometrics, invariance and discriminant validity; burden, compliance and safety pilots | — |
| **Baseline (T0)** | Separate consents for sensitive data; private safety screen; trait measures (ECR-RS, Trust Scale, Investment Model Scale, BPNSFS, CSI or parallel items, PRI, PARQ and control scales in Arm P, PHQ-9, PSS); structural variables | Baseline battery only |
| **Burst 1: days 1–28** | Short evening diary, with planned missingness in rotating channel blocks; the same blocks go to both members on a given dyad-day so that their reports can be paired. Weekly module on days 7, 14, 21 and 28: state trust, relationship-specific need satisfaction, CSI-4, SAAM, autonomy frustration and a safety check. **Micro-randomised trial (MRT) on days 15–28** in eligible dyads | — |
| **Laboratory module** (subsample), after Burst 1 | A support conversation and a disagreement, each partner rating the recording segment by segment, plus observer coding | — |
| **Months 2–5 and 7–11** | A brief check-in every four weeks: CSI-4, brief PRI and a safety re-screen | — |
| **Burst 2: month 6, 14 days** | Evening diary, weekly module and safety screen | — |
| **Burst 3: month 12, 14 days, plus follow-up** | Evening diary. Follow-up outcomes: CSI-16 or -32, PRI, PHQ-9, BPNSFS, autonomy, dissolution (Arm R), filial piety and changes in education or employment (Arm P), and global ratings of care given and received | 12-month outcomes |
| **Vignette experiment** (separate samples, at any time) | Unrelated adults rate an identical act of provision, with information about its cost and the giver's constraints randomised between subjects (hypothesis H4) | — |

**Why these lengths.**
- Twenty-eight days follows v0.2.0 and lies within the published range for dyadic diaries, 14 to 42 days. Fourteen days is the lower bound of that range.
- **The month-6 spacing of the bursts has no evidence base specific to relationships.** It must be justified by the pilot and the simulations.
- The diary is kept short and split into rotating blocks because questionnaire length, not prompt frequency, degraded data quality in an experiment ([Eisele et al. 2022](https://doi.org/10.1177/1073191120957102); abstract). Item display and order are randomised wherever ordering is not required for identification ([Arslan et al. 2021](https://doi.org/10.1037/met0000294); abstract).
- The first diary days are modelled or discarded, because early reports run high ([Shrout et al. 2018](https://doi.org/10.1073/pnas.1712277115); abstract).
- Trust measured in the previous week's module, not on the same evening, serves as the lagged confounder of the day's acts and perceptions.

## Identification assumptions

Each estimand is identified only under the assumptions listed in Table C4. **Randomisation in the micro-randomised trial (MRT) identifies total short-run effects only.** Splitting an effect into a substantive and a symbolic route runs through $`Q`$, which is never randomised, so the split stays conditional on sequential ignorability and is reported with a sensitivity analysis. Within-person centring removes stable confounders but not time-varying ones ([Rohrer & Murayama 2023](https://doi.org/10.1177/25152459221140842); abstract).

**Table C4. Identification assumptions**

| Estimand (equation) | Design | Key assumption | How it is probed |
|---|---|---|---|
| Sensitivity $`d'`$ and criterion $`c`$ (2) | Paired diaries | The giver's report stands in for occurrence, so misses and false alarms are disagreements, not errors. Reports are independent (separate devices). Each person has enough signal-present and signal-absent days | Observer criterion in the laboratory subsample. Prompted acts in the MRT supply a known signal |
| Tracking $`\tau`$, projection $`\pi`$, level bias $`\delta`$ (3) | Within-person truth-and-bias models | $`Q`$, $`X`$ and $`O`$ share a metric; the criterion is itself a report | Observer-coded criterion; Phase 0 invariance tests |
| Fit surface $`a_1`$–$`a_5`$ (5) | Multilevel response surface analysis | $`N`$ and $`S`$ are commensurate, share a midpoint and are invariant across partners; enough observations fall in incongruent regions | Report the share of observations in incongruent regions; compare constrained models |
| Excursion effects of match and of intensity on same-evening $`Q`$, need relief and detection | MRT ([Qian et al. 2022](https://doi.org/10.1037/met0000283); abstract) | Known randomisation probabilities (positivity); consistency; no anticipation. Interference within the dyad is handled by an estimand that treats the dyad as the cluster ([Shi, Wu & Dempsey 2023](https://doi.org/10.1093/biomet/asac065)). Moderators are measured before randomisation ([Boruvka et al. 2018](https://doi.org/10.1080/01621459.2017.1305274)) (abstracts) | Randomisation checks; prompt uptake logged |
| Routes $`\beta_{\text{sub}}`$, $`\beta_{\text{sym}}`$ (6) | Giver-logged or randomised $`E`$, then mediation | $`E`$ is measured independently of the receiver. For the "not through regard, carried by what was done" reading, $`S`$ is built from $`E`$ through (5) rather than from the receiver's report; both versions are reported. **Sequential ignorability:** no unmeasured same-day confounding of $`Q`$ and $`Y`$ ([Imai, Keele & Yamamoto 2010](https://doi.org/10.1214/10-STS321); abstract) | Pre-registered mediator sensitivity analysis ([Imai, Keele & Tingley 2010](https://doi.org/10.1037/a0020761)). Robustness value ([Cinelli & Hazlett 2020](https://doi.org/10.1111/rssb.12348)). E-value ([VanderWeele & Ding 2017](https://doi.org/10.7326/M16-2607)) (abstracts). A pre-stated answer to how strong a time-varying trust confounder would have to be to erase the symbolic route |
| Within-person effects against rival 4 | Person-mean centring; lagged state trust | Time-varying confounders are measured before the day's $`E`$ and $`Q`$; perceived care is not adjusted for when estimating the total effect of $`E`$ (a possible collider) | Lag structure fixed in the pre-registration |
| Relationship-specific variance $`\gamma_{ij}`$ (§8.11) | Four-member round robin | At least four members; repeated days serve as multiple indicators | Covariates: ECR-RS and trust, measured for each target |
| Trust dynamics (7); learning rate $`\lambda`$ (8) | Dynamic structural equation models; paired predictions | Stationarity within bursts; linear drift; constant $`\lambda`$ | Exploratory only |
| Change across bursts | Continuous-time models | Unequal spacing between bursts is modelled ([Voelkle et al. 2012](https://doi.org/10.1037/a0027543); abstract) | — |
| Non-compensability below the safety threshold (exploratory) | Threshold, hurdle or necessary-condition models (§8.10) | $`\mathrm{Safe}`$ is decided from $`\mathbf Z`$ alone; the threshold is normative | Never used to recommend or to rank arrangements |

**Two model types are avoided.** The classic cross-lagged panel model is not used, because it conflates stable differences with within-person effects ([Hamaker, Kuiper & Grasman 2015](https://doi.org/10.1037/a0038889); [Lucas 2023](https://doi.org/10.1177/25152459231158378); abstracts). Random-intercept versions are used only cautiously, because their results depend on parametric assumptions ([Lüdtke & Robitzsch 2022](https://doi.org/10.1080/10705511.2022.2065278); abstract).

## Competing models fitted to the same data

Every model is fitted to the same data and the same measurement models, so that no comparison is confounded by unequal reliability. The rival restrictions are written on the parameters of equations (5) and (6).

**Table C5. Competing models**

| Model | Content in v0.2.0 terms |
|---|---|
| **(M) Translation** | Equations (2), (3), (5) and (6) as frozen, with both routes |
| (M−sub) | $`\beta_{\text{sub}}=0`$. At the outcome level this is rival 2 |
| (M−sym) | $`\beta_{\text{sym}}=0`$ |
| **(1) Amount** | Total giver-logged $`E`$ (variant 1b) or total received $`S`$ (variant 1a); no congruence curvature and no $`Q`$ |
| **(2) Perception** | $`Q`$ only |
| **(3) Need fulfilment** | BPNSFS or need fulfilment within the relationship, alone |
| **(4) Trait** | Baseline trust plus relationship-specific attachment (ECR-RS), with every translation term omitted |

**How the models are compared.**
- **Nested pairs:** likelihood-ratio tests or differences in information criteria.
- **Non-nested pairs, such as (2) against (3):** Vuong-type tests for structural equation models ([Merkle, You & Preacher 2016](https://doi.org/10.1037/met0000038); abstract).
- **Bayesian variants:** leave-one-out cross-validation ([Vehtari, Gelman & Gabry 2017](https://doi.org/10.1007/s11222-016-9696-4); metadata).
- **Directional hypotheses:** informative-hypothesis Bayes factors ([Hoijtink et al. 2019](https://doi.org/10.1037/met0000201); abstract).
- **Robustness:** multiverse analysis ([Steegen et al. 2016](https://doi.org/10.1177/1745691616658637); abstract).
- **Predictive benchmark:** out-of-sample prediction of 12-month *change* beyond perceived partner commitment and appreciation, the strongest predictors in a pooled analysis of 43 datasets ([Joel et al. 2020](https://doi.org/10.1073/pnas.1917036117); full text).

## Power-analysis strategy

No sample size is fixed here, because none can be justified without simulation. The procedure has six steps.

1. **Pre-register a smallest effect size of interest (SESOI) for every confirmatory parameter.** Each is anchored to the minimum subjectively experienced difference from the Phase 0 anchor items ([Anvari & Lakens 2021](https://doi.org/10.1016/j.jesp.2021.104159); abstract). Published effect sizes from the audited sources supply sensitivity grids, not assumed true values:
   - the weakening of the slope from need to support under stress, .81 against .72 ([Neff, Nguyen & Williamson 2021](https://sites.utexas.edu/realproject/files/2024/11/too_stressed_to_help.pdf); full text);
   - same-day gratitude coefficients of .18–.41 ([Visserman et al. 2019](https://doi.org/10.1177/1948550618757599); full text);
   - laboratory d of 0.36–1.09 across contrasts ([Bolger & Amarel 2007](http://www.columbia.edu/~nb2229/docs/bolger-amarel-support-experiments-2006.pdf); full text);
   - attachment effects of sr² ≈ .06 ([Collins & Feeney 2004](https://doi.org/10.1037/0022-3514.87.3.363); full text).

   Laboratory effects are likely to overstate field effects.
2. **Simulate data from the frozen equations,** with parameter grids that include the null value each rival implies.
3. **Use the tool that fits each parameter** (Table C6).
4. **Spend the budget on more dyads rather than more days.** Small effects at level 2 and across levels could not be detected with up to 200 clusters ([Arend & Schäfer 2019](https://doi.org/10.1037/met0000195); abstract). Many subjects with few time points outperform the reverse ([Schultzberg & Muthén 2018](https://doi.org/10.1080/10705511.2017.1392862); abstract). This supports v0.2.0's guidance of several hundred dyads.
5. **Model compliance at the level of the dyad-day,** since a dyad-day is complete only if both members respond. Start from the 75–79% compliance seen in experience-sampling studies ([Jones et al. 2019](https://doi.org/10.1111/add.14503); [Wrzus & Neubauer 2023](https://doi.org/10.1177/10731911211067538); abstracts). No meta-analysis of compliance in dyadic or Korean diaries was found, so the pilot must estimate it.
6. **Report power curves against the number of dyads and the number of days.** Any hypothesis that cannot reach adequate power at a feasible size is demoted to estimation, using accuracy planning ([Lakens 2022](https://doi.org/10.1525/collabra.33267); abstract), and labelled as not a falsification test.

**Table C6. Power tools by parameter**

| Parameter | Tool |
|---|---|
| Daily actor and partner effects, including quadratic terms | PowerLAPIM ([Lafit et al. 2022](https://doi.org/10.1177/02654075221080128); abstract) |
| Multilevel and autoregressive effects for one person | PowerAnalysisIL ([Lafit et al. 2021](https://doi.org/10.1177/2515245920978738); abstract) |
| Baseline actor–partner and mediation models | Monte Carlo simulation ([Ledermann et al. 2022](https://doi.org/10.1111/fare.12644); abstract), or the APIMPowerR app, for which no citable paper was found |
| MRT excursion effects | MRTSampleSize ([CRAN](https://doi.org/10.32614/cran.package.mrtsamplesize); metadata) and the calculator of [Liao et al. 2016](https://doi.org/10.1002/sim.6847) (abstract), with the dyad as the cluster |
| Multilevel cubic response surfaces, the route decomposition and relationship-specific variance | **No published tool found.** Custom simulation in simr/lme4 ([Green & MacLeod 2016](https://doi.org/10.1111/2041-210X.12504)) or Mplus Monte Carlo ([Muthén & Muthén 2002](https://doi.org/10.1207/S15328007SEM0904_8)), with reliability formulas for the variance components ([Bonito & Kenny 2010](https://doi.org/10.1111/j.1475-6811.2010.01274.x)) |
| Equivalence tests | Two one-sided tests (TOST) against the pre-registered SESOI ([Lakens 2017](https://doi.org/10.1177/1948550617697177); [Lakens, Scheel & Isager 2018](https://doi.org/10.1177/2515245918770963); abstracts) |

**Interactions and quadratic terms.** Pre-registered one-tailed tests improve power for interactions ([Sommet et al. 2023](https://doi.org/10.1177/25152459231178728); abstract). That source covers first-order interactions only; power for quadratic terms needs its own simulation.

## Confounders and how each is handled

**Table C7. Confounders**

| Confounder | Threat | Handling |
|---|---|---|
| Global sentiment and love | Colours both $`Q`$ and the outcomes | Measured; within-person centring; outcomes from other reporters, lagged and not self-reported |
| The receiver's own giving | Inflates $`Q`$ through projection | Modelled as $`\pi`$ in (3) |
| Chronic and daily stress | Lowers both the tracking of needs and support ([Neff, Nguyen & Williamson 2021](https://sites.utexas.edu/realproject/files/2024/11/too_stressed_to_help.pdf); full text); also lowers $`Q`$ and the outcomes | Daily stress items; PSS; daily stressor log; treated as a capacity moderator |
| Income, working hours, co-residence and contact | Shape capacity, detection and the giver's learning rate $`\lambda`$ | Stratified sampling; covariates |
| Mental health of both members | Shifts reports; in parent–child reports, parental internalising symptoms moderated the mean gap (g = .287 against .031) ([Hou et al. 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC10624508/); full text) | PHQ-9 at every wave |
| Attachment | Predicts over-provision ([Brock & Lawrence 2014](https://doi.org/10.1037/a0035280); abstract) and confounds fit | ECR-RS at baseline; SAAM weekly |
| State trust | Confounds the path from $`Q`$ to outcomes | Measured before the day's $`E`$ and $`Q`$ |
| Commitment | Projection was stronger at high commitment ([Lemay, Clark & Feeney 2007](https://doi.org/10.1037/0022-3514.92.5.834); full text); tolerance standards shift with commitment ([Arriaga, Capezza & Daly 2016](https://pubmed.ncbi.nlm.nih.gov/26461796/); abstract) | Investment Model Scale; moderator |
| Scale use and social desirability | Bias comparisons of levels | Non-care calibration vignettes (v0.2.0); measurement invariance; a social desirability measure |
| Life events | Time-varying confounding | Daily log |
| Taking part in the study | Reactivity. Husbands' self-reported marital quality declined during recording ([Merrilees, Goeke-Morey & Cummings 2008](https://doi.org/10.1016/j.brat.2007.11.007); abstract). A one-session awareness intervention cut break-up ([Rogge et al. 2013](https://doi.org/10.1037/a0034209); metadata) | An assessment-only control group, assigned at random |
| Perceived care, as a possible collider | Biases the total effect of $`E`$ | Not adjusted for when estimating total effects |

## Falsification criteria

Each criterion is written as an equivalence test against a pre-registered SESOI, so a hypothesis can fail and not merely go unconfirmed. Hypotheses H1–H8 keep their v0.2.0 numbering (`paper/18-proposed-study.md:17–24`). H9 and H10 are added here.

**Table C8. Falsification criteria**

| Hypothesis (equation) | Result that counts against the framework | Rival favoured | Inconclusive if |
|---|---|---|---|
| **H1 Detection** (2): visibility shifts sensitivity $`d'`$ | The effect of visibility on $`d'`$ falls inside the SESOI once the criterion is modelled, and the receiver's sentiment or trust explains misses | 4 | Too few days without a signal; the giver's reports are unreliable |
| **H2 Fit versus level** (5) | Every mismatch term falls inside the SESOI (TOST) while the level term $`a_1`$ is clear | 1 | Few observations in incongruent regions; confidence intervals wider than the SESOI |
| **H3 Two routes** (6) | The direct path from independently measured $`E`$ falls inside the SESOI, the sensitivity analysis shows it cannot be rescued, and the outcome signatures do not differ | 2 or 3 | A modest unmeasured confounder could create or erase the direct path |
| **H4 Inferring regard from cost** (4) | The effect of cost information falls inside the SESOI | Regard is read from the act alone | The vignettes fail realism checks |
| **H5 Developmental lag** (8) | Exploratory; no confirmatory criterion | — | — |
| **H6 Relationship-specific misperception** (§8.11) | Relationship-specific variance is negligible relative to perceiver variance, after relationship-specific trust and attachment | 4 | Too few families for stable variance components |
| **H7 Filial-piety marker** (Arm P) | Reciprocal and authoritarian filial piety fall equally with low regard. **Secondary; analysed as the child's attitude, not as an obligation** | General relationship quality | Arm P measures fail Phase 0 |
| **H8 Match versus intensity** (MRT) | The match effect falls inside the SESOI while the intensity effect is clear | 1 | Need reports cannot define a match; prompts are taken up too rarely |
| **H9** (added): regard beyond need fulfilment (6) | The within-person, lagged increment of $`Q`$ over need satisfaction within the relationship falls inside the SESOI, after discriminant validity holds | 3 | Discriminant validity fails: the constructs cannot be told apart |
| **H10** (added): predictive benchmark | Translation constructs add no out-of-sample prediction of 12-month change beyond perceived commitment and appreciation, in a study powered for the SESOI | 2, at the level of prediction | The study is underpowered for change |

**What would disprove the framework.**
- **Substantially disproved for this population and timescale:** H2, H6 and H8 all fail, and H10 fails in an adequately powered study. This mirrors v0.2.0's own criteria (`paper/18-proposed-study.md:96–110`).
- **Partly disproved:** H1, H3, H4 or H9 fails.
- **Exploratory, never a test of the admissibility rule:** whether care stops predicting well-being below a safety threshold. Where the threshold sits, and the decision to exclude unsafe arrangements, are normative choices that data inform but do not settle.

## Safety, autonomy and ethics procedures

**Safety is a gate, not a covariate.** $`\mathrm{Safe}(x)`$ is decided only from behaviourally specific indicators of violence, threats, coercive control and fear. It is never decided from perceived love, satisfaction, or the receiver's own judgment of what is tolerable. Committed people's standards for a partner's aggression drift toward tolerance once aggression begins ([Arriaga, Capezza & Daly 2016](https://pubmed.ncbi.nlm.nih.gov/26461796/); abstract). The confirmatory route and fit models are estimated only in dyads that pass every screen. A sensitivity analysis adds the data that flagged dyads gave before the flag. Safety indicators never enter an outcome model as predictors, and never enter a composite with care or satisfaction.

**Asking both members about violence departs from WHO guidance.** WHO's recommendations for violence research say that "safety is paramount". In household surveys they also say that only one woman per household should be interviewed about violence, and that interviews with other household members "should not include questions exploring their attitudes, experience or use of violence" ([WHO 2001](https://www.who.int/publications/i/item/WHO-FCH-GWH-01.1); full text via the [University of Aberdeen copy](https://www.abdn.ac.uk/education/documents/WHO_FCH_GWH_01.1.pdf)). A dyadic study must screen both members, because care prompts must not run in a coercive relationship. **That is an explicit departure from the household rule, and no empirical study of the risks of asking both partners was found.** The departure is mitigated in five ways and goes to ethics review as a residual risk:
- **Neutral framing.** The study presents itself as being about "relationships and daily life".
- **Separate devices and accounts.** Each member uses their own device and account, with no shared notifications.
- **Embedded, victimisation-only items.** Safety items sit among health and stress items, asking only about acts the respondent experienced (CAS-R-SF, HARK). The CTS2 is not used, because it also asks about one's own acts.
- **Quick-exit and diversion screens.** These let a member hide the survey at once if interrupted.
- **Concealment from the partner.** Neither member ever learns what screen the other completed.

**When a screen is positive.**
- Referral information appears on the respondent's own device, and trained staff follow up through a channel the respondent chooses.
  - Crisis line: 109, Korea's unified line from 2024 (secondary sources only: [Future Chosun](https://futurechosun.com/?p=81377); [eToday](https://www.etoday.co.kr/news/view/2312343)).
  - Women's emergency line 1366: **UNVERIFIED**; confirm before use.
  - A lethality-risk tool may be used by trained staff, for example the Danger Assessment. It reached AUC .90 in an independent sample ([Campbell, Webster & Glass 2009](https://doi.org/10.1177/0886260508317180); abstract), but no Korean validation was located.
- **The dyad's chance of receiving a care prompt is set to zero.** Because the MRT already randomises days without prompts, the change is invisible to the other member. Days after the flag are excluded from the causal estimands.
- The respondent decides whether to continue unchanged, continue with less, or stop in a way that looks routine. Letters declaring a dyad ineligible are worded identically whatever the reason.
- Care is never framed as a remedy for danger. Materials never describe abuse or control as a mutual "translation" problem (`paper/18-proposed-study.md:93`).
- **Safety procedures also improve validity.** Studies built around violence, with stronger safety procedures, found lifetime partner violence of 52% and 69% against 28% in a general demographic survey of the same country ([Ellsberg et al. 2001](https://doi.org/10.1111/j.1728-4465.2001.00001.x); abstract).

**Distress.** Questions about trauma cause some immediate distress, but it is not extreme. Distress is greater among people with a trauma history, and participants rarely regret taking part ([Jaffe et al. 2015](https://doi.org/10.1016/j.cpr.2015.05.004); abstract). Not asking has costs of its own ([Becker-Blease & Freyd 2006](https://doi.org/10.1037/0003-066X.61.3.218); abstract). The protocol adopts published protocols for screening and responding to distress ([Draucker, Martsolf & Poole 2009](https://doi.org/10.1016/j.apnu.2008.10.008); abstract). For monitoring participants at risk of suicide, it adopts consensus guidance on when and how to intervene ([Nock et al. 2021](https://doi.org/10.1176/appi.prcp.20200029); abstract). PHQ-9 responses that indicate risk trigger that protocol.

**Autonomy is a separate outcome with its own stopping rule.**
- Autonomy satisfaction and frustration, and in Arm P psychological control, are measured weekly and at every wave.
- They are reported alongside satisfaction, never combined with it and never subtracted from "care". Autonomy support and psychological control each have distinct associations with outcomes ([Bradshaw et al. 2025](https://doi.org/10.1037/amp0001389); abstract).
- In the MRT, autonomy frustration is monitored as a harm outcome. Any prompt condition that exceeds a pre-registered harm bound is stopped by an independent safety monitor, however it affects perceived care.

**No deception, and confidentiality between members.**
- No message attributed to a real partner or family member is manipulated. The vignettes use unrelated people.
- No member ever sees another member's responses, and no couple or family receives feedback comparing members.
- Consent covers who owns the data and the rule of non-disclosure between family members ([Margolin et al. 2005](https://doi.org/10.1037/0893-3200.19.1.157); abstract).
- **Prompts can reveal needs.** Because MRT prompts are chosen using the receiver's need report from the previous evening, a prompt can partly reveal that report to the giver. Consent discloses this, and members may decline the MRT while staying in the diary.

**Korean law.** The English translations used here may predate amendments. The current Korean texts, and the Ministerial Decree rules on consent and exemption, were not checked.

| Rule | What it requires |
|---|---|
| Bioethics and Safety Act ([KLRI translation](https://elaw.klri.re.kr/eng_service/lawViewContent.do?hseq=52559); statute) | Institutional review board (IRB) review before research (Art. 15); written consent, which may be electronic (Art. 16(1)); consent by a legal representative for people who cannot consent (Art. 16(2)); waiver only with IRB approval (Art. 16(3)); conditions on providing data to third parties (Art. 18); keeping records (Art. 19) |
| Personal Information Protection Act ([KLRI translation](https://elaw.klri.re.kr/eng_service/lawViewContent.do?hseq=71740); statute) | Separate consent for sensitive information such as health and sex life (Art. 23). PHQ-9 answers and sexual-coercion items plausibly qualify, though that is an inference, not a ruling. Pseudonymised processing for scientific research (Art. 28-2); combining datasets only through designated institutions (Art. 28-3); consent of a legal representative for children under 14 (Art. 22-2) |
| Reporting child abuse (Act on Special Cases Concerning the Punishment of Child Abuse Crimes, Art. 10; [mirror of the statute](https://korea.legal/wiki/%ec%95%84%eb%8f%99%ed%95%99%eb%8c%80%eb%b2%94%ec%a3%84%ec%9d%98-%ec%b2%98%eb%b2%8c-%eb%93%b1%ec%97%90-%ea%b4%80%ed%95%9c-%ed%8a%b9%eb%a1%80%eb%b2%95-%ec%a0%9c10%ec%a1%b0/)) | The duty attaches to listed professions acting in the course of their duties. Researchers as such are not listed, but clinicians and staff of listed institutions may be. Consent forms state the limits of confidentiality |
| Domestic-violence reporting duty | **Not verified** |

**Proportionate burden.** Each member is paid in proportion to their burden, and incentives also raise compliance ([Wrzus & Neubauer 2023](https://doi.org/10.1177/10731911211067538); abstract). Each member may withdraw at any time without giving a reason. Consent states in advance what happens to the other member's data if one member withdraws.

**Pre-registration.** The study is submitted as a Stage 1 Registered Report ([Chambers & Tzavella 2022](https://doi.org/10.1038/s41562-021-01193-7); abstract), using a pre-registration template for experience-sampling studies ([Kirtley et al. 2021](https://doi.org/10.1177/2515245920924686); abstract). The chain of derivation from each frozen equation to its measured variables is written out before any test ([Scheel et al. 2021](https://doi.org/10.1177/1745691620966795); abstract).

## Open problems in the protocol

1. **The core translation instruments have no Korean validation.** If Phase 0 fails, the confirmatory core shrinks to detection, the MRT and the vignette experiment.
2. **The study departs from WHO's household rule** by asking both members of a dyad about violence. Its risks are unstudied, and the mitigations are reasoned, not tested.
3. **No published power method exists** for multilevel response surfaces, the route decomposition, or daily variance components in families. The custom simulations are themselves unvalidated.
4. **Compliance is unknown.** No benchmark exists for dyads or for Korean diaries.
5. **The spacing of bursts has no evidence base** specific to relationships.
6. **Sequential ignorability cannot be verified,** so the route split can only be bounded.
7. **The translation matrix $`\boldsymbol\Lambda`$ cannot be estimated** for a single dyad.
8. **Several Korean legal points are unverified:** the age of majority, the current Bioethics Act text, the Ministerial Decree rules, the domestic-violence reporting duty and the 1366 line. WHO's 2016 update was not read in full.
9. **Rules in a comparison country** are not covered.
