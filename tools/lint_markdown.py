#!/usr/bin/env python3
"""Offline checks for the repository's Markdown.

* every relative link and image resolves to a file in the repository;
* code fences are balanced;
* in the paper: inline math uses GitHub's literal $`...`$ form, no stray `$` remains,
  no raw HTML is used, and every chapter ends with a navigation line.

Usage: python3 tools/lint_markdown.py   (exit status 1 on any problem)
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import List

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+(?:\([^)\s]*\)[^)\s]*)*)\)")
INLINE_MATH_RE = re.compile(r"\$`.+?`\$")
HTML_TAG_RE = re.compile(r"</?[A-Za-z][A-Za-z0-9-]*(\s[^<>]*)?/?>")
SKIP_DIRS = {".git", "dist", "node_modules", ".venv", "venv"}


def markdown_files() -> List[Path]:
    return sorted(
        p for p in ROOT.rglob("*.md") if not any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts)
    )


def lint_file(path: Path) -> List[str]:
    problems: List[str] = []
    rel = path.relative_to(ROOT)
    in_paper = rel.parts[0] == "paper" and rel.name[0].isdigit()
    in_code = False
    fences = 0
    lines = path.read_text(encoding="utf-8").split("\n")
    for number, line in enumerate(lines, start=1):
        where = f"{rel}:{number}"
        if line.lstrip().startswith("```"):
            fences += 1
            in_code = not in_code
            continue
        if in_code:
            continue
        for target in LINK_RE.findall(line):
            if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
                continue
            file_part = target.split("#", 1)[0]
            if file_part and not (path.parent / file_part).resolve().exists():
                problems.append(f"{where}: broken relative link -> {target}")
        if in_paper:
            if line.count("$`") != line.count("`$"):
                problems.append(f"{where}: unbalanced $`...`$ math")
            outside = INLINE_MATH_RE.sub("", line).replace("\\$", "")
            if "$" in outside:
                problems.append(f"{where}: stray '$' outside $`...`$ math")
            if HTML_TAG_RE.search(INLINE_MATH_RE.sub("", line)):
                problems.append(f"{where}: raw HTML is not used in the paper")
    if fences % 2:
        problems.append(f"{rel}: unbalanced code fences")
    if in_paper and not any(line.startswith("**Navigation:**") for line in lines[-4:]):
        problems.append(f"{rel}: missing navigation line at the end")
    return problems


def lint() -> List[str]:
    problems: List[str] = []
    for path in markdown_files():
        problems.extend(lint_file(path))
    return problems


def main() -> int:
    problems = lint()
    for p in problems:
        print(p)
    count = len(markdown_files())
    if problems:
        print(f"\n{len(problems)} problem(s) in {count} Markdown files", file=sys.stderr)
        return 1
    print(f"ok: {count} Markdown files, links resolve, math and fences balanced")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
