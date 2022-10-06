#!/usr/bin/python3
"""Module Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializator"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """Area method"""
        return (self.__width * self.__height)

    def display(self):
        """Display the rectangle with the # character"""
        for i in range(self.y):
            print()
        for col in range(self.height):
            for j in range(self.x):
                print(" ", end="")
            for row in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """String method"""
        st = f"[Rectangle] ({self.id}) {self.x}/{self.y} -"\
            f" {self.__width}/{self.__height}"
        return (st)

    def update(self, *args, **kwargs):
        """Update the class"""
        if args is not None or len(args) == 0:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "height":
                    self.__height = kwargs[key]
                elif key == "width":
                    self.__width = kwargs[key]
                elif key == "x":
                    self.__x = kwargs[key]
                elif key == "y":
                    self.__y = kwargs[key]
        for idx, ag in enumerate(args):
            if idx == 0:
                self.id = args[0]
            elif idx == 1:
                self.__width = args[1]
            elif idx == 2:
                self.__height = args[2]
            elif idx == 3:
                self.__x = args[3]
            elif idx == 4:
                self.__y = args[4]

    def to_dictionary(self):
        """
        This function returns a dictionary representation of a Rectangle.
        :return: A dictionary representation of a Rectangle
        """
        my_dict = {}
        my_dict["x"] = self.__x
        my_dict["y"] = self.__y
        my_dict["id"] = self.id
        my_dict["height"] = self.__height
        my_dict["width"] = self.__width
        return my_dict
