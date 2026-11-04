# love-in-translation: run `make help` for targets
PY ?= python3

.DEFAULT_GOAL := help
.PHONY: help check test lint claims check-claims dois bibtex paper demo clean

help: ## List targets
	@grep -E '^[a-z-]+:.*## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*## "}; {printf "  %-14s %s\n", $$1, $$2}'

check: lint check-claims test ## Everything CI runs offline

test: ## Unit and repository tests (stdlib only)
	$(PY) -m unittest discover -s tests -t tests -v

lint: ## Markdown links, math delimiters, no raw HTML
	$(PY) tools/lint_markdown.py

claims: ## Regenerate evidence/claims.jsonl from the paper
	$(PY) tools/extract_claims.py --write
	$(PY) tools/extract_claims.py --stats

check-claims: ## Fail if the evidence ledger is stale
	$(PY) tools/extract_claims.py --check

dois: ## Resolve every DOI against Crossref (network)
	$(PY) tools/check_dois.py --write evidence/doi-verification.csv

bibtex: ## Rebuild evidence/references.bib (network)
	$(PY) tools/build_bibtex.py --out evidence/references.bib

paper: ## Build the single-file paper in dist/paper.md
	$(PY) tools/build_paper.py --out dist/paper.md

demo: ## Run the CLI examples from the README
	PYTHONPATH=src $(PY) -m love_translation cosine-demo
	PYTHONPATH=src $(PY) -m love_translation trust --slope 10 --midpoint 0.3
	PYTHONPATH=src $(PY) -m love_translation trust --slope 4.5 --midpoint 0.5
	PYTHONPATH=src $(PY) -m love_translation lag --drift 0.1 --learning-rate 0.2

clean: ## Remove build artefacts
	rm -rf dist build src/*.egg-info
	find . -name __pycache__ -type d -prune -exec rm -rf {} +
