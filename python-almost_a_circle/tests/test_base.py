#!/usr/bin/python3
"""Test Base"""
import unittest

from models.base import Base


class testing(unittest.TestCase):
    def test_create_without_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_create_with_id(self):
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_negative_number(self):
        b1 = Base(-5)
        self.assertEqual(b1.id, -5)

    def test_string(self):
        b1 = Base("hola")
        self.assertEqual(b1.id, "hola")

    def test_list(self):
        b1 = Base([1, 2, 3])
        self.assertEqual(b1.id, [1, 2, 3])

    def base_to_json_exists(self):
        b1 = Base.to_json_string(None)
        self.assertEqual(b1, '[]')

    def base_to_json_exists2(self):
        b1 = Base.to_json_string([])
        self.assertEqual(b1, '[]')
