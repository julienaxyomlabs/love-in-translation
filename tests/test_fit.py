"""Paper §8.7: response surface analysis separates level from mismatch.

These tests check the implementation against published worked examples. They verify the
mathematics, not any psychological claim.
"""

import unittest

import _paths  # noqa: F401
from love_translation import fit

GRID = [(s, n) for s in range(-2, 3) for n in range(-2, 3)]

# Edwards (2007), eq. 23: actual vs desired job variety and satisfaction, 358 job seekers.
EDWARDS_2007 = {"b0": 5.628, "b1": 0.314, "b2": -0.118, "b3": -0.145, "b4": 0.299, "b5": -0.102}

# Schönbrodt, Humberg & Nestler (2018), Figure 1: a prototypical similarity effect.
PROTOTYPE = {"b0": 4.0, "b1": 0.0, "b2": 0.0, "b3": -0.25, "b4": 0.5, "b5": -0.25}


def surface_for(outcome, shift=0.0):
    supply = [float(s) - shift for s, _ in GRID]
    need = [float(n) - shift for _, n in GRID]
    y = [outcome(s, n) for s, n in GRID]
    return fit.surface_parameters(fit.fit_surface(supply, need, y))


class SurfaceQuantities(unittest.TestCase):
    def test_reproduces_edwards_2007_surface_quantities(self):
        a = fit.surface_parameters(EDWARDS_2007)
        self.assertAlmostEqual(a["a1"], 0.196, places=3)   # slope along X = Y at (0, 0)
        self.assertAlmostEqual(a["a2"], 0.052, places=3)   # curvature along X = Y
        self.assertAlmostEqual(a["a3"], 0.432, places=3)   # slope along X = -Y at (0, 0)
        self.assertAlmostEqual(a["a4"], -0.546, places=3)  # curvature along X = -Y

    def test_reproduces_edwards_2007_stationary_point_and_axes(self):
        x0, y0 = fit.stationary_point(EDWARDS_2007)
        self.assertAlmostEqual(x0, -0.951, places=3)
        self.assertAlmostEqual(y0, -1.973, places=3)
        axes = fit.principal_axes(EDWARDS_2007)
        self.assertAlmostEqual(axes["p10"], -0.875, places=3)
        self.assertAlmostEqual(axes["p11"], 1.154, places=3)
        self.assertAlmostEqual(axes["p20"], -2.797, places=3)
        self.assertAlmostEqual(axes["p21"], -0.866, places=3)

    def test_reproduces_schonbrodt_2018_prototype(self):
        a = fit.surface_parameters(PROTOTYPE)
        self.assertEqual((a["a1"], a["a2"], a["a3"], a["a4"], a["a5"]), (0.0, 0.0, 0.0, -1.0, 0.0))
        screen = fit.congruence_screen(PROTOTYPE)
        self.assertTrue(screen["congruence_pattern"])
        self.assertTrue(screen["flat_ridge"])
        self.assertIsNone(fit.stationary_point(PROTOTYPE))  # a ridge line, not a point
        self.assertAlmostEqual(fit.principal_axes(PROTOTYPE)["p11"], 1.0)


class Interpretation(unittest.TestCase):
    def test_a1_is_the_slope_at_the_centring_point_only(self):
        def outcome(s, n):
            return 0.3 * (s + n) + 0.1 * (s + n) ** 2  # curved along the line of congruence
        base = surface_for(outcome)
        moved = surface_for(outcome, shift=1.0)  # same data, centred one unit lower
        self.assertAlmostEqual(moved["a1"] - base["a1"], 2.0 * base["a2"] * 1.0, places=9)

    def test_negative_a4_alone_is_not_a_congruence_pattern(self):
        optimal_margin = {"b0": 0.0, "b1": 0.4, "b2": -0.4, "b3": -0.25, "b4": 0.5, "b5": -0.25}
        screen = fit.congruence_screen(optimal_margin)
        self.assertTrue(screen["a4_negative"])
        self.assertFalse(screen["a3_zero"])
        self.assertFalse(screen["congruence_pattern"])

    def test_pure_mismatch_and_pure_level_surfaces(self):
        mismatch = surface_for(lambda s, n: -((s - n) ** 2))
        self.assertAlmostEqual(mismatch["a4"], -4.0, places=9)
        for key in ("a1", "a2", "a3", "a5"):
            self.assertAlmostEqual(mismatch[key], 0.0, places=9)
        level = surface_for(lambda s, n: float(s))
        self.assertAlmostEqual(level["a1"], 1.0, places=9)
        self.assertAlmostEqual(level["a4"], 0.0, places=9)

    def test_asymmetric_loss_separates_deficit_from_excess(self):
        self.assertEqual(fit.asymmetric_loss(1.0, 3.0, deficit_weight=2.0, excess_weight=0.5), -4.0)
        self.assertEqual(fit.asymmetric_loss(3.0, 1.0, deficit_weight=2.0, excess_weight=0.5), -1.0)
        with self.assertRaises(ValueError):
            fit.asymmetric_loss(1.0, 2.0, deficit_weight=-1.0, excess_weight=0.0)


if __name__ == "__main__":
    unittest.main()
