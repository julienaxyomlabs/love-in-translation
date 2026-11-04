"""Truth-and-bias decomposition of perceived care (West & Kenny 2011; paper §8.6).

    Q - mu = tau * (X - mu) + pi * (O - mu) + delta + u

Q      receiver's perceived care from the partner
X      criterion for the partner's care (partner report or observer coding)
O      receiver's own care given (the projection variable)
tau    truth force: does B track which days A gave more?
pi     projection force: does B read A's care off B's own?
delta  directional bias: a level shift ("90 versus 40" lives here)

A large ``delta`` is fully compatible with a high ``tau``: B can track A's ups and downs
while placing the whole series lower.
"""

from __future__ import annotations

from typing import Dict, Optional, Sequence

from .linalg import mean, ols


def truth_and_bias(
    perceived: Sequence[float],
    criterion: Sequence[float],
    own: Sequence[float],
    mean_level: Optional[float] = None,
) -> Dict[str, float]:
    """Estimate ``tau``, ``pi`` and ``delta`` by least squares.

    ``mean_level`` defaults to the criterion mean, as in West & Kenny's centring.
    All three series must be on the same metric.
    """
    if not (len(perceived) == len(criterion) == len(own)):
        raise ValueError("series must have equal length")
    mu = mean(criterion) if mean_level is None else mean_level
    rows = [[1.0, x - mu, o - mu] for x, o in zip(criterion, own)]
    delta, tau, pi = ols(rows, [q - mu for q in perceived])
    return {"tau": tau, "pi": pi, "delta": delta}
