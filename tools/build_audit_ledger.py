#!/usr/bin/env python3
"""Collect the claim-audit records into one CSV ledger.

Each audit note (evidence/notes/08-11) ends with a ```jsonl block holding one record per
audited claim. This tool gathers those records into audit/claims-audit.csv, checking that
every record has the same fields and that claim ids are unique. The notes are the source;
the CSV is generated and should not be edited by hand.

Usage:
    python3 tools/build_audit_ledger.py --write   # (re)generate audit/claims-audit.csv
    python3 tools/build_audit_ledger.py --check   # exit 1 if the ledger is stale
    python3 tools/build_audit_ledger.py --stats   # counts by verification depth and verdict
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parents[1]
NOTES = ROOT / "evidence" / "notes"
SOURCES = (
    "08-audit-transmission-support.md",
    "09-audit-perception-prediction.md",
    "10-audit-amount-direction-capacity.md",
    "11-audit-culture-provision-safety.md",
)
LEDGER = ROOT / "audit" / "claims-audit.csv"
FIELDS = (
    "claim_id",
    "short_claim",
    "source",
    "doi",
    "verification_depth",
    "sections_read",
    "design",
    "population",
    "measured",
    "key_result",
    "supports_interpretation",
    "evidence_grade",
    "paper_locations",
    "recommended_change",
    "notes",
)
BLOCK_RE = re.compile(r"^```jsonl\n(.*?)^```", re.S | re.M)
ID_RE = re.compile(r"([A-Z]+)(\d+)")


def cell(value: object) -> str:
    if isinstance(value, list):
        return "; ".join(cell(v) for v in value)
    if isinstance(value, dict):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    return "" if value is None else str(value)


def sort_key(claim_id: str) -> Tuple[str, int]:
    found = ID_RE.fullmatch(claim_id)
    return (found.group(1), int(found.group(2))) if found else (claim_id, 0)


def collect() -> List[Dict[str, object]]:
    records: List[Dict[str, object]] = []
    for name in SOURCES:
        text = (NOTES / name).read_text(encoding="utf-8")
        blocks = BLOCK_RE.findall(text)
        if len(blocks) != 1:
            raise ValueError(f"{name}: expected one jsonl block, found {len(blocks)}")
        for number, line in enumerate(blocks[0].splitlines(), start=1):
            if not line.strip():
                continue
            record = json.loads(line)
            if set(record) != set(FIELDS):
                missing = sorted(set(FIELDS) - set(record))
                extra = sorted(set(record) - set(FIELDS))
                raise ValueError(f"{name}: record {number}: missing {missing}, unexpected {extra}")
            records.append(record)
    ids = [str(r["claim_id"]) for r in records]
    duplicates = sorted(i for i, n in Counter(ids).items() if n > 1)
    if duplicates:
        raise ValueError(f"duplicate claim ids: {duplicates}")
    return sorted(records, key=lambda r: sort_key(str(r["claim_id"])))


def serialise(records: List[Dict[str, object]]) -> str:
    out = io.StringIO()
    writer = csv.writer(out, lineterminator="\n")
    writer.writerow(FIELDS)
    for record in records:
        writer.writerow([cell(record[f]) for f in FIELDS])
    return out.getvalue()


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--stats", action="store_true")
    args = parser.parse_args(argv)
    records = collect()
    text = serialise(records)
    if args.write:
        LEDGER.parent.mkdir(parents=True, exist_ok=True)
        LEDGER.write_text(text, encoding="utf-8")
        print(f"wrote {len(records)} audited claims to {LEDGER.relative_to(ROOT)}")
        return 0
    if args.check:
        current = LEDGER.read_text(encoding="utf-8") if LEDGER.exists() else ""
        if current != text:
            print("audit/claims-audit.csv is stale: run `make audit`", file=sys.stderr)
            return 1
        print(f"audit ledger up to date ({len(records)} claims)")
        return 0
    for field in ("verification_depth", "supports_interpretation"):
        counts = Counter(cell(r[field]) for r in records)
        print(field)
        for value, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
            print(f"  {n:3d}  {value}")
    print(f"total {len(records)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
