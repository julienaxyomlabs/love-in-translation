"""Trust as a latent state with a trust-dependent reading of ambiguous acts (paper §8.9).

    dT/dt = eta * (p(T) - T),   p: [0, 1] -> (0, 1) continuous and increasing

* At least one equilibrium exists because p(0) > 0 and p(1) < 1.
* An equilibrium T* is stable iff p'(T*) < 1; eta only rescales time.
* Several stable equilibria (bistability, hysteresis) require p'(T) > 1 somewhere, but
  that condition is NOT sufficient: the steep region must straddle the diagonal.

Status: theoretical. No study has shown bistability, hysteresis or critical slowing down
in relationship trust or satisfaction.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, List

from .linalg import logistic

Reading = Callable[[float], float]


@dataclass(frozen=True)
class Equilibrium:
    level: float
    stable: bool


def logistic_reading(slope: float, midpoint: float) -> Reading:
    """p(T) = logistic(slope * (T - midpoint)); its maximum slope is slope / 4."""

    def p(t: float) -> float:
        return logistic(slope * (t - midpoint))

    return p


def derivative(p: Reading, t: float, h: float = 1e-6) -> float:
    lo, hi = max(0.0, t - h), min(1.0, t + h)
    return (p(hi) - p(lo)) / (hi - lo)


def max_slope(p: Reading, grid: int = 20001) -> float:
    return max(derivative(p, i / (grid - 1)) for i in range(grid))


def _bisect(g: Callable[[float], float], lo: float, hi: float, tol: float) -> float:
    g_lo = g(lo)
    while hi - lo > tol:
        mid = 0.5 * (lo + hi)
        g_mid = g(mid)
        if g_mid == 0.0:
            return mid
        if (g_mid > 0.0) == (g_lo > 0.0):
            lo, g_lo = mid, g_mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def equilibria(p: Reading, grid: int = 20001, tol: float = 1e-12) -> List[Equilibrium]:
    """All fixed points of p on [0, 1], located by sign changes of p(T) - T."""

    def g(t: float) -> float:
        return p(t) - t

    points = [i / (grid - 1) for i in range(grid)]
    values = [g(t) for t in points]
    roots: List[float] = []
    for i, value in enumerate(values):
        if value == 0.0:
            roots.append(points[i])
        elif i + 1 < len(values) and values[i + 1] != 0.0 and (value > 0.0) != (values[i + 1] > 0.0):
            roots.append(_bisect(g, points[i], points[i + 1], tol))
    return [Equilibrium(level=r, stable=derivative(p, r) < 1.0) for r in roots]


def is_bistable(p: Reading) -> bool:
    return sum(1 for e in equilibria(p) if e.stable) >= 2


def simulate(p: Reading, start: float, eta: float, steps: int) -> List[float]:
    """Euler steps of the trust dynamics, clipped to [0, 1]."""
    if not 0.0 < eta <= 1.0:
        raise ValueError("eta must be in (0, 1] for a stable Euler scheme")
    path = [start]
    t = start
    for _ in range(steps):
        t = min(1.0, max(0.0, t + eta * (p(t) - t)))
        path.append(t)
    return path
