#!/usr/bin/python3
"""Module"""


class Student():
    """Class student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        m_dict = {}
        if attrs is None or len(attrs) == 0:
            return self.__dict__
        if type(attrs) == list:
            for at in attrs:
                try:
                    if type(at) == str:
                        m_dict[at] = self.__dict__[at]
                except Exception:
                    Exception
        return m_dict
