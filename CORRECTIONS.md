# Corrections

Changes that correct or narrow what an earlier version claimed. Each entry quotes the earlier wording, states the correction, lists the affected files and records how deeply the supporting sources were checked: **full text** (read in full), **abstract** (abstract or index record only), **prior knowledge** (formula or claim recalled, metadata verified) or **not accessed**.

The research notes in [`evidence/notes/`](evidence/notes/) are the record of the literature review and are preserved unchanged. Where they contain a statement superseded here, the entry says where.

## v0.3.0 (2026-11-05)

Prompted by a primary-source audit of the paper's 20 most consequential empirical claims and four supplementary claims ([`audit/`](audit/README.md)). The equations did not change. Entries are grouped by audited claim (C01–C20, S1–S4); these two-digit IDs are the audit's claim numbers, separate from the v0.2.0 series C1–C4 below. Each gives the earlier wording, the correction, the files changed, and the primary source with the depth to which it was checked: **full text**, **abstract**, or **secondary** (press or practitioner summaries). The audit notes behind each entry are [`evidence/notes/08`–`11`](evidence/notes/), and their `file:line` references point at the [v0.2.0 tag](https://github.com/julienaxyomlabs/love-in-translation/tree/v0.2.0).

The first-round notes ([`evidence/notes/01`–`07`](evidence/notes/)) contain earlier versions of several statements corrected here, for example the readings of invisible support and over-provision. They are preserved as written; the audit notes record the corrected readings.

### Verdicts and headline

- **Earlier wording.**
  - Verdict on intended ≠ expressed: "Supported", anchored on "Stress blocks enactment of noticed needs".
  - Verdict on expressed ≠ perceived: "Supported and quantified".
  - Verdict on perceived ≠ received: "Supported in both directions", anchored on "Invisible support helps unseen" and on "false-alarm" sacrifices earning gratitude.
  - Verdict on "translation, not amount": "Not supported as a general claim", because "amount predicts outcomes strongly". The summary said the claim "does not survive the best-powered data".
- **Correction.**
  - Intended ≠ expressed: *plausible*; intention has not been measured.
  - Expressed ≠ perceived: *supported as disagreement between giver and receiver reports*. Loss measured against an objective record has not been shown.
  - Perceived ≠ received: *supported in one direction, in a laboratory analogue; mixed in the other*.
  - "Translation, not amount": *open in both directions*. The evidence offered against it does not compare amount with translation.
  - The closing paragraph no longer says that love is "at least as often" weakened at its source as lost in translation. Which happens more often is unknown.
- **Files.** `README.md` (hypothesis block, verdict table), `paper/00-summary.md`, `paper/01-question-and-thesis.md`, `paper/05-evidence-against-it.md`, `paper/19b-is-love-enough.md`, `paper/README.md`.
- **Sources.** The claim entries below.

### C01. Coriell & Cohen: κ = .39 pools helpful and harmful acts in student–friend pairs

- **Earlier wording.** "Partners agree only moderately on whether a supportive act even happened (κ ≈ .39)". Also, behaviours "had occurred after an exam".
- **Correction.**
  - κ = .39 is across 67 helpful and harmful behaviours; for helpful behaviours alone it is .28.
  - The pairs were students and the friends or roommates who supported them.
  - Behaviours occurred while the student prepared for the exam and were reported afterwards.
  - The authors' caveat is added: without an objective record, a disagreement cannot be traced to a missed perception rather than an over-report.
- **Files.** `README.md`, `paper/00`, `01`, `03`, `04`.
- **Source.** Coriell & Cohen (1995), **full text**: the scanned published version in Carnegie Mellon's repository.
- **Grade.** Moderate/mixed, unchanged.

### C02. Visserman et al.: sample size, "false alarms" and the sacrificer's satisfaction

- **Earlier wording.**
  - "N = 426".
  - "About half the sacrifices people 'saw' had not been reported by the partner".
  - "Perceived sacrifices, accurate or not, produced gratitude", "whether or not they had occurred".
  - "False-alarm" sacrifices used as evidence of perception without benefit.
  - "Unrecognized givers lose satisfaction".
  - The limitation "two studies, one laboratory".
  - "Invisible care ... produces no gratitude" and "earns no thanks".
- **Correction.**
  - The sample was 412 individuals: 126 Dutch and 80 US couples.
  - 40–46% of perceived sacrifices were not reported by the partner (about half in the Dutch study, 39.8% in the US one).
  - Gratitude is described with associational verbs, "whether or not the partner reported sacrificing". A false alarm means only that the partner did not report a sacrifice, and benefit was never measured, so false alarms are no longer used as evidence of perception without benefit.
  - The sacrificer's lower satisfaction on undetected days is significant in one of the two samples, so it is now graded Preliminary.
  - The samples came from different countries and projects.
  - "Invisible care" is restricted to missed sacrifices and same-day gratitude. Detection showed no evident effect on gratitude at follow-ups.
- **Files.** `README.md`, `paper/00`, `01`, `02`, `03`, `04`, `05`, `07`, `08` (model summary, §8.9), `10`, `11`, `14`, `19` (the limitation now reads "two short diary studies"), `19b` (an unseen giver "may be" harmed).
- **Source.** Visserman et al. (2019), **full text**: the CC BY-NC published version in Sussex Research Online.
- **Grade.** Moderate/mixed for detection and gratitude. Preliminary for the sacrificer's satisfaction (was Moderate/mixed).

### C03. Haber et al.: r = .35 distinguishes two recipient-side constructs

- **Earlier wording.** "The clearest quantitative evidence that care given and care received come apart". The table limitation read "mostly cross-sectional".
- **Correction.**
  - Both measures come from the recipient, so r = .35 shows that receiving support and feeling supported are distinct, not that givers and receivers disagree.
  - "Mostly cross-sectional" was dropped as unverified.
- **Files.** `paper/00`, `03`.
- **Source.** Haber et al. (2007), **abstract** only.
- **Grade.** Established for that pairing of measures, unchanged.

### C04. The original invisible-support result did not replicate: the route loses its main evidence but is not refuted

- **Earlier wording.**
  - Chapter 3: invisible support was "the cleanest dissociation between benefit and perception".
  - Elsewhere in the paper: "Unnoticed ('invisible') support aids adjustment", "Unnoticed support improves adjustment", "can benefit from care they never notice", "Silent care can help without ever being noticed".
  - §8.8 and the model summary: "Invisible support and income effects show that a non-perceptual route exists [Moderate to Established]" and "Unnoticed support helps".
  - Chapter 6's social-support row was graded "Moderate to Established".
- **Correction.**
  - The same group's replication, with 312 examinees and 310 partners, more than three times the original sample, did not reproduce the pattern. Provider-reported emotional support was often associated with *more* distress, and the authors backed off the simple take-home message.
  - This is a failed replication of one specific result. It removes the paper's main evidence for the route but does not refute the general mechanism; the independent tests cited in chapter 3 (Maisel & Gable 2009; Girme, Overall & Simpson 2013; Girme et al. 2018) were not examined in the audit.
  - "Invisible" means not reported as support, which is not the same as unperceived.
  - Benefit without perception is now described as mixed, and that $`\beta_{\text{sub}}\neq0`$ in close relationships is [Our hypothesis].
  - The text now distinguishes "not through perceived regard" from "unperceived". The captions for the substantive route in Figure 1 ("needs met whether or not anyone notices") and in the model-at-a-glance figure ("counts even when unnoticed") now follow the §8.8 definition.
- **Files.** `README.md`, `paper/00`, `01`, `02`, `03`, `06`, `07` (including Figure 1's caption and the stage table), `08` (model summary, §8.8, §8.12), `09`, `11`, `19b`, `paper/figures/model.svg`, `paper/figures/model-at-a-glance.png`.
- **Sources.**
  - Bolger, Zuckerman & Kessler (2000), **abstract**, with the same group's later full texts as secondary accounts.
  - Shrout et al. (2010), **full text** (author manuscript); added to the bibliography.
- **Grade.**
  - Invisible support: Moderate/mixed, not replicated (was Moderate/mixed, and "Moderate to Established" in chapter 7 and §8.8).
  - A route that bypasses perceived regard: Our hypothesis (was Moderate to Established).

### C05. Bolger & Amarel: sample size and what the experiments show

- **Earlier wording.** "In three experiments (N = 257), invisible support reduced emotional reactivity, while visible support was ineffective or harmful because it communicated inefficacy". Visible support "could backfire", without stating the population.
- **Correction.**
  - Analysed n = 31, 86 and 150.
  - Indirect support beat direct support, but in neither test did it beat no support.
  - Direct support raised distress only when it conveyed that the recipient needed help, partly through a reflected appraisal of inefficacy.
  - The text now names the setting: female students and a confederate, in a laboratory.
- **Files.** `README.md`, `paper/01`, `03`, `04`, `06`, `07`, `08` (§8.8), `11`.
- **Source.** Bolger & Amarel (2007), **full text**: the author-posted PDF of the published article.
- **Grade.** Moderate/mixed, as a laboratory analogue.

### C06. Brock & Lawrence: concurrent covariation, not a "greater risk", and not commensurate

- **Earlier wording.**
  - Under- and over-provision "predicted declining satisfaction, and over-provision was the greater risk".
  - Over-provision was "the greater risk over five years but had minimal effect day to day".
  - "Need–supply measurement on one metric exists for partner support", classed as "Direct (commensurate)".
  - "Opposite results at different timescales".
  - "Both under- and over-provision of support matter [Moderate/mixed]".
  - Graded "Mixed" in the evidence table.
- **Correction.**
  - Both co-varied with lower satisfaction within spouses.
  - Over-provision had the larger slope per behaviour flagged. Under-provision had the larger effect size and was far more common, so which matters more cannot be shown.
  - A perceived direction of discrepancy is not commensurate need and supply and cannot support response surface analysis.
  - The contrasting studies differ in measurement and design as well as timescale.
- **Files.** `README.md`, `paper/03`, `04`, `07`, `08` (model summary, §8.7, §8.12), `17`.
- **Source.** Brock & Lawrence (2009), **full text**: the NIH accepted manuscript.
- **Grade.** Moderate that both are associated with lower satisfaction. Preliminary that over-provision is worse (was Moderate/mixed, and "Mixed").

### C07. Lemay, Clark & Feeney: projection holds for global perceptions

- **Earlier wording.** Projection was stated without its limits. "Feeling loved depends at least as much on the receiver's own love, mood, attachment and history as on the giver's acts", and "Much of what a person perceives is produced by the perceiver's own love, mood and attachment".
- **Correction.**
  - The finding concerns global perceptions measured against the partner's self-report.
  - Daily counts of benefits received tracked the partner's reported giving as much as one's own (.36 against .34).
  - Mood, attachment and history were removed, because they were not measured as predictors.
- **Files.** `paper/00`, `03`, `05`, `09` (a reading "depends partly" on the reader; mood removed), `19b`.
- **Source.** Lemay, Clark & Feeney (2007), **full text**: the published PDF on the authors' laboratory site.
- **Grade.** Moderate, unchanged. A tag was added in chapter 5.

### C08. Collins & Feeney: Moderate, and not only ambiguous messages

- **Earlier wording.**
  - "[Established for this bounded effect]" and "Established (bounded)".
  - "Only *ambiguous*, low-support notes" and "only for *ambiguous* messages".
  - Effects "confined to ambiguous signals"; attachment "adds nothing beyond relationship perceptions".
  - Chapter 18: "deceptive standard-note paradigms ... can do relational harm (Collins & Feeney 2004)".
- **Correction.**
  - Graded Moderate.
  - Effects were on hurtful appraisals of low-support notes, and the avoidance interaction was marginal. With genuine notes, effects were strongest for low-support notes, weaker for moderately supportive ones and absent for very supportive ones.
  - "Adds little beyond relationship perceptions" is now credited to Joel et al.
  - The risk of relational harm is now stated as the paper's own inference.
- **Files.** `paper/01`, `03`, `06`, `08` (§8.6), `18`.
- **Source.** Collins & Feeney (2004), **full text**.
- **Grade.** Moderate (was Established, bounded).

### C09. Fletcher & Kerr: for judgments of love the bias is negative

- **Earlier wording.** "Partners are accurate and positively biased at once [Established]" (README and model summary). "A small positive mean bias overall in couples" (chapter 5). Tracking described as "knowing *when* and *on what*".
- **Correction.**
  - Tracking is r ≈ .40 for judgments of the partner's love.
  - Signed bias is positive overall (r = .09) but −.11 for perceived love (k = 7).
  - Tracking is covariation with a benchmark across couples or items.
  - Chapter 5 now uses the love-specific estimates and notes that a dyad's disagreement and a population mean are not on the same scale.
  - The level bias δ in equation (3) is a free parameter, so only its described sign changed.
- **Files.** `README.md`, `paper/03`, `05`, `08` (model summary).
- **Source.** Fletcher & Kerr (2010), **full text**: a cached copy of the published article.
- **Grade.** Established for tracking accuracy and the small overall bias. Moderate/Preliminary for the love-specific sign.

### C10. Joel et al.: details of the predictive benchmark

- **Earlier wording.**
  - Perceived responsiveness was the "Top predictor across 43 datasets".
  - "99.4% of predictors were self-report".
  - Joel et al. were cited for reverse causation.
  - "Essentially none of its later change".
  - The heading read "The future of a relationship is barely predictable".
- **Correction.**
  - Perceived responsiveness had a 69% success rate, tied with conflict and behind perceived partner commitment (85%).
  - The 99.4% applies to the 1,149 relationship-specific variables.
  - The reverse-causation citation was removed.
  - Change was predicted at most 5% (mean about 2.2–2.5%), measured over typically one to two years; follow-up levels up to 18%.
  - The heading now names change, and the samples are described as Western.
- **Files.** `paper/03`, `05`, `06`, `08` (§8.15).
- **Source.** Joel et al. (2020), **full text**.
- **Grade.** Established for prediction, unchanged.

### C11. Le et al.: one's own love predicts non-marital persistence, which does not test translation

- **Earlier wording.** "Love, commitment and perceived partner commitment are among the strongest predictors of whether relationships last". "Amount predicts outcomes strongly". "'The problem is often not the amount of love' is wrong as a general statement".
- **Correction.**
  - Love was each person's own self-report, and the outcome was non-marital break-up, so the study does not test translation.
  - Perceived partner commitment is credited to Joel et al., as a predictor of quality.
  - Applying the result to parents is labelled an extrapolation, and the closing answer now speaks of romantic, not all close, relationships.
- **Files.** `README.md`, `paper/00`, `01`, `03`, `05`, `07`, `19b`, `paper/README.md`.
- **Source.** Le et al. (2010), **abstract**, with effect sizes from citing papers (**secondary**).
- **Grade.** Established for non-marital persistence. Moderate at best as evidence against translation.

### C12. Lavner, Karney & Bradbury: the heading overreached

- **Earlier wording.** "Communication matters less, and less causally, than its reputation", tagged Established to Moderate.
- **Correction.** The heading now reads "Communication predicts later satisfaction weakly and inconsistently", and the study is tagged Moderate. Weak lagged prediction is not evidence that causal effects are absent.
- **Files.** `paper/03`.
- **Source.** Lavner, Karney & Bradbury (2016), **full text**: the NIH author manuscript.
- **Grade.** Moderate (was Established to Moderate).

### C13. Flicker et al.: the null concerns the primary language, not matching

- **Earlier wording.**
  - Channel "matching ... adds little" and "matching null".
  - "Fewer than half have a primary channel".
  - Inconsistent tags: Preliminary in chapter 6, Moderate/mixed (null) in chapter 3.
  - Chapter 18's micro-randomised trial prompted care in "the child's stated preferred channel".
- **Correction.**
  - Fewer than half had an *identifiable* primary language, and the primary channel carried no extra predictive weight. That is not a test of giver–receiver matching.
  - Both tags are now Moderate (null).
  - The trial now defines a match from the child's need report the previous evening, and consent discloses that prompts use the child's reports.
- **Files.** `README.md`, `paper/00`, `01`, `03`, `06`, `18`.
- **Source.** Flicker, Sancier-Barbosa & Impett (2025), **abstract**.
- **Grade.** Moderate, as a null for the primary-language claim.

### C14. Neff et al.: stress dampens enactment, it does not block it

- **Earlier wording.**
  - "Stress blocks enactment of noticed needs".
  - "Stress limits acting on needs that were noticed [Moderate/mixed]".
  - "The constraint form is appropriate because the evidence describes *bounds* ... Stressed husbands failed to act on needs they had noticed".
  - "Intention high, enactment low".
  - Stress makes a partner deliver "less care than they feel".
- **Correction.**
  - On high-stress days, husbands' slope from perceived need to their own reported support fell from .81 to .72: a graded weakening, not a block.
  - The constraint form is a modelling assumption.
  - Intention, feelings and the recipient's experience were not measured.
- **Files.** `README.md`, `paper/01`, `04`, `07`, `08` (model summary, §8.4, §8.12), `11`, `19b`.
- **Source.** Neff, Nguyen & Williamson (2021), **full text**: the authors' accepted manuscript.
- **Grade.** Preliminary (was Moderate/mixed).

### C15. Hou et al.: the age trend belongs to Korelitz & Garber

- **Earlier wording.** "Across 313 studies ... reaching g ≈ −.50 by age 14 and over for both mothers and fathers (Hou et al. 2020; Korelitz & Garber 2016)". "Discordance about parenting is *higher* in more individualistic societies".
- **Correction.**
  - g = .24 comes from 221 of the 313 studies, and agreement was r = .28.
  - Neither gap differed between mothers and fathers.
  - The age result is credited to Korelitz & Garber.
  - Individualism goes with lower agreement, not with a larger mean gap.
- **Files.** `paper/04`, `05` (the "90 versus 40" comparison now notes that g and r summarise populations, not one dyad's disagreement), `12`.
- **Sources.** Hou et al. (2020), **full text** (NIH author manuscript). Korelitz & Garber (2016), **full text**.
- **Grade.** Established for the pooled estimates, unchanged.

### C16. Chentsova Dutton, Choi & Choi: "not uniquely associated", not "unrelated"

- **Earlier wording.**
  - Perceived financial support "was unrelated to distress (β = −.01)".
  - "No individual culture × support interaction was significant".
  - The finding "cuts against" cultural relativity.
  - Korean adolescents report "*more* financial ... support".
  - Emotional support "predicts lower distress in four countries alike", under [Established to Moderate].
- **Correction.**
  - Financial support was not uniquely associated with distress once other support was controlled (p = .39). It correlated with lower distress in every country (r = −.07 to −.22) and was uniquely associated with positive self-beliefs (β = .10).
  - The interaction block was significant (p = .012).
  - The finding now "gives no support to" a strong cultural-relativity version.
  - Korea–US differences: emotional support d ≈ 0.3; financial support d ≈ 0.1, with the source's table and text disagreeing on significance.
  - The study has its own Preliminary tag in chapter 13.
- **Files.** `paper/05`, `07`, `10`, `13`.
- **Source.** Chentsova Dutton, Choi & Choi (2020), **full text**.
- **Grade.** Preliminary, unchanged.

### C17. Costello et al. and Akee et al.: the income studies measured no perception

- **Earlier wording.** Income effects showed that substantive benefits "arrive whether or not they are perceived as love" [Moderate to Established]. Costello et al. were untagged in chapter 7 and cited for educational and health outcomes in chapter 3.
- **Correction.**
  - Income improved some outcomes, mainly in previously poor households.
  - No study measured whether children read the income as care, and Akee et al. attribute part of the effect to better parenting.
  - Costello et al. are tagged [Moderate; one rural US natural experiment; abstract-level check] and cited for behavioural outcomes only.
- **Files.** `paper/03`, `07`, `08` (§8.8, §8.12).
- **Sources.** Costello et al. (2003), **abstract**. Akee et al. (2010), **full text** (NIH author manuscript).
- **Grade.** Moderate for the income effects. Our hypothesis for attributing them to a route.

### C18. Khaleque & Rohner: an association, not a test of a route

- **Earlier wording.** Perceived warmth "predicts adjustment everywhere"; perceived acceptance "predicts adjustment across cultures".
- **Correction.** Perceived acceptance correlates with adjustment in every study of the meta-analyses (43 and 66 studies; 22 countries), usually same-respondent and cross-sectional. This is consistent with a symbolic route but does not test one.
- **Files.** `paper/06`, `07`.
- **Source.** Khaleque & Rohner (2002; 2012), **abstracts**.
- **Grade.** Established association. No route grade.

### C19. Arriaga, Capezza & Daly: tolerance standards, not love ratings

- **Earlier wording.**
  - "Felt love and commitment can rise as safety falls".
  - "Love and commitment measures can move in the *wrong* direction as safety falls".
  - "Danger signals that run in the opposite direction from love ratings".
  - "Harm not offset by love".
  - "The feeling of love is partly produced by commitment and dependence".
  - "Perceived love may be high".
  - The receiver's perception is "*over*-generous".
  - "Perceived love is not a valid safety indicator".
  - "Commitment shifts" and "raised" tolerance.
- **Correction.**
  - Once a partner's aggression begins, highly committed people adopt more tolerant standards for it (longitudinal n = 52; experiment n = 73). Commitment was measured, not manipulated.
  - The receiver's own judgments therefore cannot define safety. The study measured no love rating.
  - The safety constraint now rests openly on normative and design grounds plus this narrower finding.
  - Claims about love ratings are marked as needing another source.
- **Files.** `README.md`, `paper/01`, `02`, `03`, `07`, `08` (model summary, §8.10, §8.12), `15`, `19b`.
- **Source.** Arriaga, Capezza & Daly (2016), **abstract**.
- **Grade.** Moderate/mixed for the tolerance-standards finding. Not supported for love rising as safety falls.

### C20. Flynn & Adams: press accounts only

- **Earlier wording.** Stated as a finding. A "Moderate/mixed base" for the father–daughter prediction. "Strangers and one-off acts".
- **Correction.**
  - The study is marked as verified only through press accounts [Preliminary], and the base is now Preliminary.
  - The untested leap from one-off adult gifts to a parent's ongoing provision is flagged.
  - "Strangers" now applies only to Kumar & Epley.
- **Files.** `paper/03`, `04`, `10`.
- **Source.** Flynn & Adams (2009), **secondary** (press accounts).
- **Grade.** Preliminary (was Moderate/mixed).

### S1–S4. Supplementary claims

- **S1.** Gottman et al. (1976), **secondary**: a blog at the lead author's institute. "Classic" was dropped, and the text now states that the summary's source gives no sample size or statistics (`paper/04`).
- **S2.** Lakey et al. (1996), **abstract**. Tagged [Moderate; abstract-level check] (`paper/03`).
- **S3.** Rohner & Pettengill (1985), **abstract**. The study has its own [Preliminary; N unverified] tag, and the North American contrast is with other studies (`paper/13`).
- **S4.** Levine et al. (1995) is not used in the paper. No change.

### Instruments, design and bibliography

- **Korean validation status (`paper/17`).**
  - Earlier: BPNSFS "Not located"; ECR-RS "**Yes**"; CSI "No".
  - Correction:
    - BPNSFS: partly validated, in 367 cancer survivors only (Yeom & Lee 2024, **full text**).
    - ECR-RS: none found. Korean versions exist for the ECR-R and its short form, which are not relationship-specific (**abstracts**).
    - CSI: yes, the K-CSI, validated in 218 couples (Kim et al. 2022, **abstract**).
  - Source: [`evidence/notes/12-protocol-methods.md`](evidence/notes/12-protocol-methods.md).
- **Power for quadratic terms (`paper/08` §8.7, `paper/18`).**
  - Earlier: Sommet et al. (2023) was cited for "quadratic and interaction terms".
  - Correction: it is cited for interactions only; quadratic terms need their own simulation.
  - Source: Sommet et al. (2023), **abstract**.
- **Bibliography.** Added Shrout et al. (2010), Kim et al. (2022) and Yeom & Lee (2024). All three DOIs were resolved against Crossref.

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
