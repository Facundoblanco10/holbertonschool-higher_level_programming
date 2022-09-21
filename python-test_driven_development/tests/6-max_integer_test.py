#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class testing(unittest.TestCase):
    def test_max_integer(self):
        actual = max_integer([1, 2, 3, 4])
        self.assertEqual(actual, 4)

    def test_empty_list(self):
        actual = max_integer([])
        self.assertEqual(actual, None)

    def test_max_integer_negative(self):
        actual = max_integer([-1, -4, -5, -10])
        self.assertEqual(actual, -1)

    def test_only_one(self):
        actual = max_integer([5])
        self.assertEqual(actual, 5)

    def test_max_in_middle(self):
        actual = max_integer([1, 2, 7, 1, 5])
        self.assertEqual(actual, 7)
