"""Paper §8.7: response surface analysis separates level from mismatch."""

import unittest

import _paths  # noqa: F401
from love_translation import fit

GRID = [(s, n) for s in range(-2, 3) for n in range(-2, 3)]


def surface_for(outcome):
    supply = [float(s) for s, _ in GRID]
    need = [float(n) for _, n in GRID]
    y = [outcome(s, n) for s, n in GRID]
    return fit.surface_parameters(fit.fit_surface(supply, need, y))


class ResponseSurface(unittest.TestCase):
    def test_pure_mismatch_loads_on_a4(self):
        a = surface_for(lambda s, n: -((s - n) ** 2))
        self.assertAlmostEqual(a["a4"], -4.0, places=9)
        for key in ("a1", "a2", "a3"):
            self.assertAlmostEqual(a[key], 0.0, places=9)

    def test_pure_amount_loads_on_a1_not_a4(self):
        a = surface_for(lambda s, n: float(s))
        self.assertAlmostEqual(a["a1"], 1.0, places=9)
        self.assertAlmostEqual(a["a3"], 1.0, places=9)
        self.assertAlmostEqual(a["a4"], 0.0, places=9)

    def test_asymmetric_loss_separates_deficit_from_excess(self):
        self.assertEqual(fit.asymmetric_loss(1.0, 3.0, deficit_weight=2.0, excess_weight=0.5), -4.0)
        self.assertEqual(fit.asymmetric_loss(3.0, 1.0, deficit_weight=2.0, excess_weight=0.5), -1.0)
        self.assertEqual(fit.asymmetric_loss(2.0, 2.0, deficit_weight=2.0, excess_weight=0.5), 0.0)
        with self.assertRaises(ValueError):
            fit.asymmetric_loss(1.0, 2.0, deficit_weight=-1.0, excess_weight=0.0)


if __name__ == "__main__":
    unittest.main()
