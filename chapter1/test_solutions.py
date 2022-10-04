import unittest
from r_1_4 import sum_of_squares_till_n
from c_1_1 import reverse_items


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

    def test_reverse_items(self):
        test_cases = [
            {
                "items": [1, 2, 3, 4, 5, 6],
                "output": [6, 5, 4, 3, 2, 1]
            },
            {
                "items": [1, 2, 3, 4, 5, 6, 7],
                "output": [7, 6, 5, 4, 3, 2, 1]
            },
            {
                "items": [],
                "output": []
            },
            {
                "items": [1],
                "output": [1]
            },
            {
                "items": [1, 2],
                "output": [2, 1]
            },
        ]

        for test_case in test_cases:
            self.assertEqual(reverse_items(
                test_case["items"]), test_case["output"])
