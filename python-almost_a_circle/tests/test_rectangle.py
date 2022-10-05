#!/usr/bin/python3
"""Test Rectangle"""
import unittest

from models.rectangle import Rectangle


class testing(unittest.TestCase):
    def test_rectangle(self):
        self.r1 = Rectangle(3, 4)
        self.assertEqual(self.r1.__str__(), '[Rectangle] (1) 0/0 - 3/4')
        self.r2 = Rectangle(3, 4, 7)
        self.assertEqual(self.r2.__str__(), '[Rectangle] (2) 7/0 - 3/4')
        self.r3 = Rectangle(3, 4, 6, 9)
        self.assertEqual(self.r3.__str__(), '[Rectangle] (3) 6/9 - 3/4')
        self.r4 = Rectangle(1, 4, 3, 3, 9)
        self.assertEqual(self.r4.__str__(), '[Rectangle] (9) 3/3 - 1/4')
    def test_rectangle_errors(self):
        self.assertRaises(TypeError, Rectangle,"1", 4)
        self.assertRaises(TypeError, Rectangle, 1, "4")
        self.assertRaises(TypeError, Rectangle, 1, 2, "3")
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4")
        self.assertRaises(ValueError, Rectangle, -1, 4)
