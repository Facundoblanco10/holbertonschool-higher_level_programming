#!/usr/bin/python3
"""Module"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Class Rectangle"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        __width = width
        self.integer_validator("height", height)
        __height = height
