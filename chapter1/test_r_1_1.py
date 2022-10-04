from posixpath import ismount
import unittest
from r_1_1 import is_multiple


class TestIsMultiple(unittest.TestCase):
    def test_is_multiple(self):
        test_cases = [
            {
                "n": 4,
                "m": 2,
                "expected": True
            },
            {
                "n": 321,
                "m": 3,
                "expected": True
            },
            {
                "n": 81,
                "m": 9,
                "expected": True
            },
            {
                "n": 4,
                "m": 3,
                "expected": False
            },
        ]

        for test_case in test_cases:
            self.assertEqual(
                is_multiple(test_case["n"], test_case["m"]),
                test_case["expected"]
            )
