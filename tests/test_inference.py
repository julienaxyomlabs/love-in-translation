"""Paper §8.6: regard inferred from costly acts rises with the believed cost."""

import unittest

import _paths  # noqa: F401
from love_translation import inference

WEIGHTS = [i / 20.0 for i in range(21)]
COSTS = [0.0, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0]


class NaiveUtilityCalculus(unittest.TestCase):
    def assert_increasing(self, values):
        for earlier, later in zip(values, values[1:]):
            self.assertGreater(later, earlier)

    def test_caring_act_reads_as_more_regard_when_believed_costly(self):
        means = [inference.posterior_mean(True, c, 1.0, 4.0, WEIGHTS) for c in COSTS]
        self.assert_increasing(means)

    def test_absence_reads_as_less_damning_when_presence_believed_costly(self):
        means = [inference.posterior_mean(False, c, 1.0, 4.0, WEIGHTS) for c in COSTS]
        self.assert_increasing(means)

    def test_log_likelihood_ratio_derivative_is_positive(self):
        for acted in (True, False):
            values = [inference.log_likelihood_ratio(acted, c, 1.0, 4.0, high=0.9, low=0.2) for c in COSTS]
            self.assert_increasing(values)

    def test_posterior_is_a_distribution(self):
        post = inference.posterior(True, 0.5, 1.0, 4.0, WEIGHTS)
        self.assertAlmostEqual(sum(post), 1.0, places=12)
        self.assertTrue(all(p >= 0.0 for p in post))


if __name__ == "__main__":
    unittest.main()
