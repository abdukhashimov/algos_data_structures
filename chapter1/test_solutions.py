import unittest
from r_1_4 import sum_of_squares_till_n


class TestSolutions(unittest.TestCase):
    def test_sum_of_squares_till_n(self):
        test_cases = [
            {
                "n": 1,
                "output": 0,
            },
            {
                "n": 2,
                "output": 1,
            },
            {
                "n": 3,
                "output": 5
            },
            {
                "n": 4,
                "output": 14
            }
        ]

        for test_case in test_cases:
            self.assertEqual(sum_of_squares_till_n(
                test_case["n"]), test_case["output"])
