# Methods dossier: a dyadic longitudinal test of the Love in Translation model (instruments, design, power, identification, ethics, preregistration)

Scope and conventions. The model under test is frozen: it has ten components, (1) enactment through (10) safety, with two outcome routes, $\beta_{\text{sub}}$ (effects of enacted care that do not pass through perceived regard $Q$) and $\beta_{\text{sym}}$ (effects that do). Sources for this are `README.md` "Model at a glance", `paper/08` §8.8 and §8.13, `paper/17` and `paper/18`. The study must separate those routes from four simpler explanations:
- (a) total support received;
- (b) perceived support alone;
- (c) need fulfilment;
- (d) existing trust or attachment.

No new equations are proposed here. Verification was done on 2026-11-05:
- **DOIs.** Every DOI cited below was resolved against the Crossref API (`api.crossref.org/works/<DOI>`), and the first author, year and title were matched. 171 unique DOIs were checked and 169 resolved to the intended works. One DOI recalled from memory did not resolve (Claxton et al. 2015): it is marked UNVERIFIED and not relied on. Another resolved to a different paper and was replaced by the correct DOI (Shorey et al. 2011).
- **Depth tags.** Each finding carries one:
  - **[full text]**: the document was read.
  - **[abstract]**: the abstract was read via PubMed, OpenAlex or Crossref.
  - **[metadata]**: only the DOI and bibliographic record were checked; any content claim then comes from prior knowledge and is flagged.
  - **[secondary]**: search-engine summary or a third-party page.
  - **[statute]**: official English translation or a mirror of the statute, with the article text fetched.
- **Working files** are in `working-files/protocol_R5/`:
  - `crossref_verification_all.tsv`, `verify_batch*.tsv`: Crossref resolution;
  - `abstracts.json`, `abstracts3.json`: retrieved abstracts;
  - `who2001/who2001.txt`: WHO 2001 full text.
- **Flags.** "PRIOR KNOWLEDGE / UNVERIFIED" marks details, typically item counts, that were not confirmed in this session.

## 1. Instruments: best-established measure per construct, with validation reference, length, reporter, psychometrics, diary use and Korean validation

### Takeaway
Validated instruments with verified DOIs exist for every listed construct. Korean-language validation exists for only a minority of them:
- **Located:** the Couples Satisfaction Index, the BPNSFS (cancer survivors only), the ECR-R and its 12-item short form, a state attachment measure, psychological control (adolescents), the PHQ-9 and the PSS. A CTS2 study exists as a database record only.
- **Not found:** the PRI and PPRS (responsiveness), SIRRS (support adequacy), Rempel or Dyadic Trust, the Investment Model Scale, the ECR-RS, the P-PASS, the Checklist of Controlling Behaviors, and the brief IPV screens.

The core translation constructs therefore need forward and back translation plus a pre-registered Korean psychometric phase, including invariance tests, before any Korea–comparison-country test.

### Cited Findings

