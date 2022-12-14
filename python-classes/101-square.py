#!/usr/bin/python3
"""Module"""


class Square():
    """Square class"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if (type(value) != tuple or
            len(value) != 2 or
                type(value[0]) != int or
                type(value[1]) != int or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for i in range(self.__position[0]):
                    print(" ", end='')
                print('#' * self.__size)

    def __str__(self):
        st = ''
        if self.__size == 0:
            return(st)
        for i in range(self.__position[1]):
            st += '\n'
        for i in range(self.__size):
            for idx, i in enumerate(range(self.__size)):
                if idx == 0:
                    for i in range(self.__position[0]):
                        st += ' '
                st += '#'
            st += '\n'
        return st[:-1]
