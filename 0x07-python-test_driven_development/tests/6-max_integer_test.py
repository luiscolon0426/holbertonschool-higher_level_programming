#!/usr/bin/python3
"""Unittest fro max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Just testing to see if this works"""

    def test_max_integer(self):
        """ calls the function max_integer"""
        x = [None]
        self.assertEqual(max_integer(x), None)

        x = [1]
        self.assertEqual(max_integer(x), 1)

        x = [5, 3, 4, 1]
        self.assertEqual(max_integer(x), 5)

        x = [1, 1, -5, 3]
        self.assertEqual(max_integer(x), 3)

        x = [100, 3, 5, 2]
        self.assertEqual(max_integer(x), 100)

        x = [-5, -4, -3, -1]
        self.assertEqual(max_integer(x), -1)

        x = [3.14, 5, 8, 9]
        self.assertEqual(max_integer(x), 9)

        x = [7]
        self.assertEqual(max_integer(x), 7)

        x = [-10, -5, -15]
        self.assertEqual(max_integer(x), -5)

        x = [10, 1, 1, 10]
        self.assertEqual(max_integer(x), 10)

        x = []
        self.assertEqual(max_integer([]), None)


if __name__ == "__main__":
    unittest.main()
