#!/usr/bin/python3
"""Test Rectangle"""
import unittest

from models.rectangle import Rectangle


class testing(unittest.TestCase):
    def test_rectangle(self):
        r1 = Rectangle(3, 4)
        self.assertEqual(str(r1), '[Rectangle] (1) 0/0 - 3/4')
        r2 = Rectangle(3, 4, 7)
        self.assertEqual(str(r2), '[Rectangle] (2) 7/0 - 3/4')
        r3 = Rectangle(3, 4, 6, 9)
        self.assertEqual(str(r3), '[Rectangle] (3) 6/9 - 3/4')
        r4 = Rectangle(1, 4, 3, 3, 9)
        self.assertEqual(str(r4), '[Rectangle] (9) 3/3 - 1/4')
    def test_rectangle_errors(self):
        self.assertRaises(TypeError, Rectangle,"1", 4)
        self.assertRaises(TypeError, Rectangle, 1, "4")
        self.assertRaises(TypeError, Rectangle, 1, 2, "3")
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4")
        self.assertRaises(ValueError, Rectangle, -1, 4)
