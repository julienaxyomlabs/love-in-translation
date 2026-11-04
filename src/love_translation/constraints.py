"""Constraints that are not weights (paper §8.10).

Safety is an admissibility constraint. Arrangements that fail the safety criterion are
removed before anything is compared:

    F_safe = { x in F : Safe(x) = 1 }

Outcomes are compared only within F_safe. If F_safe is empty the model reports that no
admissible arrangement exists and recommends nothing. Safe(x) is decided from safety
indicators (violence, threats, coercive control, fear), never from perceived love or care.

Two weaker formalisations are kept here to show why they fail:
* a weighted sum: for every finite safety weight there is an unsafe-but-caring state the
  sum prefers to a safe one (lexicographic preferences have no real-valued utility
  representation in general; Fishburn 1974);
* a lexicographic ranking (safety first, then care): it still ranks unsafe options, so
  when every option is unsafe it picks one instead of excluding them all.

Compatibility as feasibility: F is the set of joint life patterns that meet both people's
essential requirements without pushing either below a sustainability threshold.
Understanding helps partners *find* a point in F; it cannot *create* one.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Sequence, Tuple


@dataclass(frozen=True)
class RelationshipState:
    safety: float
    care: float


def weighted_prefers(x: RelationshipState, y: RelationshipState, safety_weight: float) -> bool:
    return safety_weight * x.safety + x.care > safety_weight * y.safety + y.care


def weighted_counterexample(safety_weight: float) -> Tuple[RelationshipState, RelationshipState]:
    """An unsafe state the weighted sum ranks above a safe one, for any finite weight."""
    if safety_weight < 0:
        raise ValueError("safety weight must be non-negative")
    unsafe = RelationshipState(safety=0.0, care=safety_weight + 1.0)
    safe = RelationshipState(safety=1.0, care=0.0)
    return unsafe, safe


def lexicographic_prefers(x: RelationshipState, y: RelationshipState) -> bool:
    """A ranking, not a gate: it orders unsafe states instead of excluding them."""
    if x.safety != y.safety:
        return x.safety > y.safety
    return x.care > y.care


@dataclass(frozen=True)
class Arrangement:
    """A candidate arrangement: whether it passes the safety criterion, and its outcome score."""

    name: str
    safe: bool
    outcome: float


def admissible(options: Sequence[Arrangement]) -> List[Arrangement]:
    """F_safe: the options that pass the safety criterion."""
    return [o for o in options if o.safe]


def choose(options: Sequence[Arrangement]) -> Optional[Arrangement]:
    """Best outcome among admissible options; None when no admissible arrangement exists."""
    candidates = admissible(options)
    if not candidates:
        return None
    return max(candidates, key=lambda o: o.outcome)


@dataclass(frozen=True)
class JointPattern:
    """One way two lives could be arranged, scored against each person's requirements."""

    name: str
    meets_a: bool
    meets_b: bool
    wellbeing_a: float
    wellbeing_b: float
    safe: bool = True


@dataclass(frozen=True)
class Feasibility:
    status: str  # "compatible" | "unsafe" | "unsustainable" | "incompatible"
    feasible: Tuple[str, ...]  # names in F_safe; empty means no admissible arrangement


def classify(patterns: Sequence[JointPattern], threshold_a: float, threshold_b: float) -> Feasibility:
    """Locate F and F_safe. Any status other than "compatible" means no admissible arrangement."""
    in_f = [
        p
        for p in patterns
        if p.meets_a and p.meets_b and p.wellbeing_a >= threshold_a and p.wellbeing_b >= threshold_b
    ]
    in_f_safe = tuple(p.name for p in in_f if p.safe)
    if in_f_safe:
        return Feasibility("compatible", in_f_safe)
    if in_f:
        return Feasibility("unsafe", ())
    if any(p.meets_a and p.meets_b for p in patterns):
        return Feasibility("unsustainable", ())
    return Feasibility("incompatible", ())
