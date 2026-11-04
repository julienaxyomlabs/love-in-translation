"""Level versus mismatch: polynomial regression with response surface analysis (paper §8.7).

Model the receiver's outcome ``Y`` on received supply ``S`` and need ``N`` measured on
one metric::

    Y = b0 + b1*S + b2*N + b3*S^2 + b4*S*N + b5*N^2 + e

Surface quantities (Shanock et al. 2010; Humberg, Nestler & Back 2019):

    a1 = b1 + b2        slope along the line of congruence (level or "amount")
    a2 = b3 + b4 + b5   curvature along that line
    a3 = b1 - b2        directional misfit (over- vs under-supply)
    a4 = b3 - b4 + b5   curvature across the line of incongruence ("mismatch hurts")

"Translation-as-fit" predicts a substantial negative a4. "Amount" predicts a dominant a1
with incongruence terms near zero. Difference scores and cosine indices cannot tell the
two apart; this surface can.
"""

from __future__ import annotations

from typing import Dict, List, Sequence

from .linalg import ols

TERMS = ("b0", "b1", "b2", "b3", "b4", "b5")


def design_row(supply: float, need: float) -> List[float]:
    return [1.0, supply, need, supply * supply, supply * need, need * need]


def fit_surface(
    supply: Sequence[float], need: Sequence[float], outcome: Sequence[float]
) -> Dict[str, float]:
    """Least-squares polynomial coefficients b0..b5."""
    if not (len(supply) == len(need) == len(outcome)):
        raise ValueError("supply, need and outcome must have equal length")
    rows = [design_row(s, n) for s, n in zip(supply, need)]
    return dict(zip(TERMS, ols(rows, outcome)))


def surface_parameters(b: Dict[str, float]) -> Dict[str, float]:
    """Convert polynomial coefficients into the four response-surface quantities."""
    return {
        "a1": b["b1"] + b["b2"],
        "a2": b["b3"] + b["b4"] + b["b5"],
        "a3": b["b1"] - b["b2"],
        "a4": b["b3"] - b["b4"] + b["b5"],
    }


def asymmetric_loss(supply: float, need: float, deficit_weight: float, excess_weight: float) -> float:
    """Piecewise-linear loss with separate costs for deficiency and excess.

    The weights are symbolic inputs to be estimated (e.g. with cubic RSA or spline
    regression), never defaults: the evidence on whether excess or deficit hurts more is
    mixed and timescale-dependent (paper §8.7).
    """
    if deficit_weight < 0 or excess_weight < 0:
        raise ValueError("loss weights must be non-negative")
    return -deficit_weight * max(need - supply, 0.0) - excess_weight * max(supply - need, 0.0)
