[Overview](README.md) · **Part A: evidence audit** · [Part B: competing predictions](../protocol/competing-predictions.md) · [Part C: study protocol](../protocol/study-protocol.md) · [Corrections](corrections.md)

# Part A: Evidence audit

This part audits the empirical claims on which *Can Love Be Lost in Translation?* (version 0.2.0 of this repository, which the audit did not change) relies most heavily. The framework it supports holds that love intended ≠ love expressed ≠ love perceived ≠ love received ≠ relationship compatibility. It models these links in ten components, with a substantive and a symbolic route of effect, safety as an admissibility constraint, and autonomy as a separate outcome. Four audit passes in November 2026 compared each claim with its primary source. Sources were reached only through legitimate open routes: publisher pages, Unpaywall, OpenAlex, Semantic Scholar, Europe PMC and PMC, and author and institutional repositories. Paywalls and bot challenges were not bypassed. Each source carries a verification depth: **full text**, **abstract**, **secondary** (press or practitioner summaries only) or **inaccessible**. Grades use the paper's own scale (Established, Moderate or mixed, Preliminary, Theoretical, Our hypothesis). They are the auditors' judgement on that scale, not a consensus rating. Locations are `file:line` at the [v0.2.0 tag](https://github.com/julienaxyomlabs/love-in-translation/tree/v0.2.0).

## How the twenty claims were chosen, and what the audit leaves out

The audit notes do not record a formal selection rule. This report adopts the rule that reconstructs the selection. A claim was **eligible** if it is an empirical finding, not a statistical method or a piece of mathematics, that the v0.2.0 text uses in at least one of four ways:

- to settle a clause of its verdict table;
- to justify one of the ten model components or the form of an equation;
- to carry the distinction between the substantive and symbolic routes, or the safety constraint;
- to anchor the Korean father–daughter or the romantic worked example.

Among eligible claims, **priority** went to those cited in the README's two summary tables ("Verdict by clause" and "What each equation says") or in the summary chapter, and to those reused across several chapters. The "Where it does its work" column of Table A1 shows why each claim qualified. **S1–S4 are four further claims that the repository itself flags as resting on secondary or unverified sources.**

**This audit is not exhaustive literature coverage.** It checks whether twenty cited studies support the uses the paper makes of them. It ran no systematic search for replications or later meta-analyses beyond the sources named. A claim it did not check is unaudited, not confirmed. Applied strictly, the selection rule also covers seven anchor citations that no audit pass examined:

- Gere & Schimmack (2013), for compatibility (verdict clause 4 and component 9);
- Liu et al. (2017), for inferring regard from cost (component 4);
- Wieselquist et al. (1999) and Campbell et al. (2010), for trust (component 7);
- Hadiwijaya et al. (2017), for the giver's developmental lag (component 8);
- Lohmann et al. (2024), cited alongside Arriaga et al. for safety (component 10);
- Cooper & Stewart (2021), cited alongside Bolger et al. for the two routes (component 6).

Several co-cited studies were also left unaudited:

- Johnson et al. (2022), Bar-Kalifa & Rafaeli (2013), Lee & Seo (2021), Puente & Cohen (2003) and Kumar & Epley (2018);
- the independent tests of invisible support: Maisel & Gable (2009), Girme et al. (2013, 2018) and Howland & Simpson (2010).

## Table A1. The twenty claims, where they do their work, and what the audit found

| ID | Claim as the paper uses it | Primary source | Where it does its work | Depth | Verdict on the paper's use | Grade as used |
|---|---|---|---|---|---|---|
| C01 | Givers and receivers agree only moderately that a supportive act occurred (κ ≈ .39) | Coriell & Cohen 1995 | Summary; verdict "expressed ≠ perceived" | Full text | Qualified | Moderate/mixed |
| C02 | About half of sacrifices go unnoticed; "false alarms" still earn gratitude; unrecognised givers lose satisfaction | Visserman et al. 2019 | Verdicts "expressed ≠ perceived" and "perceived ≠ received"; component 2 | Full text | Qualified; one use not supported | Moderate/mixed; Preliminary for the giver's satisfaction |
| C03 | Received and perceived support share about 12% of their variance (r ≈ .35) | Haber et al. 2007 | Summary; literature review | Abstract | Qualified (number right, construct framing wrong) | Established, narrow |
| C04 | Invisible support aids adjustment, so a non-perceptual route exists | Bolger, Zuckerman & Kessler 2000 | Verdict "perceived ≠ received"; component 6 | Abstract, plus author-written secondary accounts | **Overstated** | Mixed; Theoretical as proof of the route |
| C05 | Visible support signals inefficacy; invisible support helps | Bolger & Amarel 2007 | Symbolic-route mechanism; romantic example | Full text | Qualified | Moderate/mixed (laboratory); Preliminary versus no support |
| C06 | Over-provision harms more than under-provision; a commensurate need–supply precedent exists | Brock & Lawrence 2009 | Component 5; precedent for response surfaces | Full text | **Overstated** | Moderate (both matter); Preliminary (excess worse) |
| C07 | Perceived responsiveness is partly projected | Lemay, Clark & Feeney 2007 | Component 3 (projection, π) | Full text | Qualified | Moderate |
| C08 | Insecure recipients misread only ambiguous messages | Collins & Feeney 2004 | Component 3 (bias moderated by ambiguity); design ethics | Full text | Qualified | Moderate |
| C09 | Partners are accurate and positively biased at once | Fletcher & Kerr 2010 | Component 3 (τ and δ) | Full text | Qualified; sign misapplied | Established; love-specific sign Moderate/Preliminary |
| C10 | Own perceptions explain 45% of baseline quality; change is barely predictable | Joel et al. 2020 | Predictive benchmark (§8.15) | Full text | Supported | Established, for prediction |
| C11 | The amount of love predicts break-up, so the problem is amount, not translation | Le et al. 2010 | Verdict "translation, not amount" | Abstract, plus secondary effect sizes | Qualified | Established (narrow); Moderate at best against translation |
| C12 | Communication matters less, and less causally, than its reputation | Lavner, Karney & Bradbury 2016 | Literature review §3.7 | Full text | Qualified (heading overreaches) | Moderate |
| C13 | The primary love language and channel matching are unsupported | Flicker, Sancier-Barbosa & Impett 2025 | Verdict "translation, not amount" | Abstract | Qualified | Moderate (null) |
| C14 | Stress blocks enactment of needs that were noticed | Neff, Nguyen & Williamson 2021 | Verdict "intended ≠ expressed"; component 1 | Full text | **Overstated** | Preliminary |
| C15 | Parent–adolescent report gaps are small (g ≈ .24) and grow with age | Hou et al. 2020 | Size of parent–child gaps; the "90 versus 40" illustration | Full text | Qualified; age clause misattributed | Established (pooled estimates) |
| C16 | Perceived financial support is unrelated to distress; Korean adolescents report more financial and less emotional support | Chentsova Dutton, Choi & Choi 2020 | Culture chapter; father–daughter example | Full text | Qualified | Preliminary |
| C17 | Casino income reduced conduct problems but not anxiety or depression, so a substantive route exists | Costello et al. 2003; Akee et al. 2010 | Component 6 | Abstract (Costello); full text (Akee) | Qualified | Moderate (income effects); Our hypothesis (route) |
| C18 | Perceived acceptance predicts adjustment across cultures | Khaleque & Rohner 2002; 2012 | Evidence for the symbolic route | Abstract | Qualified | Established association; no route grade |
| C19 | Felt love and commitment can rise as safety falls | Arriaga, Capezza & Daly 2016 | The empirical case for component 10 | Abstract | **Overstated** | Moderate/mixed (tolerance standards only) |
| C20 | Givers overvalue costly gifts | Flynn & Adams 2009 | Giver error in the father–daughter example | Secondary (press) | Qualified | Preliminary |
| S1 | Spouses' messages had the same intended impact, but distressed spouses' messages were received as more negative | Gottman et al. 1976 | Evidence for the intuition | Secondary (blog) | Cannot determine | Preliminary |
| S2 | The perceiver × supporter pairing is the largest variance component in perceived support | Lakey et al. 1996 | Literature review; hypothesis H6 | Abstract | Supported (ordinal claim) | Moderate |
| S3 | Korean youth linked parental control with warmth in 1985 | Rohner & Pettengill 1985 | Culture table | Abstract | Qualified | Preliminary |
| S4 | Cross-cultural percentages for marrying without love | Levine et al. 1995 | Not used in the paper | Abstract | Cannot determine | Not used |

## No citation is fabricated; the problems are scope, mechanism and attribution

Every source exists and was located. **Every coefficient the paper quotes matched its source wherever the source could be read.** The verdicts on the paper's uses are:

| Verdict | Claims |
|---|---|
| Supported | C10 |
| Qualified | C01, C02, C03, C05, C07, C08, C09, C11, C12, C13, C15, C16, C17, C18, C20 (fifteen claims) |
| Overstated | C04, C06, C14, C19 |

No source contradicts the direction of the claim it is cited for. The failures fall into three recurring kinds:

- **Scope creep.** Findings are stretched beyond their populations:
  - non-marital couples become "relationships" (C11);
  - parenting reports become care adequacy (C15);
  - adult gift exchange becomes a parent's ongoing provision (C20);
  - a meta-analysis of two recipient-side measures becomes evidence that givers and receivers diverge (C03).
- **Mechanism creep.** Effects are described as stronger or more causal than the designs show:
  - a graded weakening becomes a hard "bound" (C14);
  - concurrent covariation becomes "predicted declining" (C06);
  - "not reported by the partner" becomes "had not occurred" (C02);
  - a moderator becomes a cause (C19).
- **Attribution errors.**
  - An age trend is credited to Hou et al. but comes only from Korelitz & Garber (C15).
  - Collins & Feeney are cited for a relational-harm argument they never make (C08).
  - Joel et al. are cited for reverse causation they do not discuss (C10).

The numerical slips are sample sizes and one denominator:

- Visserman et al.'s abstract gives 426 participants against 412 in its Methods.
- Bolger & Amarel's abstract gives 257 against 267 analysed.
- Hou et al.'s g = .24 comes from 221 of the 313 studies.

The paper copied the abstract figures in the first two cases.

**The errors do not all run one way.** Where the paper builds its own model, the overstatements strengthen the model's components: the route split (C04, C17), the constraint form (C14), the asymmetric loss and its measurement precedent (C06), the separation of financial from emotional care (C16) and the safety case (C19). Where the paper argues against the original intuition, the overstatements strengthen that argument:

- "amount rather than translation" (C11, C13);
- "less causal" communication (C12);
- feeling loved as largely projected (C07 at `paper/19b-is-love-enough.md:7`);
- a positive perceptual bias that is in fact negative for judgments of love (C09).

Both sets of overstatement make the revised synthesis look better supported than it is. **Corrected, the comparative question of translation versus amount is more open than the paper says, and the model's distinctive components rest more on assumption.**

## Eight claims rest on abstracts or press accounts

| Verification depth | Claims |
|---|---|
| **Abstract only** for the primary source | C03 (Haber et al.); C04 (Bolger et al. 2000); C11 (Le et al.); C13 (Flicker et al.); the Costello half of C17; C18 (Khaleque & Rohner); C19 (Arriaga et al.) |
| **Press accounts only** | C20 (Flynn & Adams) |
| Supplementary claims | S1 rests on a practitioner blog; S2, S3 and S4 rest on abstracts |

Three of these claims also lean on **indirect citations**:

- C04's results are known through full texts of two later papers by the same group.
- C11's effect sizes come from the citation contexts of citing papers.
- Costello's design comes partly from a description in D'Onofrio et al. (2009).

The two claims that carry the model's most distinctive components are both abstract-level: **C04, which carries the route split, and C19, which carries the empirical case for the safety constraint.** Five full-text sources were read as accepted author manuscripts, which may differ slightly from the typeset versions: C06, C12, C14, C15 and the Akee half of C17.

## Claim-by-claim findings

### Transmission: is care lost between what one person does and what the other registers? (C01–C05)

#### C01. Coriell & Cohen (1995): do giver and receiver agree that support happened?

**Study.** Coriell, M., & Cohen, S. (1995), *Journal of Personality and Social Psychology* 69(2), 289–299 ([doi:10.1037/0022-3514.69.2.289](https://doi.org/10.1037/0022-3514.69.2.289)).

**Read.** Full text: the scanned published version in Carnegie Mellon's KiltHub repository, pp. 289–298 ([KiltHub](https://doi.org/10.1184/R1/6614096.v1)).

**Measured.** Students reported, after the exam, which of 67 supporter behaviours had occurred while they prepared for a major exam. Supporters reported the same within three days. Student judges had classed 36 behaviours as helpful and 31 as harmful. Agreement was Cohen's κ, computed within each dyad and then averaged.

**Design and population.** A single-occasion retrospective checklist comparison with no manipulation. The sample was 297 Carnegie Mellon undergraduates, each with the close friend or roommate they chose as their main peer supporter. Students were 57% men, with a median age of 18. The year of data collection is not stated.

**Key result.**
- Mean κ = **.39** across all 67 behaviours, **.28 for helpful behaviours alone** and .14 for harmful ones.
- Concordance correlated r = .53 with fulfilled expectancies and r = .41 with intimacy.
- Six predictors together explained 41% of the variance in concordance.

**Limitations.**
- The authors stress that without an objective record, a disagreement cannot be traced to a missed perception rather than an over-report.
- They also note that checklist unreliability deflates κ.
- Reports were retrospective and strongly shaped by expectations.
- The dyads were peers around one exam, not romantic partners or families.

**Does it support the paper's interpretation?** Qualified. The number is right, but it pools helpful and harmful acts. The figure for supportive acts alone is lower, which strengthens the paper's point. "Partners" misdescribes friends and roommates. And the study shows disagreement about whether acts occurred, not care lost in transmission.

**Grade.** Moderate/mixed for the general proposition, unchanged. The specific κ is a single-study estimate.

**Corrections.**
- Reword the population, add the helpful-only κ and add the authors' caveat at `paper/00-summary.md:5` and `paper/04-evidence-for-the-intuition.md:7`.
- At `paper/03-literature-review.md:23`, the behaviours occurred during exam preparation and were reported afterwards, not "after an exam".
- Carry the same qualification into `paper/01-question-and-thesis.md:14` and `README.md:47`.

#### C02. Visserman et al. (2019): missed sacrifices, "false alarms" and gratitude

**Study.** Visserman, M. L., Impett, E. A., Righetti, F., Muise, A., Keltner, D., & Van Lange, P. A. M. (2019), *Social Psychological and Personality Science* 10(3), 317–325 ([doi:10.1177/1948550618757599](https://doi.org/10.1177/1948550618757599)).

**Read.** Full text: the CC BY-NC published version in Sussex Research Online, pp. 317–324, including Notes 1–3 ([Sussex figshare](https://sussex.figshare.com/articles/journal_contribution/To_see_is_to_feel_grateful_A_quasi-signal_detection_analysis_of_romantic_partners_sacrifices/23493755)). The online supplement and the OSF data were not read.

**Measured.**
- Each evening, both partners answered yes or no to whether they had sacrificed and whether their partner had.
- Each day was coded as a hit, miss, false alarm or correct rejection, with the partner's self-report as the criterion.
- Gratitude, appreciation and satisfaction were single daily items.

**Design and population.**
- Two dyadic diaries, of 8 and 14 days, analysed with multilevel models that controlled the previous day's gratitude.
- Study 1: 126 Dutch couples (N = 252; mean age 23.3; 64% students).
- Study 2: 80 couples from the San Francisco Bay Area (N = 160; mean age 23.9).
- The abstract gives N = 426, but the Methods sections sum to 412.

**Key result.**
- About **46–47% of partner-reported sacrifice days went undetected** in both samples.
- Of the sacrifices people perceived, about 46% (Study 1) and 39.8% (Study 2) were not reported by the partner. In Study 2, false alarms were significantly fewer than hits (p < .001).
- Same-day gratitude, compared with correct-rejection days:

  | Day type | Study 1 | Study 2 |
  |---|---|---|
  | Hit | b = .19 | b = .38 |
  | False alarm | b = .18 | b = .41 |
  | Miss | b = −.11 (p = .159) | b = .03 (p = .671) |

- Sacrificers were less satisfied on miss days than on hit days: b = −.16 (p = .069) in Study 1 and b = −.23 (p = .017) in Study 2.
- Follow-ups at one year and three months showed no evident long-term effect of detection on gratitude.

**Limitations.**
- The criterion is the partner's self-report.
- The authors say causal direction cannot be confirmed.
- Satisfaction tests used only hit and miss days.
- Outcomes were single items.
- Samples were young couples in short relationships.
- Couples were trained at intake to recognise sacrifices, which may raise detection above everyday levels.

**Does it support the paper's interpretation?** Qualified, with one use not supported.
- Supported: the detection rates and the gratitude associations.
- Holds for one study only: "about half of the sacrifices people 'see' were not reported" is true in Study 1 but not Study 2.
- Overstated: "unrecognised givers lose satisfaction" uses causal and change language for a small, associational difference that was significant in one of two samples.
- Not supported: treating false alarms as "perception without benefit" or as sacrifices that "had not occurred". A false alarm means only that the partner did not report a sacrifice, and benefit was never measured.
- Inaccurate: the stated limitation "two studies, one laboratory". The samples came from different countries and projects.

**Grade.** Moderate/mixed for detection and gratitude. **Preliminary** for the sacrificer-satisfaction effect.

**Corrections.**
- Per-study samples instead of N = 426, and "40–46%" for unreported perceived sacrifices: `paper/03-literature-review.md:52` and `:140`.
- Associational verbs instead of "produced", "drives" and "depends on": `paper/03:52`, `paper/03:140`, `paper/07-revised-model.md:48`.
- "Whether or not the partner reported sacrificing" instead of "whether or not they had occurred": `paper/05-evidence-against-it.md:30`, `paper/07:48`.
- Drop false alarms as evidence of perception without benefit: `paper/01-question-and-thesis.md:15`, `paper/02-definitions-and-distinctions.md:18`, `README.md:48`.
- Tag the sacrificer effect Preliminary and use associational wording: `paper/07:34`, `paper/10-father-daughter-example.md:34`, `paper/11-romantic-partner-example.md:8`, `paper/04-evidence-for-the-intuition.md:65`.
- Restrict "invisible care earns no thanks" to sacrifices and same-day gratitude: `paper/08-mathematical-representation.md:261`, `paper/14-time-and-feedback.md:20`.

#### C03. Haber et al. (2007): received versus perceived support, r ≈ .35

**Study.** Haber, M. G., Cohen, J. L., Lucas, T., & Baltes, B. B. (2007), *American Journal of Community Psychology* 39(1–2), 133–144 ([doi:10.1007/s10464-007-9100-9](https://doi.org/10.1007/s10464-007-9100-9)).

**Read.** Abstract only, via Europe PMC, PubMed and OpenAlex ([Europe PMC](https://europepmc.org/article/MED/17308966)). The open author version at Deep Blue sat behind an automated-access challenge, which was not bypassed.

**Measured.** The correlation between the same respondent's self-reported receipt of supportive behaviours, on the Inventory of Socially Supportive Behaviors (ISSB), and that respondent's perceived social support on any measure.

**Design and population.** A meta-analysis of 23 studies. Total N, countries, years and study designs are unverified.

**Key result.** Average r = **.35** (p < .001). That is about 12% shared variance, if the correlation is uncorrected; whether it is was not verified.

**Limitations.**
- Confidence interval, heterogeneity, moderators, correction for attenuation and publication-bias checks are all unverified.
- Both measures come from the recipient.

**Does it support the paper's interpretation?** Qualified.
- The number is right, but the interpretive frame is not. The study shows that two recipient-side constructs, receiving support and feeling supported, are distinct. It does not show that givers and receivers diverge.
- The support literature's "received support" is the recipient's own report. It is not the paper's "received care", which the paper defines as need fulfilment (`paper/02-definitions-and-distinctions.md:43`).
- If the correlation is uncorrected for unreliability, "share only about 12%" understates the latent overlap.

**Grade.** Established for this narrow pairing of measures.

**Corrections.**
- Reframe as a within-recipient construct distinction: `paper/03-literature-review.md:21–22`, `paper/00-summary.md:5`.
- Verify or drop "mostly cross-sectional": `paper/03:137`.

#### C04. Bolger, Zuckerman & Kessler (2000): does invisible support help?

**Study.** Bolger, N., Zuckerman, A., & Kessler, R. C. (2000), *Journal of Personality and Social Psychology* 79(6), 953–961 ([doi:10.1037/0022-3514.79.6.953](https://doi.org/10.1037/0022-3514.79.6.953)).

**Read.** Abstract only for the primary ([OpenAlex](https://api.openalex.org/works/https://doi.org/10.1037/0022-3514.79.6.953)). Two later full texts by the same group served as secondary accounts:
- Bolger & Amarel (2007), pp. 458–460 and 471–473 ([author PDF](http://www.columbia.edu/~nb2229/docs/bolger-amarel-support-experiments-2006.pdf));
- the author manuscript of Shrout, Bolger, Iida, Burke, Gleason & Lane (2010), pp. 1–25 ([manuscript](https://psychology.columbia.edu/sites/psychology.columbia.edu/files/2016-11/shrout-2009-support%20transaction%20chapter_0.pdf); [chapter DOI](https://doi.org/10.1093/acprof:oso/9780195380170.003.0007)).

**Measured.** Daily yes/no reports of emotional support provided (by the partner) and received (by the examinee), and next-day anxiety and depressed mood, as described in the authors' later accounts.

**Design and population.** A nonexperimental daily diary of US couples in which one partner was preparing for the bar exam. The original N, number of days and years are unverified from the primary; the repository's notes give 68 couples.

**Key result.**
- *Abstract:* many transactions reported by providers went unreported by recipients, and these "invisible" transactions promoted adjustment.
- *Original pattern, per the later account:* recognised emotional support predicted higher next-day anxiety and depressed mood. Provider-reported support, adjusted for the recipient's report, predicted lower next-day depressed mood.
- *Reanalysis:* no invisible-support benefit for anger, fatigue or vigour.
- **The same group's replication did not reproduce the pattern.** It had 312 examinees and 310 partners, more than three times the original sample, with twice-daily diaries from five weeks before to one week after the exam.
  - Provider-reported emotional support was often associated with *more* anger, anxiety, depressed mood and fatigue. For example, next-evening anxiety b = 0.097 (z = 2.06) and fatigue b = 0.104 (z = 3.38).
  - The authors wrote that they now "back off from this simple take home message".

**Limitations.**
- The design is nonexperimental.
- Binary self-reports confound measurement error with real differences in perspective.
- "Invisible" means not *reported as support*, which is not the same as unperceived.
- The samples were convenience samples.

**Does it support the paper's interpretation?** **Overstated.** The paper accurately describes the 2000 finding at `paper/03-literature-review.md:30`. Elsewhere it treats the finding as established evidence that benefit occurs without perception, and as proof that a non-perceptual route "exists" (`paper/08-mathematical-representation.md:231`). The only comparable larger replication failed, and the original authors withdrew the simple message.

**Grade.** Mixed: an original diary pattern not reproduced in a larger sample using the same paradigm. Theoretical as evidence that a non-perceptual route exists.

**Corrections.**
- Add the failed replication and tag [Mixed]: `paper/03:29–30`.
- Downgrade the language of "aids", "helps" and "improves": `paper/01-question-and-thesis.md:15`, `paper/02-definitions-and-distinctions.md:19` and `:43`, `paper/06-competing-theories.md:8`.
- Remove invisible support as proof of the route: `paper/07-revised-model.md:47`, `paper/08:37`, `paper/08:231`, `README.md:48` and `:126`. The same evidence is named at `paper/08:316`, a location identified in this synthesis.
- Change "can benefit from care they never notice" to "may benefit from care they do not register as support": `paper/19b-is-love-enough.md:5`, `paper/09-model-without-math.md:7`.

#### C05. Bolger & Amarel (2007): visible support and inefficacy

**Study.** Bolger, N., & Amarel, D. (2007), *Journal of Personality and Social Psychology* 92(3), 458–475 ([doi:10.1037/0022-3514.92.3.458](https://doi.org/10.1037/0022-3514.92.3.458)).

**Read.** Full text: the author-posted PDF of the published article, pp. 458–473 ([author PDF](http://www.columbia.edu/~nb2229/docs/bolger-amarel-support-experiments-2006.pdf)).

**Measured.**
- Change in self-reported distress (POMS items, rescaled 0–10) from baseline to just before an expected speech, which was never given.
- Manipulation checks, perceived supportiveness, reflected appraisal of inefficacy and upward comparison.

**Design and population.**
- Three randomised laboratory experiments. A female confederate peer gave scripted support either directly ("visible") or framed as a question to the experimenter ("invisible").
- Study 2 added a no-support control.
- Study 3 was a five-cell incomplete factorial that separated visibility, inefficacy messages and support content.
- Participants were female NYU introductory-psychology students. Analysed n = 31, 86 and 150, which sums to 267; the abstract reports 257.

**Key result.**
- *Invisible versus visible:* invisible support produced smaller rises in distress, d = 1.09 (p = .004) in Study 1 and d = 0.63 (p = .017) in Study 2.
- *Invisible versus none:* **not significant in either test**, d = 0.36 (p = .159) and d = 0.37 (p = .069).
- *Visible versus none (Study 2):* d = 0.27 (p = .287), not significant.
- *The inefficacy message (Study 3):* visible support that said the recipient needed help raised distress by 1.09 units against no support (d = 0.66, p = .001). Removing that message removed the harm.
  - Reflected appraisal of inefficacy carried about 45% of the effect.
  - Advice content alone had no effect (p = .673).
- *Perceived supportiveness:* recipients rated the confederate as more supportive in the visible conditions (5.2 versus 2.6 on 0–10). That held even in the condition that raised distress (4.6).

**Limitations.**
- Strangers, women and a single laboratory stressor.
- A distress outcome measured over minutes, before a speech that was never delivered.
- One laboratory.

**Does it support the paper's interpretation?** Qualified.
- It supports the symbolic-route reading: support that signals inefficacy raises distress, partly through a perception.
- It overstates "invisible support reduced emotional reactivity", since neither test against no support was significant.
- It overstates "visible support was … harmful because it communicated inefficacy". Harm appeared only when inefficacy was scripted explicitly, and the mediation was partial.
- It undercuts use of invisible support as evidence of a route that bypasses perception. In the invisible conditions participants heard the advice; they simply did not read it as support.

**Grade.**
- Moderate/mixed for "support that signals the receiver's inefficacy raises short-term distress" in a laboratory analogue.
- Preliminary for invisible support beating no support.
- Theoretical for close relationships.

**Corrections.**
- Correct the N, rewrite the claim and tag [Moderate/mixed; laboratory analogue]: `paper/03-literature-review.md:31`.
- The row tag "Moderate to Established" overstates this component: `paper/06-competing-theories.md:8`.
- Keep "can" and "may", but name the population of strangers in a laboratory: `paper/04-evidence-for-the-intuition.md:34`, `paper/07-revised-model.md:54`, `paper/11-romantic-partner-example.md:5`.

### Perception, fit and prediction (C06–C10)

#### C06. Brock & Lawrence (2009): under- and over-provision of support

**Study.** Brock, R. L., & Lawrence, E. (2009), *Journal of Family Psychology* 23(2), 181–192 ([doi:10.1037/a0015402](https://doi.org/10.1037/a0015402)).

**Read.** Full text: the NIH accepted manuscript ([PMC2776033](https://pmc.ncbi.nlm.nih.gov/articles/PMC2776033/)).

**Measured.**
- On a modified 48-item Support in Intimate Relationships Rating Scale (SIRRS), each recipient rated how often the partner performed each behaviour in the past month.
- For each behaviour, the recipient also gave a preferred direction: more, less or the same.
- Under-provision is the proportion of items the recipient wanted more of; over-provision is the proportion wanted less of.
- Satisfaction was measured with the Quality of Marriage Index.

**Design and population.**
- Five mailed waves, from 3–6 to 54–57 months after the wedding.
- Growth-curve actor–partner models, with under- and over-provision entered together as time-varying covariates. The estimates are therefore concurrent within-spouse covariation, not lagged prediction.
- 103 first-married Iowa newlywed couples, mean ages about 25–26, 15% ethnic minority.

**Key result.**
- Both forms co-varied with lower satisfaction:

  | Spouse | Under-provision | Over-provision | Test of slope difference |
  |---|---|---|---|
  | Husbands | b = −7.52, r = .36 | b = −18.73, r = .28 | χ²(1) = 4.76 |
  | Wives | b = −8.02, r = .43 | b = −27.14, r = .31 | χ²(1) = 5.00 |

- The *unstandardised* slopes were larger for over-provision, but the reported *effect-size r* was larger for under-provision.
- Under-provision was far more prevalent: 61.4–91.9% of spouses per wave, against 27.1–43.4% for over-provision.
- By support type, over-provision exceeded under-provision only for informational support in husbands, and for informational, emotional and tangible support in wives.

**Limitations.** The authors state:
- the analyses show covariation, not temporal order;
- they cannot tell whether inadequate support precedes or follows discord;
- the sample was single, mostly Caucasian and educated;
- measures shared a method;
- power was insufficient to enter all type-specific predictors together.

**Does it support the paper's interpretation?** **Overstated.**
- "Over-provision was the greater risk" depends on the metric.
- "Predicted declining" claims a temporal order the design cannot show.
- The contrast "over five years versus day to day" with Bar-Kalifa & Rafaeli (2013) confounds measurement and design, not just timescale.
- Need was only a direction, so the measure is not commensurate need and supply and cannot serve as a precedent for response surface analysis.

**Grade.** Moderate for "both under- and over-provision are associated with lower satisfaction". **Preliminary** for "over-provision is worse".

**Corrections.**
- "Co-varied with lower" instead of "predicted declining": `paper/03-literature-review.md:39`, `paper/04-evidence-for-the-intuition.md:31`.
- Measurement and design differ, not only timescale: `paper/03:142`.
- Reword component 5 and the asymmetric-loss rationale: `paper/08-mathematical-representation.md:36` and `:215`, `README.md:125`.
- Remove the "commensurate" precedent: `paper/08:219` and `:315`, `paper/17-what-testing-requires.md:15`.
- Keep the evidence for type 3 ("too much"), but tag it Preliminary: `paper/07-revised-model.md:65`.

#### C07. Lemay, Clark & Feeney (2007): projection of responsiveness

**Study.** Lemay, E. P., Clark, M. S., & Feeney, B. C. (2007), *Journal of Personality and Social Psychology* 92(5), 834–853 ([doi:10.1037/0022-3514.92.5.834](https://doi.org/10.1037/0022-3514.92.5.834)).

**Read.** Full text: the published PDF on the authors' lab site ([Yale lab PDF](https://clarkrelationshiplab.yale.edu/sites/default/files/files/Projection%20of%20responsiveness%20to%20needs%20and%20construction%20of%20satisfying%20communcal%20relationships%281%29.pdf)).

**Measured.**
- Own responsiveness: caregiving and secure-base self-reports in Study 1, communal strength in Study 2.
- Perceived partner responsiveness, on reworded parallel items and a second scale.
- The partner's self-report served as the accuracy benchmark.
- Daily counts of benefits given and received, and perceived communal motives.
- A recall-difficulty manipulation in Study 3.

**Design and population.**
- Study 1: cross-sectional, 191 married couples from the Pittsburgh area (151–170 analysed).
- Study 2: a two-wave panel of 108 engaged couples (96 at the second wave), plus a five-day diary of 100 couples.
- Study 3: an online experiment with 158 adults rating a romantic partner or a close friend.

**Key result.**
- Own responsiveness predicted perceived partner responsiveness far more strongly than the partner's self-report did; all paths were significant:

  | Sample | Own | Partner's self-report |
  |---|---|---|
  | Study 1, safe haven | .60 | .22 |
  | Study 1, secure base | .52 | .17 |
  | Study 2, first wave | .51 | .17 |
  | Study 2, second wave | .47 | .18 |

- **For daily counts of benefits received, the partner's reported giving mattered as much as one's own** (.36 versus .34). Projection dominated only for perceived motives (.23 versus .08).
- Making one's own past help harder to recall lowered perceived responsiveness (F(1, 149) = 4.38, p < .05), but it did not change self-reported responsiveness (p = .27).

**Limitations.**
- The projection path shares a rater and item wording with the outcome.
- The accuracy benchmark is a report.
- One research group, and US samples.

**Does it support the paper's interpretation?** Qualified. The paper is accurate for global questionnaire perceptions, but it omits that concrete daily acts tracked the partner's giving. The strongest use, at `paper/19b-is-love-enough.md:7`, overreaches. "Love, mood, attachment and history" were not measured as predictors; attachment and depression were controls; and the giver's acts were never observed.

**Grade.** Moderate (keep).

**Corrections.**
- Add the daily result: `paper/03-literature-review.md:11`, `paper/05-evidence-against-it.md:12` (also add a tag there).
- Rewrite the overreaching sentence: `paper/19b:7`.

#### C08. Collins & Feeney (2004): attachment and appraisal of support messages

**Study.** Collins, N. L., & Feeney, B. C. (2004), *Journal of Personality and Social Psychology* 87(3), 363–383 ([doi:10.1037/0022-3514.87.3.363](https://doi.org/10.1037/0022-3514.87.3.363)).

**Read.** Full text: the published PDF on the authors' lab site ([UCSB lab PDF](https://labs.psych.ucsb.edu/collins/nancy/UCSB_Close_Relationships_Lab/Publications_files/Collins%20and%20Feeney,%202004.pdf)).

**Measured.**
- Recipients' positive and negative appraisals of support notes, and their perception of an earlier interaction.
- Attachment anxiety and avoidance.
- In Study 2, genuine notes from the partner, coded by independent raters.

**Design and population.**
- Study 1: a quasi-experiment. High- or low-support notes copied from experimenter text were randomly assigned; attachment was measured, not manipulated. 95 student-recruited couples, mean age 19.4. The low-support notes were also written to be "somewhat ambiguous", so ambiguity was never manipulated separately.
- Study 2: an observational laboratory study of 153 US college dating couples.

**Key result.**
- *Positive appraisal* was driven by condition (β = .66, sr² = .43; and β = .67, sr² = .44), with no attachment effects.
- *Negative (hurtful) appraisal:*
  - Avoidance had an effect in the low-support condition (β = .41, sr² = .06), but its interaction with condition was only marginal (p = .09).
  - Anxiety had an effect in the low-support condition (β = .40, sr² = .06), with a significant interaction.
- *Genuine notes (Study 2):* attachment predicted less favourable perceptions beyond objective ratings, satisfaction, trust and perceived partner support (sr² ≈ .02–.09). The effect was strongest for low-support notes, **weaker but present for moderately supportive notes**, and absent for very supportive ones.

**Limitations.**
- Ambiguity was confounded with low support.
- Attachment was not manipulated.
- Student samples from one laboratory.
- The paradigm involved deception.

**Does it support the paper's interpretation?** Qualified.
- The grade "Established (bounded)" overstates two studies from one laboratory with small effects.
- "Only ambiguous" is too narrow a boundary.
- "Adds nothing beyond relationship perceptions" (`paper/06-competing-theories.md:9`) comes from Joel et al.'s prediction of relationship quality. In Collins & Feeney's Study 2, attachment did add beyond such perceptions.
- `paper/18-proposed-study.md:90` misattributes an ethics claim. The authors report deception and careful debriefing, not relational harm.

**Grade.** Moderate.

**Corrections.**
- Change "Established for this bounded effect" and "Established (bounded)" to Moderate: `paper/03-literature-review.md:77–80`, `paper/06:9`.
- Replace "only ambiguous" with the graded boundary: `paper/08-mathematical-representation.md:172`.
- Present relational harm as the paper's own inference: `paper/18:90`.

#### C09. Fletcher & Kerr (2010): accuracy and bias in intimate relationships

**Study.** Fletcher, G. J. O., & Kerr, P. S. G. (2010), *Psychological Bulletin* 136(4), 627–658 ([doi:10.1037/a0019792](https://doi.org/10.1037/a0019792)).

**Read.** Full text: the published PDF, from a CiteSeerX cached copy ([CiteSeerX copy](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.471.1954&rep=rep1&type=pdf)).

**Measured.**
- *Tracking accuracy:* whether judgments covary with a benchmark, usually the partner's self-report, across couples or across items.
- *Signed and absolute mean-level bias,* in six judgment categories.

**Design and population.** A random-effects meta-analysis of published studies of heterosexual adult couples up to the end of 2008. It covered 98 tracking studies (27,064 individuals) and 48 bias studies (9,393 individuals).

**Key result.**
- Tracking accuracy r = .47 [.44, .50] overall, and **.40 for judgments of the partner's love or affection**.
- Signed bias r = .09 [.04, .13] overall, but **−.11 [−.21, −.002] for love and affection** (k = 7).
- Tracking and bias were uncorrelated across the 38 studies that reported both (r = .005).
- Positive bias related to relationship quality (r = .36), while tracking accuracy did not (about .03).

**Limitations.**
- The criterion problem: partners' self-reports are themselves likely biased.
- Effects are zero-order.
- Published studies only, ending in 2008.

**Does it support the paper's interpretation?** Qualified.
- The core numbers are verified.
- "Track reality" and "knowing *when* and on what" misdescribe a correlation computed across couples or items, not over time.
- **The sign is misapplied at the model level.** `README.md:123` and `paper/08-mathematical-representation.md:34` describe perceived care as "positively biased". For love, the bias was negative.
- `paper/05-evidence-against-it.md:46` cites the overall positive bias where the love-specific bias belongs.

**Grade.** Established for tracking accuracy and the small overall bias. Moderate/Preliminary for the negative bias in judgments of love.

**Corrections.** `paper/03-literature-review.md:58`, `paper/05:46`, `paper/08:34`, `README.md:123`.

#### C10. Joel et al. (2020): what predicts relationship quality

**Study.** Joel, S., Eastwick, P. W., et al. (2020), *PNAS* 117(32), 19061–19071 ([doi:10.1073/pnas.1917036117](https://doi.org/10.1073/pnas.1917036117)).

**Read.** Full text of the published article ([eScholarship PDF](https://escholarship.org/content/qt8mc5n2c3/qt8mc5n2c3.pdf); [PMC7431040](https://pmc.ncbi.nlm.nih.gov/articles/PMC7431040/)). The SI Appendix and OSF materials were not accessed.

**Measured.**
- 2,413 mostly self-report baseline predictors.
- Satisfaction (in 43 datasets) and commitment (in 31) at baseline, at follow-up and as change.

**Design and population.**
- Preregistered random forests in each dataset, with out-of-bag variance explained pooled by random-effects meta-analysis.
- 43 datasets from 29 laboratories, covering 11,196 couples, all from Western countries.
- One dataset holds 6,298 couples.

**Key result.**
- Actor-reported relationship variables explained **45%** of baseline satisfaction.
- Adding partner reports and individual differences gained 0.0–1.9% at baseline and 0.9–3.5% at follow-up.
- Follow-up levels were predicted up to 18%.
- **Change was predicted no better than 5%** (mean about 2.2–2.5%).
- Variable success rates:

  | Predictor | Success rate |
  |---|---|
  | Perceived partner commitment | 85% |
  | Appreciation | 72% |
  | Sexual satisfaction | 71% |
  | Perceived partner satisfaction | 70% |
  | Conflict | 69% |
  | Perceived partner responsiveness | 69% |

**Limitations.**
- All samples are Western.
- 99.4% of the 1,149 relationship-specific variables were self-report.
- The design shows prediction, not causation.
- Baseline prediction is concurrent and from the same reporter.
- Selecting variables and estimating out-of-bag on the same data may be optimistic (auditor's inference).

**Does it support the paper's interpretation?** Supported. A few details need correcting:
- Perceived responsiveness was not the "top predictor" (`paper/06-competing-theories.md:7`).
- 99.4% refers to relationship-specific variables, not to all predictors (`paper/03-literature-review.md:138`).
- Joel et al. do not argue reverse causation (`paper/06:24`).
- "Essentially none" of change should read "at most 5%" (`paper/08-mathematical-representation.md:369`, `paper/05-evidence-against-it.md:69`).

**Grade.** Established, for prediction, in Western self-report samples.

### Amount, communication, love languages, capacity and parent–child reports (C11–C15)

#### C11. Le, Dove, Agnew, Korn & Mutso (2010): does the amount of love predict break-up?

**Study.** Le, B., Dove, N. L., Agnew, C. R., Korn, M. S., & Mutso, A. A. (2010), *Personal Relationships* 17(3), 377–390 ([doi:10.1111/j.1475-6811.2010.01285.x](https://doi.org/10.1111/j.1475-6811.2010.01285.x)).

**Read.** Abstract only ([OpenAlex](https://api.openalex.org/works/doi:10.1111/j.1475-6811.2010.01285.x)). The full text is closed. Effect sizes come from secondary sources: citation contexts retrieved through Semantic Scholar, and Barrantes et al. (2017) ([PMC5501283](https://pmc.ncbi.nlm.nih.gov/articles/PMC5501283/)).

**Measured.** Predictors of whether non-marital romantic relationships ended, among them commitment, love, inclusion of other in the self, dependence, satisfaction, alternatives, investments, network support and personality. Love was each person's own self-reported love; the instruments pooled are unverified.

**Design and population.** A meta-analysis of 137 studies with 37,761 participants, spanning 33 years. Participants were 96% heterosexual. Countries and the share of students are unverified.

**Key result.**
- Commitment, love, inclusion of other in the self and dependence were among the strongest predictors of break-up.
- Satisfaction, alternatives and investments were modest predictors.
- Network support was a robust predictor; personality was a limited one.
- Secondary sources give the strongest predictors as d = .57–.85 ([Eastwick, Finkel & Simpson 2019](https://doi.org/10.1080/1047840X.2019.1577072)) and commitment as d = 0.80 ([Etcheverry et al. 2013](https://doi.org/10.1111/j.1475-6811.2012.01423.x)).
- Two citing papers report that positive illusions, a perception variable, were the strongest predictor (for example [Rigby & Cobb 2023](https://doi.org/10.1177/02654075221127241)).

**Limitations.**
- Love's exact d, the number of studies per predictor, heterogeneity and bias tests are all unverified.
- The predictors overlap heavily; commitment and satisfaction correlate about .68 ([Tan, Arriaga & Agnew 2018](https://doi.org/10.1177/0265407517702010)).
- Falling love may be a symptom of a failing relationship as much as its cause.

**Does it support the paper's interpretation?** Qualified. The study supports "one's own love and commitment predict whether non-marital relationships last". It cannot adjudicate "amount rather than translation". A person's self-reported love may itself depend on the love they perceive receiving, and the outcome is break-up, not receiving adequate care. Generalising to "relationships" (`paper/19b-is-love-enough.md:11`) and to parental "amount deficits" (`paper/07-revised-model.md:62`) extrapolates beyond non-marital couples.

**Grade.** Established for the narrow persistence claim. Indirect, Moderate at best, as evidence against translation.

**Corrections.**
- Say that the love measured was each person's own self-report, and that the study does not test translation: `paper/05-evidence-against-it.md:7`, `paper/03-literature-review.md:84` and `:146`, `paper/01-question-and-thesis.md:17`, `README.md:50`.
- Write "non-marital romantic relationships" at `paper/19b:11`.
- Label the parent–child use as an extrapolation at `paper/07:62`.

#### C12. Lavner, Karney & Bradbury (2016): communication and satisfaction over time

**Study.** Lavner, J. A., Karney, B. R., & Bradbury, T. N. (2016), *Journal of Marriage and Family* 78(3), 680–694 ([doi:10.1111/jomf.12301](https://doi.org/10.1111/jomf.12301)).

**Read.** Full text: the NIH author manuscript ([PMC4852543](https://pmc.ncbi.nlm.nih.gov/articles/PMC4852543/)). Tables 1–7 were not inspected separately.

**Measured.**
- Communication was observed in three 8-minute home discussions and coded with the Iowa Family Interaction Rating Scales into three factors: positivity (which includes warmth, affection and endearment), negativity and effectiveness.
- Satisfaction was an 8-item self-report.

**Design and population.**
- Four waves about 9 months apart, covering the first three years of marriage.
- Cross-lagged path models.
- 431 first-married newlywed couples from low-income neighbourhoods in Los Angeles County; 76% Hispanic.

**Key result.**
- Communication predicted later satisfaction in **7 of 36** lagged paths. For positivity it did so in 2 of 12 (median absolute β = .02).
- Satisfaction predicted later communication about twice as often.
- 85% of direct comparisons between the two directions were not significant.
- The authors judged both effects inconsistent and similar in size.

**Limitations.**
- One sample, and structured tasks rather than everyday interaction.
- The 9-month lags may be the wrong timescale.
- The cross-lagged model captures rank-order stability, not within-person change (the authors).

**Does it support the paper's interpretation?** Qualified. The sentence at `paper/03-literature-review.md:88` is accurate. The heading "Communication matters less, and less causally, than its reputation" (`paper/03:86`) overreaches: weak lagged prediction is not evidence that causal effects are absent. Observed affection almost never predicted later satisfaction. That is weak evidence that expressed affection in structured tasks does not drive satisfaction over 9-month lags.

**Grade.** Moderate (for this study).

**Corrections.** Retitle `paper/03:86`, for example to "Communication predicts later satisfaction weakly and inconsistently". Tag Lavner et al. as Moderate at `paper/03:88`.

#### C13. Flicker, Sancier-Barbosa & Impett (2025): love languages

**Study.** Flicker, S. M., Sancier-Barbosa, F., & Impett, E. A. (2025), *Journal of Marital and Family Therapy* 51(4), e70078 ([doi:10.1111/jmft.70078](https://doi.org/10.1111/jmft.70078)).

**Read.** Abstract only ([PubMed 40977357](https://pubmed.ncbi.nlm.nih.gov/40977357/)), together with the abstracts of two companion papers ([PubMed 39420529](https://pubmed.ncbi.nlm.nih.gov/39420529/); [PubMed 40916580](https://pubmed.ncbi.nlm.nih.gov/40916580/)). The full texts were closed or behind a bot challenge. No preregistration document was located.

**Measured.**
- Whether each participant had an identifiable primary love language.
- The participant's satisfaction with the partner's enactment of each love-language behaviour.
- Relationship quality and perceived partner love.

**Design and population.** A preregistered, cross-sectional online survey of 499 individuals in long-term cohabiting relationships. US residence is stated only in the companion abstract, whose three studies (N = 696, 500 and 499) probably overlap with this sample.

**Key result.**
- Fewer than half of participants had an *identifiable* primary love language.
- Satisfaction with the partner's enactment of one's primary language predicted quality no better than satisfaction with other behaviours.
- Quality tracked satisfaction across a wide range of loving behaviours.
- The robust predictors were verbal affirmations, encouragement for individual pursuits, support during difficult times and accountability.

**Limitations.**
- Cross-sectional, single-informant self-report.
- It measured the receiver's satisfaction, not an observed match between giver and receiver.
- The classification rule and effect sizes are unknown.
- The companion samples probably overlap.

**Does it support the paper's interpretation?** Qualified. `paper/03-literature-review.md:114` is accurate. `paper/06-competing-theories.md:18` overstates in two ways: it drops "identifiable", and it calls the result a "matching null" when what was null was the *extra* weight of the primary channel. The study also cannot show that amount beats translation, because quality tracked satisfaction with many loving behaviours, which fits a broad translation account as well. It removes the popular "primary language" version of translation. It does not remove the v0.2.0 version, whose fit term is defined on needs, not on a trait-like preferred channel.

**Grade.** Moderate, as a null for the distinctive primary-language claim.

**Corrections.**
- Reword `paper/06:18`.
- Make the tags consistent: "Moderate/mixed (null)" at `paper/03:149` against "Preliminary" at `paper/06:18`.
- Correct the uses in the verdict: `paper/01-question-and-thesis.md:17`, `README.md:50`.

#### C14. Neff, Nguyen & Williamson (2021): stress and acting on noticed needs

**Study.** Neff, L. A., Nguyen, T. T. T., & Williamson, H. C. (2021), *Personality and Social Psychology Bulletin* 47(11), 1565–1579 ([doi:10.1177/0146167220974490](https://doi.org/10.1177/0146167220974490)).

**Read.** Full text: the authors' accepted manuscript, 42 pages, including all tables ([author manuscript](https://sites.utexas.edu/realproject/files/2024/11/too_stressed_to_help.pdf)). The supplements were not read.

**Measured.** All self-reports:
- chronic non-marital stress, on a modified UCLA Life Stress Interview;
- daily stress, one item;
- perceived partner need, own need and own support provision, each one 7-point item.

Accuracy was the within-person slope of perceived need on the partner's self-reported need.

**Design and population.**
- A 14-day diary at the two-year follow-up of a newlywed panel, analysed with dyadic multilevel models.
- 121 couples, of 171 first-married, childless newlywed couples recruited from January 2010.
- About 75–78% White; the authors describe the couples as relatively happy.

**Key result.**
- *Noticing.* Chronic stress weakened husbands' tracking of their wives' needs (b = −.05, p ≈ .001). Their slope fell from .38 to .24 but remained significant. Wives were not affected, and the gender difference was not significant (p = .06).
- *Acting.* Perceived need strongly predicted reported support (b = .77 for husbands, .84 for wives).
  - Chronic stress lowered average support but did not moderate the link from need to support.
  - Daily stress weakened that link for husbands only (b = −.05, p = .011; gender difference p = .08).
  - On high-need days, the slope was **.81 on low-stress days and .72 on high-stress days**: weaker, but still strongly positive.

**Limitations.**
- A relatively happy sample.
- Single-item measures, with support reported by the provider.
- The support item directly followed the need item, a possible demand effect.
- The authors call the gender inferences tentative.

**Does it support the paper's interpretation?** **Overstated** in chapters 7, 8 and 19b and in the README.
- "Failed to act" and "blocks" describe a modest, graded weakening.
- "Intention high" names something never measured; the study measured perceived need, not intention.
- "Less care than they feel" names feelings and recipient experience, neither of which was measured.
- The evidence cannot tell a feasibility bound from a trade-off weight, so the constraint form in §8.4 is a modelling assumption.

**Grade.** **Preliminary**.

**Corrections.**
- Replace the overstated wording: `paper/08-mathematical-representation.md:150` and `:311`, `README.md:46`.
- Downgrade the tag from Moderate/mixed to Preliminary: `paper/08:32`, `README.md:121`.
- Remove "intention high" as a measured signature: `paper/07-revised-model.md:66`.
- Remove "than they feel": `paper/19b-is-love-enough.md:5`.
- Optionally note at `paper/11-romantic-partner-example.md:10` that the effects were in husbands only and graded.
- No change is needed at `paper/04-evidence-for-the-intuition.md:59` or `paper/01-question-and-thesis.md:13`, which are accurate.

#### C15. Hou et al. (2020): parents' and adolescents' reports of parenting

**Study.** Hou, Y., Benner, A. D., Kim, S. Y., Chen, S., Spitz, S., Shi, Y., & Beretvas, T. (2020), *American Psychologist* 75(3), 329–348 ([doi:10.1037/amp0000463](https://doi.org/10.1037/amp0000463)).

**Read.**
- Full text: the NIH author manuscript, including Tables 1–5 ([PMC10624508](https://pmc.ncbi.nlm.nih.gov/articles/PMC10624508/)).
- Korelitz & Garber (2016), in full text, for the age and parent-sex results ([PMC5222679](https://pmc.ncbi.nlm.nih.gov/articles/PMC5222679/)).

**Measured.** Parents' and adolescents' (aged 10–20) reports of the same parenting construct: warmth, behavioural control, psychological control, relationship quality and family functioning. Two quantities were pooled: agreement (r) and the directional mean gap (g).

**Design and population.** A meta-analysis using robust variance estimation of 313 articles. The agreement estimate drew on 280 studies; the mean gap on 221.

**Key result.**
- Agreement r = **.276** [.262, .290].
- Parents reported more positive parenting, g = **.242** [.188, .296]. Heterogeneity was very high (I² = 98.4% for g).
- The mean gap was moderated only by parental internalising symptoms: g = .287 for non-clinical parents against .031 for parents with symptoms.
- The mean gap showed no effect of the adolescent's age, of national individualism, of parent gender or of parent × adolescent gender.
- Agreement was lower in the US and in more individualistic samples.
- Korelitz & Garber found children's reports of acceptance fell below parents' (g = −.50) in samples aged 14 and over.

**Limitations.**
- Retrieval was necessarily incomplete, and about half of eligible articles lacked usable statistics.
- The data are reports of parenting, not of care adequacy.

**Does it support the paper's interpretation?** Qualified.
- The mean gap is supported.
- The age clause at `paper/04-evidence-for-the-intuition.md:20` is credited to Hou et al., but Hou et al. found no age effect; it belongs to Korelitz & Garber.
- g comes from 221 studies, not 313.
- Lower agreement in individualistic societies holds for the correlation, not for the mean gap (`paper/12-asymmetry-and-misperception.md:41`).
- Hou et al. give no support to a gap specific to fathers or to father–daughter dyads. The paper correctly does not cite them in chapter 10.
- More agreement in collectivistic samples argues *against* assuming a larger-than-average reporting gap in the Korean example.

**Grade.** Established for the pooled estimates.

**Corrections.**
- Reattribute the age clause, give 221 of 313 studies and add the low agreement: `paper/04:20`.
- Distinguish agreement from the mean gap: `paper/12:41`.
- Compare dyad-level disagreement with a population mean on the same scale: `paper/05-evidence-against-it.md:46`.

### Culture, provision, acceptance, safety and giver error (C16–C20)

#### C16. Chentsova Dutton, Choi & Choi (2020): kinds of perceived parental support in four countries

**Study.** Chentsova Dutton, Y. E., Choi, I. J., & Choi, E. (2020), *Frontiers in Psychology* 11:353 ([doi:10.3389/fpsyg.2020.00353](https://doi.org/10.3389/fpsyg.2020.00353)).

**Read.** Full text, including all results tables ([PMC7079630](https://pmc.ncbi.nlm.nih.gov/articles/PMC7079630/)). The supplementary item wording was not read.

**Measured.**
- Perceived parental emotional, informational and financial support, three items each on a 1–4 agreement scale. "Financial" meant allowance and necessities, with α = .52–.72.
- Positive self-beliefs.
- Distress, 11 items.

**Design and population.**
- A cross-sectional school survey from 2010 of 7,279 students in grades 10–12: South Korea 3,993, the US 1,002, Japan 1,112 and China 1,172.
- Only configural and metric invariance were tested.

**Key result.**
- *Distress.* Emotional support β = −.188, informational β = −.046, and financial β = −.011 (p = .393).
  - The culture × support interaction block was significant (ΔR² = .003, p = .012), but no single interaction was.
  - Zero-order correlations of financial support with distress were negative and significant in every country (r = −.07 to −.22).
- *Positive self-beliefs.* Financial support was uniquely associated with them (β = .10).
- *Korea versus the US*, with effect sizes computed by the auditors:

  | Support | Korea | US | d | Significance |
  |---|---|---|---|---|
  | Emotional | 2.78 | 3.02 | ≈ −0.32 | — |
  | Financial | 3.13 | 3.06 | ≈ 0.11 | Table 2 marks it non-significant; the text calls it significant |

**Limitations.**
- A single informant.
- "Parents" were not split into mothers and fathers.
- Scalar invariance was untested, and the distress scale fit poorly across groups (RMSEA = .102).
- The data date from 2010.

**Does it support the paper's interpretation?** Qualified.
- The coefficients are quoted exactly.
- "Unrelated to distress" misreads a partial coefficient taken net of collinear support types.
- The paper omits the significant interaction block and the self-beliefs effect.
- The Korea–US financial contrast is trivial and inconsistently reported.
- "Cuts against" cultural relativity overstates a study that never measured whether provision is read as care.

**Grade.** Preliminary.

**Corrections.**
- "Not uniquely associated" instead of "unrelated": `paper/05-evidence-against-it.md:61`, `paper/07-revised-model.md:52`.
- Call the Korea–US financial difference trivial: `paper/10-father-daughter-example.md:28`.
- Avoid "alike" and "predicts", and keep the paragraph tag [Established to Moderate] from covering this study: `paper/13-cultural-effects.md:5`.

#### C17. Costello et al. (2003) and Akee et al. (2010): household income and children's outcomes

**Studies.**
- Costello, E. J., Compton, S. N., Keeler, G., & Angold, A. (2003), *JAMA* 290(15), 2023–2029 ([doi:10.1001/jama.290.15.2023](https://doi.org/10.1001/jama.290.15.2023)).
- Akee, R. K. Q., Copeland, W. E., Keeler, G., Angold, A., & Costello, E. J. (2010), *American Economic Journal: Applied Economics* 2(1), 86–115.

**Read.**
- Costello: abstract only ([PubMed 14559956](https://pubmed.ncbi.nlm.nih.gov/14559956/)), plus a description in D'Onofrio et al. (2009) ([PMC2933111](https://pmc.ncbi.nlm.nih.gov/articles/PMC2933111/)). JAMA refused automated access.
- Akee: full text, as the NIH author manuscript ([PMC2891175](https://pmc.ncbi.nlm.nih.gov/articles/PMC2891175/)).

**Measured.**
- Costello: DSM-IV symptom levels.
- Akee: education, arrests, parental work and supervision, and child-reported interactions with parents.

**Design and population.** The Great Smoky Mountains Study: 1,420 rural children aged 9–13 at intake, 350 of them American Indian, assessed from 1993 to 2000.
- A casino began making per-capita payments to American Indian families. 14% of families left poverty, 53% stayed poor and 32% were never poor.
- Akee used a difference-in-differences design.

**Key result.**
- *Costello.* Before the payments, persistently poor and ex-poor children had more symptoms (4.38 and 4.28) than never-poor children (2.75).
  - Afterwards the ex-poor children reached never-poor levels (OR 0.91, 0.77–1.07), while the persistently poor stayed high (OR 1.50, 1.08–2.09).
  - The effect was confined to conduct and oppositional symptoms; anxiety and depression were unaffected.
- *Akee.*
  - The full-sample education effect was not significant.
  - Children in previously poor households gained 1.1 years of schooling.
  - Arrests at ages 16–17 fell by 22%, for minor offences only.
  - The authors infer improved parenting quality as a likely mechanism.

**Limitations.**
- Exit from poverty was exogenous only for American Indian families.
- One rural US region.
- No measure of how children perceived the income.
- The transfer was not a parent's act of care.

**Does it support the paper's interpretation?** Qualified.
- `paper/07-revised-model.md:51` matches the abstract.
- `paper/07:47` overreaches: that benefits "arrive whether or not they are perceived as love" was never tested, and Akee et al.'s mechanism evidence points partly to relational channels.

**Grade.** Moderate for income improving conduct symptoms, and schooling and minor arrests in poor households. Attributing the effect to a route is Our hypothesis.

**Corrections.**
- Reword the route evidence: `paper/07:47`.
- Tag [Moderate; one rural US natural experiment; abstract-level check]: `paper/07:51`.
- Costello supports only the behavioural part of `paper/03-literature-review.md:107`.

#### C18. Khaleque & Rohner (2002; 2012): perceived parental acceptance and adjustment

**Studies.**
- Khaleque, A., & Rohner, R. P. (2002), *Journal of Marriage and Family* 64(1), 54–64 ([doi:10.1111/j.1741-3737.2002.00054.x](https://doi.org/10.1111/j.1741-3737.2002.00054.x)).
- Khaleque, A., & Rohner, R. P. (2012), *Journal of Cross-Cultural Psychology* 43(5), 784–800 ([doi:10.1177/0022022111406120](https://doi.org/10.1177/0022022111406120)).

**Read.** Abstracts only ([2002 abstract](https://api.crossref.org/works/10.1111/j.1741-3737.2002.00054.x); [2012 abstract](https://api.crossref.org/works/10.1177/0022022111406120)). The 2002 article is listed as free to read, but automated retrieval was refused.

**Measured.** Child- or adult-reported parental acceptance–rejection (the PARQ) and self-reported adjustment (the PAQ), usually completed by the same respondent.

**Design and population.** Meta-analyses by the theory's originators. The 2002 analysis covered 43 studies; the 2012 analysis covered 66 studies with 19,511 respondents in 22 countries.

**Key result.**
- *2002.* The predicted relation appeared in every study, with r = **.51** for children and **.46** for adults.
- *2012.* Acceptance by mothers and by fathers was associated with adjustment in all cultures.
- *Companion reliability meta-analysis.* Cross-cultural reliability evidence for the PAQ was insufficient ([2002b abstract](https://api.crossref.org/works/10.1177/0022022102033001006)).

**Limitations.**
- Both scales are usually completed by the same respondent.
- The data are cross-sectional.
- Publication bias was assessed only with fail-safe N.
- Heterogeneity is unverified.

**Does it support the paper's interpretation?** Qualified. The association is supported, and the caveat at `paper/03-literature-review.md:105` is good. "Predicts … everywhere" (`paper/06-competing-theories.md:14`) and "predicts adjustment across cultures" (`paper/07-revised-model.md:48`) overstate. The association is consistent with a symbolic route but does not test one.

**Grade.** Established association. No causal or route grade.

**Corrections.** `paper/06:14`, `paper/07:48`.

#### C19. Arriaga, Capezza & Daly (2016): commitment and tolerance of partner aggression

**Study.** Arriaga, X. B., Capezza, N. M., & Daly, C. A. (2016), *Journal of Personality and Social Psychology* 110(1), 36–54 ([doi:10.1037/pspi0000035](https://doi.org/10.1037/pspi0000035)).

**Read.** Abstract only ([PubMed 26461796](https://pubmed.ncbi.nlm.nih.gov/26461796/)). The full text is closed, and no repository copy was found.

**Measured.**
- Personal standards, or tolerance, for judging a partner's aggressive acts.
- Experienced aggression.
- Commitment, as a measured moderator.
- **The abstract reports no measure of love or perceived love.**

**Design and population.**
- Studies 1a and 1b: cross-sectional, n = 689.
- Study 2: longitudinal, n = 52, none with prior partner aggression.
- Study 3: an experiment with n = 73 people reporting current aggression. It manipulated whether imagined acts came from the partner or from a stranger.
- Sample sources are unverified.

**Key result.**
- Experienced aggression and greater commitment predicted more tolerant standards.
- Once aggression began, standards became more tolerant only among the highly committed.
- The highly committed were more tolerant of acts imagined from the partner than from a stranger.

**Limitations.**
- Commitment was measured, not manipulated.
- Verification was at abstract level only.
- Sample origins are unknown.

**Does it support the paper's interpretation?** **Overstated** where it carries the safety constraint. The narrow uses at `paper/03-literature-review.md:127` and `paper/05-evidence-against-it.md:67` match the abstract. The following do not:
- "felt love and commitment can rise as safety falls" (`README.md:130`, `paper/08-mathematical-representation.md:41`);
- "love and commitment measures can move in the wrong direction" (`paper/08:290`);
- "danger signals … opposite … from love ratings" (`paper/02-definitions-and-distinctions.md:31`);
- "harm not offset by love" (`paper/08:319`);
- love as "produced by commitment" (`paper/19b-is-love-enough.md:9`).

The study supports a narrower and still useful design argument: a committed receiver's own judgments of acceptable aggression drift toward tolerance, so they cannot define safety.

**Grade.** Moderate/mixed for the narrow tolerance-standards finding. Not supported for love or commitment rising as safety falls.

**Corrections.**
- Rewrite each sentence listed above.
- Rename the row at `paper/03:155` to concern victims' tolerance judgments.
- Change "commitment raised/shifts" to "among highly committed people": `paper/15-counterexamples.md:24`, `paper/03:127`.
- Revise the related uses at `paper/01-question-and-thesis.md:15` and `:30` and `paper/07-revised-model.md:68`.

#### C20. Flynn & Adams (2009): gift price and appreciation

**Study.** Flynn, F. J., & Adams, G. S. (2009), *Journal of Experimental Social Psychology* 45(2), 404–409 ([doi:10.1016/j.jesp.2008.11.003](https://doi.org/10.1016/j.jesp.2008.11.003)).

**Read.** Secondary only: press accounts ([Science News](https://www.sciencenews.org/article/when-giving-gifts-price-wrong); [Stanford GSB](https://www.gsb.stanford.edu/insights/research-confirms-its-thought-counts)). The publisher elided the abstract, and ScienceDirect refused access.

**Measured.** Givers' expected appreciation against recipients' reported appreciation, and gift price.

**Design and population.** Three US studies, as described in the press:
- 33 recently engaged individuals rating real rings;
- 232 online adults who recalled a birthday gift, randomly assigned to the giver or recipient role;
- 197 participants in a hypothetical graduation-gift scenario.

**Key result.** Givers expected costlier gifts to be appreciated more; recipients' appreciation did not rise with price. Statistics are unverified.

**Limitations.**
- Small samples.
- Separate givers and recipients, rather than matched pairs, in Studies 2 and 3.
- A hypothetical Study 3.
- One-off gifts between adults.
- Flynn himself predicted different results for children, as reported in the news piece.

**Does it support the paper's interpretation?** Qualified. `paper/04-evidence-for-the-intuition.md:23` is consistent with the press accounts. `paper/10-father-daughter-example.md:30` extrapolates, untested, from one-off adult gifts and appreciation to a parent's ongoing provision registering as love. "Strangers" in `paper/03-literature-review.md:151` does not describe this study.

**Grade.** Preliminary.

**Corrections.**
- State the press-only depth: `paper/04:23`.
- Change the base from Moderate/mixed to Preliminary: `paper/10:30`.
- Drop "strangers" for this study: `paper/03:151`.

### Supplementary claims (S1–S4)

| Claim | Study and verification | What the source shows | Verdict | Grade | Correction |
|---|---|---|---|---|---|
| **S1** | Gottman, J. M., et al. (1976), *JPSP* 34(1), 14–23 ([doi:10.1037/0022-3514.34.1.14](https://doi.org/10.1037/0022-3514.34.1.14)). **Secondary only.** The only summary is a blog post at the lead author's institute ([Gottman Institute](https://www.gottman.com/blog/the-research-behavior-exchange-theory-and-marital-decision-making/)). | The blog describes couples who classed themselves as distressed or not, rating intended and received impact during decision tasks. Intent did not differ; distressed spouses' messages were received more negatively. No sample size or statistics are given, and the blog omits one of the six authors. | Cannot determine. The paper's hedges ("reportedly", secondary summary, [Preliminary]) are appropriate. | Preliminary | At `paper/04-evidence-for-the-intuition.md:9`, drop "classic" and add that the sample size and statistics are unknown and that the summary comes from the lead author's institute. |
| **S2** | Lakey, B., McCabe, K. M., Fisicaro, S. A., & Drew, J. B. (1996), *JPSP* 70(6), 1270–1280 ([PubMed 8667167](https://pubmed.ncbi.nlm.nih.gov/8667167/)). **Abstract.** An erratum, JPSP 71(2):210, was not retrieved. | Three generalizability studies. The perceiver × supporter interaction contributed most to perceived supportiveness, then supporter characteristics, then perceiver biases. Percentages are not in the abstract. | Supported, for the ordinal claim only | Moderate | Add [Moderate; abstract-level] at `paper/03-literature-review.md:24`. Do not add percentages until the full text and erratum are read. Hypothesis H6 (`paper/18-proposed-study.md:22`) relies on this decomposition. |
| **S3** | Rohner, R. P., & Pettengill, S. M. (1985), *Child Development* 56(2), 524–528 ([PubMed 3987420](https://pubmed.ncbi.nlm.nih.gov/3987420/)). **Abstract.** | Korean youths' perceived parental control correlated positively with perceived warmth and low neglect. The authors contrast this with *other studies* of North American youth, not with a US sample of the same design. N is not in the abstract. | Qualified | Preliminary | Give the 1985 study its own [Preliminary; N unverified] tag within the Moderate/mixed row at `paper/13-cultural-effects.md:32`. |
| **S4** | Levine, R., Sato, S., Hashimoto, T., & Verma, J. (1995), *JCCP* 26(5), 554–571 ([doi:10.1177/0022022195265007](https://doi.org/10.1177/0022022195265007)). **Abstract.** | College students in 11 countries rated love as most important for marriage in Western and Westernised nations. No "marry without love" percentages appear in the abstract. | Cannot determine. Not used in the paper. | Not used | None. If it is cited later, use only the qualitative pattern among students, avoid the abstract's dated "underdeveloped Eastern" framing, and do not cite country percentages until the primary has been read. |

## What the audit changes for the theory, and what it leaves standing

**The mathematics stays frozen, because the notes document no error in it.** Every correction concerns the evidence attached to an equation, the justification for a form, or the wording around it:

- The constraint form of enactment (eq. 1) was already labelled an assumption. The sentence claiming that evidence "describes bounds" (`paper/08-mathematical-representation.md:150`) must go.
- The level bias δ (eq. 3) is a free parameter. Only its described sign is wrong.
- An asymmetric loss in the fit surface (eq. 5) is already framed as an empirical question in §8.7. It simply loses its main quantitative support.
- $`\beta_{\text{sub}}`$ (eq. 6) remains a parameter. That it is non-zero in close relationships drops from [Moderate to Established] to **[Our hypothesis]**.
- The admissibility rule (eq. 10) stands on normative and design grounds plus the narrower tolerance finding. That finding is arguably a sharper argument for deciding $`\mathrm{Safe}(x)`$ from behaviourally specific indicators rather than from the receiver's own judgments.
- Autonomy as a separate outcome rests on sources this audit did not examine, and is unaffected.

**The verdict table needs rewording in four of its five rows, and in five of the six model components whose evidence the audit could check.** The narrowest defensible statement of each verdict clause:

| Clause | Narrowest defensible statement |
|---|---|
| Intended ≠ expressed | Plausible. One diary study shows stress dampening provider-reported support for perceived needs [Preliminary]. Intention itself is unmeasured. |
| Expressed ≠ perceived | Supported as **disagreement between giver and receiver reports** [Moderate/mixed]. Loss measured against an objective record has not been shown. |
| Perceived ≠ received | Supported in one direction, in a laboratory analogue: support rated as more supportive raised distress when it signalled inefficacy. Benefit without perception is mixed. |
| Received ≠ compatibility | Unaudited. |
| "Translation, not amount" | The comparative "rather than" is unsupported in either direction. One's own love predicts whether non-marital relationships last, and the primary-language claim fails, but neither result shows that translation failures are rare. |

Of the audited model components, the evidence columns for components 1, 3, 5, 6 and 10 need rewording. Component 2 (detection) stands. Components 4, 7, 8 and 9 were not audited.

The same findings are available as data in [`claims-audit.csv`](claims-audit.csv). The notes behind them, with full extraction detail, are [`evidence/notes/08`–`11`](../evidence/notes/). The corrections they imply are collected in [`corrections.md`](corrections.md).
