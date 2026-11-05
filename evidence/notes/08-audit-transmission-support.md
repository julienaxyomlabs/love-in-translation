# Primary-source audit R1: how care is lost between what one partner does and what the other perceives (claims C01–C05)

Scope and provenance. This audit covers five empirical claims in "Can Love Be Lost in Translation?" (this repository, v0.2.0, read only, not modified). Paper locations are given as `file:line` relative to that repository root. Primary sources were reached only through open routes: CMU's KiltHub repository (C01), Sussex Research Online on figshare (C02), Europe PMC, PubMed and OpenAlex abstracts (C03, C04), and an author-posted PDF on Niall Bolger's Columbia page (C05). An author manuscript of the same group's replication chapter came from Columbia Psychology's site and was used for C04.

Two routes were tried and not used:
- **Haber et al. (2007).** The green open-access copy on Deep Blue is behind an automated-access challenge, which was not bypassed.
- **Bolger et al. (2000).** The CiteSeerX copy redirects to web.archive.org, which the fetch tool cannot reach. Copies on aggregator sites of unclear authorization (typeset.io) were not used.

Local working copies of the extracted texts are kept outside the repository:
- `working-files/audit_R1/bolger_amarel_2007.txt`
- `working-files/audit_R1/visserman_2019.txt`
- `working-files/audit_R1/shrout_2009.txt`
- The Coriell & Cohen PDF is a scanned image with no text layer. It is at `working-files/audit_R1/src_coriell/coriell_cohen_1995.pdf` and was read page by page as images.

Evidence grades below use the four-level scale requested for this audit (Established / Moderate or mixed / Preliminary / Theoretical). They are compared with the paper's own tags, which are defined in `paper/00-summary.md`, lines 13–22. All coefficients are copied from the source tables and text. Minus signs lost in PDF extraction were restored from the table layout, the confidence intervals and the authors' wording.

## C01: Coriell & Cohen (1995). Do giver and receiver agree that a supportive act happened (κ ≈ .39)?

### Takeaway
The figure κ = .39 is reported correctly, but it is the **mean within-dyad agreement across 67 helpful *and harmful* behaviours**. The dyads were US college students and the close friends or roommates they chose as supporters. Agreement on the helpful (supportive) behaviours alone was lower, at **κ = .28**, and on harmful behaviours it was κ = .14. The authors stress that disagreement cannot be attributed to missed perception rather than over-reporting, and that checklist unreliability probably deflates κ. **Verdict: supported with qualifications.** The [Moderate/mixed] tag can stay, but "partners" and "supportive act" should be reworded.

### Cited Findings
- **How the paper uses it:**
  - `paper/00-summary.md:5`: "Partners agree only moderately on whether a supportive act even happened (**κ ≈ .39**)."
  - `paper/01-question-and-thesis.md:14`: "Occurrence agreement κ = .39", inside a row tagged "Moderate to Established".
  - `paper/03-literature-review.md:23`: students and supporters "independently reported which supportive behaviours had occurred after an exam, agreement was κ = .39" [Moderate/mixed].
  - `paper/04-evidence-for-the-intuition.md:7`: "Supporters and recipients agreed only at κ = .39 about which supportive behaviours had taken place."
  - `paper/12-asymmetry-and-misperception.md:22`: cited as a method for measuring "Occurrence (facts)".
  - `README.md:47`: "Occurrence agreement κ ≈ .39".
