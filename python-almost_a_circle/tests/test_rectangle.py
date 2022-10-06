#!/usr/bin/python3
"""Test Rectangle"""
import unittest
from io import StringIO
import sys

from models.rectangle import Rectangle


class testing(unittest.TestCase):
    def test_rectangle_errors(self):
        """
        The function test_rectangle_errors() tests the Rectangle class for errors
        """
        self.assertRaises(TypeError, Rectangle,"1", 4)
        self.assertRaises(TypeError, Rectangle, 1, "4")
        self.assertRaises(TypeError, Rectangle, 1, 2, "3")
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4")
        self.assertRaises(ValueError, Rectangle, -1, 4)
        self.assertRaises(ValueError, Rectangle, 1, -2)
        self.assertRaises(ValueError, Rectangle, 0, 4)
        self.assertRaises(ValueError, Rectangle, 4, 0)
        self.assertRaises(ValueError, Rectangle, 1, 4, -3)
        self.assertRaises(ValueError, Rectangle, 1, 4, 2,-3)
        
    def test_rectangle(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.area(), 2)
        self.assertEqual(r.__str__(), '[Rectangle] (5) 3/4 - 1/2')

    def test_to_dictionary(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.to_dictionary(), {'x': 3, 'y': 4, 'id': 5, 'height': 2, 'width': 1})

    def test_display(self):
        my_result = StringIO()
        sys.stdout = my_result
        r = Rectangle(2, 2)
        r.display()
        self.assertEqual(my_result.getvalue(), "##\n##\n")
    
    def test_update(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update()
        self.assertEqual(r.__str__(), '[Rectangle] (5) 3/4 - 1/2')
    
    def test_create(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.create(**{ 'id': 89 })
        self.assertEqual(r.__str__(), '[Rectangle] (5) 3/4 - 1/2')
    
    def test_save(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), '[]')
    
  