import unittest

from chapter1.is_even import is_even


class TestIsEven(unittest.TestCase):
    def test_is_even(self):
        test_cases = [
            {
                "input": 4,
                "expected": True,
            },
            {
                "input": 400000001,
                "expected": False,
            },
        ]

        for test_case in test_cases:
            self.assertEqual(
                is_even(test_case["input"]), test_case["expected"])
