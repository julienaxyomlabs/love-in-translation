# Formal models, statistics and research design for "care lost in translation": a verified methods dossier

Conventions used throughout (read first):
- **Evidence grades:** **[E]** Established; **[M]** Moderate or mixed; **[P]** Preliminary; **[T]** Theoretical proposition (no direct empirical test); **[SPEC]** flags speculative extrapolation beyond what any source shows.
- **Verification tags:** **(A)** = the content claim was checked against the abstract or publisher/index record retrieved in November 2026 (OpenAlex, Crossref, PubMed, Semantic Scholar, or a search-engine abstract record; one paper read in full text is marked "full text"). **(K)** = title, authors, year and DOI were verified, but the content statement comes from the note-writer's prior knowledge of the paper. Check page-level details before quoting a (K) claim. **(S)** = a derivation or simulation run by the note-writer in a scratch script. Every parameter value in an (S) item is an illustrative mathematical value, **not an empirical estimate**. No numerical coefficients for the paper's model are proposed anywhere in these notes.
- All DOIs were resolved against OpenAlex or Crossref unless marked UNVERIFIED. Corrections to the candidate DOIs supplied with the research brief are listed in §14.
- Notation used in these notes: A = giver, B = receiver, k = care channel (e.g., time, words, acts, touch, gifts, practical or emotional support), t = occasion (day or interaction segment). E_A = A's expressed or enacted care. I_A = A's intended care. P_B = B's perception of A's acts. N_B = B's desired or needed care. S_B = B's received care, on the same metric as N_B. T_B = B's trust in A. Y_B = B's outcome (for example satisfaction). §13 has the full glossary.

---

## 1. Mismatch and congruence: difference scores, profile similarity, cosine similarity, response surface analysis (RSA) and person–environment (P–E) fit

### Takeaway
None of the following is justified as the main way to put "translation mismatch" into numbers: a difference score, profile correlation, cosine or dot product between the giver's expressed-care vector and the receiver's need vector. These indices impose constraints that are never tested. They throw away magnitude, direction or elevation. Normative profiles inflate them, and cosine and dot product change with arbitrary scale origins and units. The defensible formalisms are polynomial regression with RSA (in its dyadic, multilevel, cubic or spline variants) and latent congruence models, applied to need and supply measured on the same scale. The empirical record from couple personality similarity and person–environment fit is the main threat to "translation rather than amount": congruence terms usually add very little beyond the levels of the two components.

