"""Quasi-signal detection of care acts from two partners' diaries (paper §8.5).

The *signal* is the giver's report that an act occurred; the *response* is the receiver's
report. Hits, misses, false alarms and correct rejections give a sensitivity ``d'`` and a
criterion ``c`` (negative ``c`` = a generous perceiver who "sees" care the giver did not
report). The giver's report is not ground truth, so misses and false alarms are
*disagreements*, not errors, unless an observer or an experiment supplies the criterion
(Visserman et al. 2019).
"""

from __future__ import annotations

from dataclasses import dataclass
from statistics import NormalDist
from typing import Sequence, Tuple

_Z = NormalDist().inv_cdf


@dataclass(frozen=True)
class Counts:
    hits: int
    misses: int
    false_alarms: int
    correct_rejections: int

    @property
    def total(self) -> int:
        return self.hits + self.misses + self.false_alarms + self.correct_rejections


def tabulate(giver_reported: Sequence[bool], receiver_reported: Sequence[bool]) -> Counts:
    """Cross-tabulate paired daily reports of the same act category."""
    if len(giver_reported) != len(receiver_reported):
        raise ValueError("report sequences differ in length")
    h = m = f = c = 0
    for signal, response in zip(giver_reported, receiver_reported):
        if signal and response:
            h += 1
        elif signal:
            m += 1
        elif response:
            f += 1
        else:
            c += 1
    return Counts(h, m, f, c)


def rates(counts: Counts) -> Tuple[float, float]:
    """Hit and false-alarm rates with the log-linear correction (Hautus 1995)."""
    signal_days = counts.hits + counts.misses
    noise_days = counts.false_alarms + counts.correct_rejections
    if signal_days == 0 or noise_days == 0:
        raise ValueError("need both signal-present and signal-absent days")
    hit_rate = (counts.hits + 0.5) / (signal_days + 1.0)
    fa_rate = (counts.false_alarms + 0.5) / (noise_days + 1.0)
    return hit_rate, fa_rate


def sensitivity(counts: Counts) -> Tuple[float, float]:
    """Return ``(d_prime, criterion)``."""
    hit_rate, fa_rate = rates(counts)
    z_h, z_f = _Z(hit_rate), _Z(fa_rate)
    return z_h - z_f, -(z_h + z_f) / 2.0
