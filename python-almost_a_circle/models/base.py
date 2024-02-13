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
        """
        Initializes an instance of the Base class.

        Parameters:
        - id (int): The identifier for the instance. If not
        provided, it is auto-generated.

        Returns:
        None
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries) -> str:
        """
        Converts a list of dictionaries to a JSON-formatted string.

        Parameters:
        - list_dictionaries (list): List of dictionaries to be converted.

        Returns:
        str: JSON-formatted string representing
        the list of dictionaries.
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string: str) -> list:
        """
        Converts a JSON-formatted string to a list of dictionaries.

        Parameters:
        - json_string (str): JSON-formatted string
        to be converted.

        Returns:
        list: List of dictionaries.
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs: list) -> None:
        """
        Saves a list of instances to a JSON file.

        Parameters:
        - list_objs (list): List of instances to be saved.

        Returns:
        None
        """

        if not list_objs:
            list_objs = []
        filename = cls.__name__ + ".json"

        with open(filename, 'w') as file:
            temp_list = [obj.to_dictionary() for obj in list_objs]
            json_string = Base.to_json_string(temp_list)
            file.write(json_string)

    @classmethod
    def create(cls, **dictionary) -> object:
        """
        Create a new obj from dictionary

        Parameters:
        - cls: class where this method call.
        - dictionary (dict): the dictionary to be obj

        Returns:
        cls instance
        """
        classname = cls.__name__
        dummy = {}
        if classname == "Square":
            dummy = cls(1)
        else:
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy
