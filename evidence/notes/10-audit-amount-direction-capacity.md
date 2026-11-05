# Primary-source audit of claims C11–C15: amount versus translation, direction of effects, love languages, stress-limited capacity, parent–child disagreement

Audit of the five empirical claims that "Can Love Be Lost in Translation?" relies on (this repository, read only and not modified). Audit date: November 2026. Access routes tried for every source: publisher page, Unpaywall, OpenAlex, Semantic Scholar `openAccessPdf`, Europe PMC and NCBI E-utilities (PMC), author and institutional repositories, and a web search for OSF or preprint copies. No paywall-circumvention sites were used. Bot-challenge pages (Cloudflare) were not bypassed. Working files are in `working-files/audit_R3/`. File:line references are to the repository.

## C11. Le, Dove, Agnew, Korn & Mutso (2010): does the "amount" of love predict break-up?

### Takeaway
The paper's sentence matches the meta-analysis abstract almost word for word. The narrow claim is well supported: in non-marital romantic relationships, people's own reported love and commitment were among the strongest predictors of break-up. The paper stretches it in three ways. It uses the study to argue "amount rather than translation", but the study measured each person's own love and whether the relationship ended, not whether love was received. It generalizes to "relationships" in general, including parent–child. And it presents love's effect as if it were independent of commitment. The full text could not be read legitimately, so love's exact effect size and how love was measured remain unverified.

### Cited Findings
- **How the paper uses it.**
  - The verdict table for the clause "translation rather than amount" rules the clause not supported as a general claim, cites Le et al. as the strongest evidence that amount matters, and tags it "Established (amount)" — `paper/01-question-and-thesis.md:17`.
  - Commitment, love, inclusion of other in the self (IOS) and dependence are "among the strongest predictors of non-marital break-up across 137 studies" [Established] — `paper/03-literature-review.md:84`.
  - Evidence table: "Love and commitment strongly predict break-up | Established | Non-marital, mostly WEIRD" — `paper/03-literature-review.md:146`.
  - "Across 137 studies with 37,761 participants…", closing with the claim that amount is one of the best-established predictors in the field [Established] — `paper/05-evidence-against-it.md:7`.
  - Evidence anchor for failure type 0, "Amount deficit (not translation)" — `paper/07-revised-model.md:62`.
  - Generalized to "whether relationships last" — `paper/19b-is-love-enough.md:11`.
  - Model summary row "translation, not amount" — `README.md:50`.
  - Also registered as claims `evidence/claims.jsonl:7, 65, 90, 120`.
- **Access: closed; abstract plus secondary sources only.**
  - Unpaywall and OpenAlex report the paper as closed, with no repository full text. Semantic Scholar lists it as CLOSED — [OpenAlex record](https://api.openalex.org/works/doi:10.1111/j.1475-6811.2010.01285.x).
  - The Wiley page and the author's ResearchGate PDF returned HTTP 403 to automated fetching. The CORE copy sits behind a bot challenge, which was not bypassed.
  - The Haverford repository holds only a record and the author's one-line description, with no file — [Haverford Scholarship](https://scholarship.haverford.edu/psychology_facpubs/271).
- **What the abstract says** (paraphrased) — [abstract via OpenAlex](https://api.openalex.org/works/doi:10.1111/j.1475-6811.2010.01285.x):
  - The meta-analysis pooled predictors of non-marital romantic break-up from 137 studies (37,761 participants) spanning 33 years, covering individual, relationship and external variables.
  - Commitment, love, IOS and dependence were among the strongest predictors.
  - Satisfaction, perceived alternatives and investments were only modest predictors.
  - Social network support was a robust predictor.
  - Personality had limited predictive value, with small effects for relational dimensions such as attachment orientation.
- **Was love separate from satisfaction and commitment?** Yes, at the level of predictor categories. The abstract places love among the strongest predictors and satisfaction among the modest ones — [OpenAlex abstract](https://api.openalex.org/works/doi:10.1111/j.1475-6811.2010.01285.x). Which love instruments were pooled, the number of studies per predictor (k), and whether effects were zero-order or adjusted could not be verified.
- **Effect sizes, from secondary sources only** (citation contexts from citing papers, retrieved through the [Semantic Scholar citations API](https://api.semanticscholar.org/graph/v1/paper/DOI:10.1111/j.1475-6811.2010.01285.x/citations?fields=contexts,title,year)):
  - A 2019 *Psychological Inquiry* review says the strongest predictors (positive illusions, commitment, love) had effect sizes from d = .57 to .85 — [doi:10.1080/1047840X.2019.1577072](https://doi.org/10.1080/1047840X.2019.1577072).
  - A 2013 *Personal Relationships* paper reports commitment d = 0.80 and attachment dimensions d = 0.14–0.24 — [doi:10.1111/j.1475-6811.2012.01423.x](https://doi.org/10.1111/j.1475-6811.2012.01423.x).
  - A 2016 *Advances in Experimental Social Psychology* chapter reports trust d = −.57 — [doi:10.1016/bs.aesp.2015.09.001](https://doi.org/10.1016/bs.aesp.2015.09.001).
  - Two citing papers describe positive illusions (idealization of the partner) as the strongest protective predictor, stronger than commitment, trust and satisfaction — [JSPR 2022](https://doi.org/10.1177/02654075221127241); [J Child Fam Stud 2014](https://doi.org/10.1007/s10826-014-9932-5). The paper does not mention this.
  - Commitment and satisfaction correlate at about r = .68 meta-analytically, according to a 2018 paper citing Le & Agnew (2003) and Le et al. (2010) — [doi:10.1177/0265407517702010](https://doi.org/10.1177/0265407517702010).
- **Population.** 96% of participants in the meta-analysis were heterosexual — [Barrantes et al. 2017, PMC5501283](https://pmc.ncbi.nlm.nih.gov/articles/PMC5501283/). The country mix, student share and age could not be verified, so the paper's "mostly WEIRD" caveat (`paper/03-literature-review.md:146`) is plausible but unverified.
- **Design and causation.** This is a meta-analysis of associations between predictors and later break-up. A citing paper describes it as covering 30 longitudinal predictors — [J Child Fam Stud 2014](https://doi.org/10.1007/s10826-014-9932-5). Causation is not identified: love is self-reported, and falling love may be a symptom of a failing relationship as much as a cause.
- **Verdict: supported with qualifications.** The study supports "a person's own love and commitment predict whether a non-marital relationship lasts". It does not by itself support the comparative verdict "amount rather than translation":
  - The love measured is each person's own felt love, which may itself depend on how the partner's love was received.
  - The outcome is break-up, not feeling loved or receiving adequate care.

### Inferences
- Le et al. cannot separate "amount given" from "translation received". A respondent's self-reported love is plausibly partly a product of the love they perceive receiving, so the meta-analysis is compatible with both accounts. The paper half-acknowledges this at `paper/01-question-and-thesis.md:17` ("the dichotomy is partly false"), but `paper/05-evidence-against-it.md:7` still treats Le et al. as refuting the "not the amount" clause.
- Because love, commitment and satisfaction overlap strongly (commitment–satisfaction r ≈ .68), the pooled effects are probably overlapping zero-order associations (unverified). They should not be read as an independent effect of how much love there is.
- If, as secondary sources say, positive illusions (a perception variable) were the single strongest predictor, the meta-analysis partly supports the paper's other theme, that perception is generated by the perceiver. Check this in the full text before relying on it.
- Proposed wording for `paper/05-evidence-against-it.md:7` and `paper/03-literature-review.md:84`: "In a meta-analysis of 137 studies of non-marital couples (N = 37,761), people's own reported love, commitment, inclusion of other in the self and dependence were among the strongest predictors of whether the relationship later ended. Satisfaction, alternatives and investments were more modest predictors (Le et al. 2010) [Established, for non-marital persistence]. This shows that how much partners love and are committed matters for whether relationships last. It does not test whether love is lost in translation, because the love measured was each person's own self-report."
- `paper/19b-is-love-enough.md:11` should say "non-marital romantic relationships", not "relationships". Using it as an anchor for parent–child "amount deficit" (`paper/07-revised-model.md:62`) is an extrapolation and should be labelled as one.
- **Grade.** Keep **Established** for the narrow persistence claim. As evidence against "translation rather than amount", it is indirect (Moderate at best).

### Gaps
- Love's exact d and its confidence interval, the love instruments pooled, k and N per predictor, heterogeneity statistics, publication-bias checks, whether any effects were adjusted, time lags, sample composition (students, countries), and the authors' stated limitations. All need the full text (Personal Relationships 17(3):377–390), for example by library access or an author request. The secondary effect sizes above were not checked against the primary tables.

## C12. Lavner, Karney & Bradbury (2016): does communication predict satisfaction, or the reverse?

### Takeaway
The paper's current sentence is accurate: both directions occurred, and neither was robust. The "7 of 36" figure and "satisfaction predicted communication more consistently" also match the authors' own conclusions. They need the caveat that most direct comparisons of the two directions were not significant and that the authors called both effects inconsistent and similar in size. The section heading's "less causally" goes beyond what a cross-lagged panel model can show.

### Cited Findings
- **How the paper uses it.**
  - Section heading "3.7 Communication matters less, and less causally, than its reputation" — `paper/03-literature-review.md:86`.
  - "In low-income newlyweds, communication→satisfaction and satisfaction→communication paths both existed but 'neither pathway was particularly robust'" [Established to Moderate, shared with Johnson et al. 2022] — `paper/03-literature-review.md:88`.
  - Bibliography entry — `paper/20-bibliography.md:229`.
  - Claims registry — `evidence/claims.jsonl:67`.
  - A grep of `paper/`, `README.md` and `CORRECTIONS.md` found no "7 of 36" and no "more consistently". Those details are not currently in the paper.
- **Access: full text** — the NIH author manuscript, [PMC4852543](https://pmc.ncbi.nlm.nih.gov/articles/PMC4852543/), retrieved through NCBI E-utilities. I read the abstract, introduction, Method (sampling, participants, procedure, behavioural coding, satisfaction measure), every Results subsection and the Discussion, including the caveats. Tables 1–7 were not inspected separately; the text reports the counts and median coefficients used here.
- **Design.** Four waves about 9 months apart, covering roughly the first 3 years of marriage — [PMC4852543](https://pmc.ncbi.nlm.nih.gov/articles/PMC4852543/). Analysis used cross-lagged path models in Mplus with FIML (N = 431), standardized coefficients and Wald tests comparing the two directions. Further checks were Wave 1→4 models and zero-order Wave 1→4 correlations.
- **Population** — [PMC4852543](https://pmc.ncbi.nlm.nih.gov/articles/PMC4852543/):
  - First-married couples from low-income neighbourhoods in Los Angeles County, sampled from 2009–2010 marriage licences.
  - Of 3,793 couples contacted, 1,522 responded and agreed to screening, 824 were eligible, 658 agreed and 431 completed the study.
  - 76% Hispanic, 12% African American, 12% Caucasian. Married 4.8 months on average at entry; 38.5% had children. Mean age 27.9 (men) and 26.3 (women).
- **What was measured** — [PMC4852543](https://pmc.ncbi.nlm.nih.gov/articles/PMC4852543/):
  - Observed behaviour in three 8-minute videotaped home discussions: one problem-solving task and two in which each spouse talked about something they wanted to change about themselves.
  - 16 coders scored them with the Iowa Family Interaction Rating Scales, reduced to three factors:
    - positivity, which includes warmth/support, physical affection and endearment;
    - negativity;
    - effectiveness.
  - Satisfaction was an 8-item, interviewer-administered self-report (mean α ≈ .75–.77).
- **Key results, 9-month lags** — [PMC4852543](https://pmc.ncbi.nlm.nih.gov/articles/PMC4852543/):

  | Behaviour | Satisfaction → behaviour | Behaviour → satisfaction |
  |---|---|---|
  | Positivity | 6 of 12 lags significant (median abs. β = .10) | 2 of 12 (median abs. β = .02) |
  | Negativity | 5 of 12 (median abs. β = .09) | 4 of 12 (median abs. β = .06) |
  | Effectiveness | 3 of 12 significant *or marginal* (median abs. β = .08) | 1 of 12 (median abs. β = .05) |

  - Communication predicted later satisfaction in 7 of 36 tests. Satisfaction predicted later communication in "twice as many" cases, a count that includes marginal effectiveness paths.
  - The two directions did not differ significantly in 85% of direct comparisons. Of the 7 that differed, 6 favoured satisfaction → communication.
- **Key results, longer lag (Wave 1 to 4)** — [PMC4852543](https://pmc.ncbi.nlm.nih.gov/articles/PMC4852543/):
  - Satisfaction predicted communication in 6 of 12 tests (median abs. β = .10); communication predicted satisfaction in 0 of 12 (median abs. β = .01).
  - The two directions did not differ significantly in any of the 12 comparisons.
  - Zero-order correlations: 10 of 12 satisfaction → behaviour correlations were significant, against 3 of 12 behaviour → satisfaction.
- **Authors' conclusion.** Satisfaction was the more consistent and stronger predictor of communication than the reverse, but both effects were fairly inconsistent and similar in size — [PMC4852543](https://pmc.ncbi.nlm.nih.gov/articles/PMC4852543/).
- **Causation.** Cross-lagged models give temporal order and control for prior levels. The authors note that the stability paths capture rank-order stability, not within-person change — [PMC4852543](https://pmc.ncbi.nlm.nih.gov/articles/PMC4852543/). Third variables such as stress or personality, which the authors raise, are not modelled.
- **Limitations the authors state** — [PMC4852543](https://pmc.ncbi.nlm.nih.gov/articles/PMC4852543/):
  - generalizability beyond low-income, ethnically diverse, first-married newlyweds in their first 3 years;
  - structured tasks may not capture everyday interaction;
  - self-reported communication might behave differently;
  - satisfaction was more stable than communication, which they checked with the zero-order correlations.
- **Verdict.**
  - The sentence at `paper/03-literature-review.md:88` is **supported**.
  - "Less causally" in the heading (`paper/03-literature-review.md:86`) is **an overreach**: few significant lagged paths show weak prediction, not that causal effects are absent.
  - Summaries of the form "satisfaction predicted later communication more consistently (only 7 of 36 communication→satisfaction paths)" are accurate only with the caveat that 85% of direct comparisons were non-significant.

### Inferences
- The study touches the translation thesis directly: observed positivity, which includes expressed affection, warmth and endearment, almost never predicted the partner's or one's own later satisfaction (2 of 12 lags, median abs. β = .02). That is weak evidence that affection expressed in structured tasks does not, by itself, drive later satisfaction. The tasks were not everyday expressions of love.
- With the authors' caveats, the findings fit "satisfaction and communication travel together" better than "communication drives satisfaction". They cannot rule out short-lag causal effects. The 9-month gaps may simply be the wrong timescale.
- Proposed wording: "In 431 low-income newlywed couples observed four times over three years, observed communication rarely predicted later satisfaction (7 of 36 lagged paths), while satisfaction predicted later communication about twice as often. Most direct comparisons of the two directions were not significant, and the authors judged both pathways weak and inconsistent (Lavner, Karney & Bradbury 2016) [Moderate]." Change the heading to something like "Communication predicts later satisfaction weakly and inconsistently".
- **Grade.** **Moderate** for Lavner alone: one sample, strong observational measures, mostly null lags. The paragraph's tag "Established to Moderate" stands or falls with Johnson et al. (2022), which this audit did not check.

### Gaps
- Coefficient-level values and confidence intervals for each path (Tables 3–6) were not extracted. No within-couple (random-intercept) reanalysis exists for this sample, as far as this audit checked.

## C13. Flicker, Sancier-Barbosa & Impett (2025), with Flicker & Sancier-Barbosa (2025): love languages

### Takeaway
At abstract level, the paper reports the preregistered study correctly. Fewer than half of participants had an *identifiable* primary love language. Satisfaction with how the partner enacted one's primary language predicted relationship quality no better than satisfaction with other loving behaviours. Two uses go further than the study. "Matching null" and "fewer than half have a primary channel" drop qualifiers. And the result is used against translation, although the study found that relationship quality tracked satisfaction across a *wide range* of loving behaviours, which is compatible with a broad translation view. The full text could not be accessed.

### Cited Findings
- **How the paper uses it.**
  - "No special role for one's 'primary love language' in a pre-registered test", within the verdict that channel matching adds little — `paper/01-question-and-thesis.md:17`.
  - "In a pre-registered study of 499 cohabiting US adults, fewer than half had an identifiable primary language. Satisfaction… predicted relationship quality no better than satisfaction with other loving behaviours" — `paper/03-literature-review.md:113-114`.
  - Evidence table: "Primary love language and matching are unsupported | Moderate/mixed (null) | Cross-sectional, US-dominated" — `paper/03-literature-review.md:149`.
  - "Fewer than half have a primary channel; 5 factors not stable; matching null | Pre-registered null… | Preliminary; core claims largely unsupported" — `paper/06-competing-theories.md:18`.
  - "Channel matching adds little" — `README.md:50`.
  - The companion papers appear at `paper/03-literature-review.md:115-116` and `paper/17-what-testing-requires.md:30`.
- **Access: abstract only.**
  - Unpaywall reports jmft.70078 as closed. Wiley served a bot challenge.
  - The Sacramento State repository record has no file and no preregistration link — [CSUS record](https://scholars.csus.edu/esploro/outputs/journalArticle/Revisiting-the-Five-Love-Languages-Framework/99258257297001671).
  - Web searches found no OSF preregistration or preprint.
  - The abstract was read via [PubMed 40977357](https://pubmed.ncbi.nlm.nih.gov/40977357/) and Crossref.
  - For jmft.12747, Unpaywall lists a free publisher PDF, but Wiley returned a bot challenge, so only the abstract was read — [PubMed 39420529](https://pubmed.ncbi.nlm.nih.gov/39420529/).
- **What the 2025 abstract says** (paraphrased) — [PubMed 40977357](https://pubmed.ncbi.nlm.nih.gov/40977357/):
  - The study was preregistered, with N = 499 individuals in long-term cohabiting relationships.
  - It tested whether having a primary love language, and receiving love that way, predicted relationship quality and perceived partner love.
  - Fewer than half had an identifiable primary language.
  - Satisfaction with the partner's expression of that language was no stronger a predictor of quality than satisfaction with other love-language behaviours.
  - Quality was more strongly tied to satisfaction across a wider range of loving behaviours.
  - The robust predictors were verbal affirmations, encouragement for individual pursuits, support during difficult times and accountability. Three of these four are not among Chapman's five, which implies an expanded behaviour inventory.
- **Country and sample.** The 2025 abstract does not state the country. The companion bottom-up paper reports three studies of US residents with N = 696, 500 and 499 — [PubMed/Europe PMC 40916580](https://pubmed.ncbi.nlm.nih.gov/40916580/). The earlier test recruited n = 696 through Amazon CloudResearch (mean age 43.8; 70% married; 97.3% cohabiting). In it, satisfaction with the partner's primary-language behaviour predicted relationship satisfaction and perceived love no better than lower-ranked languages. Words of Affirmation and Quality Time predicted better than participants' own primary language — [PubMed 39420529](https://pubmed.ncbi.nlm.nih.gov/39420529/).
- **Design and causation.** From the abstracts, these are cross-sectional, single-informant, self-report online surveys. Nothing identifies causation.
- **Verdict.**
  - Wording at `paper/03-literature-review.md:114` and `paper/01-question-and-thesis.md:17`: **supported** at abstract level. "US" is supported only indirectly, through the companion abstract.
  - `paper/06-competing-theories.md:18`: **slightly overstated.**
    - "Fewer than half have a primary channel" drops "identifiable", and identifiability depends on the authors' classification rule.
    - "Matching null" misdescribes the result. What was null is the *extra* predictive value of the primary channel; satisfaction with the partner's loving behaviours still predicted quality.
  - Overall: **qualified**.

### Inferences
- The measure is the *receiver's* satisfaction with the partner's behaviour in each channel, not an observed match between how the giver expresses love and how the receiver prefers to receive it. The study tests the special status of one "primary" channel, not dyadic matching as such.
- The positive finding, that quality tracks satisfaction with many loving behaviours, fits a broad translation account in which love must be received in forms the person values. It also fits an amount account in which more perceived love means higher quality. Because it is cross-sectional and same-source, it cannot tell them apart. The paper should not use it as evidence that amount beats translation, only as evidence against the five-languages "primary channel" premise.
- The samples behind the 2024/2025 tests probably overlap (N = 696 and 499 recur across the companion papers). Treat them as about two US online samples from one team, not independent replications. The repository's own notes flag the same point (`evidence/notes/03-love-needs-compatibility.md:118`).
- Proposed wording for `paper/06-competing-theories.md:18`: "Fewer than half had an identifiable primary language under the authors' classification. Satisfaction with one's primary channel predicted quality no better than satisfaction with other channels (pre-registered)."
- **Grade.** **Moderate**, as a null for the distinctive primary-language claim. Align the inconsistent tags: "Moderate/mixed (null)" at `paper/03-literature-review.md:149` versus "Preliminary" at `paper/06-competing-theories.md:18`. The latter seems to grade the theory rather than the evidence against it, and should say so.

### Gaps
- Not verifiable without the full text: the rule for an "identifiable" primary language, the measures (behaviour inventory, relationship-quality and perceived-love scales), effect sizes and confidence intervals, how predictors were compared, power to detect differences between correlated predictors, the preregistration link and any deviations, recruitment platform and country for the N = 499 sample, and how far the samples overlap.

## C14. Neff, Nguyen & Williamson (2021): does stress limit acting on a partner's noticed needs?

### Takeaway
The study's result is narrower than the model's use of it. Husbands under higher *chronic* stress tracked their wives' daily support needs less closely, though still significantly. On days of higher *daily* stress, husbands who perceived a need reported giving somewhat less support. Chronic stress did not weaken the link from a noticed need to support. Effects appeared only for husbands, and the gender differences were not significant. `paper/04-evidence-for-the-intuition.md:59` reports this correctly. Chapter 8 and the README overstate it as stress "blocking" support, husbands "failing to act" and evidence of "bounds".

### Cited Findings
- **How the paper uses it.**
  - Accurate: "Husbands under chronic stress were less accurate… Even when they noticed a need, they were less likely to act on it on days they were coping with their own stress" [Moderate/mixed] — `paper/04-evidence-for-the-intuition.md:59`.
  - Verdict table — `paper/01-question-and-thesis.md:13`.
  - Theory table — `paper/06-competing-theories.md:37`.
  - Type 4, "capacity-limited care: … Intention high, enactment low" — `paper/07-revised-model.md:66`.
  - Model table row "Stress limits acting on needs that were noticed" [Moderate/mixed] — `paper/08-mathematical-representation.md:32` and `README.md:121`.
  - "The constraint form is appropriate because the evidence describes *bounds*, not trade-off weights. Stressed husbands failed to act on needs they had noticed" — `paper/08-mathematical-representation.md:150`.
  - "Stress blocks enactment" — `paper/08-mathematical-representation.md:311`.
  - "Stress blocks enactment of noticed needs" — `README.md:46`.
  - Romantic-partner vignette — `paper/11-romantic-partner-example.md:10`.
  - A partner "too stressed to act on a noticed need, delivers less care than they feel" — `paper/19b-is-love-enough.md:5`.
- **Access: full text.** The authors' accepted manuscript (42 pages, marked as not the copy of record) is on the authors' lab site — [author manuscript](https://sites.utexas.edu/realproject/files/2024/11/too_stressed_to_help.pdf); [PubMed 33342361](https://pubmed.ncbi.nlm.nih.gov/33342361/). I read every section, Tables 1–4 and the figure panels. The supplementary materials (Truth-and-Bias and daily-hassles analyses) were not read, only their footnote summaries.
- **Design.** A 14-day daily diary at the 2-year follow-up of a longitudinal study of newlyweds, analysed with dyadic multilevel models (HLM 7, dual intercept). Daily variables were centred within persons, and chronic stress entered at the couple level — [author manuscript](https://sites.utexas.edu/realproject/files/2024/11/too_stressed_to_help.pdf).
- **Population** — [author manuscript](https://sites.utexas.edu/realproject/files/2024/11/too_stressed_to_help.pdf):
  - 171 first-married, childless newlywed couples recruited from January 2010 through newspapers, premarital counselling offices, wedding vendors and websites. The text does not name the location; the authors are at UT Austin.
  - 121 couples took part in the diary wave; 13 had divorced or separated, and 37 declined.
  - About 78% of husbands and 75% of wives were White, and most held bachelor's degrees.
  - The authors describe the couples as relatively happy. Diary non-participants had less education.
- **What was measured.** All measures are self-reports — [author manuscript](https://sites.utexas.edu/realproject/files/2024/11/too_stressed_to_help.pdf):
  - chronic stress: a modified UCLA Life Stress Interview, 12 non-marital life domains rated on a 9-point scale for the past 7 months;
  - daily stress: one 5-point item;
  - perceived partner need: one 7-point item;
  - own need: one 7-point item;
  - own support provision: one 7-point item.

  "Accuracy" is the within-person slope of perceived partner need on the partner's self-reported need, adjusting for one's own need. Support provision is the provider's own report, not the recipient's.
- **Key results, noticing** — [author manuscript](https://sites.utexas.edu/realproject/files/2024/11/too_stressed_to_help.pdf):
  - Spouses tracked each other's daily needs (b = .31 for both). They also showed assumed similarity, projecting their own need (b = .21 for husbands, .18 for wives).
  - Daily stress did not moderate accuracy for either spouse.
  - Chronic stress moderated husbands' accuracy (b = −.05, p ≈ .001) but not wives' (b = .02, p = .573). The gender difference was not significant (χ² = 3.34, p = .06).
  - Simple slopes for husbands: tracking b = .38 [.30, .46] at low chronic stress versus .24 [.18, .30] at high chronic stress. Tracking was weaker under chronic stress but still significant.
- **Key results, providing support** — [author manuscript](https://sites.utexas.edu/realproject/files/2024/11/too_stressed_to_help.pdf):
  - Perceived need strongly predicted reported support (b = .77 for husbands, .84 for wives).
  - Higher chronic stress went with less support on average (husbands b = −.14, p = .002; wives b = −.10, p = .055).
  - Chronic stress did **not** moderate the need → support link (husbands b = −.03, p = .100).
  - Daily stress did, for husbands (b = −.05, p = .011) but not wives (b = −.001, p = .972). The gender difference was not significant (χ² = 2.91, p = .08).
  - On days husbands perceived high need, higher daily stress went with less support: b = −.15 [−.23, −.07] per scale point on a 7-point outcome.
  - The need → support slope was .81 [.75, .87] on low-stress days and .72 [.66, .78] on high-stress days. It was weaker under stress but still strongly positive.
- **Limitations the authors state** — [author manuscript](https://sites.utexas.edu/realproject/files/2024/11/too_stressed_to_help.pdf):
  - a relatively happy early-marriage sample, with the most distressed couples already lost;
  - single-item measures;
  - no information on how needs were signalled or what type of support was given;
  - the support item directly followed the perceived-need item, a possible demand effect;
  - gender inferences are tentative.
- **Causation.** Within-person, observational and same-reporter. Stress was not manipulated, and stress, perceived need and support were reported the same evening, so their order within the day is unknown.
- **Verdict.**
  - `paper/04-evidence-for-the-intuition.md:59` and `paper/01-question-and-thesis.md:13`: **supported**.
  - **Overstated:**
    - `paper/08-mathematical-representation.md:150`: "failed to act". The study shows a modest, graded weakening, and it cannot tell a constraint (bound) apart from a trade-off.
    - `paper/08-mathematical-representation.md:311` and `README.md:46`: "blocks".
    - `paper/07-revised-model.md:66`: "intention high". Intention was not measured; perceived need was.
    - `paper/19b-is-love-enough.md:5`: "less care than they feel". Neither feelings nor the recipient's experience were measured.
  - Any summary saying that *chronically* stressed husbands gave less support even on days they noticed the need conflates the two findings. That effect was for *daily* stress. Chronic stress did not moderate it.

### Inferences
- A weaker but still strongly positive need → support slope (.81 versus .72) is better described as "stress dampens enactment" than as a feasibility bound. The data are equally consistent with a trade-off weight on the giver's own resources. Choosing the constraint form in §8.4 is therefore a modelling assumption, not something the evidence supports.
- Because both the perceived need and the support were reported by the provider, the study does not show that the wives *received* or *perceived* less support. A link to the paper's "intended → expressed" stage holds only if self-reported provision is taken as a stand-in for enactment.
- Proposed wording for `paper/08-mathematical-representation.md:150`: "On days of higher non-marital stress, husbands who perceived that their wives needed support reported giving somewhat less support than on calmer days (Neff, Nguyen & Williamson 2021) [Preliminary]. This is a graded weakening, not a hard bound. The constraint form is a modelling assumption." Replace "blocks" with "dampens" in `README.md:46` and `paper/08-mathematical-representation.md:311`.
- **Grade.** **Preliminary** for the specific mechanism, stress weakening the enactment of noticed needs: one sample of 121 couples, effects in husbands only with non-significant gender differences, single-item self-reports. The current tag is [Moderate/mixed]. Keep it only if pooled with other verified stress-and-support studies.

### Gaps
- The supplementary analyses (Truth-and-Bias accuracy, daily-hassles results and the differences the authors mention), recipient-reported support and replications were not checked. Whether the OSF protocol (osf.io/wtdsg) includes a preregistration was not checked.

## C15. Hou, Benner, Kim et al. (2020): agreement between parents' and adolescents' reports of parenting

### Takeaway
The pooled numbers are exactly right: agreement r = .276 [.262, .290], and parents more positive by g = .242 [.188, .296]. The paper misuses the source in one place. It co-cites Hou for an age trend, children's reports of acceptance falling further below parents' and reaching g ≈ −.50 by age 14. Hou found no age effect on mean gaps; that result comes only from Korelitz & Garber (2016). Hou also gives no support to a father-specific or father–daughter-specific gap. Parent gender and parent × child gender had no significant effect, and girls agreed with parents more than boys did. The paper does not cite Hou in the father–daughter chapter, which is correct.

### Cited Findings
- **How the paper uses it.**
  - Evidence table: "Parent–child report gaps are real but small | Established | … (g ≈ .24) | Parenting reports, not care adequacy" — `paper/03-literature-review.md:152`.
  - "Across 313 studies, parents described their parenting more positively than adolescents did (g = .24). Children's reports of acceptance fall further below parents' as they age, reaching g ≈ −.50 by age 14 and over for both mothers and fathers (Hou et al. 2020; Korelitz & Garber 2016)" [Established] — `paper/04-evidence-for-the-intuition.md:20`. This sits in a list next to father-specific findings at lines 18–19.
  - "Published mean-level gaps are far smaller: g ≈ .24…", contrasted with the brief's illustrative 90-versus-40 gap — `paper/05-evidence-against-it.md:46`.
  - "Discordance about parenting is *higher* in more individualistic societies such as the US" — `paper/12-asymmetry-and-misperception.md:41`.
  - Not cited in `paper/10-father-daughter-example.md` (grep).
- **Access: full text.** The NIH author manuscript, [PMC10624508](https://pmc.ncbi.nlm.nih.gov/articles/PMC10624508/), via NCBI E-utilities. I read every section, and Tables 1–5 were extracted from the XML. The supplementary Tables S1–S6 were not read.
- **Design** — [PMC10624508](https://pmc.ncbi.nlm.nih.gov/articles/PMC10624508/):
  - A meta-analysis of studies with parent and adolescent (aged 10–20) reports of the same parenting construct at the same wave.
  - Searched PsycINFO and ProQuest dissertations through September 2016, with supplementary searches up to October 2017.
  - 313 articles entered the meta-analysis (93 of them through data obtained from authors). 36 more were reviewed qualitatively for links between disagreement and adolescent outcomes.
  - Analysis used robust variance estimation (robumeta) with small-sample corrections and moderator meta-regressions.
- **What was measured.** Two quantities — [PMC10624508](https://pmc.ncbi.nlm.nih.gov/articles/PMC10624508/):
  - (a) the correlation between parent and adolescent reports;
  - (b) the mean difference (Hedges' g), computed with the repeated-measures formula that uses the pooled r = .276. Negative constructs were reverse-signed so that positive g means parents report more positively.

  Five dimensions were covered: warmth, behavioural control, psychological control, relationship quality and family functioning.
- **Key results** — [PMC10624508](https://pmc.ncbi.nlm.nih.gov/articles/PMC10624508/):
  - Agreement r = .276 [.262, .290] (280 studies, 934 effect sizes).
  - Mean gap g = .242 [.188, .296] (221 studies, 808 effect sizes).
  - Heterogeneity: I² = 91.5% for r and 98.4% for g.
  - The funnel plot for g was asymmetric, but the effect stayed significant after trim-and-fill. Published versus unpublished made no significant difference.
- **Moderators of agreement (r)** — [PMC10624508](https://pmc.ncbi.nlm.nih.gov/articles/PMC10624508/):
  - Higher for relationship quality (r = .318).
  - Higher in mid-to-late than early adolescence (.341 versus .205).
  - Higher with more girls in the sample.
  - Higher in predominantly White samples (.302 versus .242).
  - Higher in high-SES and intact families, in US samples only.
  - Lower in the US than elsewhere (.265 versus .306), and lower with higher national individualism.
- **Moderators of the mean gap (g)** — [PMC10624508](https://pmc.ncbi.nlm.nih.gov/articles/PMC10624508/):
  - Only parental clinical status mattered: g = .287 for non-clinical parents versus .031 for parents with internalizing symptoms.
  - No effect of age: mean-age b = .001; early versus later adolescence b = −.113, not significant.
  - No effect of individualism (p = .171) or of US versus non-US (p = .531).
  - No effect of parent gender (b = .027, p = .591) or of parent × adolescent gender (b = −.071, p = .559, about 17 degrees of freedom). The authors note that mother–adolescent and father–adolescent disagreement were similar.
- **Where the age-14 figure actually comes from.** Korelitz & Garber (2016), a meta-analysis of 85 studies using the Children's Report of Parental Behavior Inventory (children of all ages). Children's reports of maternal and paternal acceptance were g = −.50 below parents' in samples with mean age 14 or older. There was no or a small gap at younger ages. The overall directional gap for acceptance was g = −.21 for mothers and −.25 for fathers; the absolute gap was g = .47 for mothers and .36 for fathers — [PMC5222679](https://pmc.ncbi.nlm.nih.gov/articles/PMC5222679/).
- **Limitations the authors state** — [PMC10624508](https://pmc.ncbi.nlm.nih.gov/articles/PMC10624508/):
  - retrieval is necessarily incomplete;
  - about half of eligible articles lacked usable statistics;
  - links between disagreement and outcomes could only be reviewed qualitatively;
  - few studies test why parents and adolescents disagree.
- **Verdict.**
  - `paper/03-literature-review.md:152` and `paper/05-evidence-against-it.md:46`, for the mean gap: **supported**.
  - `paper/04-evidence-for-the-intuition.md:20`, the age clause attributed to Hou: **not supported by Hou**. It is supported by Korelitz & Garber. Also, the g = .24 comes from 221 studies, not 313.
  - `paper/12-asymmetry-and-misperception.md:41`: **qualified**. It holds for agreement (correlations) but not for mean gaps.
  - Father–daughter asymmetry: **not supported** by Hou.
  - Overall: **qualified**.

### Inferences
- "Small" describes the *average directional* gap. Agreement between individual parents and adolescents is low (r ≈ .28), and Korelitz & Garber's absolute gaps (g ≈ .36–.64) are larger than the directional ones. Disagreement within a given dyad is therefore common even though the average gap is small. The heading "Gaps are smaller than the hypothesis implies" (`paper/05-evidence-against-it.md:44`) compares a population average with a single illustrative dyad.
- My own calculation, assuming normality and equal SDs. Hou's g is scaled by the SD of difference scores (about 1.20 raw SDs when r = .276), so g = .242 is about .29 raw SDs. Under those assumptions, about 3% of dyads would show a parent-favouring gap of 2.5 raw SDs or more. The paper's conclusion still holds, that a gap like the brief's 90 versus 40 would be unusual, but it should compare quantities on the same scale.
- In Hou's data, collectivistic societies show more agreement. For the Korean father–daughter example, this argues against assuming a larger-than-average reporting gap. It does not show one.
- Proposed wording for `paper/04-evidence-for-the-intuition.md:20`: "Across 221 studies with mean-level data (from a meta-analysis of 313), parents rated their parenting slightly more positively than adolescents did (g = .24), and agreement was low (r = .28) (Hou et al. 2020). Neither gap differed between mothers and fathers. In a separate meta-analysis of one widely used measure, children's reports of acceptance fell below parents' mainly in samples aged 14 and over (g ≈ −.50 for both mothers and fathers) (Korelitz & Garber 2016)."
- **Grade.** Keep **Established** for the pooled estimates, noting the very high heterogeneity, the funnel asymmetry for g, and that these are parenting reports, not care adequacy, in adolescents aged 10–20.

### Gaps
- The supplementary tables (study list, Asian or Korean samples, effect sizes per study) were not read. Neither meta-analysis tests mechanisms such as the generational-stake versus family-dysfunction explanations, or adult children.

## Cross-claim verdicts and recommended tag changes

### Takeaway
None of the five citations is fabricated, and every number checked in an accessible source matches. Two sources could not be read in full: Le et al. (2010) and Flicker et al. (2025). The recurring problem is scope and mechanism creep: claims are pushed beyond what the studies measured.
- Neff's graded stress effect becomes a feasibility "bound".
- Hou is cited for an age trend it does not show.
- Le's self-reported love is used to adjudicate amount versus translation.
- Lavner's weak lagged effects become "less causal".
- Flicker's null on the primary channel becomes "matching null".

### Cited Findings
| Claim | Verification depth | Verdict | Current tag | Recommended tag |
|---|---|---|---|---|
| C11 Le et al. 2010 | Abstract ([OpenAlex](https://api.openalex.org/works/doi:10.1111/j.1475-6811.2010.01285.x)) plus secondary effect sizes | Supported with qualifications | Established | Established for non-marital persistence only; indirect (Moderate at best) as evidence against translation |
| C12 Lavner et al. 2016 | Full text ([PMC4852543](https://pmc.ncbi.nlm.nih.gov/articles/PMC4852543/)) | Sentence supported; "less causally" an overreach | Established to Moderate (shared) | Moderate (for Lavner) |
| C13 Flicker et al. 2025 | Abstract ([PubMed](https://pubmed.ncbi.nlm.nih.gov/40977357/)) | Supported with qualifications; slightly overstated at 06:18 | Moderate/mixed (03:149); Preliminary (06:18) | Moderate (null on the distinctive claim); make the tags consistent |
| C14 Neff et al. 2021 | Full text, author manuscript ([lab PDF](https://sites.utexas.edu/realproject/files/2024/11/too_stressed_to_help.pdf)) | Accurate in ch. 4; overstated in ch. 7, 8, 19b and the README | Moderate/mixed | Preliminary |
| C15 Hou et al. 2020 | Full text ([PMC10624508](https://pmc.ncbi.nlm.nih.gov/articles/PMC10624508/)) | Supported with qualifications; age clause misattributed | Established | Established for pooled estimates; credit the age clause to Korelitz & Garber |

### Inferences
- For the paper's central "amount versus translation" verdict, the evidence audited here supports "amount matters" (C11) and "the primary-language mechanism fails" (C13). Neither study tests whether expressed love is lost in transmission. The verdict "not supported as a general claim" at `paper/01-question-and-thesis.md:17` is defensible only as "the comparative 'rather than' is unsupported", not as evidence that translation failures are rare.
- The audit found no case where a source contradicts the direction of a claim. The problems are scope (non-marital to all relationships; parenting reports to care adequacy), mechanism (graded effects described as bounds or blocks) and attribution (the age clause).

### Gaps
- Full texts of Le et al. (2010) and Flicker et al. (2025, jmft.70078) are needed to verify effect sizes, how love and "identifiable primary language" were measured, the preregistration, and the authors' stated limitations.
- Johnson et al. (2022) and Korelitz & Garber (2016) were checked only as far as each claim needed. The K&G age result was verified from full text; Johnson et al. was not audited.
- Literature coverage is not exhaustive, and no replication searches were run beyond the sources named.

```jsonl
{"claim_id": "C11", "short_claim": "Love, commitment, IOS and dependence are among the strongest predictors of non-marital break-up; used as main evidence that the amount of love matters", "source": "Le, Dove, Agnew, Korn & Mutso (2010), Personal Relationships 17(3), 377-390", "doi": "10.1111/j.1475-6811.2010.01285.x", "verification_depth": "abstract", "sections_read": "Abstract only (via OpenAlex). Full text closed: Unpaywall/OpenAlex/Semantic Scholar list no open copy; Wiley and ResearchGate returned HTTP 403; CORE copy behind a bot challenge (not bypassed); Haverford repository has a record only. Effect sizes from secondary citation contexts (Semantic Scholar citations API) and Barrantes et al. 2017 (PMC5501283).", "design": "Meta-analysis of predictors of non-marital romantic relationship dissolution (individual, relationship and external predictors); predictors measured before break-up status, per secondary description", "population": "137 studies, 37,761 participants, 33 years; non-marital romantic couples; 96% heterosexual (Barrantes et al. 2017); country and student share not verified", "measured": "Predictors including commitment, love, IOS, dependence, satisfaction, alternatives, investments, trust, positive illusions, social network support, personality and attachment; outcome = dissolution versus persistence; love coded separately from satisfaction and commitment; love instruments not verified", "key_result": "Abstract: commitment, love, IOS and dependence among the strongest predictors; satisfaction, alternatives and investments modest; network support robust; personality limited. Secondary: strongest predictors d = .57-.85 (positive illusions, commitment, love); commitment d = 0.80; trust d = -.57; attachment d = 0.14-0.24; positive illusions reportedly strongest. Exact d for love not verified.", "supports_interpretation": "qualified", "evidence_grade": "Established (narrow: own reported love and commitment predict non-marital persistence); indirect, Moderate at best, as evidence against translation", "paper_locations": ["paper/01-question-and-thesis.md:17", "paper/03-literature-review.md:84", "paper/03-literature-review.md:146", "paper/05-evidence-against-it.md:7", "paper/07-revised-model.md:62", "paper/19b-is-love-enough.md:11", "README.md:50"], "recommended_change": "Specify that love was each person's own self-reported love, that the outcome was dissolution, and that the samples were non-marital (96% heterosexual). Say the study does not test translation. Change 'relationships' to 'non-marital romantic relationships' in 19b:11. Label its use for parent-child amount deficits (07:62) as an extrapolation. Keep Established only for the narrow claim.", "notes": "Predictors overlap (commitment-satisfaction r about .68), so love's effect is not independent of commitment. Positive illusions (a perception variable) reportedly strongest; check in full text. 'Mostly WEIRD' plausible but unverified."}
{"claim_id": "C12", "short_claim": "Communication and satisfaction lagged paths both exist but neither is robust; satisfaction predicts later communication more consistently than the reverse (7 of 36 communication-to-satisfaction paths significant)", "source": "Lavner, Karney & Bradbury (2016), Journal of Marriage and Family 78(3), 680-694", "doi": "10.1111/jomf.12301", "verification_depth": "full text", "sections_read": "NIH author manuscript PMC4852543: abstract, introduction, Method (sampling, participants, procedure, behavioural observation, satisfaction), all Results subsections, Discussion and caveats; tables not separately inspected", "design": "Four-wave longitudinal observational study, about 9-month intervals over the first 3 years of marriage; cross-lagged path models (Mplus, FIML, standardized), Wald tests, Wave 1-4 models, zero-order correlations", "population": "431 first-married newlywed couples from low-income Los Angeles County neighbourhoods, sampled from 2009-2010 marriage licences; 76% Hispanic, 12% African American, 12% Caucasian; mean ages about 28 and 26", "measured": "Observed communication in three 8-minute in-home discussions (problem-solving and two support tasks) coded with IFIRS into positivity, negativity and effectiveness; 8-item self-reported marital satisfaction", "key_result": "Communication to satisfaction: 7 of 36 lags significant (positivity 2/12, median abs beta .02; negativity 4/12, .06; effectiveness 1/12, .05). Satisfaction to communication: about twice as many (6/12, 5/12, 3/12 significant or marginal). 85% of direct comparisons non-significant; 6 of the 7 that differed favoured satisfaction to communication. Wave 1-4: 0/12 versus 6/12 but no significant magnitude differences. Authors: both effects inconsistent and similar in magnitude.", "supports_interpretation": "qualified", "evidence_grade": "Moderate (single sample; strong observational measures; cross-lagged design)", "paper_locations": ["paper/03-literature-review.md:86", "paper/03-literature-review.md:88", "paper/20-bibliography.md:229"], "recommended_change": "Keep the 03:88 sentence, which is accurate. If adding '7 of 36', add that most direct comparisons were non-significant and both pathways were weak. Retitle 3.7 to drop 'less causally' (for example 'Communication predicts later satisfaction weakly and inconsistently'). Tag Lavner as Moderate.", "notes": "The '7 of 36' and 'more consistently' phrasing is not in paper/ or README (grep). The cross-lagged model captures rank-order stability, not within-person change (authors). Observed positivity includes expressed affection, which almost never predicted later satisfaction."}
{"claim_id": "C13", "short_claim": "Preregistered US study (N = 499): fewer than half have an identifiable primary love language; satisfaction with partner's enactment of the primary language predicts quality no better than other loving behaviours", "source": "Flicker, Sancier-Barbosa & Impett (2025), Journal of Marital and Family Therapy 51(4), e70078; also Flicker & Sancier-Barbosa (2025), JMFT 51(1), e12747", "doi": "10.1111/jmft.70078", "verification_depth": "abstract", "sections_read": "Abstracts of jmft.70078 (PubMed 40977357, Crossref), jmft.12747 (PubMed 39420529) and jmft.70072 (PubMed 40916580). Full texts closed or blocked (Wiley bot challenge); CSUS repository record has no file; no OSF preregistration or preprint found", "design": "Preregistered cross-sectional online survey (from abstract); single-informant self-report", "population": "499 individuals in long-term cohabiting relationships; US residence stated only in the companion jmft.70072 abstract (studies N = 696, 500, 499), so likely US and possibly a shared sample. Companion test: n = 696 via Amazon CloudResearch, mean age 43.8, 70% married, 97.3% cohabiting", "measured": "Having an identifiable primary love language; satisfaction with partner's expression of each love-language behaviour (expanded inventory); relationship quality; perceived partner love. Exact scales and classification rule not verified", "key_result": "Fewer than half had an identifiable primary love language; satisfaction with partner's primary-language behaviour was no stronger a predictor of relationship quality than satisfaction with other behaviours; quality more strongly linked to satisfaction across a wider range of behaviours; robust predictors: verbal affirmations, encouragement for individual pursuits, support during difficult times, accountability. Effect sizes not available.", "supports_interpretation": "qualified", "evidence_grade": "Moderate (null on the distinctive primary-language claim; two US online samples from one team, likely overlapping; one preregistered; cross-sectional)", "paper_locations": ["paper/01-question-and-thesis.md:17", "paper/03-literature-review.md:113", "paper/03-literature-review.md:114", "paper/03-literature-review.md:149", "paper/06-competing-theories.md:18", "README.md:50"], "recommended_change": "Keep the 03:114 wording. At 06:18, write 'fewer than half had an identifiable primary language under the authors' classification' and replace 'matching null' with 'the primary channel carried no extra predictive weight'. Make the tags consistent (03:149 Moderate/mixed versus 06:18 Preliminary). Do not use the study as evidence for amount over translation: quality tracked satisfaction across many loving behaviours.", "notes": "The measure is the receiver's satisfaction with partner behaviours, not observed giver-receiver matching. Cross-sectional, same-source data cannot separate amount from translation. Country verified only indirectly. Primary-language classification rule unknown."}
{"claim_id": "C14", "short_claim": "In a diary study of 121 couples, stressed husbands tracked wives' support needs less accurately and gave less support even on days they noticed the need (capacity limits enactment)", "source": "Neff, Nguyen & Williamson (2021), Personality and Social Psychology Bulletin 47(11), 1565-1579", "doi": "10.1177/0146167220974490", "verification_depth": "full text", "sections_read": "Authors' accepted manuscript (42 pp., not the copy of record) from the UT Austin lab site: abstract, introduction, Method, Results, Discussion, limitations, Tables 1-4, figure panels; supplementary materials not read", "design": "14-day daily diary at the 2-year follow-up of a newlywed panel; dyadic multilevel models (HLM 7, dual intercept); daily predictors centred within persons; chronic stress at Level 2", "population": "121 married couples (of 171 first-married, childless newlyweds recruited from January 2010 via newspapers, counsellors, wedding vendors, websites); about 75-78% White, mostly bachelor's degrees, relatively happy; location not stated (authors at UT Austin)", "measured": "Chronic non-marital stress (modified UCLA Life Stress Interview, 12 domains); daily stress (1 item); perceived partner need, own need and own support provision (single 7-point self-report items); accuracy = within-person slope of perceived on partner-reported need", "key_result": "Chronic stress reduced husbands' tracking accuracy (b = -.05, p about .001; slope .38 to .24, still significant), not wives' (gender difference p = .06). Daily stress did not affect accuracy. Chronic stress lowered average support (husbands b = -.14, p = .002) but did not moderate need-to-support. Daily stress moderated need-to-support for husbands only (b = -.05, p = .011; gender difference p = .08): on high-need days, b = -.15 [-.23, -.07]; slope .81 to .72, still strongly positive.", "supports_interpretation": "overstated", "evidence_grade": "Preliminary (single sample; husband-only effects with non-significant gender differences; single-item provider self-reports)", "paper_locations": ["paper/01-question-and-thesis.md:13", "paper/04-evidence-for-the-intuition.md:59", "paper/06-competing-theories.md:37", "paper/07-revised-model.md:66", "paper/08-mathematical-representation.md:32", "paper/08-mathematical-representation.md:150", "paper/08-mathematical-representation.md:311", "paper/11-romantic-partner-example.md:10", "paper/19b-is-love-enough.md:5", "README.md:46", "README.md:121"], "recommended_change": "Keep 04:59, which is accurate. Replace 'failed to act' (08:150) and 'blocks' (08:311, README:46) with 'reported somewhat less support on high-stress days'. State that the evidence shows graded weakening, not bounds, so the constraint form is an assumption. Remove 'intention high' as a measured signature (07:66) and 'than they feel' (19b:5). Downgrade the tag to Preliminary.", "notes": "The 'even when noticed' effect was daily stress, not chronic stress; summaries crediting chronic stress conflate the findings. Support was self-reported by the provider; recipients' receipt or perception was not the outcome. The authors flag a possible demand effect from adjacent items."}
{"claim_id": "C15", "short_claim": "Meta-analysis of parent and adolescent reports of parenting: agreement r = .276; parents report more positive parenting (g = .242); used for giver-receiver and father-daughter asymmetry", "source": "Hou, Benner, Kim, Chen, Spitz, Shi & Beretvas (2020), American Psychologist 75(3), 329-348", "doi": "10.1037/amp0000463", "verification_depth": "full text", "sections_read": "NIH author manuscript PMC10624508: all sections; Tables 1-5 from XML; supplementary Tables S1-S6 not read. Also Korelitz & Garber 2016 full text (PMC5222679), searched for age and parent-sex results", "design": "Meta-analysis with robust variance estimation of cross-informant correlations and mean differences (repeated-measures Hedges' g using pooled r), moderator meta-regressions, plus qualitative review of 36 outcome studies; literature through September 2016 (supplementary searches to October 2017)", "population": "313 articles with parent and adolescent (aged 10-20) reports of the same parenting construct; r from 280 studies (934 effect sizes), g from 221 studies (808 effect sizes); international, US-heavy", "measured": "Parent- versus adolescent-reported warmth, behavioural control, psychological control, relationship quality, family functioning; agreement (r) and directional mean gap (g, positive = parents more positive)", "key_result": "r = .276 [.262, .290]; g = .242 [.188, .296]; I-squared 91.5% (r) and 98.4% (g); funnel asymmetry for g but trim-and-fill significant. Agreement higher in older adolescents, girls, White, high-SES and intact US families, and non-US or collectivistic samples. Mean gap moderated only by parental internalizing symptoms; no age, individualism, parent-gender (p = .591) or parent x adolescent gender (p = .559) effect.", "supports_interpretation": "qualified", "evidence_grade": "Established (pooled estimates; parenting reports, not care adequacy)", "paper_locations": ["paper/03-literature-review.md:152", "paper/04-evidence-for-the-intuition.md:20", "paper/05-evidence-against-it.md:46", "paper/12-asymmetry-and-misperception.md:41"], "recommended_change": "At 04:20, credit the age clause (g about -.50 at age 14 and over, mothers and fathers) to Korelitz & Garber 2016 only; Hou found no age effect on mean gaps. Say g = .24 comes from 221 studies (of 313) and add low agreement (r = .28). At 12:41, say agreement (correlation) is lower in individualistic societies; the mean gap did not differ. Do not use Hou for a father-specific or father-daughter-specific gap. At 05:46, compare like with like: dyad-level disagreement versus mean gap, and the change-score standardizer.", "notes": "Hou is not cited in ch. 10 (father-daughter), which is correct. Hou's g uses the SD of difference scores, about .29 raw SD. My calculation, assuming normality: about 3% of dyads would show a parent-favouring gap of 2.5 raw SD or more. Collectivistic samples showed more agreement, which argues against assuming large gaps in the Korean example."}
```
