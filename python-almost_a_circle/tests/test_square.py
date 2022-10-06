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
        self.assertRaises(ValueError, Square, 1, 2, -3)

    def test_to_dictionary(self):
        s = Square(2, 3, 4, 5)
        self.assertEqual(s.to_dictionary(), {'x': 3, 'y': 4, 'id': 5, 'size': 2})
    
    def test_update(self):
        s = Square(2, 3, 4, 5)
        s.update()
        self.assertEqual(s.__str__(), '[Square] (5) 3/4 - 2')
        
    def test_create(self):
        s = Square(2, 3, 4, 5)
        s.create(**{ 'id': 89 })
        self.assertEqual(s.__str__(), '[Square] (5) 3/4 - 2')

    def test_save(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), '[]')
    
    def test_save3(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), '[]')
    
    def test_load(self):
        Square.load_from_file()
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), '[{"x": 0, "y": 0, "id": 29, "size": 2}]')

class testing2(unittest.TestCase):
    def test_save2(self):
        Square.save_to_file([Square(2)])
        with open("Square.json", "r") as f:
            self.assertEqual('[{"x": 0, "y": 0, "id": 29, "size": 2}]',
            f.read())
    