#### Perceived partner responsiveness / perceived regard (model $Q_B$, symbolic route; rival b)
- **Perceived Responsiveness and Insensitivity scale (PRI)** ([Crasta, Rogge, Maniaci & Reis 2021](https://doi.org/10.1037/pas0000986); PsycTESTS record [10.1037/t79142-000](https://doi.org/10.1037/t79142-000)) [abstract, PubMed]:
  - **Development:** 246 candidate items from 19 earlier responsiveness measures (n = 2,334). Exploratory factor analysis gave two dimensions, and item response theory selected two 8-item subscales, Responsiveness and Insensitivity. Both showed incremental prediction over global satisfaction.
  - **Sensitivity to change:** n = 173 completed the brief PRI every other week for 8 weeks. In random-intercept cross-lagged models, the PRI was more sensitive than global evaluations to fluctuations in support and conflict.
  - **Dyadic validity:** in 161 couples, PRI scores were associated with the partner's self-reported behaviours after controlling for one's own behaviours.
  - **Reporter:** self (the perceiver).
  - **Interval:** a biweekly interval is validated. Daily use is not reported in the abstract.
- **Perceived Partner Responsiveness Scale (PPRS)** ([Reis et al. 2017](https://doi.org/10.1002/9781119102991.ch57), Sourcebook of Listening Research, pp. 516–521) [abstract]:
  - It defines responsiveness by "understanding and validation" and is described as having "excellent psychometric properties".
  - Item count is not given in the abstract. PRIOR KNOWLEDGE / UNVERIFIED: 18 items.
- **Daily short items in dyadic diaries:**
  - 96 married couples rated self-disclosure, partner disclosure, perceived partner responsiveness and intimacy on 42 consecutive days. Responsiveness partially mediated the disclosure–intimacy link ([Laurenceau, Barrett & Rovine 2005](https://doi.org/10.1037/0893-3200.19.2.314)) [abstract].
  - 67 cohabiting couples reported daily support given and received. Visible and invisible support were beneficial "only when the support was responsive" ([Maisel & Gable 2009](https://doi.org/10.1111/j.1467-9280.2009.02388.x)) [abstract].
  - Exact daily item wording was not verified.
- **Korean validation:** none found for the PRI or the PPRS. Crossref returned only PsycTESTS records for other languages; a Korean-language web search found unrelated Korean scales (emotional reactivity, invalidation) [secondary].

#### Desired versus received support and support adequacy (model $N$ versus $S$ on a commensurate scale; rival a)
- **SIRRS, Support in Intimate Relationships Rating Scale** ([Dehle, Larsen & Landers 2001](https://doi.org/10.1080/01926180126500)) [abstract]:
  - 177 married individuals rated the adequacy of specific spousal support behaviours **daily for 7 days**.
  - Perceived adequacy explained unique variance in marital quality, depressive symptoms and perceived stress after controlling for social desirability.
  - Reporter: recipient. Item count: UNVERIFIED.
- **SIRRS factor structure** ([Barry, Bunde, Brock & Lawrence 2009](https://doi.org/10.1037/a0014174)) [abstract]:
  - Four received-support types: esteem/emotional, physical comfort, informational and tangible.
  - The structure was reliable and valid across dating and married couples, across sexes and over time, with longitudinal incremental validity for marital adjustment, depression and anxiety.
- **Under- versus over-provision** ([Brock & Lawrence 2009](https://doi.org/10.1037/a0015402)) [abstract]:
  - 103 newlywed couples were assessed 5 times over 5 years (actor–partner models and growth curves).
  - Under-provision (less than desired) and over-provision (more than desired) were each uniquely associated with declining satisfaction. Over-provision was the greater risk, across four support types.
  - The exact item format was not verified (full text not read).
- **Risk factors for over-provision** ([Brock & Lawrence 2014](https://doi.org/10.1037/a0035280)) [abstract]:
  - The candidate predictors were attachment anxiety and avoidance, conflict management, emotional intimacy and external stress.
  - Husbands' avoidant attachment was among the predictors. **Attachment is therefore a plausible confounder of fit effects (rival d).**
- **Desired versus experienced support across cultures** ([Xu & Burleson 2001](https://doi.org/10.1111/j.1468-2958.2001.tb00792.x)) [abstract]:
  - 100 American and 102 Chinese newlyweds rated desired and experienced spousal support for 5 support types.
  - Women desired more support. Both American and Chinese women had gaps in emotional and esteem support, and Chinese women also in network support.
  - This is the closest located East Asian precedent for commensurate desired/received ratings.
- **Mismatch** ([Reynolds & Perrin 2004](https://doi.org/10.1037/0278-6133.23.4.425)) [abstract]: among 79 women recovering from breast cancer, unwanted but received support ("support commission") was uniquely associated with poor adjustment.
- **Korean validation:** none located for the SIRRS or the Brock and Lawrence items. No targeted Korean search was run for these.

#### Daily enacted and received support acts (model $E$ from the giver, detection $D$; rival a)
- **Paired provider and recipient diaries (Bolger and colleagues):**
  - In bar-exam couples, many support transactions reported by supporters were not reported by recipients, and these "invisible" transactions promoted adjustment ([Bolger, Zuckerman & Kessler 2000](https://doi.org/10.1037/0022-3514.79.6.953)) [abstract].
  - 68 couples were followed during the month before the bar exam. Partners' reports of **practical** support predicted less examinee fatigue and more vigour, while examinees' recognition of **emotional** support was costly (anger, anxious and depressed mood) ([Shrout, Herman & Bolger 2006](https://doi.org/10.1111/j.1475-6811.2006.00108.x)) [abstract].
  - Over 31 days, daily support receipt was associated with more closeness and more negative mood, with large between-person heterogeneity ([Gleason, Iida, Shrout & Bolger 2008](https://doi.org/10.1037/0022-3514.94.5.824)) [abstract].
  - Provider-reported support was modelled in 79 couples (daily stressors) and 196 couples (major stressor) over several weeks ([Iida et al. 2008](https://doi.org/10.1037/0022-3514.94.3.460)) [abstract].
- **Observer and experimental criteria for visibility:**
  - Coded invisible emotional support in 61 couples predicted goal achievement over a year without raising perceived support ([Girme, Overall & Simpson 2013](https://doi.org/10.1177/0146167213497802)) [abstract].
  - In 3 experiments (N = 257), invisible support reduced reactivity, and visible support was ineffective or harmful unless it avoided signalling inefficacy ([Bolger & Amarel 2007](https://doi.org/10.1037/0022-3514.92.3.458)) [abstract].
- **Parent–grown child support exchange:**
  - 633 parents reported support to 1,384 children older than 18: emotional, financial and practical help "every few weeks", more to needier or more successful children ([Fingerman et al. 2009](https://doi.org/10.1111/j.1741-3737.2009.00665.x)) [abstract].
  - 592 grown children and 399 parents took part. "Intense" support meant several types (financial, advice, emotional) many times a week; it was viewed as too much but was associated with children's better adjustment ([Fingerman et al. 2012](https://doi.org/10.1111/j.1741-3737.2012.00987.x)) [abstract].
  - A 7-day diary of 247 midlife parents found that 96% had contact with a child that week ([Fingerman et al. 2016](https://doi.org/10.1111/jomf.12273)) [abstract].
  - Instrument name: PRIOR KNOWLEDGE / UNVERIFIED, the Intergenerational Support Index.
- **Korean validation:** none located for daily support checklists or for intergenerational support indices. No targeted search was run.

#### Basic need satisfaction and frustration (rival c)
- **BPNSFS** ([Chen et al. 2015](https://doi.org/10.1007/s11031-014-9450-1), *Motivation and Emotion* 39(2), 216–236) [metadata].
  - The title states testing "across four cultures"; the four countries are PRIOR KNOWLEDGE / UNVERIFIED.
  - Structure: **24 items in six subscales of 4 items** (satisfaction and frustration × autonomy, relatedness, competence), as described in the Korean validation below [full text].
- **Korean validation (K-BPNSFS)** ([Yeom & Lee 2024](https://doi.org/10.3390/healthcare12242535), *Healthcare* 12(24), 2535) [full text, PMC]:
  - Sample: 367 community-dwelling cancer survivors.
  - Adaptation: a five-step cross-cultural process. The Korean version uses a 5-point scale.
  - Six-factor CFA: CFI = .953, TLI = .945, RMSEA = .050 (90% CI .043–.057), SRMR = .059.
  - Cronbach's α: from .672 (autonomy frustration) to .938 (competence satisfaction).
  - The authors state the BPNSFS "had not previously been translated or validated in Korean".
  - **Conflict:** a database record suggests a Korean workplace psychometric study (N = 486) with invariance evidence ([Kyobo Scholar record](https://scholar.kyobobook.co.kr/article/detail/4050027792125)) [secondary, not opened]. The two claims are unreconciled.
- **Relationship-specific need fulfilment, the version most relevant to rival (c):**
  - Need fulfilment was rated separately for mother, father, romantic partner and best friend. Within-person variability across partners was substantial, and relationship-level fulfilment predicted attachment security ([La Guardia, Ryan, Couchman & Deci 2000](https://doi.org/10.1037/0022-3514.79.3.367)) [abstract].
  - Both partners' need fulfilment uniquely predicted one's own relationship functioning; Study 3 used a diary ([Patrick et al. 2007](https://doi.org/10.1037/0022-3514.92.3.434)) [abstract].
  - Daily relationship-need fulfilment over 4 consecutive days predicted emotional experience ([Le & Agnew 2001](https://doi.org/10.1177/0265407501183007)) [abstract].
- **Daily diary use:** over 5 days with 2 children from each of 154 families, daily need satisfaction and frustration mediated the effects of autonomy support and psychological control ([van der Kaap-Deeder et al. 2017](https://doi.org/10.1037/dev0000218)) [abstract].

#### Relationship satisfaction (outcome $Y$)
- **Couples Satisfaction Index, CSI-32, CSI-16 and CSI-4** ([Funk & Rogge 2007](https://doi.org/10.1037/0893-3200.21.4.572)) [abstract]:
  - Developed with item response theory in 5,315 online participants.
  - It has higher precision and power than the MAT and the DAS, with strong convergent and construct validity.
- **Korean validation (K-CSI)** ([Kim et al. 2022](https://doi.org/10.4040/jkan.21177), *Journal of Korean Academy of Nursing*) [abstract]:
  - 218 couples (N = 436); translation, back-translation and review by five bilingual experts.
  - One-factor CFA for the 32-, 16- and 4-item versions, with slightly better fit for the 16- and 4-item forms.
  - Convergent validity with the Kansas Marital Satisfaction Scale, the DAS and the Family Relationship Assessment Scale; known-groups validity (depressive versus normal group).
  - Cut-offs for a distressed relationship: 105.5 (32 items), 50.25 (16 items) and 13.25 (4 items).
- **Parent–child dyads:** no validated parent–child analogue of the CSI was located (see Gaps).

#### Trust (model $T$, eq. 7; rival d)
- **Trust Scale** ([Rempel, Holmes & Zanna 1985](https://doi.org/10.1037/0022-3514.49.1.95); PsycTESTS [10.1037/t01317-000](https://doi.org/10.1037/t01317-000)) [abstract]:
  - Predictability, dependability and faith were distinct dimensions in established couples.
  - Item count: PRIOR KNOWLEDGE / UNVERIFIED, 17 items. Reporter: self about the partner.
- **Dyadic Trust Scale** ([Larzelere & Huston 1980](https://doi.org/10.2307/351903)) [metadata]. Item count: PRIOR KNOWLEDGE / UNVERIFIED, 8 items.
- **Brief or daily trust:** no validated daily trust short form was located. Trust has been used as a *between-person moderator* of daily processes: lower-trust individuals showed more day-to-day variability in perceived relationship quality in a 14-day diary, replicated in a 21-day diary ([Campbell, Simpson, Boldry & Rubin 2010](https://doi.org/10.1037/a0019714)) [abstract].
- **Korean validation:** none found for the Rempel or the Dyadic Trust Scale. The search found only Chinese (2024–25 preprint) and Indonesian (2025) adaptations of trust scales [secondary].

#### Attachment (rival d)
- **ECR-RS** ([Fraley, Heffernan, Vicary & Brumbaugh 2011](https://doi.org/10.1037/a0022898)) [abstract]:
  - Relationship-specific attachment to mother, father, partner and friend. More than 21,000 online participants; reliable, with structure similar to other measures.
  - Relationship-specific scores predicted intra- and interpersonal outcomes better than global measures (Study 2, N = 388).
  - Length: PRIOR KNOWLEDGE / UNVERIFIED, 9 items per target.
- **Korean ECR-R:**
  - Rasch analysis in N = 390 Korean college students. Items measured anxiety or avoidance, but "items measuring high levels of anxiety and avoidance may not be appropriate" for this sample ([Lee, Grossman & Krishnan 2008](https://doi.org/10.1177/0013164407313367)) [abstract].
  - **K-ECRR-SF:** a 12-item short form chosen by Rasch from the 36 ECR-R items for cultural equivalence, then CFA in a new sample. Criterion evidence covers reassurance seeking, loneliness, dyadic satisfaction, depression, anxiety and fear of intimacy ([Lee, Kim & Shin 2023](https://doi.org/10.1007/s10447-023-09503-6)) [abstract].
- **Korean ECR-RS:** no validation found. One 2015 Korean study used the ECR-RS with 317 undergraduates across four attachment figures and noted only one prior Korean use [secondary, via koreascience/earticle search].
- **State (diary-level) attachment:** the SAAM ([Gillath, Hart, Noftle & Stockdale 2009](https://doi.org/10.1016/j.jrp.2008.12.009)) [metadata]. A **Korean SAAM** exists ([Park et al. 2012](https://doi.org/10.4306/jknpa.2012.51.4.147), *Journal of Korean Neuropsychiatric Association*), designed "for capturing temporary fluctuations" [abstract, partial].

#### Commitment
- **Investment Model Scale** ([Rusbult, Martz & Agnew 1998](https://doi.org/10.1111/j.1475-6811.1998.tb00177.x)) [abstract]:
  - Three studies; good internal consistency; four factors (commitment, satisfaction, alternatives, investment).
  - Earlier scores predicted later dyadic adjustment and break-up.
  - Commitment subscale length: PRIOR KNOWLEDGE / UNVERIFIED, 7 items.
- **Repeated measurement:** in two multiwave studies, fluctuation in perceived partner commitment predicted break-up beyond its level and trend ([Arriaga et al. 2006](https://doi.org/10.1037/0022-3514.91.6.1045)) [abstract].
- **Korean validation:** none found for the IMS. A Korean *Commitment Inventory* (Stanley & Markman) validation exists: 8 factors, n = 328 for EFA and n = 333 for CFA, *Family and Family Therapy* 26(3), 2018 ([Kyobo record](https://scholar.kyobobook.co.kr/article/detail/4050026794191)) [secondary; no DOI verified].

#### Parental acceptance–rejection
- **PARQ, child, adult and parent forms:**
  - Theory and methods are summarised in [Rohner, Khaleque & Cournoyer 2005](https://doi.org/10.1525/eth.2005.33.3.299) [metadata].
  - A meta-analysis of 51 studies found the PARQ reliable among US ethnic groups and internationally ([Khaleque & Rohner 2002](https://doi.org/10.1177/0022022102033001006)) [abstract].
  - Lengths: Adult PARQ 60 items (per repository notes); short form PRIOR KNOWLEDGE / UNVERIFIED, 24 items.
  - Invariance: tested only between the US and Australia ([Gomez & Rohner 2011](https://doi.org/10.1177/1069397111403111)) [metadata; content per repository notes `evidence/notes/05-family-and-culture.md`].
- **Korean use:** "Korean youths' perceptions of parental control are correlated positively with perceived parental warmth and low neglect" ([Rohner & Pettengill 1985](https://doi.org/10.2307/1129739)) [abstract]. The repository notes that a Korean-language PARQ was used; its psychometrics were not verified. No Korean PARQ validation for emerging adults was found.

#### Psychological control and autonomy support (autonomy $U$ as a separate outcome)
- **Psychological Control Scale** ([Barber 1996](https://doi.org/10.2307/1131780)) [abstract]:
  - Two new measures; psychological control predicted youth internalising problems.
  - Refinement toward "feeling disrespected" in [Barber et al. 2012](https://doi.org/10.1016/j.adolescence.2011.10.010) [metadata].
  - Length: PRIOR KNOWLEDGE / UNVERIFIED, 8 items for the youth-report form.
- **P-PASS** ([Mageau et al. 2015](https://doi.org/10.1037/a0039325)) [metadata]:
  - A French-language validation; autonomy-support and control factors predicted young adults' life satisfaction and self-esteem [secondary].
  - Length: PRIOR KNOWLEDGE / UNVERIFIED, 24 items, 12 autonomy support and 12 control.
- **Meta-analysis** ([Bradshaw et al. 2025](https://doi.org/10.1037/amp0001389)) [abstract]:
  - k = 238, N = 126,423.
  - Autonomy support–well-being r = .30; psychological control–ill-being r = .26.
  - Each had unique effects, for example autonomy support r = .26 when controlling for control. This supports measuring both, separately from "care".
- **Korean:**
  - Dependency- and achievement-oriented psychological control in Belgian (N = 290) and South Korean (N = 321) adolescents; associations were similar across samples ([Soenens et al. 2012](https://doi.org/10.1016/j.adolescence.2011.05.001)) [abstract].
  - Two-facet model with separate intrusiveness and emotional manipulation scales in Korean adolescents aged 13–16 (N = 354) ([Choe et al. 2026](https://doi.org/10.1177/10731911261440140)) [abstract].
  - **No Korean P-PASS was found.** The closest is a Korean Helicopter Parenting and Autonomy Supportive Behaviors scale (*Child Health Nursing Research*, 2016; 229 nursing students) [secondary; DOI not verified].
  - All Korean psychological-control validations located are in adolescents, not adults aged 19–29.

#### Coercive control and intimate partner violence (safety indicators $\mathbf Z$ for $\mathrm{Safe}(x)$)
- **CTS2** ([Straus, Hamby, Boney-McCoy & Sugarman 1996](https://doi.org/10.1177/019251396017003001)) [abstract]:
  - Scales: psychological aggression, physical assault, sexual coercion, injury and negotiation. Reliability .79–.95; "preliminary evidence of construct validity".
  - Asks about both perpetration and victimisation.
  - Length: PRIOR KNOWLEDGE / UNVERIFIED, 78 items.
- **CTS2S short form** ([Straus & Douglas 2004](https://doi.org/10.1891/vivi.19.5.507.63686)) [abstract]:
  - "Comparable in validity to the full CTS2"; it identifies fewer cases, so it is a "useful screening instrument" when time is limited.
  - Length: PRIOR KNOWLEDGE / UNVERIFIED, 20 items.
- **Cross-cultural CTS2** ([Straus 2004](https://doi.org/10.1177/1069397104269543)) [abstract]: 7,179 students at 33 universities in 17 countries; high α and low confounding with social desirability. Whether a Korean site was included is UNVERIFIED.
- **Korean CTS2:** Son Jung-Young's validity study of the CTS2 with Korean couples (*Korean Journal of Family Relations*; dated 2008 in the record) reports subscale α .64–.94 and total α .90 ([KISS record](https://kiss.kstudy.com/Detail/Ar?key=219167)) [secondary; no DOI; details UNVERIFIED]. No Korean CTS2S was found.
- **Checklist of Controlling Behaviors** ([Lehmann, Simmons & Pillai 2012](https://doi.org/10.1177/1077801212456522)) [abstract]:
  - 84 items in 10 subscales (physical, sexual, male privilege, isolation, minimising/denying, blaming, intimidation, threats, emotional, economic).
  - Validated with 2,135 women in domestic-violence shelters, a survivor-report, clinical sample.
  - Korean validation: none found (also none in repository notes `04-safety-coercion-autonomy.md`).
- **Brief IPV screens:**
  - **CAS-R-SF:** 15 items, developed from pooled data on 6,278 Canadian women plus ratings by 31 international experts ([Ford-Gilboe et al. 2016](https://doi.org/10.1136/bmjopen-2016-012824)) [abstract].
  - **HARK:** four questions validated against the Composite Abuse Scale in 232 general-practice patients ([Sohal, Eldridge & Feder 2007](https://doi.org/10.1186/1471-2296-8-49)) [abstract].
  - **Systematic review** of 33 studies ([Rabin et al. 2009](https://doi.org/10.1016/j.amepre.2009.01.024)) [abstract]:
    - HITS: sensitivity 30–100%, specificity 86–99%;
    - WAST: sensitivity 47%, specificity 96%;
    - PVS: sensitivity 35–71%, specificity 80–94%;
    - AAS: sensitivity 93–94%, specificity 55–99%.
  - **AAS source:** [McFarlane et al. 1992](https://doi.org/10.1001/jama.1992.03480230068030) [metadata].
  - **USPSTF:** the 2018 update "concludes with moderate certainty that screening for IPV in women of …" ([US Preventive Services Task Force 2018](https://doi.org/10.1001/jama.2018.14741)) [abstract, truncated; population and grade not verified here].
  - **Lethality risk:** the Danger Assessment, revised from an 11-city femicide study, reached AUC .90 in an independent attempted-femicide sample ([Campbell, Webster & Glass 2009](https://doi.org/10.1177/0886260508317180)) [abstract].
  - **Definitions:** definitions of coercive control are inconsistent ([Hamberger, Larsen & Lehrner 2017](https://doi.org/10.1016/j.avb.2017.08.003)) [metadata; characterisation per repository].
- **Korean IPV measures located (none are Korean versions of HITS, WAST or CAS):**
  - a Korean Dating Violence Questionnaire–Revised (*Korean Journal of Health Psychology*, 2021; 300 young adults; five factors);
  - a Korean Index of Spouse Abuse (*KSWP*);
  - a Korean Validation and Invalidation Response Scale, a psychological-violence measure (2012; 346 female college students; α = .922).
  - All three are [secondary] via accesson.kr and university repository records; no DOIs were verified.

#### Depressive symptoms and stress (confounders $\mathbf x(t)$)
- **PHQ-9** ([Kroenke, Spitzer & Williams 2001](https://doi.org/10.1046/j.1525-1497.2001.016009606.x)) [abstract]:
  - 9 items over a 2-week window; 6,000 primary care and obstetrics-gynaecology patients.
  - A score of ≥10 gave sensitivity 88% and specificity 88% for major depression; scores of 5, 10, 15 and 20 mark mild, moderate, moderately severe and severe.
  - **PHQ-2** (depressed mood and anhedonia) ([Kroenke, Spitzer & Williams 2003](https://doi.org/10.1097/01.MLR.0000093487.78664.3C)) [abstract].
- **Korean PHQ-9:**
  - 1,060 adults over 60: internal consistency .88, test–retest .60, optimal cut-off 5 for older Koreans ([Han et al. 2008](https://doi.org/10.1016/j.comppsych.2007.08.006)) [abstract].
  - 567 psychiatric outpatients: α .876 (PHQ-9) and .892 (PHQ-8), with no AUC difference between them ([Shin et al. 2019](https://doi.org/10.30773/pi.2019.02.01)) [abstract].
  - A Korean PHQ-9 validation in *Global Health and Nursing* 7(2), 71–78 ([Park 2017](https://doi.org/10.35144/ghn.2017.7.2.71)) [metadata].
- **Perceived Stress Scale:**
  - 14 items, tested in three samples ([Cohen, Kamarck & Mermelstein 1983](https://doi.org/10.2307/2136404)) [abstract].
  - **Korean PSS-14, PSS-10 and PSS-4:** forward and back translation, EFA and CFA, and concurrent validity with the CES-D, in patients with chronic disease ([Lee et al. 2015](https://doi.org/10.1111/scs.12131)) [abstract].
  - Psychometric review: [Lee 2012](https://doi.org/10.1016/j.anr.2012.08.004) [metadata].
- **Daily stressors:** the Daily Inventory of Stressful Events, an interview-based daily telephone measure; in 1,031 US adults, at least one stressor occurred on 40% of days ([Almeida, Wethington & Kessler 2002](https://doi.org/10.1177/1073191102091006)) [abstract]. No Korean version was searched.

#### Summary: Korean-language validation status
| Construct | Measure | Korean validation |
|---|---|---|
| Perceived responsiveness | PRI; PPRS | **None found** |
| Support adequacy | SIRRS; Brock & Lawrence | None located (no targeted search) |
| Daily support acts | Bolger-style checklists; intergenerational support | None located (no targeted search) |
| Need satisfaction/frustration | BPNSFS | Cancer survivors ([10.3390/healthcare12242535](https://doi.org/10.3390/healthcare12242535)); a workplace study is an unverified lead |
| Satisfaction | CSI-32/16/4 | **Yes** ([10.4040/jkan.21177](https://doi.org/10.4040/jkan.21177)) |
| Trust | Rempel; Dyadic Trust Scale | **None found** |
| Attachment | ECR-RS | ECR-RS: none. ECR-R ([10.1177/0013164407313367](https://doi.org/10.1177/0013164407313367)); K-ECRR-SF ([10.1007/s10447-023-09503-6](https://doi.org/10.1007/s10447-023-09503-6)); SAAM ([10.4306/jknpa.2012.51.4.147](https://doi.org/10.4306/jknpa.2012.51.4.147)) |
| Commitment | IMS | **None found** (Commitment Inventory record only) |
| Acceptance–rejection | PARQ | Used in 1985 with adolescents; no psychometric validation verified |
| Control and autonomy support | PCS; P-PASS | Psychological control in adolescents ([10.1016/j.adolescence.2011.05.001](https://doi.org/10.1016/j.adolescence.2011.05.001); [10.1177/10731911261440140](https://doi.org/10.1177/10731911261440140)); **no P-PASS** |
| IPV | CTS2/CTS2S; CCB; HITS/WAST/CAS-R-SF | CTS2: record only; others **none found** |
| Depression | PHQ-9 | **Yes** ([10.1016/j.comppsych.2007.08.006](https://doi.org/10.1016/j.comppsych.2007.08.006); [10.30773/pi.2019.02.01](https://doi.org/10.30773/pi.2019.02.01)) |
| Stress | PSS | **Yes** ([10.1111/scs.12131](https://doi.org/10.1111/scs.12131)) |

### Inferences
- **Mapping to rivals:**
  - Rival (a), amount: the sum of received acts from daily checklists, or SIRRS frequency.
  - Rival (b), perception only: PRI or PPRS, plus daily responsiveness items.
  - Rival (c), need fulfilment: the BPNSFS, preferably the relationship-specific La Guardia/Patrick form, because the model's $N$ and $S$ are relationship- and channel-specific.
  - Rival (d), trust and attachment: Rempel trust and the relationship-specific ECR-RS at baseline, the SAAM for state attachment, and repeated trust ratings.
  - All four rivals need commensurate measurement alongside the translation constructs, so model comparison is not confounded by unequal reliability.
- **Commensurate desired and received ratings for $N$ and $S$ have precedent.** Xu & Burleson (desired versus experienced) and Brock & Lawrence (less or more than desired) both did this, and Xu & Burleson's includes a Chinese sample. Neither covers the care channels in the model (presence, talk, touch, practical help, money). A channel-specific version needs new items and cannot be called "validated".
- **The safety screen and the dyadic outcome battery should stay separate instruments.** CTS2 or CTS2S asks both partners about their own and the partner's acts, which raises the WHO household concern discussed in §5. The CAS-R-SF and HARK are victimisation-only and shorter; the CCB is long and was validated only in shelter samples.
- **Parent–child dyads lack direct analogues** of the CSI, the PRI and trust scales. Parallel wording (as `paper/18` proposes) needs its own invariance tests across roles (§4).

### Gaps
- No Korean validation was found for the PRI, PPRS, Rempel trust, Dyadic Trust Scale, IMS, ECR-RS, P-PASS, CCB, CTS2S or the HITS/WAST/CAS-R-SF screens. No targeted Korean search was run for the SIRRS, support checklists or daily stress inventories.
- No validated **daily** trust short form, and no validated daily form of the PRI, was located. Daily responsiveness items exist (Laurenceau 2005; Maisel & Gable 2009) but their wording was not verified.
- Item counts flagged PRIOR KNOWLEDGE (PPRS, Rempel, DTS, ECR-RS, IMS, PARQ-SF, PCS, P-PASS, CTS2, CTS2S, SAAM) need checking against the full texts.
- The BPNSFS Korean validation status conflicts between Yeom & Lee (2024) and a workplace-study record; this is unresolved.
- No parent-reported versions with Korean validation were found for any construct. The proposed study's emerging-adult (19–29) population is not covered by the Korean psychological-control validations, which are adolescent samples.

## 2. Design: dyadic diary and burst designs, and slower intervals for trust, needs and relationship quality

### Takeaway
Published dyadic diaries in the support and responsiveness literature run from 14 to 42 days with one evening report; 7-day diaries appear in single-member designs. EMA meta-analyses show average compliance of about 75–79%. Compliance depends more on incentives and questionnaire length than on prompts per day, and initial-elevation bias and measurement reactivity should be designed for, not assumed away. Slow constructs (trust, need fulfilment, relationship quality, commitment) suit weekly, biweekly or burst-level measurement, with intervals chosen to match the hypothesised timescale.

### Cited Findings
- **EMA meta-analysis** ([Wrzus & Neubauer 2023](https://doi.org/10.1177/10731911211067538)) [abstract]:
  - k = 477 articles, N = 677,536.
  - The average study "scheduled six assessments per day, lasted for 7 days, and obtained a compliance of 79%".
  - Studies with more assessments per day scheduled fewer days, but "the number of assessments did not predict compliance or dropout".
  - Compliance was higher with financial incentives.
- **Substance users** ([Jones et al. 2019](https://doi.org/10.1111/add.14503)) [abstract]: 126 studies, 19,431 participants. Pooled compliance 75.06% (95% CI 72.37–77.65%), not significantly associated with prompt frequency or length of the assessment period.
- **Severe mental disorders** ([Vachon et al. 2019](https://doi.org/10.2196/14475)) [abstract]: compliance was higher with a fixed sampling scheme, higher incentives, longer intervals between prompts and fewer prompts per day. It was lower with more male participants and in psychosis.
- **Experimental manipulation of burden** ([Eisele et al. 2022](https://doi.org/10.1177/1073191120957102)) [abstract]:
  - 163 students received 30- or 60-item questionnaires 3, 6 or 9 times a day for 14 days.
  - Longer questionnaires increased burden and compromised data quantity and quality; higher sampling frequency did not.
  - The authors "advise against the use of long ESM questionnaires".
- **Initial elevation bias** ([Shrout et al. 2018](https://doi.org/10.1073/pnas.1712277115)) [abstract]: early reports are elevated. The effect is larger for internal states than for behaviours, and for negative states and symptoms than for positive states.
- **Reactivity is item-level negligible but should be randomised** ([Arslan et al. 2021](https://doi.org/10.1037/met0000294)) [abstract]:
  - Planned-missingness daily diary with more than 1,300 people over up to 70 days.
  - Day of first presentation, item order and item number produced only negligible bias.
  - The authors recommend routinely randomising item display, order, timing and frequency.
- **Reactivity in couples** ([Merrilees, Goeke-Morey & Cummings 2008](https://doi.org/10.1016/j.brat.2007.11.007)) [abstract]:
  - 15-day event-contingent marital-conflict diaries (n = 110 couples) against a non-randomised control (n = 57).
  - No effect on *observed* emotions and behaviour, but husbands' self-reported marital quality declined during recording: "potential reactivity effects".
- **Diary design parameters in the support and responsiveness literature** [abstract]:
  - Dyadic (both members report):
    - 42 days, 96 couples ([Laurenceau, Barrett & Rovine 2005](https://doi.org/10.1037/0893-3200.19.2.314));
    - 31 days ([Gleason et al. 2008](https://doi.org/10.1037/0022-3514.94.5.824));
    - 14 and 21 days ([Campbell et al. 2010](https://doi.org/10.1037/a0019714));
    - 15 days of event-contingent diaries ([Merrilees et al. 2008](https://doi.org/10.1016/j.brat.2007.11.007));
    - several weeks, 79 and 196 couples ([Iida et al. 2008](https://doi.org/10.1037/0022-3514.94.3.460)).
  - Single-member diaries of 7 days: married individuals ([Dehle et al. 2001](https://doi.org/10.1080/01926180126500)) and parents reporting on grown children ([Fingerman et al. 2016](https://doi.org/10.1111/jomf.12273)).
- **Reviews of dyadic and family diary designs** cover the questions only such data can answer and the analysis issues specific to dyadic and family diaries ([Laurenceau & Bolger 2005](https://doi.org/10.1037/0893-3200.19.1.86); [Bolger, Davis & Rafaeli 2003](https://doi.org/10.1146/annurev.psych.54.101601.145030)) [abstract].
- **Burst designs:**
  - Repeated bursts of daily or momentary assessment "can improve detection of long-term intraindividual change". They also allow fine-grained coupling to be studied over different intervals, at some cost in implementation and analysis ([Sliwinski 2008](https://doi.org/10.1111/j.1751-9004.2007.00043.x)) [abstract].
  - Bursts separate short-term variation and learning effects from long-term change ([Rast, MacDonald & Hofer 2012](https://doi.org/10.1024/1662-9647/a000054)) [abstract].
- **Matching intervals to the process:**
  - Longitudinal design should integrate the theoretical model of change, the temporal design and the statistical model ([Collins 2006](https://doi.org/10.1146/annurev.psych.57.102904.190146)) [abstract].
  - Cross-lagged estimates depend on the lag, and "optimal time lags for panel designs are usually quite short" ([Dormann & Griffin 2015](https://doi.org/10.1037/met0000041)) [abstract, PubMed].
  - Continuous-time SEM handles unequal intervals and makes estimates comparable across studies with different lags ([Voelkle et al. 2012](https://doi.org/10.1037/a0027543)) [abstract].
  - Progress needs theorising "about the timescale that a process operates on" ([Hamaker 2023; print 2026, *Psychological Methods* 31(1), 56–76](https://doi.org/10.1037/met0000600)) [abstract].
- **Slower-interval evidence for relational constructs:**
  - The brief PRI administered every other week for 8 weeks tracked support and conflict fluctuations better than global evaluations ([Crasta et al. 2021](https://doi.org/10.1037/pas0000986)) [abstract].
  - Multiwave fluctuation in satisfaction predicted break-up beyond its level ([Arriaga 2001](https://doi.org/10.1037/0022-3514.80.5.754)) [abstract].
  - So did multiwave fluctuation in perceived partner commitment ([Arriaga et al. 2006](https://doi.org/10.1037/0022-3514.91.6.1045)) [abstract].
- **Long daily series for dynamic models:** the COGITO data (two samples of more than 100 people, about 100 days each) supported multilevel VAR with random residual variances in DSEM ([Hamaker et al. 2018](https://doi.org/10.1080/00273171.2018.1446819)) [abstract].

### Inferences
- **Diary length and burden.** A 28-day evening diary is within the published dyadic range (14–42 days), but the protocol in `paper/18` asks for a great deal each evening. By channel, it asks for acts performed, intended care, cost, acts noticed, wanted and received care, regard, inferred motive, closeness, mood, stress, trust, satisfaction and predictions of the partner. On the Eisele et al. evidence, length is what degrades data. Options:
  - planned missingness (Arslan et al. 2021), for example rotating channel blocks;
  - moving slow constructs (trust, need satisfaction, satisfaction, commitment) to weekly or biweekly modules.
- **Initial elevation and run-in.** Discarding or modelling the first diary day(s), or adding a short run-in, addresses initial elevation. The assessment-only control already planned in `paper/18` estimates reactivity. Merrilees et al. suggest checking self-reported relationship quality, not only behaviour, for reactivity.
- **A burst structure fits the model's mixed timescales.** For example, the 28-day diary plus shorter bursts at later points before the 12-month follow-up:
  - fast processes (detection $D$, construal $Q$, daily acts $E$) are measured daily;
  - slow states (trust $T$, giver model $\tilde N$, need fulfilment) are measured once per burst or weekly;
  - continuous-time models (Voelkle 2012) can absorb the unequal spacing.
  - The burst spacing itself has no evidence base specific to relationships (see Gaps).
- **Incentives.** Compliance scheduled per member, with financial incentives (Wrzus & Neubauer; Vachon), matters more in dyads, because the dyad-day is complete only if *both* members respond.

### Gaps
- No meta-analysis of compliance specific to **dyadic** diaries (joint dyad-day completeness), or to Korean samples, was found.
- No empirical guidance was found on burst spacing for trust, need or relationship-quality dynamics. Dormann & Griffin and Hamaker argue conceptually but do not give relationship-specific lags.
- Schultzberg & Muthén's numeric thresholds for days per person were not in the abstract (see §3).
- The Bolger & Laurenceau (2013) book on intensive longitudinal methods has no DOI and was not accessed.

## 3. Power analysis: simulation tools for multilevel and dyadic intensive longitudinal designs, and setting smallest effects of interest

### Takeaway
Each available tool covers one slice of the design:
- multilevel ILD with the number of time points fixed: PowerAnalysisIL;
- dyadic intensive longitudinal APIM with linear or quadratic effects: PowerLAPIM;
- cross-sectional and mediation APIM: APIMPowerR and the Ledermann et al. Monte Carlo approach;
- general (G)LMMs: simr;
- SEM and DSEM: Mplus Monte Carlo;
- micro-randomized trials: MRTSampleSize.

None covers multilevel dyadic response surfaces or the route decomposition, so a custom simulation is required. The evidence that small level-2 and cross-level interactions are badly underpowered supports budgeting several hundred dyads per country, as `paper/18` already does.

### Cited Findings
- **PowerAnalysisIL** ([Lafit et al. 2021](https://doi.org/10.1177/2515245920978738)) [abstract]; app details from the [PowerAnalysisIL repository](https://github.com/ginettelafit/PowerAnalysisIL) [secondary, fetched]:
  - Shiny app and R package for simulation-based power in multilevel models with serially correlated (AR(1)) level-1 errors.
  - It assumes a fixed sampling protocol and "focus[es] on the number of participants".
  - **Eight models:** group difference in means; level-2 predictor of the mean; level-1 predictor; group difference in a level-1 slope; cross-level interaction; mean autoregressive effect; group difference in the autoregressive effect; level-2 × lagged-outcome interaction.
  - **Cannot do:** dyadic interdependence, quadratic terms or latent measurement models; the number of occasions is not optimised.
- **PowerLAPIM** ([Lafit, Sels, Adolf, Loeys & Ceulemans 2022](https://doi.org/10.1177/02654075221080128), *JSPR*) [abstract]:
  - Simulation-based power for **32 longitudinal APIM variants**, including **linear and quadratic actor and partner effects**.
  - Moderation by time-varying covariates or a categorical dyad-level predictor (group differences), with optional autoregressive effects.
  - It targets the number of dyads, not the number of repeated measurements, which is treated as fixed; sensitivity analyses over parameter uncertainty and over the number of measurements are illustrated.
  - **Cannot do:** response-surface congruence tests ($a_1$–$a_5$), mediation or route decomposition, or MRT excursion effects.
- **APIMPowerR** (Ackerman & Kenny; Shiny app at robert-a-ackerman.shinyapps.io/APIMPowerRdis/):
  - Power, or required sample size, for the *cross-sectional* APIM with distinguishable or indistinguishable dyads.
  - Presented as "APIMPowerR: Sample Size Planning for Research Using the Actor-Partner Interdependence Model" at the 2017 APS convention ([APS archive](https://www.psychologicalscience.org/conventions/archive/2017annual/paper/2230/); [Garcia workshop slides](https://randilgarcia.github.io/week-dyad-workshop/Power.pdf)) [secondary].
  - A 2016 citable publication by Ackerman & Kenny was **not** found; cite the software.
- **Simple and mediation APIM by Monte Carlo** ([Ledermann, Rudaz, Wu & Cui 2022](https://doi.org/10.1111/fare.12644)) [abstract]:
  - Input is a correlation matrix, with skewness, kurtosis and missing data allowed.
  - Indistinguishable dyads need "about half" the sample of distinguishable dyads, and skew raises the required N.
  - In mediation APIMs, some simple indirect effects can be significant while no total indirect or total effect is.
- **Relationship-research power by simulation** ([Lane & Hennes 2018](https://doi.org/10.1177/0265407517710342)) [abstract]: multilevel and SEM designs for dyads and families, with explicit trade-offs between "the number of dyads sampled or the number of repeated measurements per dyad"; two worked examples.
- **Two-level models** ([Arend & Schäfer 2019](https://doi.org/10.1037/met0000195)) [abstract]:
  - Monte Carlo power with simr and rules of thumb.
  - With level-1 n up to 30 and level-2 N up to 200, medium and large fixed effects are detectable, but "small L2 direct- or cross-level interaction effects cannot be detected with up to 200 clusters".
- **DSEM sample sizes** ([Schultzberg & Muthén 2018](https://doi.org/10.1080/10705511.2017.1392862)) [abstract]: for two-level AR(1) models (Bayesian, Mplus 8), "samples with many subjects and few time points … perform substantially better than samples with few subjects and many time points".
- **Interactions** ([Sommet, Weissman, Cheutin & Elliot 2023](https://doi.org/10.1177/25152459231178728)) [abstract]:
  - First-order interactions only: 12 interaction shapes, with derived sample sizes for power .80, .90 and .95 in between-participants designs.
  - Median power to detect a typical interaction in 159 published studies was **.18**.
  - Preregistered one-tailed tests gave a +21% gain; mixed designs also raise power.
  - The abstract does **not** address quadratic (polynomial) terms.
- **simr** ([Green & MacLeod 2016](https://doi.org/10.1111/2041-210X.12504)) [abstract]: Monte Carlo power and power curves for lme4 (G)LMMs.
- **(G)LMM power tutorial** ([Kumle, Võ & Draschkow 2021](https://doi.org/10.3758/s13428-021-01546-0)) [abstract]: simulation-based power using published or pilot data, for numbers of stimuli, and without pilot data.
- **Mplus Monte Carlo for SEM** ([Muthén & Muthén 2002](https://doi.org/10.1207/S15328007SEM0904_8)) [metadata].
- **MRT sample size:**
  - Liao et al. proposed a test statistic for proximal effects with a sample-size calculator evaluated by simulation ([Liao, Klasnja, Tewari & Murphy 2016](https://doi.org/10.1002/sim.6847)) [abstract].
  - R package: [MRTSampleSize (CRAN)](https://doi.org/10.32614/cran.package.mrtsamplesize) [metadata].
- **Interference within clusters:** causal excursion effects can be estimated under cluster-level heterogeneity and interference ([Shi, Wu & Dempsey 2023](https://doi.org/10.1093/biomet/asac065)) [abstract]. This is relevant because a prompt to one dyad member can affect the other.
- **Few dyads:** low ICC, many singletons or few dyads produce non-convergence, bias and poor coverage for variance components in multilevel dyadic models; more dyads help ([Du & Wang 2016](https://doi.org/10.1027/1614-2241/a000105)) [abstract].
- **SRM planning:** generalizability-theory reliability formulas exist for the actor, partner, group and relationship components of round-robin data, "for planning" ([Bonito & Kenny 2010](https://doi.org/10.1111/j.1475-6811.2010.01274.x)) [abstract].
- **Smallest effect size of interest (SESOI) and justification:**
  - TOST equivalence tests reject effects at least as large as a pre-specified SESOI; the paper reviews ways to set it ([Lakens, Scheel & Isager 2018](https://doi.org/10.1177/2515245918770963)) [abstract]; TOST primer with spreadsheet and R package ([Lakens 2017](https://doi.org/10.1177/1948550617697177)) [abstract].
  - Six ways to justify sample size, including a-priori power, accuracy planning and resource constraints ([Lakens 2022](https://doi.org/10.1525/collabra.33267)) [abstract].
  - An anchor-based "minimum subjectively experienced difference" can define the SESOI ([Anvari & Lakens 2021](https://doi.org/10.1016/j.jesp.2021.104159)) [abstract].

### Inferences
- **Which tool for which parameter:**
  - H8 (MRT match versus intensity): MRTSampleSize or the Liao et al. calculator, with the dyad treated as a cluster (Shi et al.) when the outcome is the child's but the prompt goes to the parent.
  - Daily APIM actor and partner effects, including quadratic ones: PowerLAPIM.
  - Single-person multilevel and autoregressive models: PowerAnalysisIL.
  - Baseline APIM and mediation: Ledermann et al. or APIMPowerR.
  - Multilevel cubic response surfaces (H2), the route decomposition (H3) and SRM variance components (H6): **custom simulation** in simr/lme4 or Mplus Monte Carlo is the only option located.
- **Citation correction for `paper/18`.** It cites Sommet et al. (2023) for "quadratic and interaction terms". On the abstract, Sommet et al. support the claim for interactions only. The quadratic-term claim needs its own simulation or a different source.
- **Dyads over days.** Arend & Schäfer (small cross-level interactions undetectable with up to 200 clusters) and Schultzberg & Muthén (subjects matter more than time points) both point to spending budget on more dyads rather than more days, consistent with "several hundred dyads per country".
- **SESOIs per hypothesis:** effect sizes should be anchored to minimum subjectively experienced differences on the outcomes (Anvari & Lakens) or to published effect sizes, and pre-registered as TOST bounds for the mismatch terms (H2) and the match effect (H8).

### Gaps
- No published power tool for multilevel or dyadic **response surface analysis** congruence tests was found; a Crossref search returned only applied RSA papers.
- No power method for **SRM variance components in four-person families measured daily** was found, beyond Bonito & Kenny's reliability formulas.
- No citable 2016 APIMPower paper by Ackerman & Kenny was found.
- PowerLAPIM, PowerAnalysisIL and Schultzberg & Muthén do not optimise the number of days jointly with the number of dyads; Lane & Hennes discuss the trade-off but give no general rule in the abstract.

## 4. Identification: within-person mediation, micro-randomized trials, DSEM, limits of cross-lagged models, invariance, and SRM requirements

### Takeaway
Randomising giver prompts in a micro-randomized trial identifies the *total* short-run causal excursion effects of channel match and intensity. Splitting an act's effect into $\beta_{\text{sub}}$ and $\beta_{\text{sym}}$ is a mediation decomposition through $Q$, which stays unrandomised. It therefore still needs sequential ignorability of the mediator plus a pre-registered sensitivity analysis.

Within-person centring removes stable trust and attachment (rival d) but not time-varying confounding. The classic cross-lagged panel model should be avoided. Measurement invariance must be shown across partners and roles, across time and across countries before comparing paths or means. Family SRM tests need groups of at least four with multiple indicators.

### Cited Findings
- **Causal mediation:**
  - Imai, Keele & Tingley give a model-free definition, identification, estimation and sensitivity analysis for causal mediation effects, applicable to nonlinear models and to discrete mediators and outcomes ([Imai, Keele & Tingley 2010](https://doi.org/10.1037/a0020761)) [abstract].
  - Under "a particular version of sequential ignorability", the average causal mediation effect is nonparametrically identified. Because that assumption "may be too strong in many applied settings", "sensitivity analysis is essential" ([Imai, Keele & Yamamoto 2010](https://doi.org/10.1214/10-STS321)) [abstract].
  - Reversing arrows or comparing fit indices cannot pick the right causal model ([Rohrer, Hünermund, Arslan & Elson 2022](https://doi.org/10.1177/25152459221095827)) [abstract].
- **Within-person (multilevel) mediation:**
  - Random indirect effects with all variables at level 1 ([Bauer, Preacher & Gil 2006](https://doi.org/10.1037/1082-989X.11.2.142)) [abstract].
  - Within- and between-group effects can be conflated in HLM mediation ([Zhang, Zyphur & Preacher 2009](https://doi.org/10.1177/1094428108327450)) [abstract].
  - Multilevel SEM separates within and between components of indirect effects ([Preacher, Zyphur & Zhang 2010](https://doi.org/10.1037/a0020141)) [abstract].
- **Within-person data and causality:** within-person data are "not necessary" and "not sufficient" for causal inference, because "time-varying confounders can lead to spurious within-persons associations" ([Rohrer & Murayama 2023](https://doi.org/10.1177/25152459221140842)) [abstract].
- **Micro-randomized trials:**
  - The MRT design and the causal excursion effect; the weighted and centred least-squares (WCLS) estimator gives consistent estimates and can be run in standard software ([Qian et al. 2022](https://doi.org/10.1037/met0000283)) [abstract].
  - Original design for optimising just-in-time adaptive interventions ([Klasnja et al. 2015](https://doi.org/10.1037/hea0000305)) [abstract].
  - Moderated effects are defined with potential outcomes, allowing that "potential moderators might be influenced by past treatment" ([Boruvka et al. 2018](https://doi.org/10.1080/01621459.2017.1305274)) [abstract].
  - Methods exist for cluster-level heterogeneity and interference ([Shi, Wu & Dempsey 2023](https://doi.org/10.1093/biomet/asac065)) [abstract].
- **DSEM:**
  - DSEM "models intraindividual changes over time on Level 1 and allows the parameters … to vary across individuals on Level 2" ([Schultzberg & Muthén 2018](https://doi.org/10.1080/10705511.2017.1392862)) [abstract]; framework paper [Asparouhov, Hamaker & Muthén 2018](https://doi.org/10.1080/10705511.2017.1406803) [metadata].
  - Measurement models inside DSEM allow testing whether scales are "invariant across time and across people", which summed scores cannot ([McNeish et al. 2021](https://doi.org/10.1080/10705511.2021.1915788)) [abstract].
- **Cross-lagged models:**
  - With trait-like stability, CLPM lagged parameters "do not represent the actual within-person relationships"; random intercepts separate them ([Hamaker, Kuiper & Grasman 2015](https://doi.org/10.1037/a0038889)) [abstract, PubMed].
  - Under realistic assumptions the CLPM "is very likely to find spurious cross-lagged effects" ([Lucas 2023](https://doi.org/10.1177/25152459231158378)) [abstract].
  - Latent-variable alternatives such as the RI-CLPM "strongly depend on the specific parametric assumptions" ([Lüdtke & Robitzsch 2022](https://doi.org/10.1080/10705511.2022.2065278)) [abstract].
- **Measurement invariance:**
  - Configural, metric and scalar steps are usual; residual invariance is reported less often. Alternative fit indices dominate, and partial invariance is reported for about one third of tests ([Putnick & Bornstein 2016](https://doi.org/10.1016/j.dr.2016.06.004)) [abstract, PubMed].
  - ΔCFI, Δgamma-hat and ΔMcDonald's NCI are recommended, with proposed critical values ([Cheung & Rensvold 2002](https://doi.org/10.1207/S15328007SEM0902_5)) [abstract].
  - Fit-index sensitivity depends on the pattern and proportion of non-invariance and on unequal group sizes; cut-offs are recommended ([Chen 2007](https://doi.org/10.1080/10705510701301834)) [abstract]. The specific numeric cut-offs are PRIOR KNOWLEDGE / UNVERIFIED in this session.
  - **Alignment** estimates group factor means and variances "without requiring exact measurement invariance", starting from the configural model ([Asparouhov & Muthén 2014](https://doi.org/10.1080/10705511.2014.919210)) [abstract]. A Monte Carlo study shows how to assess alignment quality ([Muthén & Asparouhov 2014](https://doi.org/10.3389/fpsyg.2014.00978)) [abstract].
  - Alignment (groups as fixed) can be compared with random-intercept, random-loading two-level models (groups as random), illustrated on 26 countries and about 50,000 people ([Muthén & Asparouhov 2018](https://doi.org/10.1177/0049124117701488)) [abstract].
  - **Dyadic invariance:** fully dyadic invariance models and the *dySEM* R package were applied in a Registered Report of 282 heterosexual couples. Several popular measures were dyadically invariant, while "a few display concerning levels and interesting patterns of noninvariance" ([Sakaluk, Fisher & Kilshaw 2021](https://doi.org/10.1111/pere.12341)) [abstract].
- **Social Relations Model:**
  - Origin: [Kenny & La Voie 1984](https://doi.org/10.1016/S0065-2601(08)60144-6) [metadata].
  - **Round-robin requirement:** "all groups must have at least four people", and relationship effects are separated from error with "multiple indicators of the construct, either across time or with different measures" ([Kenny, SOREMO page](https://davidakenny.net/srm/soremo.htm)) [secondary, author's site].
  - **Family SRM with roles:**
    - Perceived coerciveness in two-parent, two-child families, analysed by SEM ([Cook 1994](https://doi.org/10.1037/0022-006X.62.3.500)) [abstract].
    - Multilevel family SRM with father, mother and child roles, covariates and missing data ([Snijders & Kenny 1999](https://doi.org/10.1111/j.1475-6811.1999.tb00204.x)) [abstract].
    - Single-family SRM assessment ([Cook & Kenny 2004](https://doi.org/10.1037/0893-3200.18.2.361)) [abstract].
    - The *fSRM* R package handles actor, partner, relationship and family levels and compares means and variances within and between groups of families ([Stas, Schönbrodt & Loeys 2015](https://doi.org/10.1037/fam0000058)) [abstract]. CRAN: "Groups ranging from three members up to an unlimited number of members are supported" ([fSRM 0.6.5](https://cran.r-project.org/package=fSRM)) [secondary, CRAN page].
  - **Review:** reanalyses of 17 family data sets found perceiver and relationship characteristics the most important sources of variance ([Eichelsheim et al. 2009](https://doi.org/10.1111/j.1741-3737.2009.00652.x)) [abstract].
  - **Longitudinal extension:** the social relations growth model ([Nestler et al. 2017](https://doi.org/10.1007/s11336-016-9546-5)) [abstract].
  - **Designs and software overview:** [Back & Kenny 2010](https://doi.org/10.1111/j.1751-9004.2010.00303.x) [abstract]; TripleR for round robins without roles, [Schönbrodt, Back & Schmukle 2012](https://doi.org/10.3758/s13428-011-0150-4) [metadata].

### Inferences
- **What the MRT identifies:**
  - Prompts in the preferred versus another channel, at a randomised intensity, identify the causal excursion effects of match and intensity on same-evening perceived care (H8).
  - With a non-perceptual outcome (for example practical stress relief logged by the receiver), the MRT also identifies the *total* effect of prompted care on it.
  - It does **not** identify $\beta_{\text{sub}}$ versus $\beta_{\text{sym}}$, because $Q$ is not randomised. The decomposition needs no unmeasured $Q$–$Y$ confounding on each day, for example by the receiver's mood, stress or trust that day, plus a sensitivity analysis (Imai et al.). This matches `paper/08` §8.8 and §8.13.
- **Handling rival (d):**
  - Person-mean centring, or using within-person estimands, removes stable trait trust and attachment.
  - Time-varying trust must be measured *before* the day's $E$ and $Q$, for example lagged, to serve as a confounder or a moderator without conditioning on a post-treatment variable. Boruvka et al. formalise moderators that may themselves respond to past treatment.
- **Dyadic interference:** in a parent-randomised MRT, effects on the child are effects across dyad members. Shi, Wu & Dempsey (2023) give the relevant estimand framework when the dyad is the cluster.
- **Invariance sequence:**
  - Order: dyadic (partner A versus B; parent versus child), then longitudinal (within DSEM, McNeish et al.), then cross-national (multigroup or alignment), before any Korea–comparison-country contrast of means or route weights.
  - For two countries, ordinary multigroup CFA with partial invariance is the standard; alignment was built for many groups.
- **H6 feasibility:** four-member families meet Kenny's at-least-four requirement, and daily repetition provides the "across time" multiple indicators needed to separate relationship-specific variance from error. Three-member families are supported by fSRM; what they can separate was not verified (see Gaps).

### Gaps
- No source was found specific to **sequential ignorability for daily within-dyad mediation with a randomised exposure and an observational mediator** in relationship research. The general results (Imai et al.) apply, but no worked dyadic example was located.
- The SRM identification limits for three-person families (what is confounded with error) were not verified. Kenny's page states only the round-robin minimum of four.
- Numeric invariance cut-offs (ΔCFI, ΔRMSEA, ΔSRMR) and the alignment rule of thumb for the proportion of non-invariant parameters were not verified in this session.
- The DOI recalled for Claxton, DeLuca & van Dulmen (2015) on dyadic CFA, 10.4473/TPM22.2.2, did **not** resolve on Crossref: **UNVERIFIED**. It was not cited.

## 5. Ethics and safety: dyadic research where coercion or violence may be present, and Korean regulation

### Takeaway
WHO's domestic-violence research recommendations make safety paramount and recommend these practices for household-based surveys:
- frame the study neutrally;
- interview only one woman per household about violence;
- **not ask other household members about violence**;
- be ready to end interviews if interrupted;
- train fieldworkers to refer;
- design to reduce distress.

A dyadic design that administers violence items to both partners runs directly against the household rule, so it needs explicit mitigation or a design change. Meta-analytic evidence shows that trauma and IPV questions cause only mild, non-extreme distress, but greater distress among people with a trauma history.

In Korea, the following apply:
- the Bioethics and Safety Act requires IRB review and written consent;
- PIPA treats health and sex-life data as sensitive, requiring separate consent, and requires legal-representative consent for children under 14;
- the child-abuse reporting duty attaches to listed professions, not to researchers as such.

### Cited Findings
- **WHO, *Putting Women First*** ([WHO 2001, WHO/FCH/GWH/01.1](https://www.who.int/publications/i/item/WHO-FCH-GWH-01.1); text from the [University of Aberdeen copy](https://www.abdn.ac.uk/education/documents/WHO_FCH_GWH_01.1.pdf)) [full text]:
  - **Box 1 recommendations a–h:**
    - safety "is paramount, and should guide all project decisions";
    - methodologically sound prevalence studies;
    - "Protecting confidentiality is essential to ensure both women's safety and data quality";
    - careful selection, specialised training and ongoing support of team members;
    - "The study design must include actions aimed at reducing any possible distress";
    - fieldworkers trained to refer, with short-term support created where few services exist;
    - an obligation to see findings properly used;
    - violence questions added to other surveys only when the requirements can be met.
  - **Household rules:**
    - The survey should not be introduced to the household or community "as a survey on violence" but as a study of women's health, life experiences or family relations. The woman herself must be fully informed, interviewed in private, forewarned before the violence section and free to stop.
    - "Only one woman per household should be interviewed about her experiences of domestic violence."
    - "Any interviews conducted with other household members (either male or female) should not include questions exploring their attitudes, experience or use of violence."
    - Interviewers should "terminate or change the subject … if an interview is interrupted by anyone", with a diversionary questionnaire ready.
  - **Question design:** ask about specific acts, avoiding loaded terms such as "abuse"; disclosure depends on interviewer sex, skill and training.
- **WHO 2016 update:** *Ethical and safety recommendations for intervention research on violence against women* "build[s] on lessons from" *Putting Women First* and covers design through post-project responsibilities ([WHO 2016, ISBN 978-92-4-151018-9](https://www.who.int/publications/i/item/9789241510189)) [secondary; full text not read].
- **Population research ethics** ([Ellsberg & Heise 2002](https://doi.org/10.1016/S0140-6736(02)08521-5)) [abstract]: key concerns are respondents living with the abuser, confidentiality breaches that "could provoke an attack", and affirming rather than distressing interviews. The risks are justified only if the research provides service information and immediate referral.
- **Safety procedures change the data** ([Ellsberg et al. 2001](https://doi.org/10.1111/j.1728-4465.2001.00001.x)) [abstract]:
  - Lifetime partner physical violence was 52% (León) and 69% (Managua) in violence-specific studies versus 28% in the DHS.
  - The main differences "concerned ethical and safety procedures and the interview setting".
- **Couple and family research ethics** ([Margolin et al. 2005](https://doi.org/10.1037/0893-3200.19.1.157)) [abstract]: multiple members, especially minors, require special handling of confidentiality, privacy and consent, "clear policies about data ownership and disclosure", respect for the family unit, and clarity on abuse reporting and certificates of confidentiality.
- **Distress from asking:**
  - Meta-analysis of 70 samples (N = 73,959): trauma research causes "some immediate psychological distress" that is "not extreme". It is greater with a trauma history or PTSD, especially in interviews, yet participants generally find participation positive and do not regret it ([Jaffe et al. 2015](https://doi.org/10.1016/j.cpr.2015.05.004)) [abstract, PubMed].
  - Students completing a dating-violence measure reported "numerous positive experiences" and only mildly increased negative reactions ([Shorey, Cornelius & Bell 2011](https://doi.org/10.1177/0886260510390956)) [abstract].
  - Not asking about abuse has its own costs ([Becker-Blease & Freyd 2006](https://doi.org/10.1037/0003-066X.61.3.218)) [abstract].
- **Distress and referral protocols:**
  - Two protocols: telephone screening for people at high risk of adverse reactions, and interviewer responses to distress ([Draucker, Martsolf & Poole 2009](https://doi.org/10.1016/j.apnu.2008.10.008)) [abstract, PubMed].
  - A Delphi consensus of 24 experts on digital monitoring studies with people at risk of suicide covers inclusion criteria, consent elements and when and how to intervene ([Nock et al. 2021](https://doi.org/10.1176/appi.prcp.20200029)) [abstract, truncated].
- **Korea, Bioethics and Safety Act** (English translation, Act No. 16372, 23 Apr 2019; [KLRI](https://elaw.klri.re.kr/eng_service/lawViewContent.do?hseq=52559)) [statute; this English version may predate later amendments]:
  - Art. 2: human-subject research includes research "through interactions including … communication, and interpersonal contact" or using personally identifiable information.
  - Art. 15: the research plan must be submitted to the institutional committee (IRB) before research. Exemption is possible only if risk is insignificant and the research meets Ministry of Health and Welfare (MOHW) standards.
  - Art. 16(1): written consent, electronic allowed, covering purpose, participation, risks and benefits, personal-information protection, compensation, withdrawal and so on.
  - Art. 16(2): written consent by a legal representative (otherwise spouse, lineal ascendant or descendant) for subjects "incapable of, or incompetent for, giving consent" as set by Ministerial Decree. It must not contradict the subject's intention.
  - Art. 16(3): consent may be waived only with IRB approval under stated conditions.
  - Art. 18: provision to third parties only with consent and IRB deliberation, anonymised unless the subject consents otherwise.
  - Art. 19: records must be kept, with subject access on request.
- **Korea, Personal Information Protection Act** (English translation, Act No. 20897, 1 Apr 2025; [KLRI](https://elaw.klri.re.kr/eng_service/lawViewContent.do?hseq=71740)) [statute]:
  - Art. 22-2: consent of the legal representative for children under 14.
  - Art. 23: sensitive information ("ideology, belief … health, sex life, and other personal information that is likely to markedly threaten the privacy") requires consent "apart from the consent to the processing of other personal information" and safety measures.
  - Art. 28-2: pseudonymised information may be processed without consent "for statistical purposes, scientific research purposes, and archiving purposes in the public interest". No uniquely identifying information goes to third parties.
  - Art. 28-3: combining pseudonymised data must go through designated institutions.
  - Art. 2(8): defines "scientific research".
  - Commentators note ambiguity over whether PIPA or the Bioethics Act governs human-subject research ([Shin & Kim newsletter](https://www.shinkim.com/eng/media/newsletter/1834); [preprint](https://preprints.org/manuscript/202403.0232/v1)) [secondary].
- **Korea, child-abuse reporting** (Act on Special Cases Concerning the Punishment of Child Abuse Crimes, Art. 10, text as revised 2026-09-16, [korea.legal mirror of law.go.kr](https://korea.legal/wiki/%ec%95%84%eb%8f%99%ed%95%99%eb%8c%80%eb%b2%94%ec%a3%84%ec%9d%98-%ec%b2%98%eb%b2%8c-%eb%93%b1%ec%97%90-%ea%b4%80%ed%95%9c-%ed%8a%b9%eb%a1%80%eb%b2%95-%ec%a0%9c10%ec%a1%b0/)) [statute via mirror]:
  - Art. 10(1): anyone may report.
  - Art. 10(2): a listed set of professions must report immediately when they learn of or suspect child-abuse crimes "in the course of their duties". The list includes medical personnel at medical institutions, mental health welfare centres and psychiatric institutions, domestic-violence, sexual-violence and youth counselling facilities, social-welfare facilities, and school staff.
  - **Researchers are not a listed category**, and university staff are covered only if they work in a listed institution type, such as a hospital.
  - Art. 10(3): reporters' identities are protected.
  - A commentary notes the duty concerns abuse by guardians [secondary].
- **Korea, crisis line:** the Ministry of Health and Welfare unified suicide-prevention counselling numbers (including the former 1393) into **109** from January 2024, running 24/7 free of charge. Press headlines: ["내년부터 자살예방 상담번호 '109'로 통합"](https://futurechosun.com/?p=81377) and ["자살예방 상담번호 '109' 통합… 예방교육 본격화"](https://www.etoday.co.kr/news/view/2312343) [secondary; web-search summary and headlines; the official MOHW notice was not opened].

### Inferences
- **WHO-aligned options for the dyadic IPV conflict.** Interviewing both members of a couple, or a parent and child, about violence is what WHO 2001 advises against for household surveys. Options consistent with WHO's rationale:
  1. Collect safety data from each member privately on separate devices and accounts (already in `paper/18`), with neutral study framing ("relationships and daily life"), quick-exit or diversion screens, and no shared notifications.
  2. Use victimisation-only screens (CAS-R-SF, HARK) rather than perpetration-and-victimisation instruments (CTS2) where the partner might see or infer the content.
  3. Pre-specify that a positive safety screen routes the person to support. It also excludes the dyad from the micro-randomized care-prompt component, rather than continuing an intervention that prompts "care" in a coercive relationship. This follows `paper/18`'s rule that safety overrides research aims and the model's admissibility constraint.
- **Proportionality.** On the Ellsberg et al. finding, these procedures protect participants and also reduce underreporting, which matters for the exploratory "care compensates for danger" aim.
- **Consent wording.** Korean consent documents should state the limits of confidentiality. Study staff who are licensed clinicians or employees of listed institutions may be mandatory reporters even when acting as researchers. Following Margolin et al., the consent should also cover data ownership and non-disclosure between family members.
- **Sensitive data.** PHQ-9 responses (health) and sexual-coercion items (sex life) plausibly fall under PIPA Art. 23, so the protocol should obtain separate consent for them. This classification is an inference from the article text, not a ruling.

### Gaps
- No empirical study was found on the **risks of interviewing both partners** about violence in research, beyond WHO's household rule and Margolin et al.'s ethics review.
- The Korean domestic-violence reporting duty (Act on Special Cases Concerning the Punishment of Domestic Violence Crimes, Art. 4) was **not verified**; the mirror page returned 404.
- The current Korean-language text of the Bioethics and Safety Act, any post-2019 amendments, and the Ministerial Decree rules on minors' consent and IRB exemption were not checked.
- These figures are PRIOR KNOWLEDGE / UNVERIFIED in this session: Korea's age of majority (19, Civil Act) and the child-age definition (under 18, Child Welfare Act). They matter for the 15–18-year-olds in four-member families.
- The Women's Emergency Hotline **1366** was not verified. Whether it was folded into 109 was unclear in the sources.
- Reporting laws and IRB rules for the comparison country are not covered.
- WHO 2016 full text was not read.

## 6. Preregistration and falsification: registered reports, equivalence tests and model comparison for competing explanations

### Takeaway
The study suits a Stage 1 Registered Report:
- equivalence tests (TOST) with pre-specified SESOIs, to let the mismatch (H2) and match (H8) hypotheses fail;
- non-nested model comparison (Vuong-type tests for SEMs; LOO or WAIC for Bayesian models) and informative-hypothesis Bayes factors, to pit the translation model against rivals (a)–(d);
- pre-registered sensitivity analyses for unmeasured confounding;
- an ESM-specific preregistration template.

### Cited Findings
- **Why preregister:** preregistration separates prediction from postdiction ([Nosek et al. 2018](https://doi.org/10.1073/pnas.1708274114)) [abstract].
- **Registered Reports:** in-principle acceptance before results; their history, practical guidance and limits are reviewed in [Chambers & Tzavella 2022 (online 2021)](https://doi.org/10.1038/s41562-021-01193-7) [abstract]. 96% of standard reports versus 44% of Registered Reports in psychology reported positive results for the first hypothesis ([Scheel, Schijen & Lakens 2021](https://doi.org/10.1177/25152459211007467)) [abstract].
- **ESM preregistration template:** ESM has extra forking paths, and preregistration must handle model selection and power ([Kirtley et al. 2021](https://doi.org/10.1177/2515245920924686)) [abstract].
- **Secondary-data preregistration template**, for analyses of existing data such as pilot panels ([Van den Akker et al. 2021](https://doi.org/10.15626/MP.2020.2625)) [abstract].
- **Transparency recommendations for relationship designs** ([Campbell, Loving & LeBel 2014](https://doi.org/10.1111/pere.12053)) [abstract].
- **Derivation chain:** hypothesis tests need a sound "derivation chain" from theory; premature testing is counterproductive ([Scheel et al. 2021](https://doi.org/10.1177/1745691620966795)) [abstract].
- **Equivalence testing:** TOST rejects the presence of effects as large as the SESOI and so can "falsify predictions about the presence … of meaningful effects" ([Lakens, Scheel & Isager 2018](https://doi.org/10.1177/2515245918770963); [Lakens 2017](https://doi.org/10.1177/1948550617697177)) [abstract].
- **Model comparison:**
  - Vuong's likelihood-ratio tests for **non-nested** SEMs, with interval estimates for differences in information criteria and R implementations ([Merkle, You & Preacher 2016](https://doi.org/10.1037/met0000038)) [abstract]; original [Vuong 1989](https://doi.org/10.2307/1912557) [metadata].
  - Leave-one-out cross-validation and WAIC ([Vehtari, Gelman & Gabry 2017](https://doi.org/10.1007/s11222-016-9696-4)) [metadata].
  - Bayes factors for informative (order-constrained) hypotheses, which quantify support for the null and handle multiple hypotheses (R package *bain*) ([Hoijtink, Mulder, van Lissa & Gu 2019](https://doi.org/10.1037/met0000201)) [abstract].
- **Robustness:** multiverse analysis across reasonable processing choices ([Steegen et al. 2016](https://doi.org/10.1177/1745691616658637)) [abstract]; specification-curve analysis ([Simonsohn, Simmons & Nelson 2020](https://doi.org/10.1038/s41562-020-0912-z)) [metadata].
- **Sensitivity to unmeasured confounding:**
  - The E-value, the minimum confounder strength on the risk-ratio scale needed to explain away an association ([VanderWeele & Ding 2017](https://doi.org/10.7326/M16-2607)) [abstract].
  - The robustness value and partial R², computable from standard regression output ([Cinelli & Hazlett 2020](https://doi.org/10.1111/rssb.12348)) [abstract].
- **Prediction benchmark:** explanation and prediction are distinct ([Shmueli 2010](https://doi.org/10.1214/10-STS330); [Yarkoni & Westfall 2017](https://doi.org/10.1177/1745691617693393)) [metadata]. The protocol's out-of-sample benchmark against perceived commitment and appreciation follows [Joel et al. 2020](https://doi.org/10.1073/pnas.1917036117) [metadata; content as summarised in `paper/08` §8.15].
- **Reactivity of participation:** one session of awareness intervention reduced break-up as much as skills programmes ([Rogge et al. 2013](https://doi.org/10.1037/a0034209)) [metadata; content per `paper/18`]. This motivates the assessment-only arm.

### Inferences
- **A pre-registered comparison set per outcome.** All models are fitted to the same data and measurement models:
  - **(a) amount model:** total received support, or total enacted $E$;
  - **(b) perception model:** $Q$ only;
  - **(c) need-fulfilment model:** BPNSFS or relationship-specific need fulfilment;
  - **(d) trait model:** baseline trust plus ECR-RS, with the translation terms omitted;
  - **(M) translation model:** detection, construal, the fit surface and both routes, as frozen.
  - Comparison: nested models by likelihood-ratio tests or $\Delta$ information criteria; non-nested pairs, such as (b) versus (c), by Merkle et al.'s Vuong tests; Bayesian variants by LOO.
  - Directional claims (for example a direct route from giver-logged $E$ beyond $Q$, H3) can be stated as informative hypotheses (Hoijtink et al.).
- **Falsification criteria as TOST bounds.** `paper/18` already states its criteria; these translate directly into equivalence tests with pre-registered bounds:
  - H2: all mismatch terms inside the SESOI while the level term is clear;
  - H8: the match effect inside the SESOI while the intensity effect is clear;
  - H6: relationship-specific SRM variance negligible.
- **Pre-registered sensitivity analyses:** for the observational $\beta_{\text{sub}}$/$\beta_{\text{sym}}$ split, the protocol should pre-register the Imai et al. mediator sensitivity analysis and a robustness value (Cinelli & Hazlett). For rival (d), it should state in advance how strong a time-varying trust confounder would have to be to erase the symbolic route.
- **Derivation chain first:** each hypothesis should be traced from the frozen equation to the measured variables before testing (Scheel et al. 2021). The constructs flagged "not reliably operationalizable" in `paper/17`, namely intention, compatibility and channel preferences, should be preregistered as exploratory, not confirmatory.

### Gaps
- No relationship-science Registered Report combining dyadic ESM, an MRT and a family SRM was found to use as a template.
- Journal policies on Registered Reports in *JSPR*, *Personal Relationships* or Korean psychology journals were not checked.
- Vehtari et al., Vuong, Simonsohn et al., Shmueli, Yarkoni & Westfall, Joel et al. and Rogge et al. were verified at metadata level only in this session.
