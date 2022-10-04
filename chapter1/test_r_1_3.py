import unittest
from r_1_3 import minmax


class TestIsMinMax(unittest.TestCase):
    def test_is_minmax(self):
        test_cases = [
            {
                "numbers": [1, 2, 3, 4, 5, 6],
                "output": (1, 6)
            },
            {
                "numbers": [1, 2, 3, 4, 5, 6, 1000],
                "output": (1, 1000)
            },
            {
                "numbers": [1000, 1000, 1000, 1000, 1000, 1000, 1000],
                "output": (1000, 1000)
            },
            {
                "numbers": [-1000, 1000, 1000, 1000, 1000, 1000, 1000],
                "output": (-1000, 1000)
            },
            {
                "numbers": [-0, 0, 0, 0, 0, 0, 0],
                "output": (0, 0)
            },
        ]

        for test_case in test_cases:
            self.assertEqual(minmax(test_case["numbers"]), test_case["output"])
