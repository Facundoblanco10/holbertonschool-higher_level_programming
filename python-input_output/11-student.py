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
        if attrs is None:
            return self.__dict__
        if type(attrs) == list:
            for at in attrs:
                try:
                    if type(at) == str:
                        m_dict[at] = self.__dict__[at]
                except Exception:
                    Exception
        return m_dict

    def reload_from_json(self, json):
        try:
            for key in json:
                self.first_name[key] = json[key]
                self.last_name[key] = json [key]
                self.age[key] = json[key]
        except Exception:
            Exception