### Cited Findings
**Classic critiques of difference and profile indices**
- Profile similarity has three separable components: elevation (mean level), scatter (spread) and shape (pattern). A profile correlation discards elevation and scatter. A distance index (D) mixes all three. **[E] (K)** — [Cronbach & Gleser 1953, Psychological Bulletin 50(6)](https://doi.org/10.1037/h0057173)
- Global "accuracy" or difference scores between a judge's predictions and a target's answers break down into elevation, differential elevation, stereotype accuracy and differential accuracy. Much apparent "understanding of others" reflects response sets and assumed similarity, not knowledge of that particular person. **[E] (K)** — [Cronbach 1955, Psychological Bulletin](https://doi.org/10.1037/h0044919)
- Profile similarity indices (D, |D|, D², profile r) are conceptually ambiguous. They discard information about the direction of misfit and about which dimension misfits, and they impose constraints that are not tested. **[E] (K)** — [Edwards 1993, Personnel Psychology](https://doi.org/10.1111/j.1744-6570.1993.tb00889.x)
- Polynomial regression with response surface methodology was introduced as an alternative to difference scores in congruence research. **[E] (K)** — [Edwards & Parry 1993, Academy of Management Journal](https://doi.org/10.5465/256822)
- Difference scores in congruence research have several problems. They lower reliability and confound the effects of the two components. They assume, without testing, that the two components have equal and opposite coefficients. They reduce a three-dimensional relation to two dimensions. The proposed alternative is polynomial regression with explicit constraint tests. **[E] (K)** — [Edwards 1994, OBHDP](https://doi.org/10.1006/obhd.1994.1029)
- Difference scores "suffer from numerous methodological problems" that polynomial regression mitigates. Ten "myths" claiming polynomial regression has drawbacks are rebutted. **[E] (A)** — [Edwards 2001, Organizational Research Methods](https://doi.org/10.1177/109442810143005)

**Response surface analysis (RSA) and successors**
- The quadratic model is Z = b0 + b1X + b2Y + b3X² + b4XY + b5Y². The surface is interpreted through four quantities:
  - a1 = b1 + b2: slope along the line of congruence (X = Y). In this paper's terms, the "level" or "amount" effect.
  - a2 = b3 + b4 + b5: curvature along the line of congruence.
  - a3 = b1 − b2: slope along the line of incongruence (X = −Y). This is directional misfit.
  - a4 = b3 − b4 + b5: curvature along the line of incongruence. This is the classic "mismatch hurts" term.

  **[E] (K for the formulas)** — [Shanock et al. 2010, J Business & Psychology](https://doi.org/10.1007/s10869-010-9183-4)
- A checklist for congruence hypotheses. A congruence claim needs a joint pattern of results, not one significant coefficient: the first principal axis must not deviate from the line of congruence, a3 must be about 0, and a4 must be negative. A "strict" claim additionally needs no level effects along the line of congruence. **[E] (A for scope; K for the list of conditions)** — [Humberg, Nestler & Back 2019, SPPS](https://doi.org/10.1177/1948550618757600)
- Dyadic RSA tests similarity-effect hypotheses with both partners' outcomes and models the non-independence of dyads. Difference scores and profile indices "have been vigorously criticized". R and Mplus scripts are provided. **[E] (A)** — [Schönbrodt, Humberg & Nestler 2018, European Journal of Personality](https://doi.org/10.1002/per.2169)
- Multilevel RSA covers repeated or diary data. It provides correct standard errors and tests whether a congruence effect depends on a Level-2 covariate. **[E] (A)** — [Nestler, Humberg & Schönbrodt 2019, Psychological Methods](https://doi.org/10.1037/met0000199)
- Cubic RSA uses third-order polynomials to test two refinements. Asymmetric congruence: incongruence in one direction (e.g., supply above need) affects the outcome differently from incongruence in the other (supply below need). Level-dependent congruence: congruence matters more at some levels than others. **[E as a method; applications P] (A)** — [Humberg, Schönbrodt, Back & Nestler 2022 (online 2020), Psychological Methods](https://doi.org/10.1037/met0000352)
- Spline regression replaces absolute difference scores and allows kinked (V-shaped) congruence relations, with tests of the assumptions that piecewise models leave untested. **[E as a method] (A)** — [Edwards & Parry 2017, ORM](https://doi.org/10.1177/1094428117715067)
- The latent congruence model (LCM, in SEM) offers four advantages: it controls measurement error, tests measurement equivalence across the two component measures, separates the mean level from the difference, and allows several congruence terms at once. **[E as a method] (A)** — [Cheung 2009 (online 2007), ORM](https://doi.org/10.1177/1094428107308914)

**Normativeness: how profile correlations get inflated**
- Profile similarity overlaps with normativeness, meaning how typical each profile is. A framework separates similarity, normativeness and distinctiveness. **[E] (A)** — [Furr 2008, J Personality](https://doi.org/10.1111/j.1467-6494.2008.00521.x)
- The "normative–desirability confound": when a common index says a person is similar to another, that strongly indicates the person has desirable, normative characteristics. The correlates of overall similarity indices are therefore "often misleadingly positive" across traits, attitudes, emotions, behaviours and values. **[E] (A)** — [Wood & Furr 2016 (online 2015), PSPR](https://doi.org/10.1177/1088868315581119)
- A best-practice guide for similarity and self–other agreement in dyads covers correlation, profile correlation, squared differences and the need to correct for mean levels. **[E] (A)** — [Rogers, Wood & Furr 2018 (online 2017), JSPR](https://doi.org/10.1177/0265407517712615)
- The social accuracy model separates normative from distinctive accuracy in interpersonal perception. **[E] (A, scope)** — [Biesanz 2010, Multivariate Behavioral Research](https://doi.org/10.1080/00273171.2010.519262)

**P–E fit theory: commensurability, deficiency versus excess, and perceived versus calculated fit**
- P–E fit theory requires the person and environment to be measured on commensurate dimensions. It distinguishes two kinds of fit: needs–supplies and demands–abilities. It also distinguishes objective from subjective person and environment, and it holds that deficiency and excess can have different effects. **[T] (K)** — [Edwards, Caplan & Harrison 1998, chapter in *Theories of Organizational Stress*](https://doi.org/10.1093/oso/9780198522799.003.0003)
- Applying theory-evaluation criteria to nearly a century of P–E fit theories, Edwards assesses the field's theoretical progress. **(A, scope only)** — [Edwards 2008, Academy of Management Annals](https://doi.org/10.5465/19416520802211503)
- Polynomial regression in the work and family domains gave three findings. Well-being improved as experiences rose toward values. It improved less as experiences exceeded values (an asymmetry). It was higher when both were high than when both were low (a level effect, not pure congruence). **[M] (A — abstract-level Semantic Scholar summary)** — [Edwards & Rothbard 1999, OBHDP](https://doi.org/10.1006/obhd.1998.2813)
- Atomistic, molecular and molar (a direct "do you fit?" question) fit measures are not interchangeable. Molar fit overlaps with affect, and molecular comparisons weight person and environment information differently depending on framing. These results "challenge fundamental assumptions underlying P-E fit theories". **[M] (A)** — [Edwards, Cable, Williamson, Lambert & Shipp 2006, JAP](https://doi.org/10.1037/0021-9010.91.4.802)
- Meta-analysis of 172 studies with 836 effect sizes: fit relates to attitudes, performance, withdrawal and strain. How fit was conceptualized and measured was analysed as a moderator. The 25 polynomial-regression studies were reviewed separately. **[E] (A)** — [Kristof-Brown, Zimmerman & Johnson 2005, Personnel Psychology](https://doi.org/10.1111/j.1744-6570.2005.00672.x)
- Meta-analysis of 30 polynomial-regression P–E fit studies (from 25 articles): the nonlinear "fit" terms (P×E, P², E²) added a mean ΔR² of only **.008** beyond the linear P and E terms. The increment was larger for attitudes and contextual performance than for task performance. None of the 30 studies cross-validated. **[M] (A)** — [Yang, Levine, Smith, Ispas & Rossi 2008, Human Resource Management Review](https://doi.org/10.1016/j.hrmr.2008.07.014); abstract record: [EconBiz](https://www.econbiz.de/Record/person-environment-fit-or-person-plus-environment-a-meta-analysis-of-studies-using-polynomial-regression-analysis/10003780343)

**Couple similarity and congruence: empirical base rates**
- Three national samples of married couples (Australia N = 5,278; UK N = 6,554; Germany N = 11,418): actor effects explained about 6% of the variance in relationship satisfaction and partner effects 1–3%. Couple similarity "consistently explained less than .5% of the variance" after controlling for actor and partner effects. **[E for personality similarity] (A)** — [Dyrenforth, Kashy, Donnellan & Lucas 2010, JPSP](https://doi.org/10.1037/a0020385)
- Dyadic polynomial regression in 237 couples: concurrently, similarity "plays a negligible role" beyond actor and partner effects. Two longitudinal similarity effects emerged. **[M] (A)** — [Weidmann, Schönbrodt, Ledermann & Grob 2017, J Research in Personality](https://doi.org/10.1016/j.jrp.2017.04.003)
- Meta-analysis of 313 studies with 460 effect sizes: attraction correlates with actual similarity (r = .47) and perceived similarity (r = .39). Actual similarity mattered in no-interaction and short-interaction studies, and the abstract then reports "a significant reduction in the effect size of actual" similarity. The retrieved abstract was truncated before naming the condition (the note-writer recalls it as existing relationships, a (K) detail to check). **[M] (A, abstract truncated)** — [Montoya, Horton & Kirchner 2008, JSPR](https://doi.org/10.1177/0265407508096700)

**Care-specific deficiency and excess (support)**
- 103 newlywed couples, measured five times over five years, analysed with APIM and growth curves. Increases in under-provision and in over-provision of partner support each uniquely predicted declines in marital satisfaction. Over-provision was the greater risk, across informational, emotional, esteem and tangible support. **[M] (A)** — [Brock & Lawrence 2009, JFP](https://doi.org/10.1037/a0015402)
- Daily quasi-signal-detection data (see §4) found the opposite pattern for excess: under-provision was harmful and over-provision had a minimal effect. **[M] (A)** — [Bar-Kalifa & Rafaeli 2013, JFP](https://doi.org/10.1037/a0034905). The two studies differ in timescale (daily versus five-year) and in measurement, so the evidence on excess is **mixed**.

**Worked example of the difference-score approach (love languages)**
- N = 100 couples, read in full text:
  - Mismatch index: for each of 20 items, the absolute difference between one partner's "felt-love" rating and the other partner's "expressed" rating, summed across items (α = .61 for men, .70 for women).
  - Analysis: hierarchical regressions controlling only for relationship length.
  - Results: men's relationship satisfaction correlated r = −.40 with their own mismatch and r = −.36 with their partner's mismatch.
  - Limitations: no control for the overall amount of love expressed; absolute differences cannot separate deficit from excess; cross-sectional design.

  **[P] (A, full text)** — [Mostova, Stolarski & Matthews 2022, PLoS ONE](https://doi.org/10.1371/journal.pone.0269429)
- 67 couples: "limited evidence that love language alignment promotes satisfaction"; self-regulation explained more variance. **[P] (A)** — [Bunt & Hazelwood 2017, Personal Relationships](https://doi.org/10.1111/pere.12182)
- The evidence "does not provide strong empirical support" for three assumptions: that each person has a preferred love language, that there are five, and that couples are happier when they speak each other's language. **[M] (A)** — [Impett, Park & Muise 2024, Current Directions in Psychological Science](https://doi.org/10.1177/09637214231217663)

### Inferences
**Mathematics of cosine and dot product (S; [E-math])**
- **Why cosine ignores magnitude.** cos(x, y) = x·y / (‖x‖‖y‖). For any α, β > 0, cos(αx, βy) = αβ(x·y) / (α‖x‖·β‖y‖) = cos(x, y). The cosine depends only on direction, meaning the relative proportions across channels. A partner who gives twice, or a quarter, as much of everything receives the identical score. Numerically, cos(N, 2N) = cos(N, 0.25N) = 1.0. Cosine therefore cannot represent "amount", so it cannot adjudicate "translation versus amount". It simply assumes amount away.
- **Why cosine is wrong for Likert data.** Cosine does not survive adding a constant. Take E = (5,3,1,2,4) and N = (4,4,2,1,5). Cosine is .959 coded 1–5, .926 coded 0–4, and .763 coded −2…+2, while the profile Pearson r is .770 under all three codings. Rating scales have no meaningful zero, so cosine on rating data has no stable meaning. It can only be meaningful on ratio-scale data (counts, minutes) with a true zero.
- **Pearson profile r is the cosine of each profile centred on its own mean.** It is therefore invariant to shift and scale, but for that reason it discards elevation and scatter (Cronbach & Gleser's components), which are exactly the amount information.
- **Cosine depends on the units of each channel.** cos((1, .5), (.5, 1)) = .800, but it becomes .858 if channel 1 is measured in units half as large. Cosine and dot product assume orthogonal, equally scaled axes and assume that one unit of "time" is commensurable with one unit of "acts of service". Neither assumption holds for correlated self-report channel scales.
- **Normative inflation, simulated (illustrative).** 2,000 simulated dyads × 12 channels, each profile = a shared normative profile (SD 1) + independent person-specific deviations. The true dyad-specific matching was exactly 0. Yet the mean raw profile correlation was .537 with deviation SD .5, .218 with SD 1, and .055 with SD 2. After subtracting the sample-mean profile, the mean "distinctive" r was .018, .005 and −.006. The more normative the profiles (everyone values being listened to, few value gifts), the more matching a raw profile r or cosine "finds" that is not there. This is the Furr / Wood & Furr confound reproduced.
- **What the dot product mixes.** E·N = ‖E‖‖N‖cos θ mixes the giver's amount, the receiver's need intensity and alignment. A translation claim requires an alignment effect net of amount and need level, and that is precisely what RSA separates (line-of-congruence terms for level, line-of-incongruence terms for mismatch). **[E-logic]**

**Mapping the hypothesis onto RSA**
- Measure N_B,k (desired) and S_B,k (received) on the same metric. "Translation, not amount" then predicts substantial line-of-incongruence curvature (a4) and/or asymmetry (a3, cubic terms), with the line-of-congruence slope (a1, "more is better") comparatively small. The falsifying pattern is a dominant a1 with line-of-incongruence terms shown by a pre-registered equivalence test to fall inside a smallest effect size of interest (§10). **[T, but directly testable]**
- **Base rates.** Congruence increments are typically tiny: ΔR² ≈ .008 in P–E fit, and under .5% of variance for couple personality similarity. Care need–supply congruence might differ, because the measures are commensurate and relationship-specific, but nothing yet shows that. Expect small effects and plan large samples, since quadratic and cubic terms have low power. **[M; SPEC on transfer from personality and work to care]**
- **Avoid "felt loved in my language" items as the key predictor.** Such items are molar fit judgments, which overlap with affect (Edwards et al. 2006) and therefore with satisfaction. Using them to predict satisfaction is near-tautological. **[M]**
- **Shape of deficiency versus excess.** Evidence on whether excess care hurts conflicts (Brock & Lawrence vs Bar-Kalifa & Rafaeli). The loss function should be estimated with cubic RSA or splines, not assumed. **[M]**

### Gaps
- Kristof-Brown et al. (2005)'s specific moderator result, that direct (perceived) fit correlates more strongly with attitudes than indirect (calculated) fit, could not be checked because the available PDF was not machine-readable. Treat it as **UNVERIFIED**. Edwards et al. (2006) independently supports non-equivalence of fit measures.
- No dyadic or multilevel RSA of commensurate need–supply data on care channels was found. Love-language studies used summed absolute differences or matching of primary categories.
- The specific mechanisms by which Edwards, Caplan & Harrison (1998) say excess supplies operate (conserved, carried over to other needs, or interfering) are paraphrased from memory (K).

---

## 2. Importance weighting and "weighted similarity"

### Takeaway
Multiplying satisfaction (or fulfilment) by self-rated importance is not justified. Locke's range-of-affect hypothesis holds, with empirical support, that importance is already embedded in domain satisfaction. Weighted composites show no predictive advantage, and multiplicative composites of interval-scale ratings have correlations that depend on the arbitrary scale origin. A weighted similarity Σ_k w_k·E_k·N_k inherits all of these problems and should be rejected. If importance matters, it should be estimated, not assumed: as person-specific slopes in within-person data, or as a tested moderator.

### Cited Findings
- 97 working college students rated 12 job facets. Facet importance moderated the link between facet amount and facet satisfaction for 9 of 12 facets. It did not moderate the link between facet satisfaction and overall job satisfaction for 11 of 12. This is consistent with range-of-affect: importance acts inside facet satisfaction, not in aggregating facets. **[M] (A, abstract record)** — [Rice, Gentile & McFarlin 1991, JAP 76(1)](https://doi.org/10.1037/0021-9010.76.1.31); record: [BVB catalogue](https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_miscellaneous_37107140)
- Under range-of-affect, item satisfaction already incorporates the importance judgement. Regressions supported this for item-level satisfaction. The importance × item-satisfaction interaction did not predict global life satisfaction, so "importance weighting on item satisfaction is unnecessary". **[M] (A, abstract record)** — [Wu & Yao 2006, Social Indicators Research 79(3):485–502 — DOI corrected, see §14](https://doi.org/10.1007/s11205-005-5666-5); record: [EconPapers](https://econpapers.repec.org/RePEc:spr:soinre:v:79:y:2006:i:3:p:485-502)
- Two companion 2006 papers by the same authors are title-verified, including an experimental test of range-of-affect. Their content was not reviewed. — [Wu & Yao 2006b](https://doi.org/10.1007/s11205-005-0212-z); [Wu & Yao 2006, experimental](https://doi.org/10.1007/s11205-006-0021-z)
- Four weighted satisfaction scores, computed from importance ranks with Hsieh's algorithms, were "not superior to unweighted satisfaction score in predicting overall QOL". **[M] (A, search abstract)** — [Wu 2008 (online 2007), Social Indicators Research 86](https://doi.org/10.1007/s11205-007-9180-9)
- Multiplying satisfaction by importance is "both undesirable and unnecessary", for four reasons. Domains are chosen for their inherent importance, so separate importance ratings are partly redundant. Weighted scores are hard to interpret. Multiplicative composites have undesirable psychometric properties. They show "little or no advantage over unweighted ratings in correlational or predictive studies". **[M–E] (A, PubMed)** — [Trauer & Mackinnon 2001, Quality of Life Research](https://doi.org/10.1023/A:1013159414364)
- Further critiques and reviews whose titles were verified but whose content was not reviewed: [Russell, Hubley, Palepu & Zumbo 2006 (online 2005)](https://doi.org/10.1007/s11205-004-2528-5); [Hsieh 2004](https://doi.org/10.1023/B:SOCI.0000025591.82518.ab); [Hsieh 2021, a review of domain-importance weighting](https://doi.org/10.1007/s11482-021-10016-w)
- For product composites of interval-scale components, the correlation with a criterion is not invariant to permissible linear rescaling of the components. The recommended analysis is hierarchical regression: enter the components first, then test the product term. **[E] (K)** — [Evans 1991, American Psychologist](https://doi.org/10.1037/0003-066X.46.1.6)

### Inferences
- **Origin dependence of a weighted product composite, simulated (S; illustrative; [E-math]).** The truth was purely additive: outcome = Σx + Σy + noise, with no matching and no weighting. 5 channels, 1–5 ratings, n = 5,000. The composite Σ_k w_k·x_k·y_k nonetheless correlated with the outcome at r = .61 coded 1–5, .63 coded 0–4, −.02 coded −2…+2 and .51 coded 3–7. A weighted similarity can therefore "predict" outcomes only because it carries the component main effects, and its sign and size depend on an arbitrary coding decision.
- **Recommendation.** Do not form Σ w·E·N. Enter E (or S), N and their polynomial terms separately (RSA). Estimate person-specific channel weights as random slopes, asking whether day-to-day supply in channel k predicts this person's felt love. Then test whether those estimated weights correspond to the person's self-rated "preferred language". That correspondence is itself a falsifiable sub-claim of the love-language idea. **[T; testable]**
- **A range-of-affect prediction for couples.** Self-rated channel importance should moderate channel-specific satisfaction, for example "satisfied with the time we spend", but not global relationship satisfaction. **[T; testable] [SPEC: transfer from job and QOL research to couples]**

### Gaps
- No couple- or family-specific test of importance-weighted need–supply matching was found.

---

## 3. Dyadic models: APIM, the Social Relations Model, truth-and-bias, and distinguishability

### Takeaway
The three standard dyadic frameworks are established statistical frameworks with known identification requirements:
- the actor–partner interdependence model (APIM), for each partner's effects on their own and the other's outcomes;
- the Social Relations Model (SRM), for splitting perceptions into perceiver, target and relationship parts;
- the truth-and-bias model, for separating accuracy from bias in judgments.

They are the right backbone for separating "intended / expressed / perceived". Three limits apply. They are associational unless combined with temporal or experimental leverage. None treats either partner's report as ground truth. The SRM component that best matches "translation" (dyad-specific relationship variance) cannot be identified from a couple alone.

### Cited Findings
**APIM**
- The APIM estimates actor effects (own X → own Y) and partner effects (partner's X → own Y), with both partners' X and Y measured. Dyads can be distinguishable (by role) or indistinguishable. It can be estimated with SEM or multilevel models. **[E] (K)** — [Cook & Kenny 2005, IJBD](https://doi.org/10.1080/01650250444000405); book: Kenny, Kashy & Cook (2006) *Dyadic Data Analysis*, Guilford (no DOI; link UNVERIFIED)
- The ratio k = partner effect / actor effect diagnoses dyadic patterns: actor-only, couple-oriented and contrast patterns. **[E] (K)** — [Kenny & Ledermann 2010, JFP](https://doi.org/10.1037/a0019651)
- SEM methods for interchangeable (indistinguishable) dyads. **[E] (K)** — [Olsen & Kenny 2006, Psychological Methods](https://doi.org/10.1037/1082-989X.11.2.127)
- Multilevel versus SEM estimation of dyadic models. **[E] (K)** — [Ledermann & Kenny 2017, JFP](https://doi.org/10.1037/fam0000290)
- Dyadic mediation (the APIM mediation model). **[E] (K)** — [Ledermann, Macho & Kenny 2011, SEM](https://doi.org/10.1080/10705511.2011.607099)
- Longitudinal APIM in SEM. **[E] (K)** — [Gistelinck & Loeys 2019 (online 2018), SEM](https://doi.org/10.1080/10705511.2018.1527223)
- Longitudinal APIM as a dynamic structural equation model (DSEM) for intensive dyadic data with 20 or more time points. The paper shows when multilevel, SEM and DSEM give the same results, and how DSEM handles questions the other two cannot (daily-diary couples example). **[E as a method] (A)** — [Savord, McNeish, Iida, Quiroz et al. 2023 (online 2022), SEM](https://doi.org/10.1080/10705511.2022.2065279)
- Links between interdependence theory and the APIM. **(K)** — [Wickham & Knee 2012, PSPR](https://doi.org/10.1177/1088868312447897); models of interdependent individuals versus dyadic processes **(K)** — [Iida, Seidman & Shrout 2018 (online 2017), JSPR](https://doi.org/10.1177/0265407517725407); reflections on the model **(K)** — [Kenny 2018, Personal Relationships](https://doi.org/10.1111/pere.12240)

**SRM and family SRM**
- The SRM splits a dyadic score X_ij (person i about person j) into a perceiver or actor effect (i's general tendency), a target or partner effect (j's general elicitation), a relationship effect (unique to i with j) and error. **[E] (K)** — [Kenny & La Voie 1984, Advances in Experimental Social Psychology](https://doi.org/10.1016/S0065-2601(08)60144-6); book: Kenny (1994) *Interpersonal Perception: A Social Relations Analysis*, Guilford (no DOI; UNVERIFIED link)
- An SEM model of dyadic relationships within the family system using round-robin data (each member rates every other member). **[E] (K)** — [Cook 1994, J Consulting & Clinical Psychology](https://doi.org/10.1037/0022-006X.62.3.500)
- The SRM can be applied to a single family's round-robin data as a clinical assessment tool. **[E] (A)** — [Cook & Kenny 2004, JFP](https://doi.org/10.1037/0893-3200.18.2.361)
- A systematic review with reanalyses of 17 family data sets: the characteristics of the person reporting (actor effects) and the unique characteristics of the relationship (relationship effects) were the most important sources of differences in family relationships. **[M–E] (A)** — [Eichelsheim, Deković, Buist & Cook 2009, J Marriage & Family](https://doi.org/10.1111/j.1741-3737.2009.00652.x)

**Truth-and-bias and accuracy in couples**
- In the truth-and-bias model, a judgment is pulled by a truth force (attraction toward the criterion) and bias forces. These include bias variables such as assumed similarity or projection, and directional bias, the pull toward one end of the scale. The model formally separates biases from moderators. **[E] (A)** — [West & Kenny 2011, Psychological Review](https://doi.org/10.1037/a0022936)
- 238 couples: evidence for both bias and accuracy, with bias (assumed similarity) "considerably stronger", especially for relationship-linked measures. **[M] (A)** — [Kenny & Acitelli 2001, JPSP](https://doi.org/10.1037/0022-3514.80.3.439)
- Meta-analysis: tracking accuracy r = .47 (98 studies) and positive mean-level bias r = .09 (48 studies), with the two uncorrelated across 38 studies. Mean-level bias was negative for interaction attributions such as love and communication. **[E] (A)** — [Fletcher & Kerr 2010, Psychological Bulletin](https://doi.org/10.1037/a0019792)
- 57 couples gave judgments every 30 seconds while reviewing their recorded conflict discussions. Perceivers underestimated their partner's regard on average (negative bias) yet tracked changes substantially, and more negatively biased perceivers tracked more accurately. **[M] (A)** — [Overall, Fletcher & Kenny 2012, PSPB](https://doi.org/10.1177/0146167211432764)
- People project their own responsiveness. Own self-reported responsiveness to a spouse predicted perceptions of the spouse's responsiveness more strongly than the spouse's self-reported responsiveness did, and daily enacted support was projected too. **[M] (A)** — [Lemay, Clark & Feeney 2007, JPSP](https://doi.org/10.1037/0022-3514.92.5.834); see also [Lemay & Clark 2008, JPSP](https://doi.org/10.1037/0022-3514.94.4.647) (K)
- Recent truth-and-bias applications to daily partner perception:
  - Tracking accuracy, projection and underperception of a partner's approach motives (2,158 daily reports; 1,228 activity reports). **[M] (A)** — [LaBuda, Gere & Impett 2020 (online 2019), JPSP](https://doi.org/10.1037/pspp0000256)
  - Stronger communal motives were associated with overestimating a partner's communal behaviour (up to 60,942 surveys from 510 individuals in 259 couples). **[M] (A)** — [Pusch, Schönbrodt, Zygar-Hoffmann & Hagemeyer 2020 (online 2019), EJP](https://doi.org/10.1002/per.2227)
  - Strong tracking accuracy and mixed directional bias for perceptions of sexual advances. **[M] (A)** — [Dobson, Campbell & Stanton 2018, JSPR](https://doi.org/10.1177/0265407517743081)
- **Ground-truth problem.** Apparent "overperception" cannot be told apart from targets understating their own intentions, because true intentions are not directly measurable. **[M] (A)** — [Perilloux & Kurzban 2015, Psychological Science](https://doi.org/10.1177/0956797614555727)
- 43 dyadic longitudinal datasets: actor-reported variables predicted two to four times more variance in relationship quality than partner-reported variables, and partner reports added nothing beyond actor-reported relationship-specific variables. **[E (predictive)] (A)** — [Joel et al. 2020, PNAS](https://doi.org/10.1073/pnas.1917036117)

### Inferences
**What each model needs to be identified** (data structure → parameters):

| Model | Minimum data structure | What is identified | What is not |
|---|---|---|---|
| Cross-sectional APIM | Both partners measured on X and Y; many dyads | Actor and partner associations (two each if distinguishable; pooled if not) | Causal effects. Partner "effects" can arise from couple-level confounds (shared events, common method). **[E]** |
| Longitudinal / DSEM APIM | Both partners × many occasions | Within-dyad lagged actor and partner associations, random effects | Still not causal if there is time-varying confounding (Rohrer & Murayama 2023) **[E]** |
| SRM | Each person rates, and is rated by, several others: round robin (e.g., a four-member family) or multiple partners per person; ≥2 indicators or occasions | Perceiver, target and relationship variances (relationship separated from error) **[E] (K: Cook 1994; Kenny 1994)** | Nothing within one couple. With two people, actor or partner effects are confounded with the relationship effect. |
| Truth-and-bias | Repeated judgments per perceiver (items or occasions); a criterion on the same metric; bias variables (e.g., the perceiver's own behaviour, for projection) | Truth force, bias forces, directional bias (with both variables centred on the criterion mean) **[E]** | "Truth" is only another report, usually the partner's self-report, not reality (Perilloux & Kurzban) **[M]** |

- **Mapping the hypothesis chain onto dyadic models [T].** Each "≠" in "intended ≠ expressed ≠ perceived ≠ received" is a separate truth-and-bias problem with a different criterion:
  - intended → expressed: A's intention report versus A's act report and observer coding;
  - expressed → perceived: A's act report or observer coding versus B's report;
  - perceived → received: B's perception of acts versus B's fulfilment.
  
  The paper's "translation" maps most naturally onto the SRM relationship effect: misperception specific to this giver–receiver pair, beyond the receiver's general perceiving style and the giver's general expressiveness. That is identifiable only with multi-partner designs, such as family round-robins, or individuals rating several relationships.
- **Projection threatens "perceived ≠ expressed" claims [M].** Perceived care partly reflects the perceiver's own giving (Lemay et al. 2007). A model that treats P_B as a function of E_A alone is misspecified. Include the perceiver's own behaviour as a bias variable.
- **The calibration baseline is not "people misread each other" [E].** Tracking accuracy is substantial (r ≈ .47) and mean-level bias is small (r ≈ .09). The hypothesis must specify which parameter is large enough to "matter": low tracking accuracy, large directional bias, or large relationship-specific variance.
- **Joel et al. (2020) does not establish translation [M].** Perceiver-side variables dominate prediction of satisfaction, which fits "perceived ≠ expressed" but is equally explained by shared-rater variance (the same person reports both perception and satisfaction).

### Gaps
- No family SRM study decomposing care expressed versus perceived was retrieved (family-focused researchers may have one).
- The SRM identification statements rely on Cook (1994) and Kenny (1994) and Kenny et al. (2006). The two books have no DOI and were not retrieved.

---

## 4. Signal detection theory for noticing a partner's behaviours (quasi-SDT)

### Takeaway
Quasi-signal detection uses both partners' daily diaries, with the enactor's report as the "signal" and the recipient's report as the "response". It is established as a descriptive design for crossing "expressed" with "perceived" and yields hits, misses, false alarms and correct rejections. It cannot estimate true sensitivity or bias, because the enactor's report is not ground truth. Most applications enter the four outcome cells as predictors of mood or satisfaction rather than estimating d′ and c. A generalized linear mixed model formulation of SDT gives proper per-person sensitivity and criterion if enough signal-present and signal-absent days are observed.

### Cited Findings
- 58 dating couples reported daily on their own behaviours and on their perceptions of their partner's. The enactor's beliefs and the perceiver's interpretation combined to affect daily mood and satisfaction, and for negative behaviours the enactor's perspective had independent effects. This paper introduced "quasi-signal detection". **[M] (A)** — [Gable, Reis & Downey 2003, Psychological Science](https://doi.org/10.1111/1467-9280.t01-1-01426) (corrected DOI form; see §14)
- Two daily-experience studies of couples (total N = 426):
  - Sacrifices were "equally likely to be missed as they are to be accurately detected".
  - About half of the time people "see" a sacrifice when the partner declares none.
  - "Seeing" a sacrifice, accurately or not, boosts gratitude; missed sacrifices fail to elicit it.

  **[M] (A)** — [Visserman, Impett, Righetti, Muise, Keltner & Van Lange 2019 (online 2018), SPPS](https://doi.org/10.1177/1948550618757599)
- Newlyweds: people are good at detecting the absence of partner behaviour, especially negative behaviour, and these correct rejections predict relationship quality beyond hits. **[M] (A)** — [Finkenauer, Wijngaards-de Meij, Reis & Rusbult 2010, Personal Relationships](https://doi.org/10.1111/j.1475-6811.2010.01300.x)
- Support matching. Both partners reported daily receipt of and desire for support for 21 days (N = 44 and 38 couples). Matching was coded as a "hit", under-provision as a "miss" and over-provision as a "false alarm". Emotional matching predicted favourable relational outcomes, under-provision of emotional and practical support predicted adverse outcomes, and over-provision had a minimal effect. **[M] (A)** — [Bar-Kalifa & Rafaeli 2013, JFP](https://doi.org/10.1037/a0034905)
- Truth-and-bias and quasi-SDT used together in experience-sampling data. **[M] (A)** — [Pusch et al. 2020](https://doi.org/10.1002/per.2227); a sexual-rejection application, title-verified **(K)** — [Dobson, Kim & Impett 2021, Archives of Sexual Behavior](https://doi.org/10.1007/s10508-021-02126-1)
- "Invisible support": support reported by the provider but not by the recipient was linked to better adjustment. **[M] (K)** — [Bolger, Zuckerman & Kessler 2000, JPSP](https://doi.org/10.1037/0022-3514.79.6.953). Visible support was associated with greater same-day satisfaction and anxiety, while invisible support predicted next-day satisfaction (one sample of 322 married couples). **[M] (A)** — [Girme, Maniaci, Reis, McNulty et al. 2018, JFP](https://doi.org/10.1037/fam0000453)
- Signal detection models can be written as a subclass of generalized linear models with different underlying distributions. **[E] (A)** — [DeCarlo 1998, Psychological Methods](https://doi.org/10.1037/1082-989X.3.2.186)

### Inferences
**How the cells are defined** (Gable et al. 2003; Visserman et al. 2019), on day t for behaviour or channel k:

| | B reports A did k | B reports A did not do k |
|---|---|---|
| **A reports doing k ("signal present")** | Hit | Miss |
| **A reports not doing k ("signal absent")** | False alarm | Correct rejection |

**[E]**

- **Why it is only "quasi" [E/M].** The enactor's report is subject to self-presentation, forgetting, effort-justification and invisible intentions, so "misses" and "false alarms" are disagreements, not errors. Three routes to a firmer criterion:
  - observer coding of recorded interactions, which gives a third criterion;
  - experimentally fixed "signals" (standardized messages or confederates, §12), which give true ground truth;
  - SRM-style multiple informants.
- **Estimation [E (method), T (application)].** A multilevel probit of the perceiver's report on the enactor's report (DeCarlo 1998) gives random per-person criterion (intercept) and sensitivity (slope). This requires adequate counts of both signal-present and signal-absent days per person. With rare behaviours, per-person d′ is unstable and pooling is needed.
- **Which deficiency/excess asymmetry is supported [M].** Daily data suggest misses (under-provision) matter more than false alarms (over-provision) (Bar-Kalifa & Rafaeli 2013). Five-year data suggest over-provision is worse (Brock & Lawrence 2009). Timescale and measurement are plausible moderators, so any asymmetric loss in the paper must be treated as an open empirical question.

### Gaps
- No quasi-SDT study crossing care channels (e.g., "A gave care via time; did B register it as care?") was found.
- No study combining quasi-SDT with an independent observer criterion in couples was retrieved.

---

## 5. Bayesian models of intention inference, impression learning, and error management

### Takeaway
Bayesian inverse planning and the naïve utility calculus are well supported in controlled laboratory stimuli as accounts of how observers infer others' goals, preferences and costs from actions, and infants infer how much an agent values a goal from the cost it pays. Asymmetric Bayesian updating explains moral impressions of strangers. Error management theory explains direction-specific biases where error costs are asymmetric. None of these models has been estimated on naturalistic close-relationship data. Their use for how partners translate care is therefore a **theoretical proposition**. They do generate precise, falsifiable predictions, testable with designed stimuli or repeated games with real partners.

### Cited Findings
- **Inverse planning.** Observers infer goals by inverting a model of approximately rational planning, and model predictions fit human goal judgments for agents moving in simple 2-D environments. **[E for lab stimuli] (K)** — [Baker, Saxe & Tenenbaum 2009, Cognition](https://doi.org/10.1016/j.cognition.2009.07.005)
- **Joint attribution.** A model jointly infers an actor's beliefs, desires and percepts by probabilistically inverting rational planning and state estimation, from how agents move in a local spatial environment. **[E for lab stimuli] (A, Semantic Scholar summary)** — [Baker, Jara-Ettinger, Saxe & Tenenbaum 2017, Nature Human Behaviour](https://doi.org/10.1038/s41562-017-0064)
- **Naïve utility calculus.** People assume agents act to maximize utility, defined as rewards minus costs, and invert this to infer preferences, competence and costs. **[E–T, review] (K)** — [Jara-Ettinger, Gweon, Schulz & Tenenbaum 2016, TiCS](https://doi.org/10.1016/j.tics.2016.05.011); a unified quantitative framework **(K)** — [Jara-Ettinger, Schulz & Tenenbaum 2020, Cognitive Psychology](https://doi.org/10.1016/j.cogpsych.2020.101334)
- **Value from cost.** Ten-month-old infants infer that an agent who pays a higher cost for a goal values it more. **[M] (A)** — [Liu, Ullman, Tenenbaum & Spelke 2017, Science](https://doi.org/10.1126/science.aag2132)
- **Asymmetric updating.** Moral inference follows an asymmetric Bayesian mechanism: beliefs about bad agents are more uncertain, and so more volatile, than beliefs about good agents. **[M] (A)** — [Siegel, Mathys, Rutledge & Crockett 2018, Nature Human Behaviour](https://doi.org/10.1038/s41562-018-0425-1)
- **Social learning as reward learning.** Information from social partners (advice) is learned through the same associative computations as reward, processed in parallel neural streams. **[M] (A)** — [Behrens, Hunt, Woolrich & Rushworth 2008, Nature](https://doi.org/10.1038/nature07538)
- **Closest to real relationships.** In an iterated trust game (N = 26), participants invested more with friends than with a confederate or a computer despite equal reinforcement rates. A social-value model, in which the reward from reciprocation depends on closeness, predicted choices. **[P] (A)** — [Fareri, Chang & Delgado 2015, J Neuroscience](https://doi.org/10.1523/JNEUROSCI.4775-14.2015)
- **Repeated trust games with anonymous partners.** Reputation building **(K)** — [King-Casas et al. 2005, Science](https://doi.org/10.1126/science.1108062); rupture and repair of cooperation in borderline personality disorder **(K)** — [King-Casas et al. 2008, Science](https://doi.org/10.1126/science.1156902)
- **Error management theory (EMT).** Inference mechanisms are predictably biased when the costs of false-positive and false-negative errors were asymmetric. EMT predicts men's overperception of women's sexual intent and women's underperception of men's commitment; Study 1 (N = 217) documented commitment underperception. **[M] (A)** — [Haselton & Buss 2000, JPSP](https://doi.org/10.1037/0022-3514.78.1.81); integrative "paranoid optimist" model **(K)** — [Haselton & Nettle 2006, PSPR](https://doi.org/10.1207/s15327957pspr1001_3)
- **The criterion problem undermines EMT tests.** See §3. **[M] (A)** — [Perilloux & Kurzban 2015](https://doi.org/10.1177/0956797614555727)
- **A relationship analogue of cost-based inference.** Commitment-inspired acts such as accommodation and sacrifice "provide diagnostic information regarding a partner's pro-relationship motives", and trust grows when partners are perceived to depart from their direct self-interest. **[M] (A)** — [Wieselquist, Rusbult, Foster & Agnew 1999, JPSP](https://doi.org/10.1037/0022-3514.77.5.942)

### Inferences
- **What the naïve utility calculus would add to the paper [T].** The inference becomes: perceived care ≈ the inferred value of B's welfare to A, which an observer can only read off the costs A incurred and the alternatives A gave up. This gives a principled translation mechanism. The same act signals much care if B believes it was costly for A, and little if B believes it was cheap. Misreading then arises when B's generative model of A's costs, competence or preferences differs from A's actual situation. These are specific, falsifiable predictions, unlike a generic "mismatch" index.
- **Identification barrier [T].** Inverse-planning parameters need many observed choices in an environment whose options and costs are known. In real relationships the giver's option set and costs are not observed. Three feasible designs:
  - standardized vignettes or animations of care acts with manipulated costs, holding the act constant;
  - repeated incentivized games with real partners versus strangers (the Fareri design);
  - diaries in which A reports the act's cost and B estimates it, with a truth-and-bias model of cost perception.
- **Siegel's asymmetric volatility applied to trust [SPEC].** Translated to trust, it implies larger updates after negative partner evidence when priors are negative. This bears on the bistability question (§8), but it has been shown only with strangers in laboratory tasks.
- **"Bias" relative to a partner's self-report [M].** In couples, EMT-style directional bias measured against the partner's self-report is confounded with the partner's own reporting bias. Third-party criteria or experimental ground truth are needed.

### Gaps
- No study was found that applies inverse planning or the naïve utility calculus to romantic partners' or family members' everyday care.
- No Bayesian or reinforcement-learning trust model estimated on couples' diary data was found. A targeted search returned only laboratory trust games and a stranger/robot trust-prediction study ([Lee et al. 2013, Frontiers in Psychology](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2013.00893/text), not about partners).

---

## 6. Dynamical models of relationships: which were estimated from data and which are purely theoretical

### Takeaway
The models fall into three groups:
1. **Theoretical or teaching only.** The classic love-ODE models (Strogatz 1988; Rinaldi and colleagues; Felmlee & Greenberg) were never estimated statistically on relationship data. The Rinaldi models were "calibrated" only on literary or fictional narratives.
2. **Estimated, but predictive claims unreliable.** The Gottman–Murray nonlinear difference equations were estimated from coded marital interaction, but the related divorce-prediction claims were not cross-validated and shrink under cross-validation.
3. **Estimated and statistically rigorous.** Threshold autoregression, dynamic factor analysis, coupled oscillators and latent differential equations, state-space models, regime-switching differential equations and hidden Markov models have been fitted to real dyadic time series. They model affect, physiology or coded behaviour on short timescales, not care translation.

### Cited Findings
**Theoretical or teaching only [T]**
- A linear two-variable ODE ("Romeo and Juliet") used to teach linear systems; for example dR/dt = aJ, dJ/dt = −bR yields a never-ending cycle. No data. **(K)** — [Strogatz 1988, Mathematics Magazine 61(1):35](https://doi.org/10.1080/0025570X.1988.11977342)
- "Love dynamics: the case of linear couples." **(K)** — [Rinaldi 1998, Applied Mathematics & Computation](https://doi.org/10.1016/S0096-3003(97)10081-9)
- The Laura–Petrarch model: three nonlinear ODEs. Parameters were calibrated "on the basis of the scarse and only qualitative information available" in Petrarch's poems and produce a roughly 20-year cycle. **(A)** — [Rinaldi 1998, SIAM J Applied Mathematics](https://doi.org/10.1137/S003613999630592X)
- "Standard couples": robust versus fragile couples with one or two stable equilibria. **(A, title and search summary)** — [Rinaldi, Della Rossa & Dercole 2010, Int J Bifurcation & Chaos](https://doi.org/10.1142/S021812741002709X)
- Saddle-node bifurcation in *Beauty and the Beast* (a fictional story). **(K)** — [Rinaldi, Landi & Della Rossa 2013, IJBC](https://doi.org/10.1142/S0218127413300383); book: **(K)** — [Rinaldi, Della Rossa, Dercole, Gragnani & Landi, *Modeling Love Dynamics*, World Scientific (Crossref 2015; often cited 2016)](https://doi.org/10.1142/9656)
- A rising reconciliation time after disputes is derived as a warning sign of a catastrophic bifurcation in a two-ODE model. The abstract calls the model "well-known and repeatedly validated", but the authors note the rule "is here justified only for couples composed of secure individuals"; it has not been tested empirically. **(A, PubMed)** — [Rinaldi & Della Rossa 2019, Nonlinear Dynamics, Psychology & Life Sciences 23(2):261–273](https://pubmed.ncbi.nlm.nih.gov/30898194/)
- A dynamic systems model of dyadic interaction. Theoretical; the abstract was not retrieved. **(K)** — [Felmlee & Greenberg 1999, J Mathematical Sociology](https://doi.org/10.1080/0022250X.1999.9990218)

**Gottman line [P–M]**
- Nonlinear difference-equation models of each spouse's coded affect during conflict, with emotional inertia, an uninfluenced set point and influence functions, estimated per couple. **(K)** — [Gottman, Swanson & Murray 1999, JFP](https://doi.org/10.1037/0893-3200.13.1.3). A "general systems theory of marriage" applicable "to any time series data generated over time for two individuals" **(A)** — [Gottman, Swanson & Swanson 2002, PSPR](https://doi.org/10.1207/S15327957PSPR0604_07); book **(K)** — [Gottman, Murray, Swanson, Tyson & Swanson 2002, *The Mathematics of Marriage*, MIT Press](https://doi.org/10.7551/mitpress/4499.001.0001)
- Predicting marital happiness and stability from newlywed interactions. **(K)** — [Gottman, Coan, Carrère & Swanson 1998, J Marriage & Family](https://doi.org/10.2307/353438)
- Accuracy and predictive value of divorce-prediction equations "drop precipitously during crossvalidation", and population base rates must be considered. **[E for the critique] (A)** — [Heyman & Slep 2001, J Marriage & Family](https://doi.org/10.1111/j.1741-3737.2001.00473.x)
- "Structural flaws" in bridging those findings to recommendations for couples interventions. **[M] (A)** — [Stanley, Bradbury & Markman 2000, J Marriage & Family](https://doi.org/10.1111/j.1741-3737.2000.00256.x)
- The Gottman–Murray model is a special case of the threshold autoregressive (TAR) model, which brings standard estimation, alternative models and model selection; a new estimation procedure was tested by simulation. **[E as a method] (A)** — [Hamaker, Zhang & van der Maas 2009, Psychometrika](https://doi.org/10.1007/s11336-009-9113-4)
- TAR applied to moment-to-moment spousal affect during marital conflict. **[P] (K)** — [Madhyastha, Hamaker & Gottman 2011, JFP](https://doi.org/10.1037/a0023028)
- "Proximal change experiments": randomized brief interventions between two conflict discussions, evaluated through the model's parameters. **[P] (A)** — [Gottman, Ryan, Swanson & Swanson 2005, J Family Communication](https://doi.org/10.1207/s15327698jfc0503_1)

**Rigorous dyadic dynamics estimated from data**
- One husband–wife dyad over 182 consecutive days, dynamic factor analysis: the spouses' affect structures differed, with unidirectional influence from husband to wife. **[P; n = 1 dyad] (A)** — [Ferrer & Nesselroade 2003, Emotion](https://doi.org/10.1037/1528-3542.3.4.344)
- Coupled-oscillator models of intimacy and disclosure in marriage, fitted to diary data. **[P] (K)** — [Boker & Laurenceau 2006, chapter in *Models for Intensive Longitudinal Data*](https://doi.org/10.1093/acprof:oso/9780195173444.003.0009)
- 48 cohabiting couples over 21 days: both covariation of daily affect and coupling of affective cycles were detected, and attachment moderated both. **[P] (A)** — [Butner, Diamond & Hicks 2007, Personal Relationships](https://doi.org/10.1111/j.1475-6811.2007.00164.x)
- Latent differential equations for self- and co-regulation of affect in couples. **[P] (K)** — [Steele & Ferrer 2011, MBR](https://doi.org/10.1080/00273171.2011.625305); physiological coregulation in dyads **[P] (K)** — [Ferrer & Helm 2013, Int J Psychophysiology](https://doi.org/10.1016/j.ijpsycho.2012.10.013)
- State-space modelling with the Kalman smoother. Monte Carlo results: state residual variances are positively biased in shorter series and become accurate as series lengthen. **[E as a method] (A)** — [Song & Ferrer 2009, SEM](https://doi.org/10.1080/10705510902751432)
- Regime-switching differential equations for sudden shifts in intensive dyadic (mother–infant) interaction data. **[E as a method; application P] (A)** — [Chow et al. 2018, Psychometrika](https://doi.org/10.1007/s11336-018-9605-1)
- Hidden Markov models of mother–infant soothing during immunizations: a 4-state model at 2 months and a 6-state model at 6 months. **[P] (A)** — [Stifter & Rovine 2015, Infant & Child Development](https://doi.org/10.1002/icd.1907)
- The TIES framework maps dynamic-systems vocabulary (coupling, coregulation, etc.) onto statistical models and gives analytic advice. **[T/review] (A)** — [Butler 2011, PSPR](https://doi.org/10.1177/1088868311411164)

### Inferences
- **None of the estimated models measures care intended, expressed or perceived.** They model affect, physiology or behaviour codes. Applying love-ODE models to care translation would be a **[SPEC]** extrapolation.
- **The "repeatedly validated" claim is unsupported.** Rinaldi & Della Rossa (2019) describe their model as "well-known and repeatedly validated", but no statistical estimation of these love-ODE models on relationship data was found. Treat the claim as unsupported. **[M — absence of evidence]**
- **Data needed.** Oscillator, latent-differential-equation and ODE parameters need dense, roughly equally spaced series covering several cycles. Three to four weeks of daily diaries identify linear autoregressive and coupling parameters at the population level, but only weakly per dyad. State-noise variances are biased in short series (Song & Ferrer 2009). **[M]**
- **Use Gottman-type models as data-analytic tools, not as evidence of predictive validity.** Use their TAR reformulation, and require cross-validated prediction before any predictive claim. **[E]**

### Gaps
- No estimated dynamical model of care translation was found.
- Abstracts for Gottman et al. 1999, Felmlee & Greenberg 1999, Steele & Ferrer 2011 and Ferrer & Helm 2013 were not retrieved, so their descriptions are (K).

---

## 7. Intensive longitudinal methods: diaries, DSEM, RI-CLPM, within/between, ergodicity

### Takeaway
Dyadic daily diaries analysed with multilevel models or dynamic structural equation models (DSEM) are the established workhorse for within-couple processes. The classic cross-lagged panel model (CLPM) should not be used for within-person causal claims. The random-intercept cross-lagged panel model (RI-CLPM) and DSEM separate stable between-dyad differences from within-dyad dynamics, but they rest on parametric assumptions. Within-person data are neither necessary nor sufficient for causal inference, and group-level results need not describe individual couples.

### Cited Findings
**Diary methods**
- Diary methods: designs and the questions they can answer. **[E] (K)** — [Bolger, Davis & Rafaeli 2003, Annual Review of Psychology](https://doi.org/10.1146/annurev.psych.54.101601.145030)
- Diary methods for marital and family processes. **[E] (K)** — [Laurenceau & Bolger 2005, JFP](https://doi.org/10.1037/0893-3200.19.1.86); book: Bolger & Laurenceau (2013) *Intensive Longitudinal Methods*, Guilford (no DOI; UNVERIFIED link)
- An application: daily diaries with multilevel modelling of the interpersonal process model of intimacy in marriage. **[M] (K)** — [Laurenceau, Barrett & Rovine 2005, JFP](https://doi.org/10.1037/0893-3200.19.2.314)

**DSEM and sample size**
- DSEM combines time-series modelling with SEM for intensive longitudinal data from many individuals, with Bayesian estimation. **[E as a method] (A)** — [Asparouhov, Hamaker & Muthén 2018 (online 2017), SEM](https://doi.org/10.1080/10705511.2017.1406803); primer **(K)** — [McNeish & Hamaker 2020, Psychological Methods](https://doi.org/10.1037/met0000250)
- Simulation of the number of subjects × time points needed for two-level AR(1) DSEM. **[E as a method] (A)** — [Schultzberg & Muthén 2018 (online 2017), SEM](https://doi.org/10.1080/10705511.2017.1392862); simulation-based power for intensive longitudinal multilevel models **(K)** — [Lafit et al. 2021, AMPPS](https://doi.org/10.1177/2515245920978738)
- Longitudinal APIM as DSEM in a couples' daily diary. **(A)** — [Savord et al. 2023](https://doi.org/10.1080/10705511.2022.2065279)

**CLPM, RI-CLPM and causal inference**
- If stability is partly trait-like, CLPM lagged parameters "do not represent the actual within-person relationships". The RI-CLPM separates stable between-person differences. **[E] (A)** — [Hamaker, Kuiper & Grasman 2015, Psychological Methods](https://doi.org/10.1037/a0038889)
- The CLPM is "almost never the right choice", and defenses of it ignore well-known limitations. **[E] (A)** — [Lucas 2023, AMPPS](https://doi.org/10.1177/25152459231158378)
- Within-person data are neither necessary nor sufficient for causal inference, because time-varying confounders produce spurious within-person associations; but they can be "tremendously helpful". **[E] (A)** — [Rohrer & Murayama 2023, AMPPS](https://doi.org/10.1177/25152459221140842)
- Progress requires theorizing the timescale on which a process operates, being explicit about the research question, and considering alternative designs. **[E] (A)** — [Hamaker 2023, Psychological Methods](https://doi.org/10.1037/met0000600)
- The CLPM is biased under unmeasured confounding. Latent-variable alternatives such as the RI-CLPM "strongly depend on the specific parametric assumptions" and are biased under other data-generating scenarios. **[E] (A)** — [Lüdtke & Robitzsch 2022, SEM](https://doi.org/10.1080/10705511.2022.2065278)
- A unified framework of reciprocal-effects models. **(K)** — [Usami, Murayama & Hamaker 2019](https://doi.org/10.1037/met0000210); RI-CLPM extensions **(K)** — [Mulder & Hamaker 2021 (online 2020)](https://doi.org/10.1080/10705511.2020.1784738); comparing cross-lagged effects in multilevel AR models requires appropriate standardization **(K)** — [Schuurman et al. 2016](https://doi.org/10.1037/met0000062)

**Within/between and group-to-individual generalization**
- Disaggregating within- and between-person effects of time-varying covariates. **[E] (A)** — [Curran & Bauer 2011 (online 2010), Annual Review of Psychology](https://doi.org/10.1146/annurev.psych.093008.100356); a bridge between the two structures **(K)** — [Voelkle et al. 2014, MBR](https://doi.org/10.1080/00273171.2014.889593)
- Between-person structure generalizes to individuals only for ergodic processes (homogeneous and stationary). **[E–T] (K)** — [Molenaar 2004, Measurement](https://doi.org/10.1207/s15366359mea0204_1)
- Within-person correlations vary far more than group estimates suggest: "the variance in individuals is up to four times larger than in groups". **[M] (A)** — [Fisher, Medaglia & Jeronimus 2018, PNAS](https://doi.org/10.1073/pnas.1711978115). Ergodicity is "sufficient but not necessary" for generalizing from group to individual. **[M] (K)** — [Adolf & Fried 2019, PNAS](https://doi.org/10.1073/pnas.1818675116)

**Time-varying parameters**
- The time-varying effect model **(K)** — [Tan et al. 2012](https://doi.org/10.1037/a0025814); time-varying AR via generalized additive models **(K)** — [Bringmann et al. 2017](https://doi.org/10.1037/met0000085); time-varying VAR tutorial **(K)** — [Haslbeck, Bringmann & Waldorp 2021](https://doi.org/10.1080/00273171.2020.1743630)

### Inferences
- **Minimal dyadic diary design for the hypothesis [T design; E methods].** Both partners report every day at matched times, by channel k:
  - own intended and enacted care (event checklist);
  - perceived partner acts;
  - desired care, on the same metric as received care;
  - received care or felt love;
  - trust and satisfaction.

  Person-mean-centre the predictors. Fit multilevel RSA (§1), truth-and-bias (§3), quasi-SDT (§4) and DSEM-APIM dynamics on the same data. Within-dyad effects remain within-dyad associations only. **[E]**
- **Interval must match timescale [E].** Daily data cannot identify minute-scale conversational misreading and repair. That needs segment-level ratings of recorded interactions, as in Overall et al. 2012.
- **No fixed rule for days or couples [E].** Justify sample size by simulation (Lafit et al. 2021; Schultzberg & Muthén 2018), not by rules of thumb.
- **Population claims versus single couples [E].** "Many relationship problems…" is a population claim. Any clinical claim about a particular couple needs idiographic (single-dyad) models.

### Gaps
- Apart from support desire-versus-receipt designs (Bar-Kalifa & Rafaeli 2013), no dyadic intensive longitudinal study measuring commensurate need and supply per care channel was found.

---

## 8. Tipping points, bistability and hysteresis (including the trust-equation mathematics)

### Takeaway
No empirical evidence of bistability or hysteresis in relationship trust or satisfaction was found. The relationship "tipping point" literature consists of theoretical ODE models plus descriptive evidence of an accelerating decline before separation. That pattern is not diagnostic of bistability: a simple selection mechanism produces it with no change in the underlying dynamics. In psychopathology, where critical-slowing-down methods entered psychology, a 2024 review concludes there is little support for early warning signals. The mathematics in the brief is correct with one refinement: p′(T) > 1 somewhere is **necessary but not sufficient** for multiple equilibria in dT/dt = η[p(T) − T].

### Cited Findings
**Early warning signals and alternative stable states**
- Generic early warning signals of critical transitions: critical slowing down, seen as rising autocorrelation and variance. **[E in ecological and physical systems] (K)** — [Scheffer et al. 2009, Nature](https://doi.org/10.1038/nature08227)
- In autorecorded mood time series, indicators of slowing down (slower mood dynamics, stronger correlation among mood aspects) were associated with future transitions in depression. **[P–M] (A)** — [van de Leemput et al. 2014, PNAS](https://doi.org/10.1073/pnas.1312114110)
- Theoretical and practical considerations for early warning signals in psychological systems. **[E as a method] (K)** — [Dablander, Pichler, Cika & Bacilieri 2023, Psychological Methods](https://doi.org/10.1037/met0000450)
- Little support for critical-slowing-down early warning signals in psychopathology; alternative methods must be improved and prospective studies are needed before clinical use. **[M] (A, abstract via search)** — [Helmich, Schreuder, Bringmann, Riese, Snippe & Smit 2024, Nature Reviews Psychology 3:767–780](https://doi.org/10.1038/s44159-024-00369-y)
- Bimodality in the frequency distribution of depressive symptoms over time, interpreted as a signature of nonlinear dynamics. **[P] (K, title)** — [Hosenfeld et al. 2015, BMC Psychiatry](https://doi.org/10.1186/s12888-015-0596-5); cusp-catastrophe fitting **(K)** — [Grasman, van der Maas & Wagenmakers 2009, J Statistical Software](https://doi.org/10.18637/jss.v032.i08)
- Regime-switching state-space models for recurrent shifts between regimes, with missing-data handling and inference. **[E as a method] (A)** — [Hamaker & Grasman 2012, Psychometrika](https://doi.org/10.1007/s11336-012-9254-8); dyadic regime-switching and HMM applications in §6.

**Relationships**
- Preregistered analysis of four national longitudinal studies, with event groups of 987–3,373 people and propensity-matched controls of 1,351–4,717:
  - Relationship satisfaction declined as a function of time-to-separation.
  - The decline had a "preterminal" phase (small) and a "terminal" phase (sharp).
  - The terminal phase began 0.58–2.30 years before separation.
  - Time-to-separation predicted change better than time-since-beginning.
  - People on the receiving end of the separation entered the terminal phase later but declined more strongly.

  **[M — descriptive] (A)** — [Bühler & Orth 2025, JPSP](https://doi.org/10.1037/pspp0000551)
- Meta-analysis of 165 samples (165,039 participants): satisfaction decreased from age 20 to 40, bottomed out at 40, rose until 65, then plateaued. **[E — descriptive] (A)** — [Bühler, Krauss & Orth 2021, Psychological Bulletin](https://doi.org/10.1037/bul0000342)
- Theoretical relationship tipping points: [Rinaldi & Della Rossa 2019](https://pubmed.ncbi.nlm.nih.gov/30898194/); [Rinaldi, Della Rossa & Dercole 2010](https://doi.org/10.1142/S021812741002709X). **[T] (A)**
- Searches in November 2026 found no study fitting cusp or hysteresis models to longitudinal romantic-relationship satisfaction or trust, and no study testing critical slowing down in couples' time series. The only empirical cusp analogue surfaced concerned employment "psychological contracts" in a Chinese management journal (not verified): [JMSC abstract page](https://jmsc.tju.edu.cn/jmscen/article/abstract/20140403).

**Analogous models of self-reinforcing expectations**
- Threshold models of collective behaviour: equilibria lie where the cumulative distribution of thresholds crosses the 45° line, and small changes in the distribution can shift the outcome dramatically. **[E–T] (K)** — [Granovetter 1978, American Journal of Sociology](https://doi.org/10.1086/226707)
- Bank runs as one of multiple equilibria sustained by self-fulfilling expectations. **[E–T] (K)** — [Diamond & Dybvig 1983, J Political Economy](https://doi.org/10.1086/261155)
- Rejection expectations lead to behaviour that elicits rejection, shown with diary and laboratory data. Highly rejection-sensitive people's relationships were more likely to break up, and the conflict mechanism was shown for highly rejection-sensitive women. **[M] (A)** — [Downey, Freitas, Michaelis & Khouri 1998, JPSP](https://doi.org/10.1037/0022-3514.75.2.545)
- Positive illusions as self-fulfilling ("love is not blind, but prescient"). **[M] (K)** — [Murray, Holmes & Griffin 1996, JPSP](https://doi.org/10.1037/0022-3514.71.6.1155)
- The risk regulation model: confidence in a partner's regard sets "if–then" rules that balance seeking closeness against self-protection. **[T/M] (A)** — [Murray, Holmes & Collins 2006, Psychological Bulletin](https://doi.org/10.1037/0033-2909.132.5.641)
- "Mutual cyclical growth" (dependence → commitment → pro-relationship acts → perceived by partner → trust → dependence), supported by mediation analyses in two longitudinal studies. **[M] (A)** — [Wieselquist et al. 1999](https://doi.org/10.1037/0022-3514.77.5.942)
- Classroom self-fulfilling prophecies "are typically small, they do not accumulate greatly across perceivers or over time, and they may be more likely to dissipate than accumulate". Teacher expectations may predict outcomes because they are accurate. **[E for that domain] (A)** — [Jussim & Harber 2005, PSPR](https://doi.org/10.1207/s15327957pspr0902_3)
- Standard reference for one-dimensional flows, linear stability, saddle-node bifurcations and hysteresis. **(K)** — [Strogatz 2018, *Nonlinear Dynamics and Chaos*, CRC](https://doi.org/10.1201/9780429492563)

### Inferences
**Mathematics of dT/dt = η[p(T) − T]** (η > 0; p: [0,1] → (0,1) continuous, differentiable and increasing; S, [E-math])
- **Existence.** Let f(T) = p(T) − T. Then f(0) = p(0) > 0 and f(1) = p(1) − 1 < 0, so at least one equilibrium exists (intermediate value theorem).
- **Uniqueness.** If p′(T) < 1 everywhere, f is strictly decreasing, so there is exactly one equilibrium and it is globally attracting. One-dimensional flows cannot oscillate.
- **Necessity, proving the brief's claim.** Suppose there are three transversal equilibria z1 < z2 < z3. Then f < 0 on (z1, z2) while f(z2) = 0, so by the mean value theorem f′(c) > 0 for some c, which means p′(c) > 1. The degenerate two-equilibrium (tangency) case needs p′ = 1 at the tangency. So **p′ > 1 somewhere is necessary for robust multistability**.
- **Not sufficient.** Take logistic p with slope k and midpoint θ; then max p′ = k/4 (all values illustrative):

  | k | θ | max p′ | Equilibria (T*) | Note |
  |---|---|---|---|---|
  | 10 | 0.3 | 2.5 | one (≈ .999) | p′ > 1 yet unique |
  | 8 | 0.15 | 2.0 | one | p′ > 1 yet unique |
  | 12 | 0.1 | 3.0 | one | p′ > 1 yet unique |
  | ≤ 4 | 0.5 | ≤ 1 | one | |
  | 4.5 | 0.5 | 1.125 | three: .224 (stable), .500 (unstable), .776 (stable) | pitchfork at k = 4 |

  The steep region must straddle the diagonal.
- **Stability.** T* is stable if and only if p′(T*) < 1. η only rescales time; it changes neither the number nor the location of equilibria.
- **Hysteresis (illustrative, k = 10).** Raising θ slowly, the high-trust branch collapses between θ ≈ .68 and .70. Lowering θ slowly, the low-trust branch recovers only between θ ≈ .32 and .30. The loop is wide.
- **Discrete-time (diary) analogue.** T_{t+1} = T_t + η[p(T_t) − T_t] + ε_t has the same fixed points. Local stability holds if and only if 0 < η(1 − p′(T*)) < 2, so for 0 < η ≤ 1 the conclusions above carry over. With noise, bistability implies a bimodal distribution within a dyad over time and noise-induced switching between modes.
- **Analogue.** Granovetter's r_{t+1} = F(r_t) has an identical fixed-point structure: F(r) = r, stable where F′ < 1.

**What it would take to show bistability empirically [T/M]**
1. Estimate p(T), the trust-dependent interpretation of the partner's acts, across the whole range of T. This needs dyads observed at both low and high trust and long within-dyad series, for example with threshold AR or nonparametric regressions.
2. Show p′ > 1 (loop gain above 1) somewhere.
3. Show multimodality within dyads over time, not just between dyads.
4. Show hysteresis under a slowly varied input.

Each step has competing explanations. Exogenous regime switching driven by life events, scale floors and ceilings, and heterogeneity across dyads (which yields between-dyad bimodality) all mimic the signatures. Manipulating partners' behaviour downward to test hysteresis would be unethical. Bistability of trust is therefore, at present, a **[T]** proposition that is hard to falsify. The paper should say so, or derive a cheaper testable implication, such as asymmetric updating after negative evidence at low trust.

**Terminal decline is not evidence of a tipping point (S; illustrative simulation)**
- Simulate a driftless random walk of satisfaction with no change in dynamics and no tipping point. Call it "separation" when the walk first crosses a threshold. Aligned on time-to-separation, the mean shows an accelerating decline: −.066 per 4 steps at 40 steps before separation, −.198 in the second-to-last block, −.464 in the final block.
- A preterminal/terminal piecewise pattern is therefore expected under selection on a threshold crossing, even with matched controls and even when time-to-separation beats time-since-beginning. Bühler & Orth's 2025 pattern is real and important as description but does **not** show bistability or critical slowing down. **[E-logic; how much of their effect is selection is SPEC]**
- **Loop gain [SPEC].** Expectancy effects in classrooms are small and dissipate (Jussim & Harber), consistent with loop gain below 1 and a unique equilibrium in that domain. Whether romantic trust has higher gain is unknown.

### Gaps
- No empirical evidence of bistability or hysteresis in relationship trust or satisfaction was found.
- No study of critical slowing down in couples' time series was found.
- The Chinese-language cusp study on psychological contracts was not verified.

---

## 9. Network models: estimation, replicability critiques and dyadic applications

### Takeaway
Psychological network models (regularized partial-correlation networks, called Gaussian graphical models, and multilevel vector-autoregressive networks) are descriptive models of conditional associations. Their replicability and the meaning of their centrality indices are contested. Dyadic applications to couples' daily emotions exist but are exploratory. For this paper, networks could map which care channels co-vary within couples. They cannot establish translation mechanisms.

### Cited Findings
- Tutorial on estimating regularized partial-correlation networks and assessing their accuracy and stability (bootnet). **[E as a method] (K)** — [Epskamp, Borsboom & Fried 2018, Behavior Research Methods](https://doi.org/10.3758/s13428-017-0862-1)
- Association networks were stable, but conditional-independence networks "had poor replicability between and within methods and samples" (NCS-R n = 9,282; NSMHWB n = 8,841). **[M] (A)** — [Forbes, Wright, Markon & Krueger 2017, J Abnormal Psychology](https://doi.org/10.1037/abn0000276). A reanalysis contests this. **(K)** — [Borsboom et al. 2017](https://doi.org/10.1037/abn0000306). Follow-up: detailed network characteristics (edge presence, sign and strength) are less reliable than standard stability metrics suggest. **(A)** — [Forbes et al. 2021 (online 2019), MBR](https://doi.org/10.1080/00273171.2019.1616526)
- A lack of theory building impedes progress in the factor and network literatures. **[M] (K)** — [Fried 2020, Psychological Inquiry](https://doi.org/10.1080/1047840X.2020.1853461)
- Dyadic application: network analysis to parameterize interpersonal emotion dynamics in two dyadic daily-diary samples (couples in routine life; couples in the transition to parenthood), at different temporal levels and through different emotional pathways, with variation in networks predicting outcomes. **[P] (A)** — [Bar-Kalifa & Sened 2020 (online 2019), MBR](https://doi.org/10.1080/00273171.2019.1624147)

### Inferences
- **A dyadic network over care channels is the translation matrix in another form.** A multilevel VAR network over channels (A's acts → B's perceived acts → B's felt love) estimates the cross-dimension "translation matrix" of §13 as partial associations. Edges are not causal, and contemporaneous edges cannot be directed. **[E]**
- **Treat edges with caution.** Preregister, check stability and replicate out of sample before interpreting specific edges. **[M]**

### Gaps
- No dyadic network study of care channels was found.

---

## 10. Explanation versus prediction, formal theory construction, theory appraisal, equivalence testing, measurement and causal graphs

### Takeaway
The hypothesis is explanatory and causal. Current evidence for its components is mostly correlational, plus some large-scale prediction. The methods literature implies six steps:
1. formalize the verbal theory so that it generates the target phenomena;
2. make the derivation chain from theory to measurable prediction explicit;
3. pre-specify smallest effects of interest and equivalence tests, so the theory can lose;
4. evaluate explanation and prediction separately, and cross-validate;
5. write causal assumptions as directed acyclic graphs (DAGs) before choosing covariates or mediators;
6. document measurement decisions.

### Cited Findings
**Explanation versus prediction**
- Explanatory and predictive modelling differ in purpose and method; conflating them is common, and explanatory power does not imply predictive power. **[E] (A)** — [Shmueli 2010, Statistical Science](https://doi.org/10.1214/10-STS330)
- Lessons from machine learning: overfitting, cross-validation and regularization. **[E] (K)** — [Yarkoni & Westfall 2017, PPS](https://doi.org/10.1177/1745691617693393); integrating explanation and prediction **(K)** — [Hofman et al. 2021, Nature](https://doi.org/10.1038/s41586-021-03659-0)
- Random forests across 43 dyadic longitudinal datasets from 29 labs:
  - The top relationship-specific predictors were perceived-partner commitment, appreciation, sexual satisfaction, perceived-partner satisfaction and conflict.
  - Relationship-specific variables predicted up to 45% of variance at baseline and up to 18% at the end of each study.
  - Actor reports predicted two to four times more than partner reports.
  - Neither individual differences nor partner reports added beyond actor-reported relationship-specific variables.
  - "Relationship-quality change … was largely unpredictable from any combination of self-report variables".

  **[E (predictive)] (A)** — [Joel et al. 2020, PNAS](https://doi.org/10.1073/pnas.1917036117)
- Cross-validation shrinkage in divorce prediction. **[E] (A)** — [Heyman & Slep 2001](https://doi.org/10.1111/j.1741-3737.2001.00473.x)

**Formal theory construction**
- Revisiting Meehl's criticisms and using formal theory as a toolkit for building theory. **[E–T] (A)** — [Robinaugh, Haslbeck, Ryan, Fried & Waldorp 2021, PPS](https://doi.org/10.1177/1745691620974697)
- Theory construction methodology in five steps: identify the phenomena, build a prototheory, formalize it as a model, check its explanatory adequacy, evaluate overall worth. **[E–T] (A)** — [Borsboom et al. 2021, PPS](https://doi.org/10.1177/1745691620969647)
- "Models are stupid, and we need more of them." **(K)** — [Smaldino 2017, chapter](https://doi.org/10.4324/9781315173726-14); computational modelling "forces" theory building **(A)** — [Guest & Martin 2021, PPS](https://doi.org/10.1177/1745691620970585); theory before the test **(K)** — [van Rooij & Baggio 2021](https://doi.org/10.1177/1745691620970604); the theory crisis **(K)** — [Eronen & Bringmann 2021](https://doi.org/10.1177/1745691620970586)

**Theory appraisal and falsification**
- Directional significance tests in "soft" psychology give weak corroboration; risky predictions are needed. **[E] (K)** — [Meehl 1978](https://doi.org/10.1037/0022-006X.46.4.806). Lakatosian defense, the "crud factor", and corroboration from narrow-range predictions. **[E] (K)** — [Meehl 1990](https://doi.org/10.1207/s15327965pli0102_1)
- Psychologists "may not be ready to test hypotheses". The derivation chain needs strengthening through work on concepts, measurement and auxiliary assumptions. **[E–T] (A partial; "derivation chain" K)** — [Scheel, Tiokhin, Isager & Lakens 2021, PPS](https://doi.org/10.1177/1745691620966795)
- The generalizability crisis: verbal hypotheses and their statistical expressions are often misaligned. **[E–T] (A)** — [Yarkoni 2022, BBS](https://doi.org/10.1017/S0140525X20001685)

**Equivalence testing, measurement and causal graphs**
- Equivalence testing with two one-sided tests (TOST) against a smallest effect size of interest (SESOI), and ways to set the SESOI. **[E] (A)** — [Lakens, Scheel & Isager 2018, AMPPS](https://doi.org/10.1177/2515245918770963); anchor-based SESOIs **(K)** — [Anvari & Lakens 2021, JESP](https://doi.org/10.1016/j.jesp.2021.104159); sample-size justification **(K)** — [Lakens 2022, Collabra](https://doi.org/10.1525/collabra.33267)
- Questionable measurement practices and the role of transparency. **[E] (A)** — [Flake & Fried 2020, AMPPS](https://doi.org/10.1177/2515245920952393)
- DAGs for observational data: the rationale for statistical control and what can go wrong. **[E] (A)** — [Rohrer 2018, AMPPS](https://doi.org/10.1177/2515245917745629)
- The taboo against explicit causal inference in nonexperimental psychology harms research. **[E] (A)** — [Grosz, Rohrer & Thoemmes 2020, PPS](https://doi.org/10.1177/1745691620921521)
- Mediation and moderation path models work only under limited conditions; "reversing arrows or comparing model fit indices cannot tell us which model is the right one". **[E] (A)** — [Rohrer, Hünermund, Arslan & Elson 2022, AMPPS](https://doi.org/10.1177/25152459221095827). Mediation needs strong assumptions **(K)** — [Bullock, Green & Ha 2010](https://doi.org/10.1037/a0018933). Cross-sectional mediation is biased for longitudinal processes **(K)** — [Maxwell & Cole 2007](https://doi.org/10.1037/1082-989X.12.1.23)

### Inferences
- **Derivation chain for this hypothesis [T, and important].** "Intended ≠ expressed ≠ perceived ≠ received ≠ compatibility" is guaranteed true by measurement error and the crud factor, and is therefore unfalsifiable as stated. It must be rewritten as quantitative claims about named parameters, for example:
  - SRM relationship variance in perceived care;
  - truth force and directional bias for each link;
  - line-of-incongruence versus line-of-congruence RSA terms;
  - the channel-match versus amount effect in experiments.

  Each claim needs a pre-registered SESOI and an equivalence test.
- **Testing "translation rather than amount" [E-logic].** This is a comparative causal claim. It needs designs that manipulate channel match holding amount fixed, and amount holding match fixed: a factorial laboratory experiment or a within-couple micro-randomized trial (§12). Observational RSA shows association only.
- **A risky predictive test [T].** Joel et al. (2020) set the benchmark. A translation model should be judged on whether its constructs predict out-of-sample beyond perceived-partner commitment, appreciation and the like, and whether they predict change, which no combination of self-reports did. A pre-registered failure would count against the hypothesis.
- **DAG warnings [M].**
  - Perceived care is plausibly a mediator between expressed care and satisfaction; it may also be a collider, for example when both expressed care and satisfaction-driven reporting tendencies affect it.
  - The perceiver's own giving confounds perceived care → satisfaction, through projection (Lemay et al. 2007).
  - "Controlling for" perceived care when estimating the effect of expressed care can therefore bias estimates.

### Gaps
- None specific; this literature is mature.

---

## 11. Measurement invariance and scale-use differences across cultures (anchoring vignettes)

### Takeaway
Comparing care, needs or translation gaps across cultures or roles requires evidence that the measures work the same way in each group, or approximate invariance via alignment. Response-scale differences can be calibrated with anchoring vignettes. Both rest on assumptions that are sometimes rejected empirically, and some methodologists argue invariance is not strictly required. One conceptual conflict matters for this paper: anchoring vignettes assume everyone perceives a described act at the same level, which is exactly what the translation hypothesis denies.

### Cited Findings
- A review and synthesis of invariance testing: the sequence of configural, metric, scalar and further tests. **[E] (K)** — [Vandenberg & Lance 2000, ORM](https://doi.org/10.1177/109442810031002); conventions and reporting **(K)** — [Putnick & Bornstein 2016, Developmental Review](https://doi.org/10.1016/j.dr.2016.06.004)
- Alignment optimization for approximate invariance across many groups. **[E] (K)** — [Asparouhov & Muthén 2014, SEM](https://doi.org/10.1080/10705511.2014.919210)
- Tutorial on multiple-group confirmatory factor analysis and alignment for transparent analysis plans: traditional approaches "are strict, vary across the field in implementation, and present multiplicity challenges". **[E] (A)** — [Luong & Flake 2023 (online 2022), Psychological Methods](https://doi.org/10.1037/met0000441)
- Measurement invariance is "not necessary for meaningful and valid comparisons across groups". There is "no support for preferring the partial invariance approach" over alignment, robust linking or Bayesian approximate invariance. **[M — contested position] (A)** — [Robitzsch & Lüdtke 2023, SEM](https://doi.org/10.1080/10705511.2023.2191292); review **(K)** — [Leitgöb et al. 2023 (online 2022), Social Science Research](https://doi.org/10.1016/j.ssresearch.2022.102805)
- Anchoring vignettes: respondents rate hypothetical people described in short vignettes on the same scale as themselves. Because the vignettes' actual levels are the same for everyone, variation in vignette ratings reveals differences in scale use, which can then be corrected. **[E] (A)** — [King, Murray, Salomon & Tandon 2004, APSR](https://doi.org/10.1017/S000305540400108X)
- Tests of the two vignette assumptions (vignette equivalence and response consistency) rejected both for cognitive and physical functioning in older English adults; a weaker test did not reject response consistency for cognition. **[M] (A)** — [Bago d'Uva, Lindeboom, O'Donnell & van Doorslaer 2011, J Human Resources](https://doi.org/10.3368/jhr.46.4.875)

### Inferences
- **Invariance across partners and roles first [E-logic].** Test invariance across men and women, or parents and children, before comparing giver and receiver means or computing commensurate need–supply differences. The latent congruence model tests equivalence across component measures (Cheung 2009).
- **Vignettes as a translation measure [T, important].** Care-act vignettes could anchor how different cultures map acts onto "how much care". But the vignette-equivalence assumption, that everyone sees the described act at the same level, is precisely what the translation hypothesis doubts. Vignette ratings may therefore *measure* translation rather than correct for scale use. Two designs could separate the two: (a) non-care calibration vignettes for scale use, plus (b) care-act vignettes as outcome data.

### Gaps
- No invariance study of care-channel or love-language measures across cultures was retrieved (the culture and Korea researchers may cover this).

---

## 12. Experimental manipulations of responsiveness and support, and their ethics with couples and families

### Takeaway
Validated paradigms exist that fix "expressed" care by design: standardized notes or instant messages, scripted confederates, visible versus invisible support, and virtual partners. Only such paradigms give the expressed → perceived link a true ground truth. Under experimental control they show that identical expressed support is perceived and used differently by different recipients. Within real couples and families, deception-based manipulations carry specific ethical risks. Non-deceptive alternatives include independent coding of genuine messages, randomized brief interventions, and micro-randomized prompts both partners agreed to.

### Cited Findings
- **Standardized notes presented as from the partner.** Study 1 (95 couples): experimenters manipulated low- versus high-support messages before a stressful task. Insecure participants who received low-support messages appraised them more negatively, rated a prior interaction with their partner as less supportive and performed worse. Study 2 (153 couples), with genuine messages: insecure participants still perceived them as less supportive after controlling for independent ratings of the messages. **[M] (A)** — [Collins & Feeney 2004, JPSP](https://doi.org/10.1037/0022-3514.87.3.363)
- **Strangers.** Responsiveness manipulated by standardized instant messages (Study 2) and by a confederate's responsive or unresponsive reactions (Study 3). **[M] (A)** — [Birnbaum & Reis 2012, PSPB](https://doi.org/10.1177/0146167212441028)
- **Visible versus invisible support.** Three experiments (N = 257 women): confederate support was visible or invisible before a speech. Invisible support reduced emotional reactivity relative to visible and no support; visible support was ineffective or made reactivity worse. **[M] (A)** — [Bolger & Amarel 2007, JPSP](https://doi.org/10.1037/0022-3514.92.3.458)
- **Responses to good news.** Four experiments plus a daily diary: enthusiastic responses to shared good news increased the perceived value of the events and promoted trust and a prosocial orientation. **[M] (A)** — [Reis et al. 2010, JPSP](https://doi.org/10.1037/a0018344)
- **Virtual partners.** Responsiveness in an immersive virtual world. **[P] (K, title)** — [Kane, McCall, Collins & Blascovich 2012 (online 2011), JESP](https://doi.org/10.1016/j.jesp.2011.07.001)
- **Listening.** High-quality listening as a manipulable route to perceived responsiveness. **[M] (K)** — [Itzchakov, Reis & Weinstein 2022, SPPC](https://doi.org/10.1111/spc3.12648)
- **Brief interventions.** Randomized brief interventions between two conflict discussions. **[P] (A)** — [Gottman et al. 2005](https://doi.org/10.1207/s15327698jfc0503_1)
- **Micro-randomized trials (MRT).** Intervention components are randomized many times within each person, enabling "modeling of causal effects and time-varying effect moderation". **[E as a method] (A)** — [Klasnja et al. 2015, Health Psychology](https://doi.org/10.1037/hea0000305). Design and analysis considerations, including causal excursion effects **(A)** — [Qian et al. 2022, Psychological Methods](https://doi.org/10.1037/met0000283)
- **Ethics.** "Federal regulations, ethical standards, and state laws governing ethics do not adequately address important issues in couple and family research". The issues include confidentiality, privacy and consent with multiple members (especially minors); ownership and disclosure of commingled data; harms and benefits for the family as a unit; abuse reporting; Certificates of Confidentiality; and observational data. **[E] (A)** — [Margolin et al. 2005, JFP](https://doi.org/10.1037/0893-3200.19.1.157). The general deception debate **(K)** — [Hertwig & Ortmann 2008, Ethics & Behavior](https://doi.org/10.1080/10508420701712990)

### Inferences
- **Ethical risk of the standard-note paradigm [T/ethics].** Telling someone that low-support notes came from their real partner can do real relational harm. Insecure participants, whom Collins & Feeney found most affected, are most at risk, and the risk is sharper in families with children. Mitigations:
  - debrief both partners;
  - keep manipulations low-intensity;
  - use strangers, confederates or virtual partners for the expressed → perceived link;
  - prefer non-deceptive designs, such as coding genuine messages or randomizing prompts that both partners consented to.
- **A within-couple MRT that directly tests "translation versus amount" [T: a design proposal; SPEC about feasibility and compliance].**
  - Each day, randomly assign A to one of: a prompt to express care in B's self-reported preferred channel; a prompt in a non-preferred channel; or no prompt.
  - Randomize prompt intensity separately to vary amount.
  - Outcome: B's evening perceived care and felt love.
  - Both partners consent to the prompt scheme, so there is no deception.

  This identifies the average causal excursion effects of channel match and of amount, and how they are moderated by trust or by B's stated importance. No such study was found.

### Gaps
- No experiment was found that crosses the amount of care with channel match.
- No published ethics guidance specific to deceptive support manipulations within couples was retrieved beyond Margolin et al. 2005.

---

## 13. Model components: justification, identifiability, recommended formulation and notation glossary

### Takeaway
Of the proposed components, these are **not justified** as specified:
- vectors E_A(t) and N_B(t) treated as living in one space;
- dot products and cosine similarity;
- importance-weighted similarity;
- cross-dimension interaction matrices estimated per dyad;
- a bistable trust equation presented as established.

These are **justified as hypotheses to estimate, not assume**:
- an asymmetric deficiency/excess loss, via cubic RSA or splines;
- latent state-space trust, possibly regime-switching;
- time-varying weights, but only with long series and a theory of why weights change.

Trust has empirical support as moderator, mediator and outcome. That points to a feedback model, not a single static role. Whether care in the wrong channel is "worthless" (a multiplicative bottleneck) or a partial substitute (additive) cannot be decided with ordinal outcome scales unless crossover predictions or experiments are used. "Safety as a constraint" is mathematically different in kind from "safety as a heavily weighted variable".

### Cited Findings
- **Commensurability.** Fit requires person and environment to be measured on the same content dimensions. **[T] (K)** — [Edwards, Caplan & Harrison 1998](https://doi.org/10.1093/oso/9780198522799.003.0003). Need and supply have been measured on one metric in partner-support research: under-provision versus over-provision relative to what was desired **(A)** — [Brock & Lawrence 2009](https://doi.org/10.1037/a0015402); daily desire versus receipt **(A)** — [Bar-Kalifa & Rafaeli 2013](https://doi.org/10.1037/a0034905)
- **Perception and projection.** Perceived responsiveness is driven more by the perceiver's own responsiveness than by the partner's reported responsiveness. **[M] (A)** — [Lemay, Clark & Feeney 2007](https://doi.org/10.1037/0022-3514.92.5.834). Tracking accuracy r = .47 and mean-level bias r = .09 **[E] (A)** — [Fletcher & Kerr 2010](https://doi.org/10.1037/a0019792)
- **Trust as outcome.** Experimentally, enthusiastic responses promoted trust. **[M] (A)** — [Reis et al. 2010](https://doi.org/10.1037/a0018344). Longitudinally, perceived pro-relationship acts led to trust. **[M] (A)** — [Wieselquist et al. 1999](https://doi.org/10.1037/0022-3514.77.5.942)
- **Trust as mediator.** Mediation analyses support mutual cyclical growth, with trust carrying a partner's acts into one's own dependence and commitment. **[M] (A)** — [Wieselquist et al. 1999](https://doi.org/10.1037/0022-3514.77.5.942)
- **Trust as moderator.** People who trusted their partners less showed greater day-to-day variability in perceived relationship quality and experienced daily conflict as more negative. **[M] (A)** — [Campbell, Simpson, Boldry & Rubin 2010, JPSP](https://doi.org/10.1037/a0019714). Confidence in a partner's regard structures the "if–then" rules of risk regulation. **[T/M] (A)** — [Murray, Holmes & Collins 2006](https://doi.org/10.1037/0033-2909.132.5.641). A validated trust measure **(K)** — [Rempel, Holmes & Zanna 1985, JPSP](https://doi.org/10.1037/0022-3514.49.1.95)
- **Multiplicative versus additive.** Interactions can be "removable", appearing or disappearing with scaling decisions. **[E] (A)** — [Rohrer & Arslan 2021, AMPPS](https://doi.org/10.1177/25152459211007368). Non-crossover interactions are tied to the measurement scale and "do not allow unambiguous conclusions about latent psychological processes". **[E] (A)** — [Wagenmakers, Krypotos, Criss & Iverson 2012 (online 2011)](https://doi.org/10.3758/s13421-011-0158-0); original argument **(K)** — [Loftus 1978](https://doi.org/10.3758/BF03197461). The expected size of an interaction depends on its shape, and interactions are often modest, which makes power hard to achieve. **[E] (A)** — [Sommet, Weissman, Cheutin & Elliot 2023, AMPPS](https://doi.org/10.1177/25152459231178728)
- **Bottlenecks and necessary conditions.** Correlation and regression are inappropriate for "necessary but not sufficient" claims; necessary condition analysis is designed for them. **[E as a method] (A)** — [Dul 2016, ORM](https://doi.org/10.1177/1094428115584005). Noncompensatory decision models **(K)** — [Einhorn 1970, Psychological Bulletin](https://doi.org/10.1037/h0028695). Necessities versus luxuries in mate preferences under budget constraints **(K)** — [Li, Bailey, Kenrick & Linsenmeier 2002, JPSP](https://doi.org/10.1037/0022-3514.82.6.947). Relationship dealbreakers **(K)** — [Jonason et al. 2015, PSPB](https://doi.org/10.1177/0146167215609064)
- **Constraints versus weights.** Lexicographic orders, utilities and decision rules. Lexicographic preferences cannot in general be represented by a real-valued utility function. **[E-math] (K)** — [Fishburn 1974, Management Science](https://doi.org/10.1287/mnsc.20.11.1442)
- **Latent states and time-varying parameters.** State-space estimation **(A)** — [Song & Ferrer 2009](https://doi.org/10.1080/10705510902751432); regime switching **(A)** — [Hamaker & Grasman 2012](https://doi.org/10.1007/s11336-012-9254-8); time-varying models (§7).
- **Validated measures of other model inputs (K):**
  - relationship satisfaction, the IRT-based Couples Satisfaction Index — [Funk & Rogge 2007](https://doi.org/10.1037/0893-3200.21.4.572);
  - relationship-specific need fulfilment in self-determination theory terms — [La Guardia, Ryan, Couchman & Deci 2000](https://doi.org/10.1037/0022-3514.79.3.367);
  - observational coding of support-behaviour types — [Cutrona & Suhr 1992](https://doi.org/10.1177/009365092019002002);
  - care-channel ("love language") measurement is contested — [Impett et al. 2024](https://doi.org/10.1177/09637214231217663) (A).

### Inferences
**Component-by-component verdicts**

1. **E_A(t) ∈ ℝ^K (expressed care by channel).** *Construct:* A's enacted acts. *Measurement:* event-contingent self-report checklists, B's report (which is perception, not expression), observer coding (e.g., support-type codes). No validated multi-channel care-act inventory exists. *Appropriate operations:* counts or durations (ratio scale) per channel; never Likert scores in a cosine. *Verdict:* **justified as observed variables**, not as a vector in a shared space with needs. **[T/M]**
2. **N_B(t) (needs by channel).** *Construct:* desired amount of each kind of care. *Measurement:* "how much X did you want today", as in support-desire items. *Verdict:* **justified only if** measured on the same metric as received supply S_B. **[M]**
3. **Same space?** **No.** Needs are motivational states and behaviours are acts; they are not commensurate. The formalism needs a received-supply variable S_B,k on N_B's metric and an explicit translation function S_B = f(E_A, context, B's model of A). A cosine between E_A and N_B collapses the translation step (the hypothesis itself) into one unjustified operation. **[T, strongly argued from P–E fit commensurability]**
4. **Dot product, cosine, weighted similarity.** **Reject** (§1–2). They ignore magnitude, depend on origin and units, are inflated by normativeness, and add redundant importance weights. **[E-math; M empirical]**
5. **Asymmetric deficiency/excess loss.** **Justified as a hypothesis.** Estimate it with cubic RSA or spline regression on (N, S); do not fix its shape. Evidence on excess is mixed (Brock & Lawrence vs Bar-Kalifa & Rafaeli). **[M]**
6. **Cross-dimension interaction matrix (S_B = Λ·E_A, or E_Aᵀ M N_B).** K channels give K² parameters per dyad (25 for K = 5). Per-dyad estimation from weeks of diary data is underdetermined. Identification needs (a) pooling with random effects and structure (for example, diagonal plus a few theorized off-diagonal terms), or (b) within-dyad randomization of the channel (an MRT). No measure or estimate of Λ exists. **[SPEC]**
7. **Time-varying weights.** Estimable with time-varying effect, AR or VAR models. This needs long series and a theory of why weights change (e.g., life transitions); otherwise it is overfitting. No relationship application was found. **[T]**
8. **Latent-state (state-space) trust.** **Justified.** Trust is latent and measured with error. Separating measurement error from state noise needs several indicators per occasion or long series (Song & Ferrer 2009). Regime-switching or hidden Markov variants represent sudden shifts without assuming bistability. **[M]**
9. **Role of trust.** There is evidence for all three roles (outcome: Reis 2010, Wieselquist 1999; mediator: Wieselquist 1999; moderator: Campbell 2010, Murray 2006), so a static moderator-or-mediator model is misspecified. Use a dynamic model with feedback: lagged trust ↔ perceived care ↔ satisfaction, with trust moderating how perceived acts update trust. Cross-sectional mediation is biased (Maxwell & Cole). **[M]**
10. **Multiplicative bottleneck versus additive.** **Not decidable with Likert outcomes** unless the theory predicts a crossover interaction. A multiplicative Y = A·B becomes exactly additive after a log transform: the 2×2 interaction contrast of 1 becomes 0 (S). Test with factorial experiments (amount × match) with pre-registered functional forms, necessary condition analysis ceiling lines for "no care registers without X", and adequate power. **[E-logic]**
11. **Safety as a constraint versus a weighted variable.** **Formally distinct.** Lexicographic (constraint-first) preferences cannot be represented by any finite weighting in a real-valued utility. *Empirical signature of a constraint:* below a safety threshold, outcomes are insensitive to care in other channels (gating). Test it with threshold, hurdle or necessary condition analysis models versus additive models. The substance is covered by the abuse/coercion researcher. **[T; E-math]**

**Comparison of alternative formulations (dossier table)**

Abbreviations: APIM = actor–partner interdependence model; SRM = Social Relations Model; RSA = response surface analysis; DSEM = dynamic structural equation model; CLPM / RI-CLPM = (random-intercept) cross-lagged panel model; MRT = micro-randomized trial; NCA = necessary condition analysis; TAR = threshold autoregressive; LDE = latent differential equation; HMM = hidden Markov model; VAR = vector autoregression; GGM = Gaussian graphical model; ODE = ordinary differential equation.

| Formalism | Construct represented | Validated measurement? | Operation appropriate? | Key assumptions | Track record | Data that identify it | Inferential status | Verdict |
|---|---|---|---|---|---|---|---|---|
| Difference score (N − E or \|N − E\|) | Mismatch | Inputs sometimes valid, index not | No: imposes equal and opposite coefficients; confounds components | Constraints true; commensurate | Widely used, widely critiqued ([Edwards 1994](https://doi.org/10.1006/obhd.1994.1029)) | Any paired measure | Descriptive | **Reject** |
| Profile r / cosine / dot product | Pattern or "direction" of match | No | No (§1 math) | Ratio scale, orthogonal equal units, no normativeness | Inflated correlates ([Wood & Furr 2016](https://doi.org/10.1177/1088868315581119)) | Profiles | Descriptive | **Reject** (normatively corrected profile r only as a secondary description) |
| Weighted similarity Σ w·E·N | Importance-weighted match | No | No | Ratio scale; additive importance | Weighting gives no advantage ([Trauer & Mackinnon 2001](https://doi.org/10.1023/A:1013159414364)) | — | — | **Reject** |
| Polynomial regression + RSA (dyadic, multilevel, cubic) | Need–supply congruence vs level | Depends on N and S measures | Yes | Commensurate N and S; adequate N; no strong measurement error (or use LCM) | Mature method; congruence increments usually small ([Yang 2008](https://doi.org/10.1016/j.hrmr.2008.07.014); [Dyrenforth 2010](https://doi.org/10.1037/a0020385)) | Cross-sectional dyads (dyadic RSA) or diaries (multilevel RSA) | Associational | **Use (primary)** |
| Spline regression / LCM | Kinked or asymmetric fit; latent congruence | — | Yes | As RSA | Methodological ([Edwards & Parry 2017](https://doi.org/10.1177/1094428117715067); [Cheung 2009](https://doi.org/10.1177/1094428107308914)) | As RSA; multi-item indicators for LCM | Associational | **Use** |
| APIM (cross-sectional, longitudinal, DSEM) | Actor and partner associations | Yes, for many outcomes | Yes | Correct dyad type; no unmodelled confounds for causal reading | Extensive | Both partners' X and Y; occasions for dynamics | Associational | **Use** |
| SRM (family round robin) | Perceiver / target / relationship ("translation") variance | Round-robin ratings | Yes | Groups of four or more (or multiple partners); ≥2 indicators | Family reviews ([Eichelsheim 2009](https://doi.org/10.1111/j.1741-3737.2009.00652.x)) | Families or multi-partner designs | Descriptive variance decomposition | **Use for the "translation" variance claim** |
| Truth-and-bias model | Accuracy vs bias for each link | Criterion = other's report | Yes | Same metric; criterion ≠ truth | Strong in couples ([Fletcher & Kerr 2010](https://doi.org/10.1037/a0019792)) | Repeated judgments per perceiver + criterion | Descriptive | **Use** |
| Quasi-SDT (GLMM form) | Noticing acts: hits, misses, false alarms | Diary checklists | Yes, with caveats | Enactor report as "signal" | Several couple studies (§4) | Both partners' daily reports; enough signal-present and signal-absent days | Descriptive | **Use** (with observer or experimental criterion where possible) |
| Inverse planning / naïve utility calculus | Inferring value of B to A from A's costs | None in couples | Yes, in designed tasks | Known options and costs | Strong in lab; none in couples | Vignettes, animations, games | Mechanistic model, lab | **Theoretical for couples; test with stimuli** |
| Asymmetric Bayesian or RL trust updating | Trust learning, volatility | No partner-specific version | Plausible | Stationary learning rule | Strangers ([Siegel 2018](https://doi.org/10.1038/s41562-018-0425-1)); friends ([Fareri 2015](https://doi.org/10.1523/JNEUROSCI.4775-14.2015)) | Repeated games or long diaries | Mechanistic | **[SPEC] for couples** |
| Linear or nonlinear love ODEs (Strogatz, Rinaldi) | Mutual feelings over time | No | Only as thought experiments | Deterministic, low-dimensional | Never estimated on data (§6) | — | Theoretical | **Reject as empirical model** |
| Gottman-type nonlinear difference equations / TAR | Affect influence in conflict | Coded affect | Yes (TAR form) | Thresholds; stationarity | Estimated; divorce prediction not cross-validated ([Heyman & Slep 2001](https://doi.org/10.1111/j.1741-3737.2001.00473.x)) | Dense coded interaction series | Descriptive or predictive | **Use (TAR) for interaction data only** |
| Coupled oscillators / LDE / dynamic factor analysis / state space | Coregulation, latent dynamics | Affect or physiology | Yes | Dense, equally spaced data | Several dyadic applications (§6) | Long series per dyad | Descriptive dynamics | **Use if the process is oscillatory or latent** |
| DSEM / multilevel VAR | Within-dyad lagged dynamics | Diaries | Yes | Correct lag; no time-varying confounding | Growing ([Savord 2023](https://doi.org/10.1080/10705511.2022.2065279)) | Many dyads × many days | Associational (within) | **Use (workhorse)** |
| CLPM | "Reciprocal effects" | — | No | No stable traits | Critiqued ([Lucas 2023](https://doi.org/10.1177/25152459231158378)) | Panel | — | **Reject** |
| RI-CLPM | Within-person reciprocal associations | Panel | Conditional | Parametric assumptions ([Lüdtke & Robitzsch 2022](https://doi.org/10.1080/10705511.2022.2065278)) | Widely used | ≥3 waves | Associational | **Use cautiously** |
| Regime-switching / HMM | Discrete relational states | Diaries or coded data | Yes | Number of states; Markov switching | Mother–infant ([Chow 2018](https://doi.org/10.1007/s11336-018-9605-1); [Stifter & Rovine 2015](https://doi.org/10.1002/icd.1907)) | Long series | Descriptive | **Use** |
| Bistable feedback dT/dt = η[p(T) − T] | Self-reinforcing trust | No | Mathematically sound (§8) | p′ > 1 somewhere and straddling the diagonal | No relationship evidence | p(T) across the T range; within-dyad multimodality; hysteresis | Theoretical | **Theoretical proposition only** |
| Critical slowing down / early warning signals | Approaching transition | — | Questionable | Bifurcation-type transitions | Weak in psychopathology ([Helmich 2024](https://doi.org/10.1038/s44159-024-00369-y)) | Long, dense series | Predictive (unproven) | **Do not rely on** |
| Networks (GGM / VAR) | Channel co-variation | Diaries | Exploratory | Partial-correlation structure | Replicability concerns ([Forbes 2017](https://doi.org/10.1037/abn0000276)) | Many observations | Descriptive | **Exploratory only** |
| Necessary condition analysis / bottleneck | "No X → no felt care" | — | Yes for necessity claims | Ceiling-line logic | Methodological ([Dul 2016](https://doi.org/10.1177/1094428115584005)) | Large N | Descriptive | **Use for bottleneck claims** |
| Machine-learning prediction | Predictability of outcomes | — | Yes for prediction | Cross-validation | [Joel 2020](https://doi.org/10.1073/pnas.1917036117) | Large pooled data | Predictive | **Use as benchmark** |
| Within-couple MRT / factorial experiments | Causal effect of channel match vs amount | Prompts; standardized messages | Yes | Consistency, positivity | MRT method established ([Qian 2022](https://doi.org/10.1037/met0000283)); not used for care channels | Repeated randomization within couples | **Causal** | **Use (strongest test)** |

**Notation glossary (recommended symbols)**

| Symbol | Meaning | Observed / latent | Measurement | Status |
|---|---|---|---|---|
| A, B; d; k = 1…K; t | Giver, receiver; dyad; care channel; occasion | — | — | — |
| I_A,k(t) | A's intended care in channel k | Latent; self-report proxy | A's diary ("I meant to show care by…") | No validated measure **[T]** |
| E_A,k(t) | A's expressed or enacted acts | Observed | A's event checklist (counts or durations); observer coding | Partially validated (support coding) |
| P_B,k(t) | B's perception that A did k | Observed | B's checklist | Quasi-SDT practice |
| N_B,k(t) | B's desired amount of k | Observed | "How much k did you want" | Support-desire items |
| S_B,k(t) | B's received amount of k, on N's metric | Observed | "How much k did you receive" | Support-receipt items |
| R_B(t) | B's overall felt love or need fulfilment | Observed | Global items | Overlaps with affect (molar fit) |
| T_B(t) | B's trust in A | Latent | Multi-indicator trust items (e.g., [Rempel 1985](https://doi.org/10.1037/0022-3514.49.1.95)) | Validated (trait level) |
| Y_B(t) | Outcome, e.g., satisfaction | Observed or latent | e.g., CSI ([Funk & Rogge 2007](https://doi.org/10.1037/0893-3200.21.4.572)) | Validated |
| a, p | APIM actor and partner coefficients | Parameter | — | — |
| α_i, β_j, γ_ij | SRM perceiver, target and relationship effects | Random effects | Round robin | — |
| τ, π, δ | Truth force, projection (bias) force, directional bias | Parameters | Truth-and-bias model | — |
| d′, c | Sensitivity and criterion (probit form) | Parameters | GLMM-SDT | — |
| b0…b5 (b6…b9); a1…a4 | RSA coefficients and surface tests (cubic extensions) | Parameters | Polynomial regression | — |
| φ, κ | Autoregressive (inertia) and cross-lagged (coupling) coefficients | Parameters | DSEM / VAR | — |
| f(·), Λ | Translation function / matrix from acts to received supply | Parameter set | Requires randomization or long series | **[SPEC]** |
| p(T), η | Trust-dependent interpretation function; updating rate | Function / parameter | Nonlinear AR on long series | **[T]** |

Symbols deliberately **not** recommended: cos(E_A, N_B), E_A·N_B, Σ w·E·N (see §1–2).

**Designs that identify parameters (summary)**

| Design | Informants | Time points | Manipulation | Identifies |
|---|---|---|---|---|
| D1. Cross-sectional dyadic survey with commensurate N/S per channel | Both partners | 1 | None | Dyadic RSA congruence vs level; APIM associations |
| D2. Dyadic daily diary (event checklists + N/S + trust + outcomes) | Both partners | Many days (simulation-justified) | None | Truth-and-bias per link; quasi-SDT; multilevel RSA; DSEM-APIM dynamics (within-dyad associations) |
| D3. Lab interaction + segment-by-segment ratings + observer coding | Both partners + coders | Many 30-s segments | Optional | Perception accuracy and bias against an observer criterion |
| D4. Factorial standardized-message experiment (amount × channel match) | Recipient (+ coders) | 1–few | Yes (ground truth) | Causal effects of match vs amount on perceived care |
| D5. Within-couple micro-randomized trial | Both partners | Many days | Yes (randomized prompts) | Causal excursion effects of channel match and amount; moderation by trust or importance |
| D6. Family round robin | ≥4 members (or multi-partner) | 1+ | None | SRM relationship ("translation") variance vs perceiver and target variance |
| D7. Long panel + joint longitudinal/time-to-event models | Both partners | Years | None | Trajectories before separation (aware of selection artifacts, §8) |
| D8. Cross-cultural invariance + calibration vignettes | Individuals or dyads | 1 | Vignettes | Invariance; scale-use correction (with §11 caveat) |

Sources for these designs: §§3–4, 7, 11–12, especially [Overall et al. 2012](https://doi.org/10.1177/0146167211432764), [Collins & Feeney 2004](https://doi.org/10.1037/0022-3514.87.3.363), [Klasnja et al. 2015](https://doi.org/10.1037/hea0000305), [Cook 1994](https://doi.org/10.1037/0022-006X.62.3.500).

**What would falsify the core claim, given these tools [T]**
1. Dyadic or multilevel RSA on commensurate care N/S: line-of-incongruence curvature and asymmetry fall within a pre-registered SESOI (equivalence shown) while line-of-congruence or level effects dominate. That would mean amount, not translation.
2. SRM in families: relationship-specific variance in perceived care is negligible relative to perceiver variance. That would mean misperception is a property of the perceiver, not of the giver–receiver pair.
3. Factorial or MRT experiments: the effect of channel match on perceived care is within the SESOI while amount has a clear effect.
4. Out-of-sample prediction: translation constructs add nothing beyond perceived-partner commitment and appreciation (cf. [Joel et al. 2020](https://doi.org/10.1073/pnas.1917036117)).

The existing evidence on similarity and P–E fit (§1), love-language matching ([Impett et al. 2024](https://doi.org/10.1177/09637214231217663)), tracking accuracy ([Fletcher & Kerr 2010](https://doi.org/10.1037/a0019792)) and projection ([Lemay et al. 2007](https://doi.org/10.1037/0022-3514.92.5.834)) makes outcomes 1, 2 and 4 plausible. The strongest existing support for pieces of the hypothesis comes from quasi-SDT "misses" ([Visserman et al. 2019](https://doi.org/10.1177/1948550618757599)), under-provision effects ([Bar-Kalifa & Rafaeli 2013](https://doi.org/10.1037/a0034905)) and experimentally identical messages being perceived differently ([Collins & Feeney 2004](https://doi.org/10.1037/0022-3514.87.3.363)). **[M]**

### Gaps
- No validated instrument measures intended care, or a commensurate per-channel need/supply pair, beyond support types.
- No estimate of a translation matrix Λ exists.
- No relationship application of time-varying weights was found.
- No study tests safety-as-constraint versus additive models in ongoing relationships (the substance belongs to the abuse/coercion researcher).

---

## 14. Verification status of the candidate citations (DOI ledger)

### Takeaway
All 58 candidate leads supplied with the research brief (57 with a DOI, plus Strogatz 1988 without one) were checked against OpenAlex or Crossref. 56 DOIs resolved to the claimed paper. One was wrong and is corrected (Wu & Yao 2006). Strogatz 1988 had no DOI and one is now supplied. Several "wrong-year" appearances are online-first versus print dates, not errors. Three books on the candidate list have no DOI and are marked UNVERIFIED as links. Several DOIs the note-writer recalled from memory were also wrong and were corrected before use.

### Cited Findings
- **Verified as supplied (title, authors and year match; venue checked).**
  - Congruence and fit: Cronbach 1955; Edwards 1994; Edwards & Parry 1993; Furr 2008; Wood & Furr 2016 (online 2015); Shanock et al. 2010; Humberg, Nestler & Back 2019 (online 2018); Schönbrodt et al. 2018; Kristof-Brown et al. 2005.
  - Dyadic models: Cook & Kenny 2005; Kenny & La Voie 1984; Cook 1994; West & Kenny 2011.
  - Signal detection and inference: Visserman et al. 2019 (online 2018); Baker et al. 2009; Baker et al. 2017; Jara-Ettinger et al. 2016; Siegel et al. 2018; Behrens et al. 2008; Haselton & Buss 2000.
  - Dynamical models: Rinaldi 1998 (AMC); Gottman, Swanson & Murray 1999; Heyman & Slep 2001; Felmlee & Greenberg 1999; Butler 2011; Ferrer & Helm 2013; Steele & Ferrer 2011.
  - Intensive longitudinal methods: Bolger et al. 2003; Laurenceau & Bolger 2005; Asparouhov et al. 2018 (online 2017); Hamaker et al. 2015; Lucas 2023; Rohrer & Murayama 2023; Curran & Bauer 2011 (online 2010); Molenaar 2004; Fisher et al. 2018.
  - Tipping points and networks: van de Leemput et al. 2014; Epskamp et al. 2018; Forbes et al. 2017.
  - Theory, prediction and measurement: Shmueli 2010; Yarkoni & Westfall 2017; Robinaugh et al. 2021; Borsboom et al. 2021; Meehl 1978; Meehl 1990; Scheel et al. 2021; Lakens et al. 2018; Flake & Fried 2020; Rohrer 2018.
  - Invariance: Vandenberg & Lance 2000; Putnick & Bornstein 2016; Asparouhov & Muthén 2014; King et al. 2004.
  - Experiments and self-fulfilling expectations: Downey et al. 1998; Birnbaum & Reis 2012; Collins & Feeney 2004.

  All are linked by DOI in the sections above. Sources: [OpenAlex API](https://api.openalex.org/works/doi:10.1037/h0044919); [Crossref API](https://api.crossref.org/works/10.1037/a0022936) (example endpoints).
- **Corrected or supplied:**
  - **Wu & Yao 2006.** Supplied DOI 10.1007/s11205-005-5666-**0** returns 404. Correct: [10.1007/s11205-005-5666-5](https://doi.org/10.1007/s11205-005-5666-5), *Do We Need to Weight Item Satisfaction by Item Importance? A Perspective from Locke's Range-of-Affect Hypothesis*, Social Indicators Research 79(3):485–502.
  - **Strogatz 1988.** [10.1080/0025570X.1988.11977342](https://doi.org/10.1080/0025570X.1988.11977342), *Love Affairs and Differential Equations*, Mathematics Magazine 61(1). Caution: JSTOR DOI 10.2307/2689917 resolves to a *different* paper (Rawsthorne 1985, "Imitation of an Iteration").
- **Book-length leads (candidate list):**
  - Gottman et al. 2002 → [10.7551/mitpress/4499.001.0001](https://doi.org/10.7551/mitpress/4499.001.0001).
  - Rinaldi et al. "2016" → [10.1142/9656](https://doi.org/10.1142/9656) (Crossref year 2015).
  - Edwards, Caplan & Harrison 1998 → [10.1093/oso/9780198522799.003.0003](https://doi.org/10.1093/oso/9780198522799.003.0003).
  - Smaldino 2017 → [10.4324/9781315173726-14](https://doi.org/10.4324/9781315173726-14).
  - **UNVERIFIED (no DOI; not checked):** Kenny 1994 *Interpersonal Perception*; Kenny, Kashy & Cook 2006 *Dyadic Data Analysis*; Bolger & Laurenceau 2013 *Intensive Longitudinal Methods* (all Guilford).
- **Note-writer's own recalled DOIs that failed verification (404 or resolved to another paper), corrected before use:**
  - Rogers, Wood & Furr → [10.1177/0265407517712615](https://doi.org/10.1177/0265407517712615)
  - Savord et al. → [10.1080/10705511.2022.2065279](https://doi.org/10.1080/10705511.2022.2065279). The recalled …2065278 is Lüdtke & Robitzsch 2022, which is itself used in §7.
  - Stifter & Rovine → [10.1002/icd.1907](https://doi.org/10.1002/icd.1907). The recalled …icd.1917 is Guo et al. 2015 on mother–child co-regulation.
  - Helmich et al. → [10.1038/s44159-024-00369-y](https://doi.org/10.1038/s44159-024-00369-y)
  - Bühler, Krauss & Orth 2021 → [10.1037/bul0000342](https://doi.org/10.1037/bul0000342)
  - Russell et al. → [10.1007/s11205-004-2528-5](https://doi.org/10.1007/s11205-004-2528-5)
  - Gable, Reis & Downey → [10.1111/1467-9280.t01-1-01426](https://doi.org/10.1111/1467-9280.t01-1-01426)
- **Located by bibliographic query rather than from a recalled DOI, then resolved:** Cronbach & Gleser 1953 ([10.1037/h0057173](https://doi.org/10.1037/h0057173)); Fletcher & Kerr 2010 ([10.1037/a0019792](https://doi.org/10.1037/a0019792)); Kane et al. 2012 ([10.1016/j.jesp.2011.07.001](https://doi.org/10.1016/j.jesp.2011.07.001)); Wu 2008 ([10.1007/s11205-007-9180-9](https://doi.org/10.1007/s11205-007-9180-9)); Yang et al. 2008; Cheung 2009; Edwards 1993; Edwards 2008; Bar-Kalifa & Rafaeli 2013; Bühler & Orth 2025; Rinaldi 1998 (SIAM); Rinaldi et al. 2010 and 2013; Bago d'Uva et al. 2011.

### Inferences
- **Cite print years consistently.** Where OpenAlex shows an earlier year (online-first), cite the print year and volume in the paper. Examples: Wood & Furr 2016, PSPR 20; Humberg et al. 2019, SPPS 10; Visserman et al. 2019, SPPS 10; Asparouhov et al. 2018, SEM 25; Humberg et al. 2022, Psychological Methods 27.
- **A data-quality warning.** OpenAlex's abstract for Granovetter 1978 is a mismatched French text; its metadata (title, author, year) are correct. Do not quote OpenAlex abstracts without a cross-check.

### Gaps
- Full texts were not read except Mostova et al. 2022. Content tagged (K) should be spot-checked against the PDFs before quoting specific numbers or wording.
- The Kristof-Brown et al. 2005 direct-versus-indirect fit result remains UNVERIFIED.
