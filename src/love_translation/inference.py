"""Inferring how much a giver values the receiver from costly choices (paper §8.6).

Status: a theoretical mechanism (the naive utility calculus; Jara-Ettinger et al. 2016)
applied to care. It has never been estimated on family or couple data.

A softmax-rational giver chooses the caring act with probability

    P(act | w) = logistic(beta * (w * b - c))

where ``w`` is the weight the giver places on the receiver's welfare, ``b`` the act's
benefit to the receiver, ``c`` its cost to the giver and ``beta`` choice precision. The
receiver infers ``w`` by Bayes' rule using the cost they *believe* the act had. The
posterior on ``w`` rises with the believed cost after a caring act, and absence is read
more harshly the cheaper presence is believed to have been. When the costs of provision
are invisible but its by-product (absence) is visible, inferred regard falls even if the
true ``w`` is high: the paper's "visibility asymmetry".
"""

from __future__ import annotations

import math
from typing import List, Optional, Sequence

from .linalg import logistic


def choice_probability(weight: float, benefit: float, cost: float, precision: float) -> float:
    return logistic(precision * (weight * benefit - cost))


def posterior(
    acted: bool,
    believed_cost: float,
    benefit: float,
    precision: float,
    weights: Sequence[float],
    prior: Optional[Sequence[float]] = None,
) -> List[float]:
    """Posterior over candidate weights after observing the act (or its absence)."""
    if prior is None:
        prior = [1.0 / len(weights)] * len(weights)
    if len(prior) != len(weights):
        raise ValueError("prior and weights differ in length")
    unnormalised = []
    for w, p in zip(weights, prior):
        p_act = choice_probability(w, benefit, believed_cost, precision)
        unnormalised.append(p * (p_act if acted else 1.0 - p_act))
    total = math.fsum(unnormalised)
    if total == 0.0:
        raise ValueError("observation has zero probability under every weight")
    return [u / total for u in unnormalised]


def posterior_mean(
    acted: bool,
    believed_cost: float,
    benefit: float,
    precision: float,
    weights: Sequence[float],
    prior: Optional[Sequence[float]] = None,
) -> float:
    post = posterior(acted, believed_cost, benefit, precision, weights, prior)
    return math.fsum(w * p for w, p in zip(weights, post))


def log_likelihood_ratio(
    acted: bool, believed_cost: float, benefit: float, precision: float, high: float, low: float
) -> float:
    """log P(obs | w=high) - log P(obs | w=low); its derivative in cost is positive."""
    p_high = choice_probability(high, benefit, believed_cost, precision)
    p_low = choice_probability(low, benefit, believed_cost, precision)
    if acted:
        return math.log(p_high) - math.log(p_low)
    return math.log(1.0 - p_high) - math.log(1.0 - p_low)
