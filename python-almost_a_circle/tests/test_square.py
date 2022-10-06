#!/usr/bin/python3
"""Test Square"""
import unittest

from models.square import Square

class testing(unittest.TestCase):
    def test_square(self):
        s = Square(3)
        self.assertEqual(s.width, 3)
        self.assertEqual(s.height, 3)
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 4)
        self.assertEqual(s.area(), 1)
        self.assertEqual(s.__str__(), '[Square] (4) 2/3 - 1')
        s = Square(1, 2)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 0)
    
    def test_square_errors(self):
        self.assertRaises(TypeError, Square, "1")
        self.assertRaises(TypeError, Square, 1, "4")
        self.assertRaises(TypeError, Square, 1, 2, "3")
        self.assertRaises(ValueError, Square, -1, 4)
        self.assertRaises(ValueError, Square, 1, -2)
        self.assertRaises(ValueError, Square, 0, 4)
        self.assertRaises(ValueError, Square, 0)