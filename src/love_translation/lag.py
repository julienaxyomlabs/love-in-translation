"""Developmental lag in a giver's model of a changing need (paper §8.9).

The giver's model of a need updates by error correction

    model[t+1] = model[t] + lam * (need[t] - model[t]),   0 < lam <= 1

with ``lam`` increasing in contact and disclosure. If the need drifts at rate ``r`` per
step, the tracking error obeys e[t+1] = (1 - lam) * e[t] + r, whose steady state is

    e* = r / lam

so the lag grows with the speed of developmental change and shrinks with contact and
disclosure. Status: original hypothesis of the paper; no study has estimated ``lam``.
"""

from __future__ import annotations

from typing import List, Sequence


def _check_rate(lam: float) -> None:
    if not 0.0 < lam <= 1.0:
        raise ValueError("learning rate must be in (0, 1]")


def steady_state_lag(drift: float, lam: float) -> float:
    _check_rate(lam)
    return drift / lam


def simulate_error(drift: float, lam: float, steps: int, initial_error: float = 0.0) -> List[float]:
    _check_rate(lam)
    errors = [initial_error]
    e = initial_error
    for _ in range(steps):
        e = (1.0 - lam) * e + drift
        errors.append(e)
    return errors


def track(need_path: Sequence[float], lam: float, initial_model: float) -> List[float]:
    """The giver's model of the need, step by step, for an arbitrary need trajectory."""
    _check_rate(lam)
    model = [initial_model]
    current = initial_model
    for need in need_path[:-1]:
        current = current + lam * (need - current)
        model.append(current)
    return model
