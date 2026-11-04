"""Command-line interface: ``love-translation <command>`` or ``python -m love_translation``.

Commands
--------
trust        equilibria of the trust dynamics for a logistic reading function
lag          steady-state developmental lag for a drift rate and a learning rate
cosine-demo  the paper's demonstration that cosine ignores amount and depends on coding
infer        posterior regard inferred from an act (or its absence) at a believed cost
claims       query the machine-readable evidence ledger (evidence/claims.jsonl)
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Optional, Sequence

from . import __version__, inference, lag, similarity, trust

PAPER_E = (5.0, 3.0, 1.0, 2.0, 4.0)
PAPER_N = (4.0, 4.0, 2.0, 1.0, 5.0)


def _cmd_trust(args: argparse.Namespace) -> int:
    p = trust.logistic_reading(args.slope, args.midpoint)
    eqs = trust.equilibria(p)
    print(f"reading function: logistic(slope={args.slope:g}, midpoint={args.midpoint:g})")
    print(f"max p'(T) = {trust.max_slope(p):.4f}   (bistability needs > 1; not sufficient)")
    for e in eqs:
        print(f"  equilibrium T* = {e.level:.4f}   {'stable' if e.stable else 'unstable'}")
    print(f"bistable: {'yes' if trust.is_bistable(p) else 'no'}")
    return 0


def _cmd_lag(args: argparse.Namespace) -> int:
    star = lag.steady_state_lag(args.drift, args.learning_rate)
    path = lag.simulate_error(args.drift, args.learning_rate, args.steps)
    print(f"steady-state lag e* = r / lambda = {args.drift:g} / {args.learning_rate:g} = {star:.4f}")
    print(f"simulated error after {args.steps} steps: {path[-1]:.4f}")
    return 0


def _cmd_cosine_demo(_: argparse.Namespace) -> int:
    print("E = (5,3,1,2,4) expressed care, N = (4,4,2,1,5) needs, same profiles three codings")
    print(f"{'coding':>10}  {'cosine':>7}  {'profile r':>9}")
    for label, offset in (("1..5", 0.0), ("0..4", -1.0), ("-2..+2", -3.0)):
        e = similarity.shift(PAPER_E, offset)
        n = similarity.shift(PAPER_N, offset)
        print(f"{label:>10}  {similarity.cosine(e, n):7.3f}  {similarity.pearson(e, n):9.3f}")
    quarter = [v / 4.0 for v in PAPER_N]
    print(f"giving a quarter of what is needed, in proportion: cosine = {similarity.cosine(quarter, PAPER_N):.3f}")
    return 0


def _cmd_infer(args: argparse.Namespace) -> int:
    grid = [i / 20.0 for i in range(21)]
    acted = not args.absent
    m = inference.posterior_mean(acted, args.believed_cost, args.benefit, args.precision, grid)
    what = "absence" if args.absent else "a caring act"
    print(f"after observing {what} at believed cost {args.believed_cost:g}:")
    print(f"  posterior mean weight on the receiver's welfare = {m:.4f} (uniform prior on [0, 1])")
    return 0


def _find_ledger(explicit: Optional[str]) -> Path:
    if explicit:
        return Path(explicit)
    here = Path.cwd()
    for folder in (here, *here.parents):
        candidate = folder / "evidence" / "claims.jsonl"
        if candidate.exists():
            return candidate
    raise SystemExit("evidence/claims.jsonl not found; pass --file")


def _cmd_claims(args: argparse.Namespace) -> int:
    path = _find_ledger(args.file)
    shown = 0
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            row = json.loads(line)
            if args.grade and row["grade"] != args.grade:
                continue
            if args.chapter and not row["chapter"].startswith(args.chapter):
                continue
            if args.doi and args.doi not in row["dois"]:
                continue
            shown += 1
            if not args.count:
                print(f"[{row['grade']}] {row['chapter']} :: {row['text'][:args.width]}")
    if args.count:
        print(shown)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="love-translation", description=__doc__.split("\n")[0])
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    t = sub.add_parser("trust", help="equilibria of the trust dynamics")
    t.add_argument("--slope", type=float, required=True)
    t.add_argument("--midpoint", type=float, required=True)
    t.set_defaults(func=_cmd_trust)

    g = sub.add_parser("lag", help="developmental lag e* = r / lambda")
    g.add_argument("--drift", type=float, required=True)
    g.add_argument("--learning-rate", type=float, required=True)
    g.add_argument("--steps", type=int, default=200)
    g.set_defaults(func=_cmd_lag)

    c = sub.add_parser("cosine-demo", help="why cosine cannot measure fit")
    c.set_defaults(func=_cmd_cosine_demo)

    i = sub.add_parser("infer", help="regard inferred from a costly act")
    i.add_argument("--believed-cost", type=float, required=True)
    i.add_argument("--benefit", type=float, default=1.0)
    i.add_argument("--precision", type=float, default=4.0)
    i.add_argument("--absent", action="store_true", help="observe absence instead of the act")
    i.set_defaults(func=_cmd_infer)

    q = sub.add_parser("claims", help="query the evidence ledger")
    q.add_argument("--grade", choices=["established", "moderate", "preliminary", "theoretical", "hypothesis", "assumption"])
    q.add_argument("--chapter", help="chapter prefix, e.g. 08")
    q.add_argument("--doi", help="only claims citing this DOI")
    q.add_argument("--count", action="store_true", help="print the number of matches only")
    q.add_argument("--width", type=int, default=160)
    q.add_argument("--file", help="path to claims.jsonl")
    q.set_defaults(func=_cmd_claims)
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_parser().parse_args(list(argv) if argv is not None else None)
    return int(args.func(args))


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
