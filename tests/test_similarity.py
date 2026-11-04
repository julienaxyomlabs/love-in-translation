"""Paper §8.3: cosine similarity cannot adjudicate translation versus amount."""

import unittest

import _paths  # noqa: F401
from love_translation import similarity as sim

E = (5.0, 3.0, 1.0, 2.0, 4.0)  # expressed care, the paper's illustrative profile
N = (4.0, 4.0, 2.0, 1.0, 5.0)  # needs


class CosineIgnoresAmount(unittest.TestCase):
    def test_scale_invariance(self):
        for a, b in ((0.25, 1.0), (3.0, 0.5), (10.0, 10.0)):
            self.assertAlmostEqual(sim.cosine([a * v for v in E], [b * v for v in N]), sim.cosine(E, N), places=12)

    def test_quarter_of_the_need_in_proportion_scores_one(self):
        self.assertAlmostEqual(sim.cosine([v / 4.0 for v in N], N), 1.0, places=12)


class CosineDependsOnCoding(unittest.TestCase):
    """Same two profiles, three codings of one rating scale (values quoted in the paper)."""

    def test_paper_values(self):
        expected = {0.0: 0.959, -1.0: 0.926, -3.0: 0.763}
        for offset, value in expected.items():
            e, n = sim.shift(E, offset), sim.shift(N, offset)
            self.assertAlmostEqual(round(sim.cosine(e, n), 3), value)
            self.assertAlmostEqual(round(sim.pearson(e, n), 3), 0.770)

    def test_units_of_one_channel_change_cosine(self):
        self.assertAlmostEqual(sim.cosine((1.0, 0.5), (0.5, 1.0)), 0.80, places=12)
        rescaled = sim.cosine(sim.rescale_channel((1.0, 0.5), 0, 2.0), sim.rescale_channel((0.5, 1.0), 0, 2.0))
        self.assertAlmostEqual(round(rescaled, 2), 0.86)


class ProfileCorrelationIsInflatedByNormativeness(unittest.TestCase):
    def test_zero_matching_still_correlates(self):
        result = sim.normative_inflation()
        self.assertGreater(result["raw_profile_r"], 0.3)
        self.assertLess(abs(result["distinctive_profile_r"]), 0.05)

    def test_zero_vector_rejected(self):
        with self.assertRaises(ValueError):
            sim.cosine((0.0, 0.0), (1.0, 2.0))


if __name__ == "__main__":
    unittest.main()
