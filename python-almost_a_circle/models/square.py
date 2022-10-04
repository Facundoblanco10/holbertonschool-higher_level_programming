#!/usr/bin/python3
"""Module Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String method"""
        st = f"[Square] ({self.id}) {self.x}/{self.y} - {super().width}"
        return (st)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the class"""
        if args is not None or len(args) == 0:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "size":
                    self.height = kwargs[key]
                    self.width = kwargs[key]
                elif key == "x":
                    self.x = kwargs[key]
                elif key == "y":
                    self.y = kwargs[key]
        for idx, ag in enumerate(args):
            if idx == 0:
                self.id = args[0]
            elif idx == 1:
                self.width = args[1]
            elif idx == 2:
                self.height = args[2]
            elif idx == 3:
                self.x = args[3]
            elif idx == 4:
                self.y = args[4]
