"""Small dense linear algebra for least-squares problems, using the standard library only."""

from __future__ import annotations

import math
from typing import List, Sequence

Vector = List[float]


def solve(a: Sequence[Sequence[float]], b: Sequence[float]) -> Vector:
    """Solve ``a @ x = b`` by Gaussian elimination with partial pivoting."""
    n = len(a)
    if n == 0 or any(len(row) != n for row in a) or len(b) != n:
        raise ValueError("solve() needs a square matrix and a matching right-hand side")
    m = [[float(v) for v in row] + [float(rhs)] for row, rhs in zip(a, b)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(m[r][col]))
        if abs(m[pivot][col]) < 1e-12:
            raise ValueError("matrix is singular or ill-conditioned")
        m[col], m[pivot] = m[pivot], m[col]
        for r in range(col + 1, n):
            factor = m[r][col] / m[col][col]
            if factor != 0.0:
                for c in range(col, n + 1):
                    m[r][c] -= factor * m[col][c]
    x = [0.0] * n
    for r in range(n - 1, -1, -1):
        acc = m[r][n] - math.fsum(m[r][c] * x[c] for c in range(r + 1, n))
        x[r] = acc / m[r][r]
    return x


def ols(rows: Sequence[Sequence[float]], y: Sequence[float]) -> Vector:
    """Ordinary least squares through the normal equations.

    ``rows`` is the design matrix, one row per observation; include a column of ones
    for an intercept.
    """
    if not rows or len(rows) != len(y):
        raise ValueError("rows and y must be non-empty and of equal length")
    k = len(rows[0])
    xtx = [[math.fsum(r[i] * r[j] for r in rows) for j in range(k)] for i in range(k)]
    xty = [math.fsum(r[i] * yi for r, yi in zip(rows, y)) for i in range(k)]
    return solve(xtx, xty)


def mean(values: Sequence[float]) -> float:
    """Arithmetic mean with compensated summation."""
    if len(values) == 0:
        raise ValueError("mean of an empty sequence")
    return math.fsum(values) / len(values)


def logistic(x: float) -> float:
    """Numerically stable logistic function."""
    if x >= 0.0:
        return 1.0 / (1.0 + math.exp(-x))
    z = math.exp(x)
    return z / (1.0 + z)