- **Verification depth: full text.** The published JPSP version (scanned) is held in CMU's KiltHub repository, and pp. 289–298 were read (abstract, introduction, Method, Results with Tables 1–4 and Figure 1, Discussion, Considerations and Conclusions). The reference list on p. 299 was not read. — [KiltHub record](https://doi.org/10.1184/R1/6614096.v1); [file](https://ndownloader.figshare.com/files/12106754); [DOI](https://doi.org/10.1037/0022-3514.69.2.289)
- **Design.**
  - In the first week of term, students listed which supporter behaviours they *expected* for their first major introductory-psychology exam, which was worth one third of the grade.
  - In the class period after the exam, before any feedback, students checked which of 67 behaviours their supporter had actually provided.
  - Within 3 days, supporters checked, in supervised sessions, which behaviours they had provided. The two sides were not told their answers would be compared.
  - Agreement was computed as Cohen's κ within each dyad from a 2×2 table (student "received" × supporter "provided") and then averaged across dyads.
  - The design is a one-off retrospective checklist comparison, not a diary, and there is no causal manipulation. — [Coriell & Cohen 1995, pp. 291–292](https://doi.org/10.1184/R1/6614096.v1)
- **Population.**
  - 297 dyads drawn from eight introductory-psychology classes at Carnegie Mellon (Pittsburgh, US), recruited for extra credit: 212 freshmen, 78 sophomores and 7 juniors, median age 18 (range 17–46).
  - Students were 57% men and supporters 53% men.
  - Dyad types were 99 man–man, 71 woman–woman and 127 mixed-gender.
  - Each supporter was a close friend or roommate whom the student chose as their main peer supporter. The authors could not tell which mixed-gender dyads were romantic.
  - Social-competence and communal-orientation analyses used 220 dyads. The year of data collection is not stated in the pages read. — [Coriell & Cohen 1995, pp. 291, 297](https://doi.org/10.1184/R1/6614096.v1)
- **What was measured.** The 67 behaviours came from 22 students. Student judges (70% criterion) classed 36 as helpful and 31 as harmful. Examples are "gave good advice about studying for the exam" and "distracted me from my work". The study also measured intimacy (3 items, α = .67), social competence (α = .81 for students, .77 for supporters), communal orientation (α = .76) and fulfilled expectancies (a κ between expected and received behaviours). — [Coriell & Cohen 1995, pp. 291–292](https://doi.org/10.1184/R1/6614096.v1)
- **Key results.**
  - Table 1 gives mean total concordance **κ = .39 (SD .21)**, helpful behaviours **κ = .28 (SD .21)** and harmful behaviours **κ = .14 (SD .26)**.
  - Concordance correlated with fulfilled expectancies (r = .53), intimacy (r = .41), student communal orientation (.27), supporter communal orientation (.23) and social competence (.16, .18).
  - In a simultaneous regression the six variables explained 41% of the variance in concordance; fulfilled expectancies alone contributed 18% independently.
  - Concordance was higher for helpful than harmful behaviours (t(296) = 7.70). Man–man dyads were the least concordant. Intimacy and fulfilled expectancies together accounted for 89% of the gender-pairing effect. — [Coriell & Cohen 1995, pp. 293–296](https://doi.org/10.1184/R1/6614096.v1)
- **Limitations stated by the authors.**
  - Naturalistic concordance studies have "no objective verification of what really happened". A disagreement could be a behaviour that occurred but was not attended to, encoded or remembered, or a behaviour reported that did not occur.
  - Because the behaviour checklist's reliability is imperfect and was not assessed, the κ values are underestimates of true agreement.
  - Agreement might be higher for broad support categories than for specific behaviours.
  - Greater concordance on helpful behaviours may be limited to primary, historically supportive relationships. — [Coriell & Cohen 1995, pp. 296–298](https://doi.org/10.1184/R1/6614096.v1)

### Inferences
- **Support judgment: Supported with qualifications.**
  - The number is right, but it covers helpful and harmful acts together. For the "supportive acts" the paper describes, agreement was weaker (κ = .28), which actually strengthens the paper's point.
  - The study shows *disagreement about occurrence*. It cannot show that care was *lost* between expression and perception: by design, misses cannot be told apart from over-reports by supporters or false reports by recipients. The paper acknowledges this elsewhere (`paper/08-mathematical-representation.md:160`).
- **Population mismatch.** `00-summary.md:5` says "Partners", which in a paper about love will be read as romantic partners. The dyads were students and same-age friends or roommates around a single exam.
- **Timing.** `03:23` says behaviours "had occurred after an exam". The behaviours occurred during exam preparation and were *reported* after the exam.
- **Additional limitations.**
  - Retrospective recall over several weeks.
  - Students' expectations strongly predicted concordance (r = .53), so students may partly report what they expected rather than what they registered. This fits the paper's perceiver-driven account but means κ mixes perception with schema-driven recall.
  - A single exam stressor, one US university, and an unknown collection year.
- **Evidence grade.** Moderate or mixed for the general proposition that providers and recipients agree only moderately on which specific support acts occurred. It is consistent with the C02 and C04 sources. The specific κ value is a single-study estimate (under the paper's own rubric, a single convenience-sample study would be [Preliminary]). Keep the [Moderate/mixed] tag, but attach the population and the helpful-only figure. The "Moderate to Established" row tag at `01:14` is acceptable only because that row pools several findings.
- **Proposed wording for `00-summary.md:5` and `04:7`.** "In 297 US student–supporter pairs (friends or roommates), reports of which of 67 helpful or harmful behaviours had occurred during exam preparation agreed only moderately (mean within-pair κ = .39; κ = .28 for helpful behaviours alone). Without an objective record, disagreement cannot be assigned to missed perception or to over-reporting."

### Gaps
- The year of data collection and the number of behaviours each side endorsed on average (beyond the expected-behaviour counts) were not extracted.
- Kappa depends on prevalence. The study does not report how much of the low harmful-behaviour κ reflects low base rates.
- No later replication of this specific κ in romantic or family dyads was checked.

## C02: Visserman et al. (2019). Missed sacrifices, "false-alarm" gratitude and the sacrificer's satisfaction

### Takeaway
The core findings replicate across two diary samples:
- About 46–47% of the days on which a partner reported a sacrifice were missed by the other partner.
- Perceived sacrifices, whether hits or "false alarms", were associated with higher same-day gratitude.
- Missed sacrifices were not associated with higher gratitude.

Several of the paper's uses go further than the source:
- The share of "seen" sacrifices the partner did not report was about half only in the Dutch sample (≈46–47%). It was 39.8% in the US sample, significantly fewer than hits.
- The lower satisfaction of sacrificers on missed days was **marginal in Study 1 (p = .069)** and significant in Study 2 (p = .017). It is small and correlational, and only miss days were compared with hit days.
- "False alarms" mean only that the partner did *not report* a sacrifice. They are not evidence that no sacrifice or no benefit occurred.
- The paper repeats the abstract's total N = 426. The Method sections sum to 412.
- The paper describes the limitation as "Two studies, one laboratory". This is inaccurate: the two samples came from different countries and projects.

**Verdict: supported with qualifications. Some sentences are overstated, and one use is not supported** (false alarms as "perception without benefit").

### Cited Findings
- **How the paper uses it:**
  - `paper/00-summary.md:5`: "**About half of romantic sacrifices go unnoticed**, and about half of the sacrifices people 'see' were not reported by the partner."
  - `paper/01-question-and-thesis.md:14`: "about half of sacrifices missed".
  - `paper/01-question-and-thesis.md:15`: "'false-alarm' sacrifices still produce gratitude", offered as evidence that "perception can occur without benefit".
  - `paper/02-definitions-and-distinctions.md:17`: "about half of sacrifices are missed".
  - `paper/02-definitions-and-distinctions.md:18`: "Can someone perceive love without receiving appropriate care? Yes. Perceived 'false-alarm' sacrifices still produce gratitude".
  - `paper/03-literature-review.md:52`: "two daily-experience studies (N = 426) … as likely to be missed as detected … about half the sacrifices people 'saw' had not been reported … Perceived sacrifices, accurate or not, produced gratitude. Missed sacrifices produced none, and on days they sacrificed, unrecognized givers were less satisfied" [Moderate/mixed].
  - `paper/03-literature-review.md:140`: "perception, not accuracy, drives gratitude | Moderate/mixed | … | Two studies, one laboratory; enactor report is not ground truth".
  - `paper/04-evidence-for-the-intuition.md:7`: sacrifices "as likely to be missed as detected".
  - `paper/04-evidence-for-the-intuition.md:65`: "Givers whose sacrifices went unnoticed were less satisfied on those days".
  - `paper/05-evidence-against-it.md:30`: "Perceived sacrifices produced gratitude whether or not they had occurred".
  - `paper/07-revised-model.md:34`: "unrecognized givers lose satisfaction" [Moderate/mixed].
  - `paper/07-revised-model.md:48`: "gratitude depends on perceived, not actual, sacrifice".
  - `paper/07-revised-model.md:63`: failure type 1, "Undetected care".
  - `paper/08-mathematical-representation.md:33` and `README.md:122`: "About half of sacrifices go unnoticed" [Moderate/mixed].
  - `paper/08-mathematical-representation.md:158` and `:312`: the giver's report as the signal; misses and false alarms.
  - `paper/08-mathematical-representation.md:261`: "invisible care, which produces no gratitude".
  - `paper/10-father-daughter-example.md:34`: "unrecognized givers lose satisfaction".
  - `paper/11-romantic-partner-example.md:8`: "A's unthanked effort lowers A's own satisfaction".
  - `paper/14-time-and-feedback.md:20`: "invisible care earns no thanks".
  - `README.md:47–48`: "about half of sacrifices go unnoticed"; "'false-alarm' sacrifices still earn gratitude".
- **Verification depth: full text.** The published version (CC BY-NC 4.0) is held in Sussex Research Online, and pp. 317–324 were read, including Notes 1–3. The online supplement (predictors of detection) and the OSF data were not read. — [Sussex figshare record](https://sussex.figshare.com/articles/journal_contribution/To_see_is_to_feel_grateful_A_quasi-signal_detection_analysis_of_romantic_partners_sacrifices/23493755); [DOI](https://doi.org/10.1177/1948550618757599)
- **Design.**
  - Two dyadic daily-experience studies. Each evening, both partners answered yes or no to whether they had sacrificed and whether their partner had sacrificed.
  - Each day was coded as a hit, miss, false alarm or correct rejection, with the partner's self-report as the criterion.
  - Multilevel models (participants and days crossed within dyads, random intercepts, dyads treated as indistinguishable) predicted gratitude and controlled for the previous day's gratitude.
  - Satisfaction effects were tested only on hit-or-miss days (miss = 1, hit = 0) with sequential mediation in Mplus.
  - Follow-ups were run at 1 year (Study 1) and 3 months (Study 2).
  - Couples were trained at intake to recognise sacrifices. Data and syntax are posted on OSF (osf.io/dhmca). — [Visserman et al. 2019, pp. 318–320](https://doi.org/10.1177/1948550618757599)
- **Population.**
  - Study 1: 125 heterosexual couples and 1 lesbian couple in the Netherlands (N = 252; mean age 23.3; 64% university students; 35% cohabiting; 8-day diary; 87.6% of surveys completed).
  - Study 2: 75 heterosexual, 4 lesbian and 1 gay male couple in the San Francisco Bay Area (N = 160; mean age 23.9; about half students; 48% cohabiting; 14-day diary).
  - Both were secondary analyses of larger projects.
  - **The abstract says total N = 426, but 252 + 160 = 412.** — [Visserman et al. 2019, pp. 317, 319, 321](https://doi.org/10.1177/1948550618757599)
- **What was measured.** Sacrifice was a single daily yes/no item; more than one sacrifice in a day still counts as one day. Gratitude, perceived appreciation and satisfaction were single daily items: on a 0–6 scale in Study 1, and on 1–5 scales in Study 2, where gratitude was rated as grateful/appreciative/thankful. — [Visserman et al. 2019, pp. 319, 321](https://doi.org/10.1177/1948550618757599)
- **Detection results.**
  - Study 1 day counts: hits 234 (13.6%), misses 202 (11.8%), false alarms 210 (12.2%), correct rejections 1,073 (62.4%).
  - Study 1 rates: hits 52.6% and misses 47.3% of partner-reported sacrifices (Z = 1.53, p = .126). Of perceived sacrifices, 53.7% were accurate and 46.3% were false alarms (Z = 1.14, p = .254).
  - Study 2 day counts: hits 218, misses 194, false alarms 144, correct rejections 1,093.
  - Study 2 rates: hits 52.9% and misses 47.1% (p = .238). Of perceived sacrifices, **60.2% were hits and 39.8% false alarms (Z = 3.89, p < .001)**.
  - Note: the in-text Study 1 percentages look transposed relative to the Table 2 counts. The counts give 53.7% detection and 52.7% precision. Both readings are still about half. — [Visserman et al. 2019, pp. 320–321](https://doi.org/10.1177/1948550618757599)
- **Gratitude results.** Coefficients are relative to correct-rejection days, controlling for the previous day's gratitude.

  | | Hit | Miss | False alarm |
  |---|---|---|---|
  | Study 1 | b = .19, 95% CI [.04, .34], p = .015 | b = −.11, [−.26, .04], p = .159 | b = .18, [.04, .33], p = .015 |
  | Study 2 | b = .38, [.23, .54], p < .001 | b = .03, [−.12, .19], p = .671 | b = .41, [.24, .59], p < .001 |

  Results held when controlling for positive mood or positive emotions. — [Visserman et al. 2019, Tables 3 and 5, Note 3](https://doi.org/10.1177/1948550618757599)
- **Satisfaction results.** These compare miss days with hit days.
  - Perceivers were less satisfied on miss days, mediated by lower gratitude: total effect b = −.19 (p = .048) in Study 1 and −.24 (p = .011) in Study 2.
  - For the **sacrificer**, the total effect was b = −.16, 95% CI [−.34, .01], **p = .069 in Study 1**, and b = −.23, 95% CI [−.43, −.04], **p = .017 in Study 2**.
  - The sequential indirect effect (miss → lower perceiver gratitude → lower perceived or felt appreciation → lower satisfaction) was small: b = −.008, p = .045 in Study 1 and b = −.05, p = .022 in Study 2. The direct effects were not significant.
  - In Study 1 the appreciation-to-satisfaction link held for women only (Note 1).
  - In the full models against correct-rejection days (Note 2), misses did not predict partner satisfaction in Study 1, and predicted it at b = −.12 (p = .044) in Study 2. — [Visserman et al. 2019, pp. 320–323](https://doi.org/10.1177/1948550618757599)
- **Follow-up.** Average rates of hits, misses and false alarms did not clearly predict gratitude 1 year later (Study 1: hits p = .127) or 3 months later (Study 2: hits p = .069). The authors report no evident long-term effect. — [Visserman et al. 2019, p. 322](https://doi.org/10.1177/1948550618757599)
- **Limitations stated by the authors.**
  - The causal direction of the associations cannot be confirmed.
  - Satisfaction findings rest on a subset of days (hits and misses) and need a larger sample.
  - As a strength, they cite ecological validity and replication across two Western countries.
  - They note that sacrificers may sometimes downplay or "play up" their sacrifices. — [Visserman et al. 2019, pp. 322–323](https://doi.org/10.1177/1948550618757599)

### Inferences
- **Supported:**
  - About half of partner-reported sacrifice days go undetected (≈46–47% in both samples).
  - Misses are about as common as hits.
  - Perceiving a sacrifice, accurate or not, goes with higher same-day gratitude.
  - Missed sacrifices are not followed by higher gratitude.
- **Supported with qualifications:**
  - "About half of the sacrifices people 'see' were not reported" holds for Study 1 only. Study 2 found 39.8%, significantly below half. Suggested wording: "40–46% of perceived sacrifices were not reported by the partner."
  - The unit is days with at least one self-reported sacrifice, not individual acts.
- **Overstated:**
  - "Unrecognized givers lose satisfaction" (`07:34`, `10:34`) and "lowers A's own satisfaction" (`11:8`) use causal and change language. The data show slightly lower same-day satisfaction on miss days than on hit days, marginal in one sample and significant in the other. The effects are small (b ≈ −.16 to −.23 on 7- or 5-point single items), and the authors say causal direction cannot be confirmed.
  - "Produced", "drives" and "depends on" (`03:52`, `03:140`, `07:48`) should be "was associated with".
- **Not supported as worded:**
  - "Perceived sacrifices produced gratitude whether or not they had occurred" (`05:30`) and "perceived, not actual, sacrifice" (`07:48`). The criterion is the partner's self-report, so a false alarm may be a real act the partner did not count as a sacrifice. The paper itself says the enactor report "is not ground truth" (`03:140`; `08:160`).
  - Using false alarms as evidence that "perception can occur without benefit" (`01:15`) or that one can "perceive love without receiving appropriate care" (`02:18`). Neither care received nor benefit was measured on false-alarm days.
  - The limitation "Two studies, one laboratory" (`03:140`) is inaccurate. The samples came from a Dutch project (VU Amsterdam) and a US project (San Francisco Bay Area). Better: "two short diary studies (8 and 14 days) of young Dutch and US couples; partner self-report as criterion; associational".
- **Generalisation.** "Invisible care earns no thanks" (`14:20`) and "produces no gratitude" (`08:261`) extend a finding about *sacrifices* and same-day *felt gratitude* to all invisible care. The follow-ups found no evident long-term effect of detection on gratitude, so the dynamic feedback story in `08:261` and `14:20` remains [Our hypothesis], as the paper labels it.
- **Additional limitations not stressed by the authors.**
  - Young, partly student samples in short relationships (1.3–2.8 years).
  - Diaries of 8 and 14 days.
  - Single-item outcomes.
  - Intake training on recognising sacrifices may have raised detection above everyday levels.
- **Evidence grades.**
  - Moderate or mixed for detection rates and for the gratitude associations: two samples, consistent, associational. The paper's tag fits.
  - **Preliminary** for the sacrificer-satisfaction effect: significant in one sample only, small, and dependent on a mediation chain. It should not carry [Moderate/mixed] at `07:34` or `10:34`.
- **Proposed wording for `03:52`.** "In two diary studies of young couples (126 Dutch and 80 US couples), about half the days on which a partner reported a sacrifice went undetected, and 40–46% of the sacrifices people 'saw' were not reported by the partner. Perceived sacrifices, matching the partner's report or not, were associated with higher same-day gratitude; undetected ones were not. On days their sacrifice went undetected, sacrificers reported slightly lower satisfaction than on days it was detected (significant in the US sample, marginal in the Dutch one) [Moderate/mixed; satisfaction effect Preliminary]."

### Gaps
- The online supplement (whether communication, cost or type of sacrifice predicts detection) and the OSF data were not read, so the claim that detection is "largely independent" of these factors is taken from the main text only.
- The source does not explain why its abstract N (426) differs from its Method N (412).
- Data-collection years are not stated in the article.

## C03: Haber, Cohen, Lucas & Baltes (2007). Received and perceived support, r ≈ .35 across 23 studies

### Takeaway
The abstract confirms the numbers: 23 studies, average r = .35, p < .001. The squared value, .35² ≈ .12, matches the "about 12% shared variance" in the summary. The study correlates **two self-reports by the same person**, so the paper's framing of it as evidence that "care given and care received come apart" does not fit. Received support was measured with the Inventory of Socially Supportive Behaviors (ISSB), and perceived support with "any measure of perceived social support". No provider report is involved. The meta-analysis shows that two recipient-side constructs are distinct; it does not show that givers and receivers diverge. The full text could not be read, so confidence intervals, heterogeneity, moderators, correction for attenuation and study designs are unverified. **Verdict: the number is supported; the interpretation needs qualifying.**

### Cited Findings
- **How the paper uses it:**
  - `paper/00-summary.md:5`: "Received and perceived support share only **about 12% of their variance** (r ≈ .35)."
  - `paper/03-literature-review.md:21–22`: "Support research supplies the clearest quantitative evidence that care given and care received come apart: Across 23 studies, *received* support (reported enacted behaviours) and *perceived* support (felt availability) correlated only **r = .35**" [Established for that measure pairing].
  - `paper/03-literature-review.md:137`: "Received and perceived support are distinct (r ≈ .35) | Established | … | One received-support inventory; mostly cross-sectional".
  - `paper/06-competing-theories.md:8`: cited as the best evidence for social support theory, in a row tagged "Moderate to Established".
- **Verification depth: abstract only.** The abstract was read via Europe PMC and PubMed (PMID 17308966) and OpenAlex. OpenAlex lists a green open-access author version at Deep Blue (hdl 2027.42/117157), but the repository returned an automated-access challenge and it was not bypassed. — [Europe PMC](https://europepmc.org/article/MED/17308966); [PubMed](https://pubmed.ncbi.nlm.nih.gov/17308966/); [Deep Blue handle](https://hdl.handle.net/2027.42/117157); [DOI](https://doi.org/10.1007/s10464-007-9100-9)
- **Design and measures, from the abstract.** A meta-analysis of all available studies that used the ISSB together with any measure of perceived social support. The abstract defines received support as receipt of supportive behaviours and perceived support as support perceptions. — [Europe PMC abstract](https://europepmc.org/article/MED/17308966)
- **Key result, from the abstract.** "Using effect sizes from 23 studies", the average correlation was r = .35, p < .001. — [Europe PMC abstract](https://europepmc.org/article/MED/17308966)
- **Wider context.** Bolger & Amarel (2007) treat the distinctiveness of received from perceived support as settled, which is consistent with the paper's general point that the two are different constructs. — [Bolger & Amarel 2007, p. 459](http://www.columbia.edu/~nb2229/docs/bolger-amarel-support-experiments-2006.pdf)

### Inferences
- **Support judgment: Supported with qualifications.**
  - The figures r = .35, 23 studies and ≈12% shared variance are accurate to the abstract.
  - The interpretive frame is a construct mismatch. In the support literature, "received support" is the recipient's own report of behaviours received. It is not the care the giver enacted, and it is not the paper's "received care". The paper defines received care as need fulfilment (`02-definitions-and-distinctions.md:43`).
  - The r = .35 therefore speaks to the paper's *perceived* stage: two ways the same receiver describes support. It does not speak to the transmission from giver to receiver.
- **The 12% figure.** It is correct arithmetic for r = .35. Whether .35 is an observed or an attenuation-corrected correlation is unverified. If it is uncorrected, the latent overlap would be larger than 12%, so "share only about 12%" may understate the true relationship.
- **The paper's own limitation note.** "Mostly cross-sectional" (`03:137`) could not be verified from the abstract.
- **Evidence grade.** Established for the narrow association between ISSB-measured received support and perceived support in the same respondent (a meta-analysis with a consistent instrument). The tag "Established for that measure pairing" is appropriate. Its use as evidence of giver–receiver loss should be dropped or reframed, which affects `03:21` and `00:5`.
- **Proposed wording for `03:21–22`.** "Recipients' own reports of supportive behaviours received (ISSB) correlated r = .35 with their perceived support across 23 studies (about 12% shared variance) (Haber et al. 2007). Both measures come from the recipient, so this shows that receiving support and feeling supported are distinct, not that givers and receivers disagree."

### Gaps
- Not verified for lack of full text:
  - the total N;
  - confidence interval and heterogeneity (Q or I²);
  - moderators (perceived-support measure type, population, stressor);
  - the proportion of cross-sectional versus longitudinal studies;
  - whether the correlations were corrected for unreliability;
  - publication-bias checks;
  - the countries and years of the included studies.

## C04: Bolger, Zuckerman & Kessler (2000). Invisible support predicts better adjustment

### Takeaway
The abstract supports the paper's description of the 2000 finding. Many transactions reported by providers were not reported by recipients, and these "invisible" transactions predicted better adjustment. The paper omits a decisive qualification: **the same research group's larger replication (312 examinees and 310 partners in the same bar-exam diary paradigm, more than three times the original sample) did not reproduce the invisible-support pattern.** In that replication, provider-reported emotional support was often associated with *more* anger, anxiety, depressed mood and fatigue, and the authors said they now "back off from this simple take home message". In addition, "invisible" means not *reported as support* by the recipient, which is not the same as unperceived. **Verdict: overstated as used.** The paper's language ("aids", "helps", "improves", "cleanest dissociation") and its tags ([Moderate/mixed], "Moderate to Established") need downgrading.

### Cited Findings
- **How the paper uses it:**
  - `paper/01-question-and-thesis.md:15`: "Unnoticed ('invisible') support aids adjustment" [Moderate/mixed].
  - `paper/02-definitions-and-distinctions.md:19`: "Unnoticed support improves adjustment and goal attainment".
  - `paper/02-definitions-and-distinctions.md:43`: need fulfilment "Can occur without perception (invisible support)".
  - `paper/03-literature-review.md:29`: "**Invisible support** is the cleanest dissociation between benefit and perception".
  - `paper/03-literature-review.md:30`: "support the provider reported but the recipient did not notice predicted *better* adjustment".
  - `paper/06-competing-theories.md:8`: theory row.
  - `paper/07-revised-model.md:47`: "invisible support predicts adjustment and goal attainment without being noticed", cited as evidence that the substantive route exists [Moderate to Established].
  - `paper/07-revised-model.md:63`: undetected care.
  - `paper/08-mathematical-representation.md:37` and `README.md:126`: "Unnoticed support helps" [Moderate/mixed].
  - `paper/08-mathematical-representation.md:231`: "invisible support and income effects show that a non-perceptual route exists [Moderate to Established]".
  - `paper/09-model-without-math.md:7`: "Silent care can help without ever being noticed" (no citation).
  - `paper/19b-is-love-enough.md:5`: people "can benefit from care they never notice".
  - `README.md:48`: "Invisible support helps unseen".
- **Verification depth: abstract plus author-written secondary sources.**
  - The primary abstract was read via OpenAlex and the Harvard Health Care Policy listing.
  - No authorised open copy of the primary was found. OpenAlex lists only CiteSeerX entries, and CiteSeerX redirects to web.archive.org, which could not be fetched.
  - Two later full texts by the same first or senior author were read: Bolger & Amarel (2007), pp. 458–460 and 471–473, and the author manuscript of Shrout, Bolger, Iida, Burke, Gleason & Lane (2010), pp. 1–25. — [DOI](https://doi.org/10.1037/0022-3514.79.6.953); [PubMed](https://pubmed.ncbi.nlm.nih.gov/11138764/); [HCP listing](https://hcp.hms.harvard.edu/publication/invisible-support-and-adjustment-stress); [Shrout et al. 2010, DOI](https://doi.org/10.1093/acprof:oso/9780195380170.003.0007); [Shrout et al. manuscript](https://psychology.columbia.edu/sites/psychology.columbia.edu/files/2016-11/shrout-2009-support%20transaction%20chapter_0.pdf)
- **Abstract content.**
  - The authors start from the puzzle that support receipt had not been shown to predict adjustment, although perceived availability does.
  - They hypothesise that awareness of receiving support has an emotional cost.
  - In a daily diary study of couples, many provider-reported transactions went unreported by recipients, and the abstract says these invisible transactions promoted adjustment to a major stressor. — [OpenAlex record](https://api.openalex.org/works/https://doi.org/10.1037/0022-3514.79.6.953)
- **What was measured and found, as the authors later described it.**
  - Stressed partners who recognised emotional support on one day had higher anxiety and depressed mood the next day.
  - Adjusting for the recipient's report, partner-reported provision of emotional support predicted *lower* next-day depressed mood.
  - The model predicted tomorrow's mood from today's support while adjusting for today's mood. — [Shrout et al. 2010 MS, pp. 2–3, 7](https://psychology.columbia.edu/sites/psychology.columbia.edu/files/2016-11/shrout-2009-support%20transaction%20chapter_0.pdf)
  - Bolger & Amarel describe the 2000 finding as unacknowledged provider support attempts being the most effective at reducing distress. — [Bolger & Amarel 2007, p. 458](http://www.columbia.edu/~nb2229/docs/bolger-amarel-support-experiments-2006.pdf)
- **Causal identification.**
  - The design is nonexperimental. Bolger & Amarel acknowledge that the 2000 field study was open to rival interpretations. — [Bolger & Amarel 2007, p. 458](http://www.columbia.edu/~nb2229/docs/bolger-amarel-support-experiments-2006.pdf)
  - Shrout et al. list common causes the 2000 analysis did not model: days to the exam and weekends. A reanalysis of the same data that adjusted for them (Shrout, Herman & Bolger 2006) found the same pattern.
  - Simulations suggested reverse causation was unlikely to produce spurious support-cost results. The authors judged a third-variable process a greater threat, though implausible given the effect sizes.
  - The same reanalysis found **no benefit of invisible emotional support for anger, fatigue or vigor**. It did find that provider-reported *practical* support went with lower fatigue and higher vigor. — [Shrout et al. 2010 MS, pp. 3–5, 7](https://psychology.columbia.edu/sites/psychology.columbia.edu/files/2016-11/shrout-2009-support%20transaction%20chapter_0.pdf)
- **Replication by the same group.**
  - *Sample:* married or cohabiting couples (at least 6 months together) with one partner taking the July bar exam, recruited through law schools over three years. Of 552 couples assigned to the diary condition, 472 (77%) agreed to take part, and the final analysis group was 312 examinees and 310 partners. Diaries were completed twice daily from 5 weeks before to 1 week after the exam. Examinees' mean age was about 30; 54% of examinees were women; 80% were White; it was a volunteer sample.
  - *Result:* the authors failed to replicate the invisible-support pattern. Recipient-reported support was not linked to more depression, and partner-reported support (adjusted for recipient reports) was not linked to less depression.
  - Instead, provider-reported emotional support was often associated with increased anger, anxiety, depressed mood and fatigue. For example, next-evening anxiety b = 0.097 (z = 2.06) and fatigue b = 0.104 (z = 3.38).
  - Received emotional support was associated with higher vigor.
  - Across 20 lagged effects in refined models, only one was significant.
  - The authors attribute the difference to the data, not to model specification. They conclude that provider-reported emotional support carried costs on average whether or not the recipient recognised it, and that effects vary across couples. — [Shrout et al. 2010 MS, pp. 10–11, 15–16, 20–25](https://psychology.columbia.edu/sites/psychology.columbia.edu/files/2016-11/shrout-2009-support%20transaction%20chapter_0.pdf)
  - *Stated limitations:* a convenience sample, binary self-reports of support, and binary reports that confound measurement error with genuine differences in perspective between provider and recipient. — [Shrout et al. 2010 MS, p. 23](https://psychology.columbia.edu/sites/psychology.columbia.edu/files/2016-11/shrout-2009-support%20transaction%20chapter_0.pdf)

### Inferences
- **Support judgment: Overstated.**
  - `03:30` accurately describes what the 2000 study found.
  - The paper treats that finding as established evidence that benefit occurs without perception. It does so in `01:15`, `02:19`, `03:29`, `07:47`, `08:37`, `08:231`, `19b:5` and `README:48/126`.
  - The only directly comparable larger replication failed, and the original authors withdrew the simple message.
  - "Invisible" was operationalised as the recipient not *reporting* support on a binary item. That is not the same as the recipient not perceiving the act, as the replication authors themselves note.
- **The two-route model.**
  - Bolger & Amarel's experiments (C05) locate the advantage of invisible support in avoiding a negative *perception*, namely feeling seen as inefficacious. The support content itself showed no detectable effect.
  - So the invisible-support literature mainly informs the paper's *symbolic* route, about what an act signals. It does not show that a non-perceptual substantive route "exists" (`08:231`).
  - That proposition should be [Theoretical] or [Our hypothesis] unless other cited evidence carries it. The income studies cited alongside it were not audited here.
- **"While visible support does not."** This understates the original pattern. Recipient-recognised emotional support was associated with *worse* next-day mood. In the replication, recognised support did not show those costs and went with higher vigor, so the visible-support pattern is also inconsistent across samples.
- **Evidence grade.** Moderate or mixed, specifically *mixed*: one positive diary study, a same-group replication with more than three times the sample that failed, and supportive but different-mechanism laboratory evidence (C05). The tags "Moderate to Established" (`07:47`, `08:231`) are not justified. [Moderate/mixed] at `01:15`, `08:37` and `README:126` should name the failed replication.
- **Proposed wording for `03:30`.** "In a daily-diary study of couples facing the bar exam, support reported by the provider but not by the recipient predicted better next-day mood (Bolger, Zuckerman & Kessler 2000). The same group's replication with more than three times as many couples did not reproduce this pattern: provider-reported emotional support was more often associated with worse mood (Shrout et al. 2010) [Mixed]."
- **Proposed wording for `03:29`.** "Invisible support is the most-cited candidate for benefit without recognition, but the evidence is mixed, and 'invisible' means not labelled as support rather than unperceived."
- **Proposed wording for `19b:5` and `09:7`.** Change "can benefit from care they never notice" to "may benefit from care they do not register as support".

### Gaps
- Not verified from the primary article: the original N (the repository's notes say 68 couples), the number of diary days, the exact outcome measures, the coefficients and CIs, the study years and the location. The replication chapter says only that the new study had more than three times as many couples.
- The Shrout et al. account was read from the author manuscript. The published OUP chapter (pp. 175–199) may differ slightly.
- Other independent tests of invisible support were not audited: Maisel & Gable 2009, Girme et al. 2013 and 2018, Howland & Simpson 2010, Zee et al. Their results are not summarised here.

## C05: Bolger & Amarel (2007). Visible support is ineffective or distress-raising because it signals inefficacy; invisible support helps

### Takeaway
The experiments are randomised and give causal evidence within a laboratory analogue, and the paper's summary follows the abstract. The tests show that *visible* support raised distress only when the script explicitly told the recipient she needed help. When that message was removed, visible support was no different from no support. *Invisible* support beat visible support in both studies that compared them, but its advantage over **no support was not statistically significant in either study that tested it** (p = .159 and p = .069). The participants were female undergraduates supported by a female stranger, and the outcome was minutes-long anticipatory distress before a speech that was never given. The paper's "N = 257" comes from the abstract; the analysed samples sum to 267. **Verdict: supported with qualifications.**

### Cited Findings
- **How the paper uses it:**
  - `paper/03-literature-review.md:31`: "In three experiments (N = 257), invisible support reduced emotional reactivity, while visible support was ineffective or harmful because it communicated inefficacy". This bullet has no tag.
  - `paper/04-evidence-for-the-intuition.md:34`: "Visible support could backfire by signalling inefficacy".
  - `paper/06-competing-theories.md:8`: "does not signal inefficacy", row tagged "Moderate to Established".
  - `paper/07-revised-model.md:54`: "Visible support can turn the symbolic route negative by signalling the receiver's inefficacy".
  - `paper/11-romantic-partner-example.md:5`: "A's advice may also be *visible* support that signals B's inefficacy".
- **Verification depth: full text.** The author-posted PDF of the published JPSP article was read, pp. 458–473: abstract, introduction, Studies 1–3, Tables 1–5, Figures 2–3, mediation analyses, General Discussion, Unresolved Issues and Conclusions. — [Columbia PDF](http://www.columbia.edu/~nb2229/docs/bolger-amarel-support-experiments-2006.pdf); [DOI](https://doi.org/10.1037/0022-3514.92.3.458); [PubMed](https://pubmed.ncbi.nlm.nih.gov/17352603/)
- **Design.**
  - Participants expected to give a speech, on a personally important topic, to graduate-student evaluators. After a 5-minute practice, a female confederate peer delivered scripted support.
  - In the *visible* condition the support was said directly to the participant. In the *invisible* condition it was framed as a question to the experimenter.
  - The outcome was change in distress (POMS anxiety and depression items, plus anger in Study 3, rescaled 0–10) from baseline to just before the speech. The speech was cancelled after a suspicion check.
  - Study 1: practical advice, visible vs invisible.
  - Study 2: emotional reassurance, visible vs invisible vs none.
  - Study 3: practical advice in a five-cell incomplete factorial that separated visibility, recipient-inefficacy messages, peer-inefficacy messages and content, with measured mediators (reflected appraisal of inefficacy, upward comparison).
  - Experimenters were kept blind to condition until as late as possible in the procedure. Confederates were blind to the hypotheses. — [Bolger & Amarel 2007, pp. 460–462, 465–467](http://www.columbia.edu/~nb2229/docs/bolger-amarel-support-experiments-2006.pdf)
- **Population.**
  - All participants were women from NYU's introductory-psychology pool, and the confederates were women in their early 20s. The authors chose women to avoid cross-sex romantic readings and because of "tend and befriend" arguments.
  - Final analysed samples were Study 1 n = 31 (of 35), Study 2 n = 86 (of 96) and Study 3 n = 150 (of 167). **That sums to 267, while the abstract reports N = 257.**
  - The samples were 53–60% White, and the years of data collection are not stated. — [Bolger & Amarel 2007, pp. 460–461, 463, 466](http://www.columbia.edu/~nb2229/docs/bolger-amarel-support-experiments-2006.pdf)
- **Study 1.** Adjusting for baseline distress, distress rose 1.05 units (95% CI 0.10–2.00) with invisible support and 3.13 (2.15–4.12) with visible support: d = 1.09 (CI 0.37–1.81), t(28) = 3.10, p = .004. All visible-condition participants reported receiving advice, and none in the invisible condition did. — [Bolger & Amarel 2007, pp. 462–463](http://www.columbia.edu/~nb2229/docs/bolger-amarel-support-experiments-2006.pdf)
- **Study 2.**
  - Distress rose 0.87 units with invisible support (CI 0.07–1.66), 1.65 with no support (0.90–2.39) and 2.22 with visible support (1.46–2.98).
  - Invisible vs visible: d = 0.63 (CI 0.12–1.15), p = .017.
  - Invisible vs none: d = 0.36 (CI −0.15 to 0.88), **p = .159**.
  - Visible vs none: d = 0.27 (CI −0.23 to 0.76), **p = .287**.
  - 7 of 27 invisible-condition participants reported being reassured. Excluding them did not change the results. — [Bolger & Amarel 2007, pp. 463–464](http://www.columbia.edu/~nb2229/docs/bolger-amarel-support-experiments-2006.pdf)
- **Study 3, contrasts.** The omnibus test was F(4, 142) = 6.65, p < .001.
  - *Visible A* (the confederate says she can tell the participant could use some help) vs none: +1.09 units (CI 0.43–1.75), d = 0.66, p = .001.
  - *Visible B* (the same advice while saying the participant does not need help) vs A: −0.99, d = 0.60, p = .004. The Visible B mean (0.88) was about the same as no support (0.77).
  - *Invisible A* (the peer voices her own need) vs none: −0.61 (CI −1.26 to 0.05), d = 0.37 (CI −0.03 to 0.76), **p = .069**.
  - *Invisible B* (the peer not in need) vs A: +0.75 (CI 0.09–1.40), p = .026. Invisible B was about the same as no support.
  - "Pure visibility" (Visible B vs Invisible B): p = .915. "Pure content" (Invisible B vs none): p = .673. — [Bolger & Amarel 2007, pp. 467–469](http://www.columbia.edu/~nb2229/docs/bolger-amarel-support-experiments-2006.pdf)
- **Study 3, mediation.** The analysis used Baron & Kenny regressions with bootstrap confidence intervals.
  - Reflected appraisal of inefficacy carried 0.49 units (bootstrap CI 0.19–0.91) of the 1.09-unit Visible A effect, about 45%. With upward comparison added, 55% was mediated in total.
  - Inefficacy appraisal also carried −0.35 units of the Invisible A vs none contrast (CI −0.70 to −0.14).
  - Upward social comparison did not mediate any contrast. — [Bolger & Amarel 2007, pp. 469–471, Table 5](http://www.columbia.edu/~nb2229/docs/bolger-amarel-support-experiments-2006.pdf)
- **The authors' own interpretation and caveats.**
  - Invisibility itself is not what makes invisible support work; the authors write that "invisibility per se is not the essence". What matters, at least in part, is avoiding the message that the recipient is inefficacious.
  - Recipients rated the confederate as more supportive in the visible conditions than in the invisible ones (M = 5.2 vs 2.6 on a 0–10 scale). That held even in the condition that raised distress (Visible A, M = 4.6).
  - Their one test of the advice content found no benefit.
  - The speech was never delivered, so performance could not be assessed.
  - The paradigm uses unfamiliar peers, not intimate partners.
  - Requested support is a boundary condition.
  - Positive emotions such as intimacy may respond differently.
  - They caution against concluding that people are unaware of the support they receive. — [Bolger & Amarel 2007, pp. 460, 471–473](http://www.columbia.edu/~nb2229/docs/bolger-amarel-support-experiments-2006.pdf)

### Inferences
- **Support judgment: Supported with qualifications.**
  - *Supported:* visible support that conveys the recipient's inefficacy can raise distress, partly through reflected appraisals. This is the experimental contrast plus partial mediation in Study 3. Invisible support produced smaller distress rises than visible support (Studies 1 and 2).
  - *Overstated in `03:31`:* "invisible support reduced emotional reactivity". Against no support, neither test reached significance.
  - *Overstated in `03:31`:* "visible support was … harmful because it communicated inefficacy". Harm appeared only when inefficacy was scripted explicitly, and the mediation was partial (about 45%) and rested on a measured 2-item mediator.
  - *Wrong sample size in `03:31`:* N = 257 conflicts with the analysed 267.
- **Mechanism and the paper's routes.** The evidence supports the paper's *symbolic-route* reading (`07:54`, `04:34`) and *undercuts* using invisible support as evidence of a non-perceptual route (`07:47`, `08:231`; see C04).
  - In the "invisible" conditions the participant heard the advice or reassurance; she simply did not interpret it as support.
  - The benefit vanished when the peer did not voice her own difficulty, and support content showed no effect.
- **Generalisation.**
  - The participants were women and the supporters strangers.
  - The stressor was a single laboratory one, and the outcome was distress measured within about 20 minutes.
  - Applications to romantic partners (`11:5`) or parents are extrapolations, and the paper should say so. `11:5` already uses "may".
- **Evidence grade.**
  - Moderate or mixed for "support that signals the recipient's inefficacy raises short-term distress": randomised, replicated across studies within one laboratory, small samples, and a narrow population.
  - Preliminary for "invisible support helps relative to none".
  - Untested in this source (so Theoretical) for close relationships.
  - Tag `03:31` [Moderate/mixed; laboratory analogue with strangers]. The "Moderate to Established" row tag at `06:8` overstates this component.
- **Proposed wording for `03:31`.** "In three laboratory experiments with female US undergraduates supported by a female stranger (analysed n = 31, 86 and 150; the abstract reports N = 257), support delivered indirectly, so that it was not interpreted as support, produced smaller rises in anticipatory distress than the same support given directly. Against no support, the indirect form's advantage was not statistically significant. Direct support raised distress only when it conveyed that the recipient needed help, an effect partly carried by feeling seen as inefficacious (Bolger & Amarel 2007) [Moderate/mixed; laboratory analogue]."

### Gaps
- Not checked: later direct replications or meta-analyses of the support-visibility experiments, including independent laboratories, male participants and close dyads.
- The source does not explain the 257 vs 267 discrepancy. One possibility, unverified, is a typo in the abstract.

## Across the five claims: what should change, and how confident is this audit?

### Takeaway
In aggregate:
- Two claims hold with wording fixes: C01 (κ) and C03 (r = .35).
- One holds at its core but has overstated extensions: C02 (sacrifice detection).
- One is materially overstated because its key finding did not replicate in the original group's larger study: C04 (invisible support).
- One is accurate to its abstract but overstated in its details: C05 (support visibility experiments).

The most consequential correction concerns how the paper uses C04 and C05. Together they support a *symbolic* mechanism, in which visible help can signal inefficacy. They do not establish benefit that arrives without perception, which is what the paper's "substantive route" claims (`07:47`, `08:231`).

### Cited Findings
- Two sources report abstract sample sizes that do not match their Method sections, and the paper reproduces the abstract figures:
  - Visserman et al.: 426 in the abstract vs 252 + 160 = 412. — [Visserman et al. 2019](https://doi.org/10.1177/1948550618757599)
  - Bolger & Amarel: 257 in the abstract vs 31 + 86 + 150 = 267. — [Bolger & Amarel 2007](http://www.columbia.edu/~nb2229/docs/bolger-amarel-support-experiments-2006.pdf)
- The invisible-support diary pattern was not replicated by its originating group in a sample more than three times larger, and the authors retreated from it. — [Shrout et al. 2010 MS](https://psychology.columbia.edu/sites/psychology.columbia.edu/files/2016-11/shrout-2009-support%20transaction%20chapter_0.pdf)
- The laboratory benefit of invisible support depended on the provider voicing her own difficulty, the support content had no detectable effect, and the mediator was a perception (reflected appraisal of inefficacy). — [Bolger & Amarel 2007](http://www.columbia.edu/~nb2229/docs/bolger-amarel-support-experiments-2006.pdf)
- C01, C02 and C04 all use one party's self-report as the criterion for whether an act "occurred". Coriell & Cohen explicitly note that such data cannot separate missed perception from over-reporting. — [Coriell & Cohen 1995](https://doi.org/10.1184/R1/6614096.v1)
- The repository's corrections log already distinguishes verification depth (full text, abstract, prior knowledge, not accessed). It states that many findings were checked only against abstracts and that a resolving DOI does not show the study supports the claim. — `CORRECTIONS.md`, entry C4.

### Inferences
- **Priority 1: C04.**
  - Downgrade "invisible support helps or aids or improves adjustment" everywhere to [Mixed] and cite the failed replication.
  - Remove C04 and C05 as evidence that a non-perceptual route "exists" (`07:47`, `08:231`, `08:37`, `README:126`, `02:19`, `02:43`, `19b:5`, `09:7`).
  - Consider a CORRECTIONS.md entry, since this changes an empirical grade.
- **Priority 2: C02 false alarms.** Stop using false alarms as evidence of "perception without benefit" (`01:15`, `02:18`) or of perceiving sacrifices that "had not occurred" (`05:30`, `07:48`). Reword as "not reported by the partner".
- **Priority 3: sacrificer satisfaction.** Downgrade the C02 sacrificer-satisfaction effect to [Preliminary] and replace causal verbs ("lose", "lowers") with associational ones (`07:34`, `10:34`, `11:8`, `04:65`).
- **Priority 4: C03.** Reframe it as a within-recipient construct distinction (`03:21–22`, `00:5`), not giver–receiver loss.
- **Priority 5: specifics.**
  - Fix the population and helpful-only κ for C01 (`00:5`, `04:7`).
  - Fix N and the significance of the no-support contrasts for C05 (`03:31`).
  - Fix N, the 40–46% false-alarm range and the "one laboratory" limitation for C02 (`03:52`, `03:140`).
- **Grades, as used versus recommended:**

  | Claim | Paper's tag | Recommended grade |
  |---|---|---|
  | C01 | [Moderate/mixed] | Keep Moderate or mixed |
  | C02 detection and gratitude | [Moderate/mixed] | Keep Moderate or mixed |
  | C02 sacrificer satisfaction | [Moderate/mixed] | Preliminary |
  | C03 | [Established for that measure pairing] | Keep Established, narrow scope |
  | C04 | [Moderate/mixed] to "Moderate to Established" | Mixed (not replicated); Theoretical as proof of a non-perceptual route |
  | C05 | untagged at `03:31`; part of "Moderate to Established" at `06:8` | Moderate or mixed for the laboratory analogue; Preliminary for invisible support versus none |

- **Confidence of this audit.**
  - High for C01, C02 and C05, which were read in full.
  - Moderate for C04: the abstract plus two full-text secondary accounts by the original authors.
  - Limited for C03: abstract only.

### Gaps
- This audit does not claim exhaustive coverage of the literature. It did not check independent replications of invisible support or support visibility (beyond the same group's chapter), later meta-analyses, or the Visserman supplement and OSF data.
- The Haber full text and the Bolger et al. (2000) full text remain unread. Their key numbers rest on abstracts and author summaries.

```jsonl
{"claim_id": "C01", "short_claim": "Givers and recipients agree only moderately on whether a supportive act occurred (kappa about .39)", "source": "Coriell, M., & Cohen, S. (1995). Concordance in the face of a stressful event: When do members of a dyad agree that one person supported the other? Journal of Personality and Social Psychology, 69(2), 289-299.", "doi": "10.1037/0022-3514.69.2.289", "verification_depth": "full text", "sections_read": "Published version (scanned) via CMU KiltHub (doi 10.1184/R1/6614096.v1), pp. 289-298: abstract, introduction, Method (participants, behaviour list, kappa computation, measures), Results (Tables 1-4, Figure 1), Discussion, Considerations and Conclusions; reference list p. 299 not read", "design": "Single-occasion dyadic comparison of independent retrospective checklists after an exam (student-reported received vs supporter-reported provided), within-dyad Cohen's kappa averaged across dyads; correlational predictors of concordance; no manipulation", "population": "297 US undergraduate-supporter dyads at Carnegie Mellon (eight intro psychology classes; supporters were self-chosen close friends or roommates; students 57% men, median age 18; 99 man-man, 71 woman-woman, 127 mixed dyads); 220 dyads for competence and communality analyses; collection year not stated", "measured": "Occurrence (yes/no) of 67 supporter behaviours (36 judged helpful, 31 harmful) during preparation for a major exam, reported by student after the exam and by supporter within 3 days; expected behaviours; intimacy; social competence; communal orientation", "key_result": "Mean within-dyad kappa = .39 (SD .21) across all 67 behaviours; .28 (SD .21) for helpful and .14 (SD .26) for harmful behaviours; concordance correlated r = .53 with fulfilled expectancies and r = .41 with intimacy; six predictors explained 41% of variance; man-man dyads least concordant", "supports_interpretation": "qualified", "evidence_grade": "Moderate or mixed (general proposition); the specific kappa is a single-study estimate in student-peer dyads", "paper_locations": ["paper/00-summary.md:5", "paper/01-question-and-thesis.md:14", "paper/03-literature-review.md:23", "paper/04-evidence-for-the-intuition.md:7", "paper/12-asymmetry-and-misperception.md:22", "README.md:47"], "recommended_change": "Replace 'Partners agree only moderately on whether a supportive act even happened' with: In 297 US student-supporter pairs (friends or roommates), reports of which of 67 helpful or harmful behaviours occurred during exam preparation agreed only moderately (mean within-pair kappa = .39; .28 for helpful behaviours alone). Add the authors' caveats that disagreement cannot be assigned to missed perception versus over-reporting and that checklist unreliability likely deflates kappa. Keep [Moderate/mixed]; fix 'after an exam' to 'reported after an exam about preparation-period behaviours'.", "notes": "The .39 figure is for helpful plus harmful behaviours combined; agreement on supportive acts specifically was lower. Dyads were not romantic partners or family. Fulfilled expectancies were the strongest correlate, so reports partly track what students expected."}
{"claim_id": "C02", "short_claim": "About half of sacrifices go unnoticed; detected and false-alarm sacrifices are followed by gratitude; unnoticed sacrifices lower the sacrificer's satisfaction", "source": "Visserman, M. L., Impett, E. A., Righetti, F., Muise, A., Keltner, D., & Van Lange, P. A. M. (2019). To 'see' is to feel grateful? A quasi-signal detection analysis of romantic partners' sacrifices. Social Psychological and Personality Science, 10(3), 317-325.", "doi": "10.1177/1948550618757599", "verification_depth": "full text", "sections_read": "Published version (CC BY-NC 4.0) via Sussex Research Online figshare, pp. 317-324: abstract, introduction, Study 1 and Study 2 Method and Results (Tables 1-6, Figures 1-3), auxiliary and follow-up analyses, General Discussion, Strengths and Limitations, Notes 1-3; online supplement and OSF data (osf.io/dhmca) not read", "design": "Two dyadic daily-experience studies (8 and 14 days) with quasi-signal-detection coding of each day from both partners' yes/no reports (partner self-report as criterion); multilevel models controlling previous-day gratitude; sequential mediation on hit/miss days only; 1-year and 3-month follow-ups; associational", "population": "Study 1: 126 Dutch couples (N = 252; mean age 23.3; 64% students). Study 2: 80 San Francisco Bay Area couples (N = 160; mean age 23.9; about half students). Abstract reports total N = 426 but Method sections sum to 412. Both secondary analyses of larger projects", "measured": "Daily single yes/no item for own and partner's sacrifice; daily single-item gratitude, perceived or felt appreciation from partner, and relationship satisfaction (0-6 in Study 1; 1-5 in Study 2)", "key_result": "Partner-reported sacrifice days missed: about 46-47% in both studies (hits vs misses n.s.). Perceived sacrifices not reported by partner: about 46-47% in Study 1, 39.8% in Study 2 (significantly fewer than hits, p < .001). Same-day gratitude vs correct rejections: hits b = .19 and .38, false alarms b = .18 and .41 (all p <= .015), misses b = -.11 (p = .159) and .03 (p = .671). Sacrificer satisfaction on miss vs hit days: b = -.16, p = .069 (Study 1); b = -.23, p = .017 (Study 2); small significant indirect effects via partner gratitude and appreciation. No evident long-term effect of detection on gratitude at follow-up", "supports_interpretation": "qualified", "evidence_grade": "Moderate or mixed (detection rates and gratitude associations); Preliminary (sacrificer-satisfaction effect)", "paper_locations": ["paper/00-summary.md:5", "paper/01-question-and-thesis.md:14", "paper/01-question-and-thesis.md:15", "paper/02-definitions-and-distinctions.md:17", "paper/02-definitions-and-distinctions.md:18", "paper/03-literature-review.md:52", "paper/03-literature-review.md:140", "paper/04-evidence-for-the-intuition.md:7", "paper/04-evidence-for-the-intuition.md:65", "paper/05-evidence-against-it.md:30", "paper/07-revised-model.md:34", "paper/07-revised-model.md:48", "paper/07-revised-model.md:63", "paper/08-mathematical-representation.md:33", "paper/08-mathematical-representation.md:158", "paper/08-mathematical-representation.md:261", "paper/08-mathematical-representation.md:312", "paper/10-father-daughter-example.md:34", "paper/11-romantic-partner-example.md:8", "paper/14-time-and-feedback.md:20", "README.md:47", "README.md:48", "README.md:122"], "recommended_change": "Use per-study samples (126 Dutch and 80 US couples) instead of N = 426. Say 40-46% (not about half) of perceived sacrifices were unreported by the partner. Replace 'whether or not they had occurred' and 'perceived, not actual' with 'whether or not the partner reported sacrificing'. Drop false alarms as evidence of perception without benefit (01:15, 02:18). Replace 'lose satisfaction' and 'lowers' with 'reported slightly lower same-day satisfaction than on days the sacrifice was detected (significant in one of two samples)' and tag Preliminary. Replace 'produced' and 'drives' with 'was associated with'. Fix the limitation 'Two studies, one laboratory' to 'two short diary studies of young Dutch and US couples; partner self-report as criterion; associational'.", "notes": "In-text Study 1 percentages appear transposed relative to Table 2 counts (counts give 53.7% detection and 52.7% precision); both are about half. Study 1 appreciation-to-satisfaction link held for women only (Note 1). Couples were trained at intake to recognise sacrifices, which may raise detection above everyday levels."}
{"claim_id": "C03", "short_claim": "Received and perceived support correlate about r = .35 across 23 studies (about 12% shared variance)", "source": "Haber, M. G., Cohen, J. L., Lucas, T., & Baltes, B. B. (2007). The relationship between self-reported received and perceived social support: A meta-analytic review. American Journal of Community Psychology, 39(1-2), 133-144.", "doi": "10.1007/s10464-007-9100-9", "verification_depth": "abstract", "sections_read": "Abstract via Europe PMC and PubMed (PMID 17308966) and OpenAlex; green open-access author version at Deep Blue (hdl 2027.42/117157) not read because the repository served an automated-access challenge, which was not bypassed", "design": "Meta-analysis of studies using the Inventory of Socially Supportive Behaviors (ISSB) together with any perceived-support measure", "population": "23 studies; total N, countries, years and study designs not verified", "measured": "Correlation between the same respondents' self-reported receipt of supportive behaviours (ISSB) and their perceived social support (any measure)", "key_result": "Average r = .35, p < .001 (abstract). r squared = .1225, matching about 12% shared variance if .35 is an uncorrected observed correlation (not verified). CI, heterogeneity, moderators and attenuation correction not verified", "supports_interpretation": "qualified", "evidence_grade": "Established (narrow: ISSB-measured received support vs perceived support in the same respondent)", "paper_locations": ["paper/00-summary.md:5", "paper/03-literature-review.md:21", "paper/03-literature-review.md:22", "paper/03-literature-review.md:137", "paper/06-competing-theories.md:8"], "recommended_change": "Reframe 03:21-22 and 00:5: both measures are the recipient's own reports, so r = .35 shows that receiving support and feeling supported are distinct constructs within the recipient, not that givers and receivers disagree or that care given is lost. Note that the support literature's 'received support' (reported receipt of behaviours) is not the paper's 'received care' (need fulfilment, 02:43). Keep the tag 'Established for that measure pairing'; verify or drop 'mostly cross-sectional' (03:137).", "notes": "The number is correct but the construct mapping is off for the paper's giver-to-receiver argument. If the meta-analytic r is uncorrected for unreliability, latent overlap exceeds 12%."}
{"claim_id": "C04", "short_claim": "Invisible support (reported by provider, not recipient) predicts better adjustment; visible support does not", "source": "Bolger, N., Zuckerman, A., & Kessler, R. C. (2000). Invisible support and adjustment to stress. Journal of Personality and Social Psychology, 79(6), 953-961.", "doi": "10.1037/0022-3514.79.6.953", "verification_depth": "abstract", "sections_read": "Primary: abstract only (OpenAlex; Harvard HCP listing); no authorised open full text found (CiteSeerX copy redirects to web.archive.org, not fetchable). Secondary, full text, by the same authors: Bolger & Amarel 2007 pp. 458-460 and 471-473; Shrout, Bolger, Iida, Burke, Gleason & Lane 2010 (OUP chapter, doi 10.1093/acprof:oso/9780195380170.003.0007) author manuscript pp. 1-25", "design": "Nonexperimental daily diary study of couples with one partner facing a major stressor (bar exam); provider- and recipient-reported support entered jointly; next-day mood predicted adjusting for same-day mood (per Shrout et al.)", "population": "US couples in which one partner was preparing for a bar examination; original N, days and years not verified from the primary (a later replication had more than three times as many couples)", "measured": "Daily yes/no reports of emotional support provided (partner) and received (examinee); next-day anxiety and depressed mood (per authors' later descriptions)", "key_result": "Abstract: many provider-reported transactions were not reported by recipients, and these invisible transactions predicted better adjustment. Per Shrout et al.: recipient-recognised emotional support predicted higher next-day anxiety and depressed mood, while partner-reported provision (adjusted for recipient report) predicted lower next-day depressed mood; a reanalysis found no invisible-support benefit for anger, fatigue or vigor. The same group's replication (312 examinees, 310 partners) failed to reproduce the invisible-support pattern; provider-reported emotional support was often associated with more anger, anxiety, depressed mood and fatigue, and the authors retreated from the take-home message", "supports_interpretation": "overstated", "evidence_grade": "Moderate or mixed (inconsistent: original diary pattern not replicated in a larger same-paradigm sample); Theoretical as evidence that a non-perceptual route exists", "paper_locations": ["paper/01-question-and-thesis.md:15", "paper/02-definitions-and-distinctions.md:19", "paper/02-definitions-and-distinctions.md:43", "paper/03-literature-review.md:29", "paper/03-literature-review.md:30", "paper/06-competing-theories.md:8", "paper/07-revised-model.md:47", "paper/07-revised-model.md:63", "paper/08-mathematical-representation.md:37", "paper/08-mathematical-representation.md:231", "paper/09-model-without-math.md:7", "paper/19b-is-love-enough.md:5", "README.md:48", "README.md:126"], "recommended_change": "At 03:30 add that the same group's larger replication (Shrout et al. 2010) did not reproduce the pattern and found provider-reported emotional support associated with worse mood; tag [Mixed]. Replace 'aids', 'helps', 'improves' and 'cleanest dissociation between benefit and perception' with mixed-evidence wording, noting that 'invisible' means not reported as support rather than unperceived. Downgrade 'Moderate to Established' at 07:47 and 08:231 and remove invisible support as proof that a non-perceptual (substantive) route exists. Change 19b:5 and 09:7 to 'may benefit from care they do not register as support'. Consider a CORRECTIONS.md entry.", "notes": "Original study details (N, days, coefficients, CIs) unverified. The replication chapter was read as an author manuscript; the published version may differ slightly. Independent tests (Maisel & Gable 2009; Girme et al. 2013, 2018; Howland & Simpson 2010) were not audited."}
{"claim_id": "C05", "short_claim": "Experiments: visible support is ineffective or raises distress by signalling inefficacy, while invisible support helps", "source": "Bolger, N., & Amarel, D. (2007). Effects of social support visibility on adjustment to stress: Experimental evidence. Journal of Personality and Social Psychology, 92(3), 458-475.", "doi": "10.1037/0022-3514.92.3.458", "verification_depth": "full text", "sections_read": "Author-posted PDF of the published article (columbia.edu/~nb2229), pp. 458-473: abstract, introduction, Studies 1-3 Method and Results (Tables 1-5, Figures 2-3), mediation analyses, General Discussion, Unresolved Issues, Conclusions", "design": "Three randomised laboratory experiments; anticipated-speech stressor; scripted support from a female confederate peer delivered directly (visible) or as a question to the experimenter (invisible); Study 2 added no-support control; Study 3 five-cell incomplete factorial separating visibility, recipient-inefficacy and peer-inefficacy messages and content, with measured mediators", "population": "Female NYU introductory-psychology students; analysed n = 31, 86 and 150 (sum 267; abstract reports N = 257); female stranger confederates; years not stated", "measured": "Change in self-reported distress (6-9 POMS anxiety, depression and anger items, 0-10 scale) from baseline to just before an expected speech that was never given; manipulation checks; perceived supportiveness; reflected appraisal of inefficacy; upward social comparison", "key_result": "Invisible vs visible: Study 1 d = 1.09 (CI 0.37-1.81), p = .004; Study 2 d = 0.63 (CI 0.12-1.15), p = .017. Invisible vs none: Study 2 d = 0.36, p = .159; Study 3 d = 0.37 (CI -0.03 to 0.76), p = .069 (both n.s.). Visible vs none: Study 2 d = 0.27, p = .287 (n.s.); Study 3 visible support stating the recipient needed help raised distress 1.09 units (CI 0.43-1.75), d = 0.66, p = .001, and removing that message eliminated the harm. Reflected appraisal of inefficacy mediated about 45% of that effect; advice content showed no effect (p = .673)", "supports_interpretation": "qualified", "evidence_grade": "Moderate or mixed (causal within a lab analogue; one laboratory, women, strangers); Preliminary for invisible support beating no support; Theoretical for close relationships", "paper_locations": ["paper/03-literature-review.md:31", "paper/04-evidence-for-the-intuition.md:34", "paper/06-competing-theories.md:8", "paper/07-revised-model.md:54", "paper/11-romantic-partner-example.md:5"], "recommended_change": "Rewrite 03:31: in three lab experiments with female US undergraduates supported by a female stranger (analysed n = 31, 86, 150; abstract N = 257), indirect support produced smaller rises in anticipatory distress than direct support; its advantage over no support was not statistically significant; direct support raised distress only when it conveyed that the recipient needed help, partly via feeling seen as inefficacious. Tag [Moderate/mixed; laboratory analogue]. Keep 04:34, 07:54 and 11:5 as 'can/may' but name the strangers-in-the-lab population.", "notes": "The evidence locates the visibility effect in a perception (reflected appraisal of inefficacy), supporting the paper's symbolic route and undercutting use of invisible support as evidence of a non-perceptual substantive route. In invisible conditions participants heard the advice; they did not interpret it as support. The benefit disappeared when the peer did not voice her own difficulty."}
```
