# Contributing

This repository is built to be argued with. The most valuable contribution is evidence that a claim is wrong, overstated or mis-graded.

## Evidence rules

1. **Every empirical claim needs a verifiable source**: a DOI (preferred) or a stable URL. No citation from memory; run `make dois` before opening a pull request that adds references.
2. **Every claim carries a grade**, written as an inline tag:

   | Tag | Use when |
   |---|---|
   | `[Established]` | meta-analytic or multiply replicated, consistent direction |
   | `[Moderate/mixed]` | several studies or one strong design, with inconsistency or single-lab dependence |
   | `[Preliminary]` | single study, small or convenience sample, preprint, or secondary-source only |
   | `[Theoretical]` | a proposition from an existing theory that has not been tested directly |
   | `[Our hypothesis]` | original to this project and untested |
   | `[Assumption]` | a modelling or measurement assumption |

3. **Separate what a study measured from what its authors inferred.** Report design, N, population and how causation is identified.
4. **Flag WEIRD-only samples** and never let a national average describe an individual or a family.
5. **No invented coefficients.** Formal components use symbolic parameters. Numbers in tests are arithmetic illustrations and are labelled as such.
6. **Parental care is not romantic reciprocity.** Contributions must keep the asymmetry explicit.

## Workflow

```bash
make check     # markdown lint + claims-ledger freshness + tests (offline)
make claims    # regenerate evidence/claims.jsonl after editing the paper
make dois      # resolve every DOI against Crossref (network)
make bibtex    # rebuild evidence/references.bib (network)
```

- **Paper edits** go in `paper/NN-*.md`. Inline math uses GitHub's literal form `` $`…`$ ``; display math uses fenced `math` blocks; raw HTML is not used. Run `make claims` so the ledger matches.
- **Model edits** go in `src/love_translation/` with a test in `tests/` that states the paper section it implements. Standard library only.
- **Modelling decisions** that change what the framework claims need an ADR in `docs/adr/`.

## Opening an issue

Use the **Challenge a claim** form for disputes and the **New evidence** form for studies the paper should weigh. Point to a chapter and heading, or to a claim id from `evidence/claims.jsonl` (for example `05.004`).

## Conduct

Argue with evidence, not with people. Personal stories are welcome as motivation but are never treated as data about anyone else's family or relationship.
