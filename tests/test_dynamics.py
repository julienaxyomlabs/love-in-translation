"""Paper §8.9: trust equilibria, the bistability condition, and developmental lag."""

import unittest

import _paths  # noqa: F401
from love_translation import lag, trust


class TrustEquilibria(unittest.TestCase):
    def test_steep_reading_can_still_have_one_equilibrium(self):
        p = trust.logistic_reading(10.0, 0.3)
        self.assertAlmostEqual(trust.max_slope(p), 2.5, places=3)  # p' > 1 somewhere ...
        self.assertEqual(len(trust.equilibria(p)), 1)  # ... yet only one equilibrium
        self.assertFalse(trust.is_bistable(p))

    def test_symmetric_steep_reading_is_bistable(self):
        p = trust.logistic_reading(4.5, 0.5)
        eqs = trust.equilibria(p)
        self.assertEqual(len(eqs), 3)
        self.assertEqual([e.stable for e in eqs], [True, False, True])
        self.assertAlmostEqual(eqs[1].level, 0.5, places=9)
        self.assertTrue(trust.is_bistable(p))

    def test_shallow_reading_has_a_unique_equilibrium(self):
        p = trust.logistic_reading(3.0, 0.5)
        self.assertLess(trust.max_slope(p), 1.0)
        self.assertEqual(len(trust.equilibria(p)), 1)

    def test_hysteresis_under_bistability(self):
        p = trust.logistic_reading(4.5, 0.5)
        low = trust.simulate(p, start=0.2, eta=0.2, steps=400)[-1]
        high = trust.simulate(p, start=0.8, eta=0.2, steps=400)[-1]
        self.assertLess(low, 0.5)
        self.assertGreater(high, 0.5)


class DevelopmentalLag(unittest.TestCase):
    def test_steady_state_is_drift_over_learning_rate(self):
        for drift, lam in ((0.1, 0.2), (0.05, 0.5), (0.3, 1.0)):
            errors = lag.simulate_error(drift, lam, steps=2000)
            self.assertAlmostEqual(errors[-1], lag.steady_state_lag(drift, lam), places=9)
            self.assertAlmostEqual(lag.steady_state_lag(drift, lam), drift / lam)

    def test_tracking_a_linear_drift(self):
        need = [0.1 * t for t in range(400)]
        model = lag.track(need, 0.25, initial_model=0.0)
        self.assertAlmostEqual(need[-1] - model[-1], 0.1 / 0.25, places=6)

    def test_learning_rate_must_be_in_unit_interval(self):
        for bad in (0.0, -0.1, 1.5):
            with self.assertRaises(ValueError):
                lag.steady_state_lag(0.1, bad)


if __name__ == "__main__":
    unittest.main()
