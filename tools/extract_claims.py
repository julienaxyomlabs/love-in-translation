#!/usr/bin/env python3
"""Extract every graded claim in the paper into a JSON Lines evidence ledger.

A claim is either
  * a span of prose (paragraph or list item) ending in an evidence tag such as
    ``[Established]`` or ``[Our hypothesis, built on Moderate/mixed evidence]``, or
  * a table row whose "Tag", "Overall grade" or "Status" column names a grade.

Each record carries the chapter, the nearest heading, the normalised grade, the raw tag,
the claim text (Markdown stripped) and every DOI cited in the span.

Usage:
    python3 tools/extract_claims.py --write          # (re)generate evidence/claims.jsonl
    python3 tools/extract_claims.py --check          # exit 1 if the ledger is stale
    python3 tools/extract_claims.py --stats          # grade counts
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Dict, Iterator, List, Optional, Tuple

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"
LEDGER = ROOT / "evidence" / "claims.jsonl"

KEYWORDS = ("Established", "Moderate", "Preliminary", "Theoretical", "Our hypothesis", "Assumption")
GRADE = {
    "Established": "established",
    "Moderate": "moderate",
    "Preliminary": "preliminary",
    "Theoretical": "theoretical",
    "Our hypothesis": "hypothesis",
    "Assumption": "assumption",
}
TAG_RE = re.compile(r"\[(Established|Moderate|Preliminary|Theoretical|Our hypothesis|Assumption)([^\[\]]*)\]")
KEYWORD_RE = re.compile(r"\b(Established|Moderate|Preliminary|Theoretical|Our hypothesis|Assumption)\b")
DOI_RE = re.compile(r"10\.\d{4,9}/[^\s\"'`<>]+")
GRADE_COLUMNS = {"tag", "overall grade", "status"}
SUMMARY_SECTION = "Model at a glance"


def clean_doi(doi: str) -> str:
    doi = doi.rstrip(".,;:*_")
    for opening, closing in (("(", ")"), ("[", "]")):
        while doi.endswith(closing) and doi.count(opening) < doi.count(closing):
            doi = doi[:-1].rstrip(".,;:*_")
    return doi


def plain(text: str) -> str:
    """Strip Markdown links, emphasis and math delimiters, keeping readable text."""
    out, i, n = [], 0, len(text)
    while i < n:
        if text[i] == "[":
            close = text.find("](", i)
            if close != -1:
                depth, k = 1, close + 2
                while k < n and depth:
                    depth += {"(": 1, ")": -1}.get(text[k], 0)
                    k += 1
                if depth == 0:
                    out.append(text[i + 1:close])
                    i = k
                    continue
        out.append(text[i])
        i += 1
    s = "".join(out)
    s = re.sub(r"\$`(.+?)`\$", r"\1", s)
    s = s.replace("**", "").replace("`", "")
    s = re.sub(r"(?<!\w)\*(?=\S)(.+?)(?<=\S)\*(?!\w)", r"\1", s)
    return re.sub(r"\s+", " ", s).strip(" -|")


def dois_in(text: str) -> List[str]:
    seen: List[str] = []
    for match in DOI_RE.findall(text):
        doi = clean_doi(match)
        if doi not in seen:
            seen.append(doi)
    return seen


def split_cells(row: str) -> List[str]:
    row = row.strip()
    row = row[1:] if row.startswith("|") else row
    row = row[:-1] if row.endswith("|") else row
    return [c.strip() for c in row.split("|")]


def blocks(path: Path) -> Iterator[Tuple[str, str, Optional[List[str]]]]:
    """Yield (heading, text, header_cells_or_None) for prose blocks and table rows."""
    heading = ""
    in_code = False
    skipping = False  # the "Model at a glance" summary restates claims graded elsewhere
    header: Optional[List[str]] = None
    para: List[str] = []

    def flush() -> Iterator[Tuple[str, str, Optional[List[str]]]]:
        if para:
            yield heading, " ".join(para), None
            para.clear()

    for raw in path.read_text(encoding="utf-8").split("\n"):
        line = raw.rstrip()
        if line.startswith("```"):
            yield from flush()
            in_code = not in_code
            continue
        if in_code or line.startswith("**Navigation:**"):
            continue
        if line.startswith("#"):
            yield from flush()
            heading = plain(line.lstrip("#").strip())
            header = None
            if len(line) - len(line.lstrip("#")) <= 2:
                skipping = heading == SUMMARY_SECTION
            continue
        if skipping:
            continue
        if line.startswith("|"):
            yield from flush()
            cells = split_cells(line)
            if header is None:
                header = cells
            elif not all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
                yield heading, line, header
            continue
        header = None
        if not line.strip() or line.strip() == "---":
            yield from flush()
            continue
        if re.match(r"^(- |\d+\. )", line):
            yield from flush()
            para.append(re.sub(r"^(- |\d+\. )", "", line))
            yield from flush()
            continue
        para.append(line.strip())
    yield from flush()


def records_for(path: Path) -> Iterator[Dict[str, object]]:
    chapter = path.stem
    for heading, text, header in blocks(path):
        if header is not None:
            cells = split_cells(text)
            names = [plain(h).lower() for h in header]
            if names == ["tag", "meaning"]:  # the legend defines the grades; it makes no claims
                continue
            grade_idx = next((i for i, h in enumerate(names) if h in GRADE_COLUMNS), None)
            if grade_idx is not None and grade_idx < len(cells):
                found = KEYWORD_RE.search(cells[grade_idx])
                if found:
                    body = " | ".join(plain(c) for i, c in enumerate(cells) if i != grade_idx)
                    yield {
                        "chapter": chapter,
                        "heading": heading,
                        "grade": GRADE[found.group(1)],
                        "tag": plain(cells[grade_idx]),
                        "text": body,
                        "dois": dois_in(text),
                        "kind": "table-row",
                    }
                continue
        start = 0
        for match in TAG_RE.finditer(text):
            span = text[start:match.start()]
            start = match.end()
            claim = plain(span)
            if not claim:
                continue
            yield {
                "chapter": chapter,
                "heading": heading,
                "grade": GRADE[match.group(1)],
                "tag": (match.group(1) + match.group(2)).strip(),
                "text": claim,
                "dois": dois_in(span),
                "kind": "prose",
            }


def build() -> List[Dict[str, object]]:
    chapters = sorted(p for p in PAPER.glob("[0-9]*.md") if not p.name.startswith("20-"))
    rows: List[Dict[str, object]] = []
    for path in chapters:
        for n, rec in enumerate(records_for(path), start=1):
            rows.append({"id": f"{path.stem.split('-')[0]}.{n:03d}", **rec})
    return rows


def serialise(rows: List[Dict[str, object]]) -> str:
    return "".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in rows)


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--stats", action="store_true")
    args = parser.parse_args(argv)
    rows = build()
    text = serialise(rows)
    if args.write:
        LEDGER.parent.mkdir(parents=True, exist_ok=True)
        LEDGER.write_text(text, encoding="utf-8")
        print(f"wrote {len(rows)} claims to {LEDGER.relative_to(ROOT)}")
        return 0
    if args.check:
        current = LEDGER.read_text(encoding="utf-8") if LEDGER.exists() else ""
        if current != text:
            print("evidence/claims.jsonl is stale: run `make claims`", file=sys.stderr)
            return 1
        print(f"claims ledger up to date ({len(rows)} claims)")
        return 0
    counts = Counter(str(r["grade"]) for r in rows)
    width = max(len(k) for k in counts)
    for grade in ("established", "moderate", "preliminary", "theoretical", "hypothesis", "assumption"):
        print(f"{grade:<{width}}  {counts.get(grade, 0):4d}")
    print(f"{'total':<{width}}  {len(rows):4d}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
