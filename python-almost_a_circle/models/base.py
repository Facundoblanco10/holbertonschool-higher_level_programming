#!/usr/bin/python3
"""Base module"""


from fileinput import filename
import json
import os


class Base():
    """Class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This function converts a list of dictionaries to a JSON string.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        "Save a list of objects to a file in JSON format."
        """
        new_list = []
        if list_objs is not None:
            for obj in list_objs:
                new_list.append(obj.to_dictionary())
        with open(f"{cls.__name__}.json", "w") as f:
            f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """
        It takes a json string and returns a python object.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            new_instance = cls(3, 3)
        if cls.__name__ == "Square":
            new_instance = cls(5)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        new_list = []
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return new_list
        with open(filename, "r") as f:
            f_cont = f.read()
        instances = cls.from_json_string(f_cont)
        for d in instances:
            new_list.append(cls.create(**d))
        return new_list
