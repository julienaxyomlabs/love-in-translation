"""Polynomial regression with response surface analysis (paper §8.7).

Model the receiver's outcome ``Y`` on received supply ``S`` and need ``N``::

    Y = b0 + b1*S + b2*N + b3*S^2 + b4*S*N + b5*N^2 + e

Preconditions (Edwards 2007; Schönbrodt, Humberg & Nestler 2018):
* S and N must be *commensurable*: the same construct on the same metric, with
  measurement invariance where groups are compared.
* Both are centred at the same meaningful zero, conventionally the scale midpoint.
  The line S = -N represents misfit only under that common centring.

Surface quantities, all defined relative to the centring point (0, 0):

    a1 = b1 + b2        slope along the line of congruence (S = N) AT the point (0, 0);
                        along that line the slope at level t is a1 + 2*a2*t
    a2 = b3 + b4 + b5   curvature along the line of congruence
    a3 = b1 - b2        slope along the line of incongruence (S = -N) at (0, 0); with a4 != 0
                        it locates the peak or trough of that line away from (0, 0)
    a4 = b3 - b4 + b5   curvature along the line of incongruence
    a5 = b3 - b5        zero when the ridge (or trough) can lie on the line of congruence

a1 is not "the effect of the amount of care" everywhere, and a4 alone is not a mismatch
penalty. A congruence (similarity) effect requires a joint pattern: a4 < 0, a3 = 0 and the
first principal axis on the line of congruence (p10 = 0, p11 = 1; equivalently a5 = 0 with
a3 = 0), established with confidence intervals and model comparison, not point estimates.
A flat ridge (a1 = a2 = 0) makes the pattern the prototypical one; a1 or a2 != 0 means
outcomes also depend on the level at which supply and need agree.
"""

from __future__ import annotations

import math
from typing import Dict, List, Optional, Sequence, Tuple

from .linalg import ols

TERMS = ("b0", "b1", "b2", "b3", "b4", "b5")


def design_row(supply: float, need: float) -> List[float]:
    return [1.0, supply, need, supply * supply, supply * need, need * need]


def fit_surface(
    supply: Sequence[float], need: Sequence[float], outcome: Sequence[float]
) -> Dict[str, float]:
    """Least-squares polynomial coefficients b0..b5 (centre S and N first)."""
    if not (len(supply) == len(need) == len(outcome)):
        raise ValueError("supply, need and outcome must have equal length")
    rows = [design_row(s, n) for s, n in zip(supply, need)]
    return dict(zip(TERMS, ols(rows, outcome)))


def surface_parameters(b: Dict[str, float]) -> Dict[str, float]:
    """Slopes and curvatures along the lines of congruence and incongruence, plus a5."""
    return {
        "a1": b["b1"] + b["b2"],
        "a2": b["b3"] + b["b4"] + b["b5"],
        "a3": b["b1"] - b["b2"],
        "a4": b["b3"] - b["b4"] + b["b5"],
        "a5": b["b3"] - b["b5"],
    }


def stationary_point(b: Dict[str, float], tol: float = 1e-12) -> Optional[Tuple[float, float]]:
    """Point where the surface is flat (Edwards 2007, eqs. 11–12); None for a ridge or trough line."""
    den = 4.0 * b["b3"] * b["b5"] - b["b4"] ** 2
    if abs(den) < tol:
        return None
    x0 = (b["b2"] * b["b4"] - 2.0 * b["b1"] * b["b5"]) / den
    y0 = (b["b1"] * b["b4"] - 2.0 * b["b2"] * b["b3"]) / den
    return x0, y0


def principal_axes(b: Dict[str, float], tol: float = 1e-12) -> Dict[str, Optional[float]]:
    """Slopes and intercepts of the principal axes (Edwards 2007, eqs. 13–18).

    The first axis is the line of least downward curvature on a concave surface (the
    ridge). Slopes are undefined when b4 = 0 and intercepts when there is no unique
    stationary point; those entries are None.
    """
    out: Dict[str, Optional[float]] = {"p10": None, "p11": None, "p20": None, "p21": None}
    if abs(b["b4"]) < tol:
        return out
    root = math.sqrt((b["b3"] - b["b5"]) ** 2 + b["b4"] ** 2)
    out["p11"] = (b["b5"] - b["b3"] + root) / b["b4"]
    out["p21"] = (b["b5"] - b["b3"] - root) / b["b4"]
    point = stationary_point(b, tol)
    if point is not None:
        x0, y0 = point
        out["p10"] = y0 - out["p11"] * x0
        out["p20"] = y0 - out["p21"] * x0
    return out


def congruence_screen(b: Dict[str, float], tol: float = 1e-6) -> Dict[str, bool]:
    """Check point estimates against the joint congruence pattern.

    A screen, not a test: real claims need confidence intervals (e.g. bootstrap) for
    a3, a4, a5/p10/p11, comparison with constrained models such as the squared-difference
    model (b1 = b2 = 0, b3 = b5, b4 = -2*b3), and data covering incongruent combinations.
    """
    a = surface_parameters(b)
    pattern = {
        "a4_negative": a["a4"] < 0.0,
        "a3_zero": abs(a["a3"]) <= tol,
        "ridge_on_congruence_line": abs(a["a5"]) <= tol,
    }
    pattern["congruence_pattern"] = all(pattern.values())
    pattern["flat_ridge"] = abs(a["a1"]) <= tol and abs(a["a2"]) <= tol
    return pattern


def asymmetric_loss(supply: float, need: float, deficit_weight: float, excess_weight: float) -> float:
    """Piecewise-linear loss with separate costs for deficiency and excess.

    The weights are symbolic inputs to be estimated (e.g. with cubic RSA or spline
    regression), never defaults: the evidence on whether excess or deficit hurts more is
    mixed and timescale-dependent (paper §8.7).
    """
    if deficit_weight < 0 or excess_weight < 0:
        raise ValueError("loss weights must be non-negative")
    return -deficit_weight * max(need - supply, 0.0) - excess_weight * max(supply - need, 0.0)
