#!/usr/bin/env python3
"""Concatenate the chapters in paper/ into one Markdown file (default: dist/paper.md).

Chapter headings are demoted one level under the title, navigation lines are dropped and
links between chapters are rewritten to in-document anchors.

Usage: python3 tools/build_paper.py --out dist/paper.md
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Dict, List, Optional

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"


def github_slug(heading: str) -> str:
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", heading).strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"\s", "-", text)


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--out", default="dist/paper.md")
    args = parser.parse_args(argv)

    chapters = sorted(PAPER.glob("[0-9]*.md"))
    anchors: Dict[str, str] = {}
    for path in chapters:
        first = next(line for line in path.read_text(encoding="utf-8").split("\n") if line.startswith("# "))
        anchors[path.name] = "#" + github_slug(first[2:])

    out_lines: List[str] = []
    for index, path in enumerate(chapters):
        lines = path.read_text(encoding="utf-8").rstrip("\n").split("\n")
        while lines and (lines[-1].startswith("**Navigation:**") or lines[-1].strip() in ("", "---")):
            lines.pop()
        for line in lines:
            if index > 0 and line.startswith("#"):
                line = "#" + line
            for name, anchor in anchors.items():
                line = line.replace(f"]({name})", f"]({anchor})")
            line = line.replace("](figures/", "](../paper/figures/")
            out_lines.append(line)
        out_lines.append("")

    out = ROOT / args.out
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(out_lines).rstrip("\n") + "\n", encoding="utf-8")
    words = sum(len(line.split()) for line in out_lines)
    print(f"wrote {args.out}: {len(chapters)} chapters, {words} words")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
