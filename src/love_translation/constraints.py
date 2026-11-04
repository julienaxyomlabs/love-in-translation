"""Constraints that are not weights (paper §8.10).

Safety as a lexicographic gate: states are compared on safety first, and on care only
among equally safe states. Lexicographic orders cannot in general be represented by any
real-valued utility (Fishburn 1974), so no finite safety weight in a weighted sum
reproduces the gate: for every weight there is an unsafe-but-caring state the weighted
sum prefers to a safe one.

Compatibility as feasibility: let F be the set of joint life patterns that meet both
people's essential requirements without pushing either below a sustainability threshold.
An unmet need is a gap a reallocation within F could close; incompatibility is F = {};
unsustainable need is F = {} because one person's requirements can be met only at the
other's unsustainable cost. Understanding helps partners *find* a point in F; it cannot
*create* one.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Sequence, Tuple


@dataclass(frozen=True)
class RelationshipState:
    safety: float
    care: float


def lexicographic_prefers(x: RelationshipState, y: RelationshipState) -> bool:
    if x.safety != y.safety:
        return x.safety > y.safety
    return x.care > y.care


def weighted_prefers(x: RelationshipState, y: RelationshipState, safety_weight: float) -> bool:
    return safety_weight * x.safety + x.care > safety_weight * y.safety + y.care


def weighted_counterexample(safety_weight: float) -> Tuple[RelationshipState, RelationshipState]:
    """An unsafe state the weighted sum ranks above a safe one, for any finite weight."""
    if safety_weight < 0:
        raise ValueError("safety weight must be non-negative")
    unsafe = RelationshipState(safety=0.0, care=safety_weight + 1.0)
    safe = RelationshipState(safety=1.0, care=0.0)
    return unsafe, safe


@dataclass(frozen=True)
class JointPattern:
    """One way two lives could be arranged, scored against each person's requirements."""

    name: str
    meets_a: bool
    meets_b: bool
    wellbeing_a: float
    wellbeing_b: float


@dataclass(frozen=True)
class Feasibility:
    status: str  # "compatible" | "unsustainable" | "incompatible"
    feasible: Tuple[str, ...]


def classify(patterns: Sequence[JointPattern], threshold_a: float, threshold_b: float) -> Feasibility:
    feasible: List[str] = [
        p.name
        for p in patterns
        if p.meets_a and p.meets_b and p.wellbeing_a >= threshold_a and p.wellbeing_b >= threshold_b
    ]
    if feasible:
        return Feasibility("compatible", tuple(feasible))
    if any(p.meets_a and p.meets_b for p in patterns):
        return Feasibility("unsustainable", ())
    return Feasibility("incompatible", ())
