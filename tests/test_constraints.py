"""Paper §8.10: safety is an admissibility constraint; compatibility is feasibility.

These tests check the decision rules as implemented. They do not show that any
relationship outcome behaves this way.
"""

import unittest

import _paths  # noqa: F401
from love_translation import constraints as c


class SafetyIsAConstraint(unittest.TestCase):
    def test_no_finite_weight_excludes_unsafe_options(self):
        for weight in (0.0, 1.0, 10.0, 1e3, 1e9):
            unsafe, safe = c.weighted_counterexample(weight)
            self.assertTrue(c.weighted_prefers(unsafe, safe, weight))

    def test_lexicographic_ranking_still_picks_among_unsafe_options(self):
        worse = c.RelationshipState(safety=0.0, care=1.0)
        better = c.RelationshipState(safety=0.0, care=2.0)
        self.assertTrue(c.lexicographic_prefers(better, worse))  # a ranking, not an exclusion

    def test_choose_returns_nothing_when_no_option_is_safe(self):
        options = [c.Arrangement("caring but coercive", safe=False, outcome=9.0),
                   c.Arrangement("distant but violent", safe=False, outcome=2.0)]
        self.assertEqual(c.admissible(options), [])
        self.assertIsNone(c.choose(options))

    def test_choose_ignores_unsafe_options_however_good_they_look(self):
        options = [c.Arrangement("intense but coercive", safe=False, outcome=10.0),
                   c.Arrangement("modest and safe", safe=True, outcome=3.0)]
        self.assertEqual(c.choose(options).name, "modest and safe")


class Feasibility(unittest.TestCase):
    def test_compatible_when_a_safe_pattern_meets_everything(self):
        patterns = [
            c.JointPattern("same city, shared care", True, True, 0.7, 0.6),
            c.JointPattern("A moves alone", True, False, 0.8, 0.2),
        ]
        result = c.classify(patterns, threshold_a=0.5, threshold_b=0.5)
        self.assertEqual(result.status, "compatible")
        self.assertEqual(result.feasible, ("same city, shared care",))

    def test_unsafe_when_only_unsafe_patterns_meet_requirements(self):
        patterns = [c.JointPattern("together under control", True, True, 0.6, 0.6, safe=False)]
        result = c.classify(patterns, 0.5, 0.5)
        self.assertEqual(result.status, "unsafe")
        self.assertEqual(result.feasible, ())

    def test_incompatible_when_no_pattern_meets_both(self):
        patterns = [
            c.JointPattern("A's job city", True, False, 0.9, 0.4),
            c.JointPattern("B's job city", False, True, 0.4, 0.9),
        ]
        self.assertEqual(c.classify(patterns, 0.5, 0.5).status, "incompatible")

    def test_unsustainable_when_meeting_needs_costs_too_much(self):
        patterns = [c.JointPattern("A provides round-the-clock care", True, True, 0.1, 0.9)]
        self.assertEqual(c.classify(patterns, 0.5, 0.5).status, "unsustainable")


if __name__ == "__main__":
    unittest.main()
