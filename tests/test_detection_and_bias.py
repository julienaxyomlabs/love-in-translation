"""Paper §8.5–8.6: quasi-signal detection and the truth-and-bias decomposition."""

import unittest

import _paths  # noqa: F401
from love_translation import detection, truth_bias


class QuasiSignalDetection(unittest.TestCase):
    def test_tabulation(self):
        giver = [True, True, False, False, True, False]
        receiver = [True, False, True, False, True, False]
        self.assertEqual(detection.tabulate(giver, receiver), detection.Counts(2, 1, 1, 2))

    def test_attentive_receiver_has_high_sensitivity(self):
        d_prime, criterion = detection.sensitivity(detection.Counts(48, 2, 3, 47))
        self.assertGreater(d_prime, 2.5)
        self.assertLess(abs(criterion), 0.3)

    def test_generous_perceiver_has_negative_criterion(self):
        _, criterion = detection.sensitivity(detection.Counts(45, 5, 30, 20))
        self.assertLess(criterion, 0.0)

    def test_needs_both_kinds_of_day(self):
        with self.assertRaises(ValueError):
            detection.sensitivity(detection.Counts(5, 0, 0, 0))


class TruthAndBias(unittest.TestCase):
    """Synthetic, noise-free series: the decomposition must recover the generating terms."""

    def test_recovers_truth_projection_and_level_bias(self):
        criterion = [3.0, 5.0, 4.0, 6.0, 2.0, 5.5, 4.5, 3.5]
        own = [4.0, 4.5, 6.0, 3.0, 5.0, 2.5, 4.0, 5.5]
        mu = sum(criterion) / len(criterion)
        tau, pi, delta = 0.6, 0.25, -0.5  # arbitrary test values, not estimates
        perceived = [mu + tau * (x - mu) + pi * (o - mu) + delta for x, o in zip(criterion, own)]
        est = truth_bias.truth_and_bias(perceived, criterion, own)
        self.assertAlmostEqual(est["tau"], tau, places=9)
        self.assertAlmostEqual(est["pi"], pi, places=9)
        self.assertAlmostEqual(est["delta"], delta, places=9)


if __name__ == "__main__":
    unittest.main()
