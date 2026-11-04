"""Executable companion to the paper "Can Love Be Lost in Translation?".

Each module implements one formal component of the paper's model
(``paper/08-mathematical-representation.md``) with the Python standard library only.

Parameters are symbolic. Nothing in this package ships an estimated psychological
coefficient: numbers that appear in tests and examples are arithmetic illustrations.

Modules
-------
similarity   Why cosine, dot products and profile correlations cannot separate amount from fit.
fit          Polynomial regression with response surface analysis (level vs. mismatch).
detection    Quasi-signal detection of care acts from two partners' diaries.
truth_bias   Truth-and-bias decomposition of perceived care.
inference    Inferring how much a giver values the receiver from costly choices.
trust        Trust as a latent state; equilibria and the bistability condition.
lag          Developmental lag in a giver's model of a changing need.
constraints  Safety as a lexicographic gate; compatibility as a feasible set.
"""

from . import constraints, detection, fit, inference, lag, linalg, similarity, trust, truth_bias

__version__ = "0.1.0"

__all__ = [
    "constraints",
    "detection",
    "fit",
    "inference",
    "lag",
    "linalg",
    "similarity",
    "trust",
    "truth_bias",
]
