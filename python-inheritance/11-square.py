#!/usr/bin/python3
"""Module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        super().__init__(self.__size, self.__size)
        st = f"[Square] {self.__size} / {self.__size}"
        return st
