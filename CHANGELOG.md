# Changelog

All notable changes to this project are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses [Semantic Versioning](https://semver.org/).

## [0.2.0] - 2026-11-04

Corrections prompted by an external review; each is documented with earlier wording, sources and verification depth in [CORRECTIONS.md](CORRECTIONS.md).

### Fixed

- Response-surface interpretation: $`a_1`$ is the slope along the line of congruence at the centring point only, and a negative $`a_4`$ is one part of a joint congruence pattern, not a mismatch penalty by itself (C1).
- Safety is now an admissibility constraint that excludes unsafe arrangements and recommends nothing when none is safe; the lexicographic ranking it replaces still picked among unsafe options (C3, ADR-0009 supersedes ADR-0005).

### Changed

- The substantive and symbolic routes are described as pathways of effect for any act, not as categories of acts (C2).
- The README separates what the tests and DOI checks show from empirical validation, which has not been done (C4).
- `constraints.classify()` reports `"unsafe"` when only unsafe arrangements meet both people's requirements; `JointPattern` gains a `safe` field.

### Added

- "Model at a glance" in the README and chapter 8: the ten equations, what each says, its method and evidence status, every variable's unit and domain, and identifiability limits; figure `paper/figures/model-at-a-glance.png`.
- `fit.stationary_point()`, `fit.principal_axes()`, `fit.congruence_screen()` and $`a_5`$; tests reproduce the worked examples in Edwards (2007) and Schönbrodt, Humberg & Nestler (2018).
- `constraints.admissible()` and `constraints.choose()`.
- `CORRECTIONS.md`.

## [0.1.0] - 2026-11-04

### Added

- Paper in 22 chapters (`paper/`), with GitHub-native math, Figure 1 as SVG plus editable Mermaid source, and navigation between chapters.
- `love_translation` reference implementation (standard library only): similarity pitfalls, response surface analysis, quasi-signal detection, truth-and-bias decomposition, cost-based motive inference, trust dynamics, developmental lag, safety gate and feasibility.
- `love-translation` command-line interface: `cosine-demo`, `trust`, `lag`, `infer`, `claims`.
- 36 tests executing the paper's formal claims, plus repository-integrity tests.
- Evidence ledger `evidence/claims.jsonl` (276 graded claims), `evidence/references.bib`, `evidence/doi-verification.csv` and the seven literature reviews in `evidence/notes/`.
- Tooling: claims extraction, Markdown lint, DOI verification, BibTeX build, single-file paper build.
- CI on Python 3.9–3.13, monthly citation re-check, issue forms and architecture decision records.

[0.2.0]: https://github.com/julienaxyomlabs/love-in-translation/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/julienaxyomlabs/love-in-translation/releases/tag/v0.1.0
