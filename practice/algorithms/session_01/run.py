"""Run local checks for your algorithm (standard library only).

From the Programming repository root:
    python practice/algorithms/session_01/run.py
"""
import unittest

from solution import longest_unique_substring


class LongestUniqueSubstringTests(unittest.TestCase):
    def test_examples(self):
        cases = [
            ("abcabcbb", 3),
            ("bbbbb", 1),
            ("pwwkew", 3),
            ("", 0),
        ]
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertEqual(longest_unique_substring(text), expected)

    def test_other_cases(self):
        cases = [
            ("a", 1),
            ("abba", 2),
            ("dvdf", 3),
            ("abcdef", 6),
            ("aA", 2),
            ("tmmzuxt", 5),
            ("anviaj", 5),
        ]
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertEqual(longest_unique_substring(text), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
