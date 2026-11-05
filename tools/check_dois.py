#!/usr/bin/env python3
"""Resolve every DOI cited in the paper against Crossref (fallback: the doi.org handle API).

Checks that each DOI exists and that its registered title and authors match the text it is
cited with. Needs network access.

Usage:
    python3 tools/check_dois.py                                   # report problems only
    python3 tools/check_dois.py --write evidence/doi-verification.csv
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import socket
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Dict, List, Optional

ROOT = Path(__file__).resolve().parents[1]
DOI_RE = re.compile(r"10\.\d{4,9}/[^\s\"'`<>]+")
USER_AGENT = "love-in-translation-citation-check/0.1 (+https://github.com/)"
STOP = set("a an the of and in on for to with from by at as is are be or vs versus its their his her our".split())


def clean(doi: str) -> str:
    doi = doi.rstrip(".,;:*_")
    for opening, closing in (("(", ")"), ("[", "]")):
        while doi.endswith(closing) and doi.count(opening) < doi.count(closing):
            doi = doi[:-1].rstrip(".,;:*_")
    return doi


def fetch_json(url: str, attempts: int = 3) -> "tuple[int, Optional[dict]]":
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    for attempt in range(attempts):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return response.status, json.loads(response.read().decode("utf-8", "replace"))
        except urllib.error.HTTPError as err:
            return err.code, None
        # socket.timeout only became an alias of TimeoutError in Python 3.10
        except (urllib.error.URLError, TimeoutError, socket.timeout, ValueError):
            if attempt + 1 < attempts:
                time.sleep(2 * (attempt + 1))
    return -1, None


def resolve(doi: str) -> Dict[str, str]:
    status, payload = fetch_json("https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="/"))
    if status == 200 and payload and "message" in payload:
        msg = payload["message"]
        authors = [a.get("family", "") for a in msg.get("author", []) if a.get("family")]
        # Registries sometimes swap family and given names (common for East Asian names),
        # so accept either for the first three authors when matching the reference text.
        names = [n for a in msg.get("author", [])[:3] for n in (a.get("family", ""), a.get("given", "")) if n]
        year = ""
        for key in ("published-print", "published-online", "issued"):
            parts = (msg.get(key) or {}).get("date-parts") or []
            if parts and parts[0] and parts[0][0]:
                year = str(parts[0][0])
                break
        return {"status": "resolved", "source": "crossref", "title": " ".join(msg.get("title") or []),
                "first_author": authors[0] if authors else "", "year": year, "names": "|".join(names)}
    status2, payload2 = fetch_json("https://doi.org/api/handles/" + urllib.parse.quote(doi, safe="/"))
    if status2 == 200 and payload2 and payload2.get("responseCode") == 1:
        return {"status": "resolved", "source": "doi.org", "title": "", "first_author": "", "year": "", "names": ""}
    return {"status": "unresolved", "source": "", "title": "", "first_author": "", "year": "", "names": ""}


def words(text: str) -> List[str]:
    return [w for w in re.findall(r"[a-z0-9]+", text.lower()) if w not in STOP and len(w) > 2]


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--write", metavar="CSV", help="write the verification table to this path")
    parser.add_argument("--delay", type=float, default=0.15, help="seconds between requests")
    args = parser.parse_args(argv)

    cited: Dict[str, List[str]] = {}
    context: Dict[str, str] = {}
    for path in sorted((ROOT / "paper").glob("*.md")):
        for line in path.read_text(encoding="utf-8").split("\n"):
            for match in DOI_RE.findall(line):
                doi = clean(match)
                cited.setdefault(doi, [])
                if path.stem not in cited[doi]:
                    cited[doi].append(path.stem)
                if path.name.startswith("20-"):
                    context[doi] = line

    rows, problems = [], 0
    for doi in sorted(cited, key=str.lower):
        result = resolve(doi)
        names = [n.lower() for n in result.pop("names").split("|") if n]
        time.sleep(args.delay)
        flag = ""
        if result["status"] != "resolved":
            flag = "unresolved"
        elif result["title"] and doi in context:
            title_words = words(result["title"])
            line = context[doi].lower()
            overlap = sum(w in set(words(line)) for w in title_words) / max(len(title_words), 1)
            if overlap < 0.5 or (names and not any(n in line for n in names)):
                flag = "metadata-mismatch"
        if flag:
            problems += 1
            print(f"[{flag}] {doi}  {result['first_author']} {result['year']} {result['title'][:90]}")
        rows.append({"doi": doi, **result, "flag": flag, "cited_in": " ".join(cited[doi])})

    if args.write:
        out = ROOT / args.write
        out.parent.mkdir(parents=True, exist_ok=True)
        with out.open("w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=["doi", "status", "source", "first_author", "year", "title", "flag", "cited_in"])
            writer.writeheader()
            writer.writerows(rows)
        print(f"wrote {len(rows)} rows to {args.write}")
    print(f"{len(rows)} unique DOIs, {problems} flagged")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
