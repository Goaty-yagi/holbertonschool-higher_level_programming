#!/usr/bin/python3

""" This module provides Base class
"""

import json


class Base:
    """
    This class representing base class
    """
    __nb_objects = 0

    def __init__(self, id: int = None) -> None:
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries) -> str:
        if list_dictionaries == None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string: str) -> list:
        if json_string == None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs: list) -> None:
        filename = ""

        if list_objs == None:
            list_objs = []
        filename = cls.__name__ + ".json"

        with open(filename, 'w') as file:
            temp_list = [obj.to_dictionary() for obj in list_objs]
            json_string = Base.to_json_string(temp_list)
            file.write(json_string)

    def create(cls, **dictionary):
        pass
