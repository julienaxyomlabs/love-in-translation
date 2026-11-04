"""Why similarity indices cannot adjudicate "translation versus amount" (paper §8.3).

* Cosine similarity is scale-invariant: ``cos(a*E, b*N) == cos(E, N)`` for a, b > 0,
  so a partner who gives a quarter of what is needed, in the right proportions, scores 1.
* On rating scales cosine depends on the arbitrary origin and on the units of each channel.
* The profile (Pearson) correlation escapes the origin problem only by discarding
  elevation, which is exactly the "amount" information, and it is inflated whenever
  both profiles share a normative shape (Cronbach & Gleser 1953; Furr 2008).
"""

from __future__ import annotations

import math
import random
from typing import Dict, List, Sequence

from .linalg import mean


def dot(x: Sequence[float], y: Sequence[float]) -> float:
    if len(x) != len(y):
        raise ValueError("vectors differ in length")
    return math.fsum(a * b for a, b in zip(x, y))


def norm(x: Sequence[float]) -> float:
    return math.sqrt(dot(x, x))


def cosine(x: Sequence[float], y: Sequence[float]) -> float:
    denominator = norm(x) * norm(y)
    if denominator == 0.0:
        raise ValueError("cosine is undefined for a zero vector")
    return dot(x, y) / denominator


def pearson(x: Sequence[float], y: Sequence[float]) -> float:
    """Profile correlation: the cosine of the mean-centred profiles."""
    mx, my = mean(x), mean(y)
    return cosine([a - mx for a in x], [b - my for b in y])


def shift(x: Sequence[float], offset: float) -> List[float]:
    """Re-code a rating profile, e.g. 1-5 to 0-4 (offset -1)."""
    return [v + offset for v in x]


def rescale_channel(x: Sequence[float], index: int, factor: float) -> List[float]:
    """Express one channel in different units (multiply it by ``factor``)."""
    out = list(x)
    out[index] = out[index] * factor
    return out


def normative_inflation(
    n_pairs: int = 4000,
    n_channels: int = 6,
    normative_sd: float = 1.0,
    personal_sd: float = 1.0,
    seed: int = 2026,
) -> Dict[str, float]:
    """Simulate expressed-care and need profiles with *zero* person-specific matching.

    Both profiles share one normative shape (everyone values some channels more than
    others) plus independent personal deviations. The mean raw profile correlation is
    then clearly positive although nobody is matched to anybody; removing the sample's
    average profile (the "distinctive" correlation) brings it back to about zero.
    """
    if n_channels < 3 or n_pairs < 2:
        raise ValueError("need at least 3 channels and 2 pairs")
    rng = random.Random(seed)
    centre = (n_channels - 1) / 2.0
    raw_shape = [(k - centre) for k in range(n_channels)]
    shape_sd = math.sqrt(mean([v * v for v in raw_shape]))
    shape = [normative_sd * v / shape_sd for v in raw_shape]

    needs: List[List[float]] = []
    given: List[List[float]] = []
    for _ in range(n_pairs):
        needs.append([m + rng.gauss(0.0, personal_sd) for m in shape])
        given.append([m + rng.gauss(0.0, personal_sd) for m in shape])

    raw = mean([pearson(e, n) for e, n in zip(given, needs)])
    avg_need = [mean([row[k] for row in needs]) for k in range(n_channels)]
    avg_given = [mean([row[k] for row in given]) for k in range(n_channels)]
    distinctive = mean(
        [
            pearson([v - a for v, a in zip(e, avg_given)], [v - a for v, a in zip(n, avg_need)])
            for e, n in zip(given, needs)
        ]
    )
    return {"raw_profile_r": raw, "distinctive_profile_r": distinctive}
