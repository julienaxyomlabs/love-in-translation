"""Paper §8.10: safety is a gate, not a weight; compatibility is feasibility."""

import unittest

import _paths  # noqa: F401
from love_translation import constraints as c


class SafetyGate(unittest.TestCase):
    def test_no_finite_weight_reproduces_the_gate(self):
        for weight in (0.0, 1.0, 10.0, 1e3, 1e9):
            unsafe, safe = c.weighted_counterexample(weight)
            self.assertTrue(c.weighted_prefers(unsafe, safe, weight))
            self.assertTrue(c.lexicographic_prefers(safe, unsafe))

    def test_care_decides_among_equally_safe_states(self):
        a = c.RelationshipState(safety=1.0, care=2.0)
        b = c.RelationshipState(safety=1.0, care=1.0)
        self.assertTrue(c.lexicographic_prefers(a, b))
        self.assertFalse(c.lexicographic_prefers(b, a))


class Feasibility(unittest.TestCase):
    def test_compatible_when_some_pattern_meets_everything(self):
        patterns = [
            c.JointPattern("same city, shared care", True, True, 0.7, 0.6),
            c.JointPattern("A moves alone", True, False, 0.8, 0.2),
        ]
        result = c.classify(patterns, threshold_a=0.5, threshold_b=0.5)
        self.assertEqual(result.status, "compatible")
        self.assertEqual(result.feasible, ("same city, shared care",))

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
