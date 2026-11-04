# Changelog

All notable changes to this project are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses [Semantic Versioning](https://semver.org/).

## [0.1.0] - 2026-11-04

### Added

- Paper in 22 chapters (`paper/`), with GitHub-native math, Figure 1 as SVG plus editable Mermaid source, and navigation between chapters.
- `love_translation` reference implementation (standard library only): similarity pitfalls, response surface analysis, quasi-signal detection, truth-and-bias decomposition, cost-based motive inference, trust dynamics, developmental lag, safety gate and feasibility.
- `love-translation` command-line interface: `cosine-demo`, `trust`, `lag`, `infer`, `claims`.
- 36 tests executing the paper's formal claims, plus repository-integrity tests.
- Evidence ledger `evidence/claims.jsonl` (276 graded claims), `evidence/references.bib`, `evidence/doi-verification.csv` and the seven literature reviews in `evidence/notes/`.
- Tooling: claims extraction, Markdown lint, DOI verification, BibTeX build, single-file paper build.
- CI on Python 3.9–3.13, monthly citation re-check, issue forms and architecture decision records.

[0.1.0]: https://github.com/julienaxyomlabs/love-in-translation/releases/tag/v0.1.0
