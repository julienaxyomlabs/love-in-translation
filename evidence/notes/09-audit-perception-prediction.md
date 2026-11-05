# Primary-source audit of C06–C10: support fit, perception biases and predictors of relationship quality

Scope: five empirical claims used by the paper *Can Love Be Lost in Translation?* (this repository, read but not modified). I read each primary source in full text through a legitimate open copy, then compared what it measured and found with how the paper uses it. Line references are `file:line` in that repository. Every effect size below comes from the primary source unless it is marked as my own conversion. This is not a review of the wider literature: I did not search for replications or later meta-analyses except where noted.

Abbreviations: B&L = Brock & Lawrence 2009; LCF = Lemay, Clark & Feeney 2007; C&F = Collins & Feeney 2004; F&K = Fletcher & Kerr 2010; Joel = Joel et al. 2020; PPR = perceived partner responsiveness.

Full-text copies used:
- B&L: NIH author manuscript, [PMC2776033](https://pmc.ncbi.nlm.nih.gov/articles/PMC2776033/), retrieved as XML through NCBI E-utilities.
- LCF: published PDF on the [Yale Clark Relationship Lab site](https://clarkrelationshiplab.yale.edu/sites/default/files/files/Projection%20of%20responsiveness%20to%20needs%20and%20construction%20of%20satisfying%20communcal%20relationships(1).pdf).
- C&F: published PDF on the [UCSB Close Relationships Lab site](https://labs.psych.ucsb.edu/collins/nancy/UCSB_Close_Relationships_Lab/Publications_files/Collins%20and%20Feeney,%202004.pdf).
- F&K: published PDF from a [CiteSeerX cached copy](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.471.1954&rep=rep1&type=pdf).
- Joel: published PNAS PDF from [UC Davis eScholarship](https://escholarship.org/content/qt8mc5n2c3/qt8mc5n2c3.pdf), also at [PMC7431040](https://pmc.ncbi.nlm.nih.gov/articles/PMC7431040/).

Extracted texts are kept in `working-files/audit_R2/`.

## 1. Where and how does the paper state or use each claim?

### Takeaway
All five sources carry real weight in the paper. Each is cited in the literature review and again in the model or method chapters, and three of them (LCF, F&K, B&L) also appear in the README's model table. Several downstream uses go beyond the source:
- B&L is cited as a commensurate need–supply measure.
- F&K's overall positive bias is applied to perceived care, the one domain where its signed bias was negative.
- PPR is called the "top predictor" in Joel.
- C&F is credited with a relational-harm claim it does not make.
- LCF is stretched into "love, mood, attachment and history".

None of the five appears in `CORRECTIONS.md`, whose v0.2.0 entries C1–C4 do not re-grade any empirical finding ([CORRECTIONS.md](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/CORRECTIONS.md)).

### Cited Findings

**C06 Brock & Lawrence (2009)**
- Literature review: in 103 newlywed couples over five years, both under- and over-provision "predicted declining satisfaction", and over-provision "was the greater risk". The next bullet notes that a daily study found the reverse, tagged [Moderate/mixed] — [03-literature-review.md:39–40](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/03-literature-review.md).
- Evidence table: "Over-provision harms more than under-provision", graded **Mixed** and explained as "Opposite results at different timescales" — [03:142](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/03-literature-review.md).
- Used as the leading evidence that form and fit matter beyond amount: both under- and over-provision "predicted declining marital satisfaction" — [04-evidence-for-the-intuition.md:31](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/04-evidence-for-the-intuition.md).
- Evidence anchor for failure type 3, "Mis-targeted care … too much" — [07-revised-model.md:65](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/07-revised-model.md).
- Model table, component 5: "Both under- and over-provision of support matter", tagged [Moderate/mixed] — [08-mathematical-representation.md:36](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/08-mathematical-representation.md); same row in [README.md:125](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/README.md).
- Over-provision "was the greater risk over five years" but had minimal effect day to day, tagged [Moderate/mixed]; used to justify estimating an asymmetric loss — [08:215](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/08-mathematical-representation.md).
- Methods precedent: "need–supply measurement on one metric exists for partner support" — [08:219](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/08-mathematical-representation.md). Measure for RSA, "Support desire and receipt items" — [08:315](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/08-mathematical-representation.md). Construct table: "Need versus supply … over- and under-provision ratings", classed **Direct (commensurate)** — [17-what-testing-requires.md:15](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/17-what-testing-requires.md).
- Limitations: the finding rests on a single sample, and the timescale question is listed as open — [19-limitations.md:3, :12](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/19-limitations.md).

**C07 Lemay, Clark & Feeney (2007)**
- A spouse's own responsiveness predicted perception of the partner's responsiveness more strongly than the partner's self-report did, and a recall-difficulty experiment lowered PPR. Tagged [Moderate/mixed] — [03-literature-review.md:11](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/03-literature-review.md). Evidence table: "Perceived responsiveness is partly projected", Moderate/mixed — [03:139](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/03-literature-review.md).
- Headline bullet of "Much of what is perceived is generated by the perceiver" — [05-evidence-against-it.md:12](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/05-evidence-against-it.md).
- Thesis verdict: "Perception partly reflects the perceiver's own love", tagged Moderate (projection) — [01-question-and-thesis.md:17](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/01-question-and-thesis.md).
- Theory table — [06-competing-theories.md:7](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/06-competing-theories.md).
- Model component 3: projection force π, tagged [Moderate] — [08:34](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/08-mathematical-representation.md) and [README.md:123](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/README.md). Further model uses at [08:170](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/08-mathematical-representation.md) ("Moderate evidence for π > 0") and [08:313](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/08-mathematical-representation.md).
- Projection and sentiment — [12-asymmetry-and-misperception.md:12](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/12-asymmetry-and-misperception.md).
- Strongest use: feeling loved "depends at least as much on the receiver's own love, mood, attachment and history as on the giver's acts", untagged — [19b-is-love-enough.md:7](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/19b-is-love-enough.md).

**C08 Collins & Feeney (2004)**
- Key-experiment passage, tagged **[Established for this bounded effect]** — [03-literature-review.md:77–80](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/03-literature-review.md):
  - clearly supportive notes were appraised alike (β = .66);
  - only ambiguous, low-support notes were appraised more negatively by avoidant (β = .41, sr² = .06) and anxious (β = .40, sr² = .06) recipients;
  - insecure recipients re-rated an earlier interaction.
- Evidence table: "Moderate/mixed (strong design, small effects)", with the caveat "Students; ambiguous messages only" — [03:141](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/03-literature-review.md).
- Thesis table: "identical ambiguous messages appraised more negatively by insecure recipients" — [01:14](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/01-question-and-thesis.md). Definitions table, tagged Moderate/mixed — [02-definitions-and-distinctions.md:17](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/02-definitions-and-distinctions.md).
- Theory table: "Effects confined to ambiguous signals and small; adds nothing beyond relationship perceptions in prediction", tagged **Established (bounded)** — [06-competing-theories.md:9](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/06-competing-theories.md).
- Revised model — [07:31, :64](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/07-revised-model.md). Attachment effect on δ depends on ambiguity — [08:172](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/08-mathematical-representation.md). Re-rating of earlier care — [14-time-and-feedback.md:22](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/14-time-and-feedback.md). Design precedent — [17:38](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/17-what-testing-requires.md).
- Ethics rule: "deceptive standard-note paradigms with real partners can do relational harm", cited to C&F — [18-proposed-study.md:90](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/18-proposed-study.md).

**C09 Fletcher & Kerr (2010)**
- Core passage, tagged [Established] — [03-literature-review.md:58](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/03-literature-review.md):
  - tracking accuracy, glossed as knowing "*when* and *on what*" a partner is higher or lower, r = .47 across 98 studies;
  - mean-level bias r = .09 across 48 studies;
  - "The two were statistically independent";
  - for love and communication the signed bias was slightly negative, so people slightly underestimate their partner's love.
- Evidence table: "Partners track each other well but show small mean bias", Established, with the caveat "Criterion is partner self-report" — [03:144](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/03-literature-review.md).
- Thesis verdict that love expressed ≠ love perceived is "Supported and quantified", citing "tracking accuracy r ≈ .47" — [01:14](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/01-question-and-thesis.md).
- "a small positive mean bias overall in couples", used against the 90-versus-40 illustration — [05:46](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/05-evidence-against-it.md).
- Theory table — [06:12](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/06-competing-theories.md).
- Model component 3, perceived care: "partners are accurate and positively biased at once" [Established] — [08:34](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/08-mathematical-representation.md) and [README.md:123](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/README.md). Also [08:313](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/08-mathematical-representation.md).

**C10 Joel et al. (2020)**
- PPR is described as "among the top relationship-specific predictors", ranked behind four others; 43 datasets, 29 labs, 11,196 couples; tagged [Established, for prediction] — [03-literature-review.md:7](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/03-literature-review.md).
- Evidence table caveats: "99.4% of predictors were self-report; all samples from Western countries; change unpredictable" — [03:138](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/03-literature-review.md).
- Perceived partner commitment as the single best relationship-specific predictor — [05:7](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/05-evidence-against-it.md). Joel cited for needing giver-independent designs — [05:20](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/05-evidence-against-it.md).
- No combination of self-reports explained more than about 5% of change in satisfaction — [05:71](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/05-evidence-against-it.md).
- Perceived responsiveness row: "Top predictor across 43 datasets" — [06:7](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/06-competing-theories.md). Joel cited for "reverse causation from satisfaction to perception" — [06:24](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/06-competing-theories.md).
- Predictive benchmark: up to 45% of baseline quality but "essentially none of its later change" — [08:362, :369](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/08-mathematical-representation.md).
- Further uses — [14:23](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/14-time-and-feedback.md), [17:46](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/17-what-testing-requires.md), [18:71](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/18-proposed-study.md), [19:3](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/19-limitations.md).

### Inferences
- The paper uses these studies at two levels: as facts about relationships (chapters 3–6) and as justification for model structure (chapter 8, README). The model-level uses are where the drift happens. Examples: a commensurate-measurement claim for B&L, and F&K's positive bias attached to perceived care.
- Grades for the same study differ across chapters. C&F is "Established" in chapters 3 and 6 but "Moderate/mixed" in chapters 2, 3 (table) and 8. B&L is "Mixed" in the 03 table but has no tag at 04:31.

### Gaps
- I searched `paper/`, `README.md` and `CORRECTIONS.md` by author name and DOI. The `evidence/notes/` files were read only for context and were not audited line by line.

## 2. Can each primary source be read in full through a legitimate open route?

### Takeaway
Yes, all five. B&L is an NIH author manuscript in PMC. Joel is open on PNAS and PMC; I read a publisher PDF mirrored by UC Davis eScholarship. LCF and C&F are publisher PDFs posted on the authors' lab sites. F&K is a publisher PDF cached by CiteSeerX. Several catalogue "open access" pointers were misleading, as listed below.

### Cited Findings
- **B&L.** Semantic Scholar lists a green open-access copy at PMC2776033 ([API record](https://api.semanticscholar.org/graph/v1/paper/DOI:10.1037/a0015402?fields=title,openAccessPdf,externalIds,isOpenAccess)). NCBI E-utilities returned the full-text XML ([PMC2776033](https://pmc.ncbi.nlm.nih.gov/articles/PMC2776033/)). The manuscript says it is the final accepted manuscript, not the copy-edited published version ([PMC2776033](https://pmc.ncbi.nlm.nih.gov/articles/PMC2776033/)).
- **Joel.** The [eScholarship PDF](https://escholarship.org/content/qt8mc5n2c3/qt8mc5n2c3.pdf) is the PNAS typeset article, 117(32):19061–19071. Direct requests to PMC were served a reCAPTCHA page; I did not try to get around it. The Europe PMC full-text endpoint returned HTTP 500. The PNAS PDF returned 403.
- **LCF and C&F.** Semantic Scholar's "open access" links point to CMU KiltHub/figshare records. Those records hold no file, only a link to APA PsycNET ([figshare API 6617744](https://api.figshare.com/v2/articles/6617744); [figshare API 6619205](https://api.figshare.com/v2/articles/6619205)). The full texts came from the authors' lab sites instead ([Yale lab PDF](https://clarkrelationshiplab.yale.edu/sites/default/files/files/Projection%20of%20responsiveness%20to%20needs%20and%20construction%20of%20satisfying%20communcal%20relationships(1).pdf); [UCSB lab PDF](https://labs.psych.ucsb.edu/collins/nancy/UCSB_Close_Relationships_Lab/Publications_files/Collins%20and%20Feeney,%202004.pdf)).
- **F&K.** OpenAlex marks the article as closed but lists two CiteSeerX entries ([OpenAlex record](https://api.openalex.org/works/doi:10.1037/a0019792)). One of them served the full 32-page published article ([CiteSeerX copy](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.471.1954&rep=rep1&type=pdf)). Semantic Scholar's openAccessPdf for this DOI points to a file named `FletcherSSSP07.pdf` on a 2007 Sydney Symposium site. By its name and venue it is a different work; I did not open it ([API record](https://api.semanticscholar.org/graph/v1/paper/DOI:10.1037/a0019792?fields=title,openAccessPdf)).

### Inferences
- The B&L text is the accepted manuscript. Its table values could differ slightly from the typeset JFP version, which I did not see.
- Automated open-access pointers misfired for three of the five papers. Someone re-checking these papers should not rely on an `openAccessPdf` field alone.

### Gaps
- Joel's SI Appendix and OSF materials (https://osf.io/v5e34/, https://osf.io/4pbfh/) were not accessed. Exact change-model R² values and the numbers for the "none" and "stringent" predictor sets are in those files ([Joel PDF](https://escholarship.org/content/qt8mc5n2c3/qt8mc5n2c3.pdf)).

## 3. What did each study measure, in whom, and what did it find?

### Takeaway
All five are observational except C&F Study 1 (manipulated messages, measured attachment) and LCF Study 3 (a recall-difficulty manipulation). In every source, "perception" is benchmarked against a self-report: the partner's in LCF, F&K and Joel, and the recipient's own in B&L. The sources acknowledge most of the key caveats themselves. The paper often omits them.

### Cited Findings

#### C06 Brock & Lawrence (2009), JFP 23(2):181–192
- **Population.** Couples recruited through Iowa marriage-license records ([PMC2776033](https://pmc.ncbi.nlm.nih.gov/articles/PMC2776033/)):
  - 350 couples responded; eligible couples were married less than 6 months, in a first marriage, both spouses 18 or older;
  - the first 105 eligible couples were enrolled; one couple and one husband's data were excluded; the abstract gives N = 103 couples;
  - mean ages 25.8 (husbands) and 24.8 (wives); 15% ethnic minority; modal joint income $40,001–50,000; modal education 14 years;
  - couples had dated 44 months on average and 76% had cohabited.
  - The years of data collection are not stated in the text I read.
- **Design** ([PMC2776033](https://pmc.ncbi.nlm.nih.gov/articles/PMC2776033/)):
  - five mailed-questionnaire waves at 3–6, 12–15, 21–24, 30–33 and 54–57 months after the wedding;
  - by wave 5, 12 couples had separated or divorced and 3 had withdrawn, and their available data were kept;
  - growth-curve modelling with an APIM; level-1 variables were group-mean centred;
  - under- and over-provision were entered together as time-varying covariates, so the estimates are within-spouse covariation of changes across waves, not lagged prediction.
- **Measures** ([PMC2776033](https://pmc.ncbi.nlm.nih.gov/articles/PMC2776033/)):
  - modified 48-item SIRRS: each spouse rated how often the partner performed each support behaviour in the past month (never to almost always), then a preferred direction for that behaviour (more, less or the same);
  - **under-provision** = proportion of the 48 items the recipient wanted more of; **over-provision** = proportion wanted less of; both scored 0–1;
  - type subscales: informational, emotional, esteem, tangible; network support was dropped for low reliability;
  - satisfaction: 6-item QMI, α .91–.97.
- **Prevalence** ([PMC2776033](https://pmc.ncbi.nlm.nih.gov/articles/PMC2776033/)):
  - under-provision was reported by 61.4–71.3% of husbands and 81.4–91.9% of wives per wave; over-provision by 27.1–40.8% of husbands and 32.6–43.4% of wives;
  - spouses reported significantly more under- than over-provision; the two measures correlated .02–.33.
- **Aim 2, Table 1** ([PMC2776033](https://pmc.ncbi.nlm.nih.gov/articles/PMC2776033/)):
  - husbands: under-provision b = −7.52 (SE 1.92), t(101) = −3.92, effect size r = .36; over-provision b = −18.73 (SE 6.52), t = −2.88, r = .28; χ²(1) = 4.76;
  - wives: under-provision b = −8.02 (1.66), t = −4.84, r = .43; over-provision b = −27.14 (8.03), t = −3.38, r = .31; χ²(1) = 5.00;
  - the table note says the under-versus-over comparisons used **unstandardized** coefficients.
- **Aim 3, by support type** ([PMC2776033](https://pmc.ncbi.nlm.nih.gov/articles/PMC2776033/)):
  - husbands: over-provision exceeded under-provision only for informational support (χ² = 5.03);
  - wives: over exceeded under for informational (4.07), emotional (11.37) and tangible (4.14) support;
  - esteem: no difference for either spouse, and over-provision of esteem support was not significantly related to satisfaction in either spouse.
- **Limitations stated by the authors** ([PMC2776033](https://pmc.ncbi.nlm.nih.gov/articles/PMC2776033/)):
  - replication with a larger sample is recommended;
  - there was not enough power to enter all type-specific predictors together;
  - the sample was mostly Caucasian, educated, married and heterosexual;
  - the study was not experimental; the approach shows covariation, not temporal order, and they cannot say whether under- or over-provision precede or result from discord;
  - shared-method self-report;
  - couples were not new relationships, and the sample was generally satisfied.

#### C07 Lemay, Clark & Feeney (2007), JPSP 92(5):834–853
- **Study 1** ([Yale lab PDF](https://clarkrelationshiplab.yale.edu/sites/default/files/files/Projection%20of%20responsiveness%20to%20needs%20and%20construction%20of%20satisfying%20communcal%20relationships(1).pdf)):
  - 191 married couples from the Pittsburgh area, recruited by newspaper ads; ages 18–82; married 10 years on average; about 77% of women and 75% of men Caucasian;
  - cross-sectional questionnaires; analysed N = 151 couples (safe haven) and 170 couples (secure base);
  - measures: own and perceived-partner safe-haven responsiveness (reworded caregiving items, plus a second perceived-support scale) and secure-base responsiveness;
  - two-level HLM with standardized variables.
- **Study 1 results, Table 1** ([Yale lab PDF](https://clarkrelationshiplab.yale.edu/sites/default/files/files/Projection%20of%20responsiveness%20to%20needs%20and%20construction%20of%20satisfying%20communcal%20relationships(1).pdf)):
  - own responsiveness predicted PPR at β = .60 (safe haven) and .52 (secure base);
  - the partner's self-reported responsiveness predicted it at β = .22 and .17;
  - with self-esteem and attachment controlled: .49 vs .20, and .43 vs .17.
- **Study 1, further tests** ([Yale lab PDF](https://clarkrelationshiplab.yale.edu/sites/default/files/files/Projection%20of%20responsiveness%20to%20needs%20and%20construction%20of%20satisfying%20communcal%20relationships(1).pdf)):
  - own responsiveness still predicted PPR with satisfaction controlled (β = .23 and .30);
  - the projection effect was stronger at high commitment.
- **Study 2, design** ([Yale lab PDF](https://clarkrelationshiplab.yale.edu/sites/default/files/files/Projection%20of%20responsiveness%20to%20needs%20and%20construction%20of%20satisfying%20communcal%20relationships(1).pdf)):
  - 108 engaged, never-married, childless couples assessed a few weeks before the wedding; 96 couples again about 25 months after;
  - predominantly Caucasian; 80% finished college; ages 20–38;
  - "own responsiveness" was **communal strength**, a motivation measure.
- **Study 2, Table 3** ([Yale lab PDF](https://clarkrelationshiplab.yale.edu/sites/default/files/files/Projection%20of%20responsiveness%20to%20needs%20and%20construction%20of%20satisfying%20communcal%20relationships(1).pdf)):
  - own β = .51 vs partner .17 at T1; .47 vs .18 at T2;
  - .47/.17 and .40/.18 with depression, attachment and communal orientation controlled.
  - Longitudinally, T1 own responsiveness predicted residualized change in satisfaction through T1 PPR.
- **Study 2 daily diary** ([Yale lab PDF](https://clarkrelationshiplab.yale.edu/sites/default/files/files/Projection%20of%20responsiveness%20to%20needs%20and%20construction%20of%20satisfying%20communcal%20relationships(1).pdf)):
  - about 5 months after the wedding; 100 couples, 5 days, 874 daily observations (Table 6);
  - **perceived number of benefits received** was predicted about equally by one's own daily giving (.34) and by the partner's reported giving (.36);
  - **perceived communal motivation** was predicted more by one's own (.23) than by the partner's (.08).
- **Study 3** ([Yale lab PDF](https://clarkrelationshiplab.yale.edu/sites/default/files/files/Projection%20of%20responsiveness%20to%20needs%20and%20construction%20of%20satisfying%20communcal%20relationships(1).pdf)):
  - 158 online participants (116 women; mean age 25) rating a romantic partner (n = 101) or a **close friend** (n = 50);
  - they were randomly assigned to recall eight acts of their own help (difficult) or two (easy);
  - the difficult condition lowered PPR, F(1, 149) = 4.38, p < .05, mediated by experienced difficulty;
  - the manipulation did **not** significantly change self-reported own responsiveness (F = 1.24, p = .27), which the authors say complicates interpretation.
  - My conversion of the PPR effect: d ≈ 0.34.
- **Caveats the authors address** ([Yale lab PDF](https://clarkrelationshiplab.yale.edu/sites/default/files/files/Projection%20of%20responsiveness%20to%20needs%20and%20construction%20of%20satisfying%20communcal%20relationships(1).pdf)):
  - self-reported responsiveness is probably exaggerated, which they expect to affect means more than linear relations;
  - the same respondent answered similarly worded items for self and partner; they argue commitment moderation, an alternative PPR measure, diary-form counts and Study 3 mitigate this;
  - accuracy may dominate for specific, easily observed support and for extreme partners, while projection may dominate everyday perception.

#### C08 Collins & Feeney (2004), JPSP 87(3):363–383
- **Study 1 design** ([UCSB lab PDF](https://labs.psych.ucsb.edu/collins/nancy/UCSB_Close_Relationships_Lab/Publications_files/Collins%20and%20Feeney,%202004.pdf)):
  - 95 couples, recruited through an introductory psychology student; recipients 49 women and 46 men, mean age 19.4; 93.5% dating; together 15.8 months on average;
  - quasi-experiment: support level (high or low) was randomly assigned; attachment anxiety and avoidance were measured, not manipulated;
  - the recipient prepared a speech, supposedly to be videotaped, and received two notes that the partner copied in their own handwriting from experimenter text;
  - the low-support notes were written to be "somewhat ambiguous", so ambiguity and low support were not separately manipulated;
  - the study involved several deceptions and special debriefing.
- **Study 1 results: positive appraisal** ([UCSB lab PDF](https://labs.psych.ucsb.edu/collins/nancy/UCSB_Close_Relationships_Lab/Publications_files/Collins%20and%20Feeney,%202004.pdf)):
  - note condition had large effects (β = .66, sr² = .43 before the speech; β = .67, sr² = .44 after);
  - attachment had no effects.
- **Study 1 results: negative appraisal** ([UCSB lab PDF](https://labs.psych.ucsb.edu/collins/nancy/UCSB_Close_Relationships_Lab/Publications_files/Collins%20and%20Feeney,%202004.pdf)):
  - pre-speech note: avoidance main effect sr² = .03; avoidance × condition only **marginal** (p = .09, sr² = .02); simple effect in the low-support condition β = .41, sr² = .06; in the high-support condition β = .06, ns;
  - post-speech note: anxiety main effect sr² = .03; anxiety × condition significant (sr² = .03); simple effect low support β = .40, sr² = .06; high support β = .00.
- **Study 1, re-rating of the earlier interaction** (n = 73; [UCSB lab PDF](https://labs.psych.ucsb.edu/collins/nancy/UCSB_Close_Relationships_Lab/Publications_files/Collins%20and%20Feeney,%202004.pdf)):
  - the 3-way interaction was marginal (p = .07, sr² = .03); within the low-support condition the anxiety × avoidance interaction was significant (sr² = .10);
  - effect of the notes on re-rating, by profile: secure β = .05, ns; preoccupied β = .80, sr² = .10; fearful β = .35, sr² = .04; dismissing β = .36, ns;
  - observer ratings showed partners were no less supportive in the low-support condition.
  - The speech-performance results are labelled exploratory by the authors.
- **Study 2** ([UCSB lab PDF](https://labs.psych.ucsb.edu/collins/nancy/UCSB_Close_Relationships_Lab/Publications_files/Collins%20and%20Feeney,%202004.pdf)):
  - 153 couples (86 women and 67 men as recipients); partners wrote **genuine** notes, which independent raters coded;
  - with objective note ratings, satisfaction, trust and perceived partner support controlled, anxiety and avoidance still predicted less favourable note perceptions (sr² roughly .02–.09);
  - three-way interactions with support quality: sr² .03–.08;
  - attachment effects were strongest for low-support notes and **still present but weaker for moderately supportive notes**; they were absent only for very supportive notes.
- **Sample listing in F&K.** C&F Study 2 is listed as a United States dating, college sample ([F&K PDF](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.471.1954&rep=rep1&type=pdf)).
- **Authors' caveats** ([UCSB lab PDF](https://labs.psych.ucsb.edu/collins/nancy/UCSB_Close_Relationships_Lab/Publications_files/Collins%20and%20Feeney,%202004.pdf)):
  - attachment was not manipulated, so its causal role is not established; a correlated third variable is possible;
  - there was no objective standard of which group appraised "accurately";
  - the abstract's own bound is that bias appears "especially when the support message is ambiguous".

#### C09 Fletcher & Kerr (2010), Psychological Bulletin 136(4):627–658
- **Inclusion** ([F&K PDF](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.471.1954&rep=rep1&type=pdf)):
  - published, peer-reviewed studies up to the end of 2008; adults; all located samples heterosexual;
  - the benchmark had to be external to the judge, most commonly the partner's self-judgment; memory and prediction studies were the exception, using the same person's past or future states or outcomes;
  - difference-score and projection (path-model) studies were excluded;
  - effect sizes were entered by the first author; judgment categories were double-coded with 94% agreement.
- **Tracking accuracy** ([F&K PDF](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.471.1954&rep=rep1&type=pdf)):
  - overall r = .47, 95% CI [.44, .50] (98 studies, 27,064 individuals);
  - 75 studies used across-sample correlations for a trait; 23 used within-couple or mind-reading indices;
  - by category: personality .43; negative interaction traits .51; **positive interaction traits (love, affection) .40 [.33, .47]**; mind reading .58; memories .62; predictions .36.
- **Mean-level bias** ([F&K PDF](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.471.1954&rep=rep1&type=pdf)):
  - signed r = .09 [.04, .13] (48 studies, 9,393 individuals); absolute r = .18 [.14, .21];
  - by category, signed: personality .15; memories .26; predictions .23; **positive interaction traits −.11 [−.21, −.002], p = .05, k = 7**; negative interaction traits −.07 [−.15, .02], ns.
- **Independence and relationship quality** ([F&K PDF](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.471.1954&rep=rep1&type=pdf)):
  - across the 38 studies reporting both, tracking and signed bias effect sizes correlated r = .005; with absolute bias the correlation was weak and ns (p = .53);
  - positive bias related to relationship quality (r = .36, 14 studies); tracking accuracy did not (r ≈ .03, ns, 27 studies);
  - gender did not moderate tracking or signed bias.
- **Caveats the authors note** ([F&K PDF](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.471.1954&rep=rep1&type=pdf)):
  - the criterion problem: targets' self-perceptions are often biased;
  - the meta-analytic effects are zero-order and do not control for actual similarity; studies that do control for it show mixed results, sometimes with large drops in direct accuracy.

#### C10 Joel et al. (2020), PNAS 117(32):19061–19071
- **Sample** ([Joel PDF](https://escholarship.org/content/qt8mc5n2c3/qt8mc5n2c3.pdf)):
  - 43 dyadic longitudinal datasets from 29 laboratories; 11,196 couples (22,163 participants at baseline); 2,413 mostly self-report baseline measures;
  - on average 4 waves over 14 months (range 2–48 months);
  - all Western: US, Canada, Switzerland, New Zealand, Netherlands, Israel;
  - Dataset 38 (Supporting Healthy Marriage, low-income oversample) holds 6,298 couples, more than half of the total.
- **Methods** ([Joel PDF](https://escholarship.org/content/qt8mc5n2c3/qt8mc5n2c3.pdf)):
  - preregistered overall (June 2018) and per dataset (43 plans);
  - outcomes: satisfaction (primary) and commitment (31 datasets);
  - random forests (5,000 trees) with VSURF variable selection; variance explained is out-of-bag within each dataset, then pooled by random-effects meta-analysis (r → Fisher z, weight N−3);
  - trust, intimacy, love and passion were removed from the main models as possible indicators of quality;
  - change = each person's slope across waves.
- **Baseline satisfaction results** ([Joel PDF](https://escholarship.org/content/qt8mc5n2c3/qt8mc5n2c3.pdf)):
  - actor-reported relationship variables explained 45%; partner-reported 15%; actor and partner together 46%; all variables 44%;
  - individual differences: actor 19%, partner 5%, combined 21%;
  - follow-up: up to 18% (relationship variables) and 12% (individual differences);
  - change: no analysis exceeded 5%, and confidence intervals overlapped substantially; change typically spanned 1–2 years;
  - commitment estimates averaged 3% smaller.
- **Robustness and constructs** ([Joel PDF](https://escholarship.org/content/qt8mc5n2c3/qt8mc5n2c3.pdf)):
  - across predictor-restriction variants, partner reports and individual differences added 0.0–1.9% at baseline and 0.9–3.5% at follow-up; mean change prediction was about 2.2–2.5%;
  - success rates (Table 2): perceived partner commitment 85%, appreciation 72%, sexual satisfaction 71%, perceived partner satisfaction 70%, conflict 69%, **PPR 69%**;
  - the table note says success rates are not effect sizes and give no direction.
- **Limitations stated** ([Joel PDF](https://escholarship.org/content/qt8mc5n2c3/qt8mc5n2c3.pdf)):
  - all samples Western;
  - 99.4% of the **1,149 relationship-specific variables** were explicit self-report rating scales;
  - contextual variables were self-reported; datasets came mostly from psychologists' labs.
  - The authors read the absence of incremental prediction as mediation through one's own perceptions, which they call "plausible".

### Inferences
- **B&L.** "Over-provision" is the recipient's wish for less of a behaviour. A spouse who is becoming dissatisfied may come to want less advice or help, so reverse causation is as plausible as harm from excess. The authors say they cannot order the two. The proportion score counts how many behaviours are flagged, not how much excess there is.
- **LCF.** The "accuracy" benchmark is the partner's self-report, a different rater with independent error. The "projection" path shares rater and item wording with the outcome. Comparing the two coefficients therefore favours projection unless reliabilities are equated. The authors' commitment-moderation and Study 3 arguments reduce but do not remove this concern (my inference).
- **F&K.** The meta-analytic r = .47 is a zero-order agreement correlation. It is not the "truth force" τ of a truth-and-bias model with projection estimated separately. "Independence" is a between-study correlation over 38 studies, not a within-person result.
- **Joel.** Variable selection (VSURF) and out-of-bag estimation run on the same dataset, so the variance estimates could be somewhat optimistic (my inference; not discussed in the main text). Weighting by N−3 gives Dataset 38 a large weight, which random effects temper; the authors report that its pattern matched the other datasets.
- **Joel.** Baseline "prediction" is concurrent prediction by the same reporter, so shared method and general sentiment can contribute to the 45%.

### Gaps
- B&L: I did not check the published JFP version or later replications. Brock & Lawrence 2014 uses the same sample. Data-collection years were not found.
- LCF: Study 2's recruitment location is not stated in the pages I read. The full Table 5 coefficients were not extracted.
- C&F: Study 2 Table 1 and Table 2 coefficients were not transcribed in full. I did not search for replications of the standardized-note paradigm.
- F&K: I did not tabulate the full country mix of Table 2. The rows I read were mostly US. I did not search for meta-analyses after 2010.
- Joel: SI Appendix, the per-dataset results and OSF materials were not accessed.

## 4. Does each study support the way the paper uses it? (verdicts and corrected wording)

### Takeaway
- **C10: supported.** There are minor wording errors elsewhere in the paper.
- **C07: supported with qualifications.** One passage (19b:7) is overstated.
- **C08: supported with qualifications.** The paper overstates the evidence grade and the "only ambiguous" boundary, and misattributes an ethics claim.
- **C09: supported with qualifications.** The model chapter and README apply the overall *positive* bias to perceived care, where F&K's love-domain bias was *negative*.
- **C06: overstated.** "Over-provision predicted decline more strongly" depends on the metric; the reported effect sizes favour under-provision. "Predicted" implies a temporal order that the design cannot show. The "commensurate measurement" use is wrong.

### Cited Findings

**C06 — overstated**
- **"more strongly" depends on the metric.** The χ² tests compare unstandardized slopes per unit of the 0–1 proportion score. In the same table, the effect-size r is larger for under-provision: husbands .36 vs .28, wives .43 vs .31. Under-provision was also roughly twice as prevalent ([PMC2776033](https://pmc.ncbi.nlm.nih.gov/articles/PMC2776033/)).
- **"predicted declining" claims a temporal order the study does not show.** The estimates are concurrent within-spouse covariation from time-varying covariates, and the authors say they cannot tell whether inadequate support precedes or follows discord ([PMC2776033](https://pmc.ncbi.nlm.nih.gov/articles/PMC2776033/)).
- **The "over five years versus day to day" contrast is not only a timescale difference.** It also confounds measurement: past-month preferred-direction ratings here versus daily reports in Bar-Kalifa & Rafaeli. The design differs too: within-person covariation across waves versus daily data. This bears on 08:215 and 03:142.
- **Not "commensurate" (08:219, 08:315, 17:15).** Supply was rated on a 5-point frequency scale. Need was only the preferred direction (more/less/same), so need and supply are not on one metric. The measure is a respondent-judged discrepancy and cannot be analysed with response-surface analysis ([PMC2776033](https://pmc.ncbi.nlm.nih.gov/articles/PMC2776033/)).
- **Corrected wording for 03:39 and 04:31.** "In 103 Iowa newlywed couples assessed five times over five years, within-spouse increases in perceived under-provision and in perceived over-provision (wanting less of a support behaviour) each co-varied with lower marital satisfaction. Per behaviour flagged, over-provision had the larger slope. By the effect sizes reported, under-provision's association was at least as strong (r = .36–.43 vs .28–.31), and under-provision was far more common. The design cannot show which came first (Brock & Lawrence 2009) [Preliminary for 'over-provision is worse'; Moderate for 'both matter']."
- **Corrected wording for 17:15 and 08:219.** Class "Direct (perceived discrepancy; not commensurate)". Replace "need–supply measurement on one metric exists" with: "partner-support research has measured received frequency plus a perceived direction of discrepancy (Brock & Lawrence 2009). That is not commensurate need and supply, so it does not support RSA." Bar-Kalifa & Rafaeli 2013 (daily desire vs receipt) may be a better precedent; I did not check it.

**C07 — supported with qualifications**
- **Accurate for global perceptions.** 03:11, 05:12 and 08:34 are accurate for questionnaire-based global perceptions: own β .47–.60 vs partner β .17–.22 in two samples, both significant ([Yale lab PDF](https://clarkrelationshiplab.yale.edu/sites/default/files/files/Projection%20of%20responsiveness%20to%20needs%20and%20construction%20of%20satisfying%20communcal%20relationships(1).pdf)).
- **Omitted daily result.** The paper omits that daily *counts of benefits received* tracked the partner's reported giving as strongly as one's own (.36 vs .34). Projection dominated only for perceived motives (.23 vs .08) ([Yale lab PDF](https://clarkrelationshiplab.yale.edu/sites/default/files/files/Projection%20of%20responsiveness%20to%20needs%20and%20construction%20of%20satisfying%20communcal%20relationships(1).pdf)). This matters for a translation model: detection of concrete acts was not projection-dominated.
- **19b:7 is overstated.** LCF measured own responsiveness or communal strength, not "love, mood, … history". Attachment and depression were control variables. The giver's *acts* were never observed; the benchmark was the giver's self-report ([Yale lab PDF](https://clarkrelationshiplab.yale.edu/sites/default/files/files/Projection%20of%20responsiveness%20to%20needs%20and%20construction%20of%20satisfying%20communcal%20relationships(1).pdf)).
- **Corrected wording for 05:12 and 03:11.** "In two US samples of married and engaged couples, a spouse's own self-reported responsiveness predicted their global perception of the partner's responsiveness more strongly (β ≈ .47–.60) than the partner's self-report did (β ≈ .17–.22); both paths were significant. For daily counts of benefits received, the partner's reported giving mattered as much as one's own. Making one's own past help harder to recall lowered perceived responsiveness (Lemay, Clark & Feeney 2007) [Moderate]."
- **Corrected wording for 19b:7.** "Feeling cared for depends substantially on the receiver's own responsiveness, which is projected onto the partner. The partner's self-reported care also registers, especially for concrete acts (Lemay, Clark & Feeney 2007)." Cite other sources for mood, attachment and history.

**C08 — supported with qualifications**
- **The numbers in 03:78–79 match Study 1** ([UCSB lab PDF](https://labs.psych.ucsb.edu/collins/nancy/UCSB_Close_Relationships_Lab/Publications_files/Collins%20and%20Feeney,%202004.pdf)). The paper omits four points:
  - the avoidance × condition interaction was only marginal (p = .09);
  - the avoidance effect concerned the pre-speech note and the anxiety effect the post-speech note;
  - effects appeared on *negative* (hurtful) appraisal, not on positive appraisal;
  - ambiguity was built into the low-support notes and never manipulated separately.
- **The "only ambiguous" boundary is too narrow** (03:79, 06:9 "confined", 08:172). In Study 2's genuine notes, attachment effects were strongest for low-support notes, weaker but present for moderately supportive notes, and absent for very supportive notes ([UCSB lab PDF](https://labs.psych.ucsb.edu/collins/nancy/UCSB_Close_Relationships_Lab/Publications_files/Collins%20and%20Feeney,%202004.pdf)).
- **06:9 "adds nothing beyond relationship perceptions"** comes from Joel's prediction of relationship quality. In C&F Study 2, attachment predicted appraisal of messages *beyond* satisfaction, trust and perceived partner support ([UCSB lab PDF](https://labs.psych.ucsb.edu/collins/nancy/UCSB_Close_Relationships_Lab/Publications_files/Collins%20and%20Feeney,%202004.pdf); [Joel PDF](https://escholarship.org/content/qt8mc5n2c3/qt8mc5n2c3.pdf)). The cell conflates two different outcomes.
- **18:90 misattributes an ethics claim.** C&F report only that the study involved several deceptions and that they debriefed with special care. They do not report or argue relational harm ([UCSB lab PDF](https://labs.psych.ucsb.edu/collins/nancy/UCSB_Close_Relationships_Lab/Publications_files/Collins%20and%20Feeney,%202004.pdf)).
- **Corrected wording for 03:77–80.** Tag [Moderate]. Add: "Effects were on hurtful-intent appraisals (sr² ≈ .06; the first note's interaction was marginal). With genuine notes (153 couples), attachment effects were strongest for low-support notes, weaker for moderately supportive ones and absent for very supportive ones."
- **Corrected wording for 18:90.** "…because the paradigm deceives participants about messages from real partners (Collins & Feeney 2004 describe several deceptions and careful debriefing); the risk of relational harm is our inference."

**C09 — supported with qualifications**
- **Core numbers verified.** r = .47 [.44, .50] across 98 studies; r = .09 [.04, .13] across 48 studies ([F&K PDF](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.471.1954&rep=rep1&type=pdf)).
- **"track reality" (task framing) and "*when* and on what" (03:58) are inaccurate.** The benchmark is mostly the partner's self-report, and tracking was measured across couples or across items, not over time ([F&K PDF](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.471.1954&rep=rep1&type=pdf)).
- **The sign of bias is misapplied in the model chapter and README.** For love and affection judgments, the domain of the model's perceived-care component, signed bias was **−.11** (k = 7, CI upper limit −.002). Tracking accuracy for that category was .40, not .47 ([F&K PDF](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.471.1954&rep=rep1&type=pdf)). README:123 and 08:34 ("positively biased") therefore misstate the sign for perceived care, and 05:46 ("small positive mean bias overall") cites the wrong category.
- **"underestimate their partner's love" needs a benchmark qualifier.** The shortfall is relative to the partner's self-report, which F&K note is itself likely self-enhancing ([F&K PDF](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.471.1954&rep=rep1&type=pdf)).
- **Corrected wording for 03:58.** "…tracking accuracy (whether judgments covary with a benchmark, usually the partner's self-report, across couples or items), r = .47 [.44, .50] across 98 studies, and mean-level bias, r = .09 [.04, .13] across 48 studies; the two effect sizes were uncorrelated across the 38 studies reporting both. For judgments of the partner's love or affection, tracking was r = .40, and signed bias was slightly negative (r = −.11, 95% CI −.21 to −.002, 7 studies): relative to partners' self-reports, people slightly underestimated their partner's love."
- **Corrected wording for 08:34 and README:123.** "partners track each other moderately well (r ≈ .40 for judgments of partner love) with small mean-level bias, positive overall but slightly negative for perceived love".
- **Corrected wording for 05:46.** Signed r ≈ −.11 and absolute r ≈ .15 for love-type judgments; by my conversion d ≈ .2–.3.

**C10 — supported**
- **Central claims verified.** Actor-reported relationship variables explained 45% of baseline satisfaction. Adding partner reports and individual differences gained essentially nothing (46% and 44%). No analysis exceeded 5% for change ([Joel PDF](https://escholarship.org/content/qt8mc5n2c3/qt8mc5n2c3.pdf)).
- **06:7 is overstated.** PPR was not the top predictor. Its success rate was 69%, tied with conflict, behind perceived partner commitment (85%) ([Joel PDF](https://escholarship.org/content/qt8mc5n2c3/qt8mc5n2c3.pdf)).
- **03:138 misstates the base.** The 99.4% figure refers to the 1,149 relationship-specific variables, not to all predictors ([Joel PDF](https://escholarship.org/content/qt8mc5n2c3/qt8mc5n2c3.pdf)).
- **06:24 cites Joel for something Joel does not argue.** Joel does not raise reverse causation from satisfaction to perceptions. The authors favour a mediation reading and mention a "likely bidirectional" link only for relationship quality and well-being ([Joel PDF](https://escholarship.org/content/qt8mc5n2c3/qt8mc5n2c3.pdf)).
- **08:369 "essentially none"** is better stated as "at most 5% (mean about 2–2.5%) for change measured as slopes over typically 1–2 years". Follow-up *levels* were predicted up to 18%, so the heading "the future of a relationship is barely predictable" (05:69) should specify *change* ([05:69](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/paper/05-evidence-against-it.md); [Joel PDF](https://escholarship.org/content/qt8mc5n2c3/qt8mc5n2c3.pdf)).

### Inferences
- The biggest model consequence is in C09. The paper's own source suggests a level bias δ < 0 for perceived love (receivers rate love below the giver's self-report). That is directionally *consistent* with the "love perceived < love expressed" intuition, but small: about d −0.2 by my conversion. The paper currently states the opposite sign at the model level.
- The C06 correction weakens the paper's only quantitative support for an asymmetric loss that penalizes excess more than deficit. In B&L's own effect sizes, deficit is at least as strongly associated with satisfaction.

### Gaps
- I did not check whether any later study re-analysed B&L with standardized coefficients.
- I did not check Bar-Kalifa & Rafaeli 2013, so the "timescale" explanation is assessed only from the B&L side.

## 5. What evidence grade does each claim deserve as used, and should the paper's tag change?

### Takeaway
- **C06:** split the grade. "Over-provision is worse" is Preliminary; "both directions matter" is Moderate.
- **C07:** keep Moderate.
- **C08:** downgrade "Established (bounded)" to Moderate, and make the tags consistent across chapters.
- **C09:** keep Established for tracking accuracy and the small overall bias. Grade the love-specific negative bias Moderate/Preliminary.
- **C10:** keep "Established, for prediction".

### Cited Findings
- **C06.** Single sample of N = 103, recipient-perceived measures, concurrent within-spouse covariation, the authors call for replication. The "greater risk" conclusion rests on unstandardized comparisons ([PMC2776033](https://pmc.ncbi.nlm.nih.gov/articles/PMC2776033/)). Current tags: "Mixed" (03:142) and [Moderate/mixed] (08:36, 08:215, README:125); 03:39 and 04:31 have no tag. **Recommend:** [Preliminary] wherever over-provision is said to be worse; [Moderate] for "both under- and over-provision are associated with lower satisfaction".
- **C07.** Two dyadic samples (191 and 108 couples) and one online experiment (N = 158), all from one research group, all US. The benchmark is the partner's self-report ([Yale lab PDF](https://clarkrelationshiplab.yale.edu/sites/default/files/files/Projection%20of%20responsiveness%20to%20needs%20and%20construction%20of%20satisfying%20communcal%20relationships(1).pdf)). The current "Moderate" (01:17, 08:34) and "Moderate/mixed" (03:11, 03:139) fit. **Recommend:** add [Moderate] to 05:12, and a tag plus the qualification at 19b:7.
- **C08.** One lab and two studies; the experimental study had N = 95, with simple effects within about 47 per condition; one key interaction was marginal; attachment was not manipulated; samples were students (Study 2 listed as US by F&K) ([UCSB lab PDF](https://labs.psych.ucsb.edu/collins/nancy/UCSB_Close_Relationships_Lab/Publications_files/Collins%20and%20Feeney,%202004.pdf)). sr² .03–.10 corresponds to sr ≈ .17–.32 (my conversion), small to moderate. **Recommend:** change 03:77 "[Established for this bounded effect]" and 06:9 "Established (bounded)" to [Moderate]. That matches 02:17, 03:141 and 08:172.
- **C09.** 98 and 48 studies, random effects, tight CIs, no sign of publication bias by trim-and-fill or fail-safe N. Limits: published-only, ends in 2008, partner-self-report benchmark ([F&K PDF](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.471.1954&rep=rep1&type=pdf)). **Recommend:** keep [Established] for tracking accuracy and the small overall bias. Tag the love-specific underestimation [Moderate/Preliminary] (k = 7, p = .05).
- **C10.** Preregistered; 43 datasets and 11,196 couples; consistent across restriction variants and in the large low-income dataset. Limits: Western, self-report only, prediction rather than causation ([Joel PDF](https://escholarship.org/content/qt8mc5n2c3/qt8mc5n2c3.pdf)). **Recommend:** keep [Established, for prediction], and add "Western, self-report" wherever the 45% figure is quoted.

### Inferences
- Grading for C08 and C06 is inconsistent across chapters. A single canonical tag per claim, kept in `evidence/claims.jsonl` and propagated to every chapter, would prevent the drift.

### Gaps
- My grades follow the paper's scale (Established / Moderate or mixed / Preliminary / Theoretical) and rest only on the five primary texts. No systematic replication search was done.

## 6. Verification depth for each claim

### Takeaway
All five were verified at **full text**. The B&L copy is the accepted manuscript. Joel was read without its SI Appendix.

### Cited Findings
- **C06**, full text of the accepted manuscript, which differs from the typeset version only by copy-editing ([PMC2776033](https://pmc.ncbi.nlm.nih.gov/articles/PMC2776033/)). Read: abstract; theoretical summary; Method (participants, procedures, SIRRS, QMI, analyses); all Results (Aims 1–3, sex differences); Table 1; Discussion including limitations and clinical implications; footnotes.
- **C07**, full text of the published version ([Yale lab PDF](https://clarkrelationshiplab.yale.edu/sites/default/files/files/Projection%20of%20responsiveness%20to%20needs%20and%20construction%20of%20satisfying%20communcal%20relationships(1).pdf)). Read: abstract; Study 1 Method, Results, Tables 1–2 and footnotes; Study 2 Method and Results (Tables 3, 4, 6, longitudinal text); Study 3 Method and Results; General Discussion on projection versus accuracy, method variance and when accuracy dominates. Skimmed: introduction and the closing General Discussion.
- **C08**, full text of the published version ([UCSB lab PDF](https://labs.psych.ucsb.edu/collins/nancy/UCSB_Close_Relationships_Lab/Publications_files/Collins%20and%20Feeney,%202004.pdf)). Read: abstract; Study 1 rationale, Method, Results and Discussion; Study 2 rationale, participants, analytic strategy, main results, moderation by support quality and Discussion; General Discussion caveat on causality. Skimmed: introduction, Study 2 measures, the coefficient tables.
- **C09**, full text of the published version ([F&K PDF](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.471.1954&rep=rep1&type=pdf)). Read: abstract; conceptual sections on benchmarks and categories; Method (selection, coding, effect sizes); all Results (Table 3, publication bias, independence, links to quality, gender, relationship length); Discussion summary; projection section; criterion problem. Skimmed: Table 2 study list and the remaining Discussion.
- **C10**, full text of the published main article ([Joel PDF](https://escholarship.org/content/qt8mc5n2c3/qt8mc5n2c3.pdf)). Read: abstract; Significance; introduction; data solicitation; Measures; analysis strategy; meta-analysis; Results; Tables 1–3; Discussion; limitations; conclusion. Not accessed: SI Appendix, OSF.

### Inferences
- Earlier project notes leave several gaps that this audit closes for the five claims:
  - Lemay and B&L coefficients are recorded as not extracted because the full texts were paywalled ([evidence/notes/01-interpersonal-processes.md](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/evidence/notes/01-interpersonal-processes.md), lines 54 and 347);
  - the love-specific F&K bias is described as not extractable from the abstract ([evidence/notes/02-misperception-and-asymmetry.md](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/evidence/notes/02-misperception-and-asymmetry.md), line 130);
  - Joel's change values are listed as not retrieved ([evidence/notes/03-love-needs-compatibility.md](https://github.com/julienaxyomlabs/love-in-translation/blob/v0.2.0/evidence/notes/03-love-needs-compatibility.md), line 329).

### Gaps
- The PDF-to-text extraction dropped Greek letters and minus signs. Signs were reconstructed from the surrounding text and confidence intervals, e.g. F&K positive-interaction bias −.11 [−.21, −.002]. The sign of the F&K absolute-bias × tracking correlation (|r| = .11) and of the tracking × quality correlation (|r| ≈ .03) could not be confirmed; both are non-significant.

Machine-readable summary (one JSON object per claim):

```jsonl
{"claim_id": "C06", "short_claim": "Over-provision of partner support (more than wanted) predicted declining marital satisfaction more strongly than under-provision in 103 newlywed couples over 5 years", "source": "Brock, R. L., & Lawrence, E. (2009). Too much of a good thing: Underprovision versus overprovision of partner support. Journal of Family Psychology, 23(2), 181-192.", "doi": "10.1037/a0015402", "verification_depth": "full text", "sections_read": "NIH accepted manuscript PMC2776033: abstract, theory summary, Method (participants, SIRRS, QMI, analyses), Results Aims 1-3, Table 1, Discussion incl. limitations, footnotes", "design": "Longitudinal observational dyadic study, 5 mailed waves (3-6 to 54-57 months after wedding); growth-curve APIM with under- and over-provision as group-mean-centred time-varying covariates, i.e. concurrent within-spouse covariation, not lagged prediction", "population": "103 first-married newlywed couples recruited via Iowa marriage-license records; ages about 25-26; 15% ethnic minority; modal education 14 years; mostly satisfied; data-collection years not stated in text read", "measured": "Recipient-reported modified SIRRS (48 behaviours): past-month frequency plus preferred direction (more/less/same); under-provision = proportion wanted more, over-provision = proportion wanted less; informational, emotional, esteem, tangible subscales; satisfaction via QMI", "key_result": "Both forms uniquely co-varied with lower satisfaction. Husbands: under b=-7.52, t=-3.92, r=.36; over b=-18.73, t=-2.88, r=.28; chi2=4.76. Wives: under b=-8.02, t=-4.84, r=.43; over b=-27.14, t=-3.38, r=.31; chi2=5.00. Unstandardized over-provision slopes larger (p<.05) but reported effect-size r larger for under-provision. By type: over>under only for informational (husbands) and informational, emotional, tangible (wives); esteem over-provision ns. Under-provision far more prevalent (61-92% vs 27-43% of spouses per wave).", "supports_interpretation": "overstated", "evidence_grade": "Preliminary (over-provision worse than under-provision); Moderate (both forms associated with lower satisfaction)", "paper_locations": ["paper/03-literature-review.md:39", "paper/03-literature-review.md:142", "paper/04-evidence-for-the-intuition.md:31", "paper/07-revised-model.md:65", "paper/08-mathematical-representation.md:36", "paper/08-mathematical-representation.md:215", "paper/08-mathematical-representation.md:219", "paper/08-mathematical-representation.md:315", "paper/17-what-testing-requires.md:15", "paper/19-limitations.md:3", "paper/19-limitations.md:12", "README.md:125"], "recommended_change": "Replace 'predicted declining' with 'co-varied with lower'; state that over-provision had the larger per-item slope but under-provision the larger reported effect size and higher prevalence; tag over-provision-is-worse as Preliminary. At 08:219, 08:315 and 17:15 remove the claim that B&L measured need and supply on one metric (need was only a more/less/same direction); reclassify as a direct perceived-discrepancy measure unusable for RSA.", "notes": "Authors state analyses show covariation, not temporal order, and they cannot tell whether inadequate support precedes or follows discord. Over-provision = recipient wanting less of a behaviour, which may partly express dissatisfaction (reverse causation). Contrast with Bar-Kalifa & Rafaeli 2013 involves measurement and design differences, not only timescale. Accepted manuscript, not typeset version."}
{"claim_id": "C07", "short_claim": "A perceiver's own responsiveness predicts perceived partner responsiveness more strongly than the partner's own report does (projection)", "source": "Lemay, E. P., Clark, M. S., & Feeney, B. C. (2007). Projection of responsiveness to needs and the construction of satisfying communal relationships. Journal of Personality and Social Psychology, 92(5), 834-853.", "doi": "10.1037/0022-3514.92.5.834", "verification_depth": "full text", "sections_read": "Published PDF (Yale lab site): abstract; Study 1 Method, Results, Tables 1-2, footnotes; Study 2 Method, Results, Tables 3, 4, 6, longitudinal text; Study 3 Method and Results; General Discussion sections on projection vs accuracy, method variance, when accuracy dominates", "design": "Study 1 cross-sectional dyadic questionnaires (HLM); Study 2 two-wave dyadic panel (premarital and about 25 months after wedding) plus 5-day diary; Study 3 online randomized recall-difficulty experiment", "population": "Study 1: 191 married couples, Pittsburgh area, newspaper ads, ages 18-82, about 75-77% Caucasian (analysed 151-170 couples). Study 2: 108 engaged couples (96 at T2), predominantly Caucasian, 80% college graduates, ages 20-38; diary 100 couples. Study 3: 158 online adults (116 women, mean age 25) rating a romantic partner (101) or close friend (50).", "measured": "Own responsiveness (caregiving and secure-base self-reports in Study 1; communal strength in Study 2) and perceived partner responsiveness (reworded parallel items plus a second scale); partner's self-reported responsiveness as accuracy benchmark; satisfaction; commitment; attachment, self-esteem, depression controls; daily benefits given and received and perceived communal motives", "key_result": "Own vs partner paths to perceived responsiveness: Study 1 .60 vs .22 (safe haven), .52 vs .17 (secure base); Study 2 .51 vs .17 (T1), .47 vs .18 (T2); all significant. Daily perceived number of benefits: own giving .34 vs partner's reported giving .36; daily perceived communal motive: .23 vs .08. Study 3: difficult recall lowered perceived responsiveness, F(1,149)=4.38, p<.05, but did not significantly change self-reported own responsiveness (p=.27).", "supports_interpretation": "qualified", "evidence_grade": "Moderate", "paper_locations": ["paper/01-question-and-thesis.md:17", "paper/03-literature-review.md:11", "paper/03-literature-review.md:139", "paper/05-evidence-against-it.md:12", "paper/06-competing-theories.md:7", "paper/08-mathematical-representation.md:34", "paper/08-mathematical-representation.md:170", "paper/08-mathematical-representation.md:313", "paper/12-asymmetry-and-misperception.md:12", "paper/19b-is-love-enough.md:7", "README.md:123"], "recommended_change": "Keep Moderate. Specify that the finding concerns global questionnaire perceptions benchmarked against the partner's self-report, and that for daily counts of benefits received the partner's reported giving predicted perception as strongly as own giving. Rewrite 19b:7: LCF does not show that feeling loved depends at least as much on the receiver's love, mood, attachment and history as on the giver's acts (acts were not observed; attachment and depression were controls).", "notes": "Projection path shares rater and item wording with the outcome while the accuracy path uses a different rater, which favours projection; authors counter with commitment moderation, an alternative PPR scale, diary-form counts and Study 3. Single research group, US samples. Authors say accuracy may dominate for specific, observable support."}
{"claim_id": "C08", "short_claim": "Insecurely attached recipients appraised identical standardized support notes more negatively only when notes were ambiguous; effects small (sr2 about .03-.10); clearly supportive notes read alike", "source": "Collins, N. L., & Feeney, B. C. (2004). Working models of attachment shape perceptions of social support: Evidence from experimental and observational studies. Journal of Personality and Social Psychology, 87(3), 363-383.", "doi": "10.1037/0022-3514.87.3.363", "verification_depth": "full text", "sections_read": "Published PDF (UCSB lab site): abstract; Study 1 rationale, Method, Results, Discussion; Study 2 rationale, participants, analytic strategy, main results, moderation by support quality, Discussion; General Discussion causal caveat", "design": "Study 1 quasi-experiment: randomized high vs low (ambiguous) support notes copied by partner from experimenter text, attachment measured; Study 2 laboratory observational study with genuine partner notes coded by independent raters", "population": "Study 1: 95 student-recruited couples (country not stated in text read), recipients 49 women and 46 men, mean age 19.4, 93.5% dating. Study 2: 153 couples (86 women, 67 men as recipients), US college dating sample", "measured": "Recipient positive and negative appraisal of each note; perceived partner support in an earlier videotaped interaction (n=73) plus observer ratings; speech performance; attachment anxiety and avoidance composites; relationship satisfaction (Study 2 also trust and perceived partner support)", "key_result": "Study 1: positive appraisal driven by condition (beta .66, sr2 .43; .67, sr2 .44) with no attachment effects. Negative appraisal: avoidance effect in low-support condition (beta .41, sr2 .06; high support .06 ns) on pre-speech note with only marginal interaction (p=.09); anxiety effect in low-support condition (beta .40, sr2 .06; high .00) on post-speech note with significant interaction. Insecure low-support recipients re-rated an earlier interaction as less supportive (preoccupied beta .80, sr2 .10; fearful .35, sr2 .04; dismissing ns; 3-way p=.07). Study 2: attachment predicted less favourable perceptions of genuine notes beyond objective ratings, satisfaction, trust and perceived support (sr2 about .02-.09); effects strongest for low-support notes, weaker but present for moderately supportive notes, absent for very supportive notes.", "supports_interpretation": "qualified", "evidence_grade": "Moderate", "paper_locations": ["paper/01-question-and-thesis.md:14", "paper/02-definitions-and-distinctions.md:17", "paper/03-literature-review.md:77", "paper/03-literature-review.md:78", "paper/03-literature-review.md:79", "paper/03-literature-review.md:80", "paper/03-literature-review.md:141", "paper/06-competing-theories.md:9", "paper/07-revised-model.md:31", "paper/07-revised-model.md:64", "paper/08-mathematical-representation.md:172", "paper/14-time-and-feedback.md:22", "paper/17-what-testing-requires.md:38", "paper/18-proposed-study.md:90"], "recommended_change": "Change 'Established for this bounded effect' (03:77) and 'Established (bounded)' (06:9) to Moderate. Replace 'only ambiguous' and 'confined to ambiguous signals' with: strongest for low-support or ambiguous messages, weaker for moderately supportive genuine notes, absent for clearly supportive ones. Note the marginal interaction and that effects were on hurtful-intent appraisal. In 06:9 attribute 'adds nothing beyond relationship perceptions' to Joel 2020 (relationship quality), not to C&F. At 18:90 present relational harm as the paper's inference; C&F report only deception and careful debriefing.", "notes": "Ambiguity was confounded with low support in Study 1. Attachment was not manipulated, so its causal role is not identified (authors). sr2 .06-.10 corresponds to sr about .25-.32, small to moderate. Single lab, student samples (Study 2 US); performance results labelled exploratory by the authors."}
{"claim_id": "C09", "short_claim": "Meta-analysis: partners' judgments track reality (r about .47) while showing small positive mean-level bias (r about .09); accuracy and bias coexist", "source": "Fletcher, G. J. O., & Kerr, P. S. G. (2010). Through the eyes of love: Reality and illusion in intimate relationships. Psychological Bulletin, 136(4), 627-658.", "doi": "10.1037/a0019792", "verification_depth": "full text", "sections_read": "Published PDF (CiteSeerX cache): abstract; conceptual sections on benchmarks and judgment categories; Method (selection, coding, effect sizes); Results (Table 3, publication bias, independence, links to relationship quality, gender, relationship length); Discussion summary; projection section; criterion problem", "design": "Random-effects meta-analysis of published studies to end-2008 with external benchmarks (mostly partner self-report; own past or future states for memory and prediction studies); zero-order effect sizes; projection and difference-score studies excluded", "population": "98 tracking-accuracy studies (27,064 individuals) and 48 mean-level-bias studies (9,393 individuals); 38 studies reporting both; adults in heterosexual romantic relationships; mostly US in the rows read (full country mix not tabulated)", "measured": "Tracking accuracy (correlation of judgments with benchmark across couples or within couples or items) and signed and absolute mean-level bias (judgment minus benchmark, converted to r) across six categories: personality, negative interaction traits, positive interaction traits (love, affection), mind reading, memories, predictions", "key_result": "Tracking r=.47 [.44,.50]; by category .36-.62, positive interaction traits .40 [.33,.47]. Signed bias r=.09 [.04,.13]; absolute .18 [.14,.21]; signed bias for positive interaction traits -.11 [-.21,-.002], p=.05, k=7; negative interaction traits -.07 ns. Tracking and bias effect sizes uncorrelated across 38 studies (r=.005). Positive bias related to relationship quality (r=.36, 14 studies); tracking did not (about .03, 27 studies).", "supports_interpretation": "qualified", "evidence_grade": "Established (tracking accuracy and small overall bias); Moderate/Preliminary (negative bias for love judgments, k=7)", "paper_locations": ["paper/01-question-and-thesis.md:14", "paper/03-literature-review.md:58", "paper/03-literature-review.md:144", "paper/05-evidence-against-it.md:46", "paper/06-competing-theories.md:12", "paper/08-mathematical-representation.md:34", "paper/08-mathematical-representation.md:313", "README.md:123"], "recommended_change": "Replace 'track reality' and 'knowing when and on what' with 'covary with a benchmark, usually the partner's self-report, across couples or items'. Fix README:123 and 08:34: for perceived love the signed bias was slightly negative (-.11), not positive; tracking for love-type judgments was .40. At 05:46 cite the love-domain estimates (signed -.11, absolute .15) instead of the overall positive .09. Present 'independent' as 'uncorrelated across 38 studies'. Add 'relative to partners' self-reports' to 'underestimate their partner's love'.", "notes": "Authors flag the criterion problem: partner self-reports used as benchmarks are themselves likely biased. Effects are zero-order and do not separate tracking from projection or actual similarity; studies controlling for similarity show mixed, sometimes large, drops in accuracy. Published-only, ends in 2008, effect sizes entered by one author."}
{"claim_id": "C10", "short_claim": "Machine learning across 43 longitudinal datasets (11,196 couples): own relationship-specific perceptions explain up to 45% of baseline relationship quality; partner reports and individual differences add little; change barely predictable", "source": "Joel, S., Eastwick, P. W., et al. (2020). Machine learning uncovers the most robust self-report predictors of relationship quality across 43 longitudinal couples studies. PNAS, 117(32), 19061-19071.", "doi": "10.1073/pnas.1917036117", "verification_depth": "full text", "sections_read": "Published PNAS PDF (UC Davis eScholarship): abstract, Significance, introduction, data solicitation, Measures, analysis strategy, meta-analysis, Results, Tables 1-3, Discussion, limitations, conclusion; SI Appendix and OSF not accessed", "design": "Preregistered pooled analysis: random forests with VSURF variable selection in each of 43 dyadic longitudinal datasets (out-of-bag variance explained), pooled by random-effects meta-analysis; outcomes satisfaction (43 datasets) and commitment (31) at baseline, follow-up, and change (person-level slope)", "population": "43 datasets from 29 labs; 11,196 couples (22,163 participants at baseline); average 4 waves over 14 months (range 2-48); all Western (US, Canada, Switzerland, New Zealand, Netherlands, Israel); Dataset 38 low-income oversample = 6,298 couples", "measured": "2,413 mostly self-report baseline predictors grouped as actor and partner individual differences and relationship-specific variables (99.4% of 1,149 relationship-specific variables were self-report rating scales); trust, intimacy, love, passion removed from main models", "key_result": "Baseline satisfaction: actor relationship variables 45%, partner relationship 15%, actor+partner 46%, all 44%; individual differences 19% (actor), 5% (partner), 21% combined. Follow-up up to 18% (relationship) and 12% (individual). Change: no analysis exceeded 5% (mean about 2.2-2.5%). Partner reports and individual differences added 0.0-1.9% (baseline) and 0.9-3.5% (follow-up). Top success rates: perceived partner commitment 85%, appreciation 72%, sexual satisfaction 71%, perceived partner satisfaction 70%, conflict and perceived partner responsiveness 69%.", "supports_interpretation": "supported", "evidence_grade": "Established (for prediction, in Western self-report samples)", "paper_locations": ["paper/03-literature-review.md:7", "paper/03-literature-review.md:138", "paper/05-evidence-against-it.md:7", "paper/05-evidence-against-it.md:20", "paper/05-evidence-against-it.md:71", "paper/06-competing-theories.md:7", "paper/06-competing-theories.md:24", "paper/08-mathematical-representation.md:362", "paper/08-mathematical-representation.md:369", "paper/14-time-and-feedback.md:23", "paper/17-what-testing-requires.md:46", "paper/18-proposed-study.md:71", "paper/19-limitations.md:3"], "recommended_change": "Keep the tag. Fix 06:7 ('Top predictor' -> PPR 69% success rate, tied with conflict, behind perceived partner commitment 85%). Fix 03:138 ('99.4% of predictors' -> 99.4% of the 1,149 relationship-specific variables). At 08:369 say change explained at most 5% (slopes over typically 1-2 years) and note follow-up levels up to 18%. Do not cite Joel for reverse causation at 06:24. Say 'predicted (concurrently, out-of-bag within dataset)' rather than implying causal explanation.", "notes": "Authors read the lack of incremental prediction as mediation through actor perceptions (plausible, untested). Baseline prediction is concurrent and same-reporter, so shared method and sentiment may contribute. Variable selection and out-of-bag estimation on the same data may make estimates optimistic (auditor inference). Success rates are not effect sizes (authors)."}
```
