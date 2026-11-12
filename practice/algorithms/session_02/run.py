"""Run tests for algorithm session 02; no extra dependencies needed.

From the Programming repo root:
    python practice/algorithms/session_02/run.py
"""
import unittest

from solution import min_subarray_length


class MinimumSubarrayTests(unittest.TestCase):
    def test_examples(self):
        cases = [
            (7, [2, 3, 1, 2, 4, 3], 2),
            (4, [1, 4, 4], 1),
            (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
            (3, [], 0),
        ]
        for target, numbers, expected in cases:
            with self.subTest(target=target, numbers=numbers):
                self.assertEqual(min_subarray_length(target, numbers), expected)

    def test_boundaries_and_other_cases(self):
        cases = [
            (3, [1, 1, 1], 3),
            (10, [5, 5], 2),
            (9, [1, 2, 3, 4, 5], 2),
            (15, [1, 2, 3, 4, 5], 5),
            (6, [1, 2, 3, 1, 1, 1], 3),
            (8, [2, 3, 1, 2, 4, 3], 3),
            (5, [4, 1], 2),
            (5, [1, 2, 1], 0),
            (5, [5, 1, 1], 1),
            (8, [1, 3, 2, 5, 1, 1], 3),
        ]
        for target, numbers, expected in cases:
            with self.subTest(target=target, numbers=numbers):
                self.assertEqual(min_subarray_length(target, numbers), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
