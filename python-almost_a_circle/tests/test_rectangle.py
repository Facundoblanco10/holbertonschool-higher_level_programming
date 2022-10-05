#!/usr/bin/python3
"""Test Rectangle"""
import unittest

from models.rectangle import Rectangle


class testing(unittest.TestCase):
    def test_rectangle_errors(self):
        self.assertRaises(TypeError, Rectangle,"1", 4)
        self.assertRaises(TypeError, Rectangle, 1, "4")
        self.assertRaises(TypeError, Rectangle, 1, 2, "3")
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4")
        self.assertRaises(ValueError, Rectangle, -1, 4)
    def test_rectangle(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.__str__(), '[Rectangle] (1) 0/0 - 3/4')
        r = Rectangle(3, 4, 7)
        self.assertEqual(r.__str__(), '[Rectangle] (2) 7/0 - 3/4')
        r = Rectangle(3, 4, 6, 9)
        self.assertEqual(r.__str__(), '[Rectangle] (3) 6/9 - 3/4')
        r = Rectangle(1, 4, 3, 3, 9)
        self.assertEqual(r.__str__(), '[Rectangle] (9) 3/3 - 1/4')
    