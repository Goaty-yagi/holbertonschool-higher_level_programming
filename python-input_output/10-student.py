#!/usr/bin/python3

""" This module provides Student class.
"""


class Student:
    """ This class create student instance.
    Args:
        - first_name(str): it representing first name.
        - last_name(str): it representing last_name.
        - age (int): it representing student age.
    Methods:
        - to_json(self, attrs: any): If attrs is a list of strings, only
        attribute names contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs: any = None) -> dict:
        retrieve_dict = self.__dict__
        if isinstance(attrs, list) and all(isinstance(attr, str)
                                           for attr in attrs):
            retrieve_dict = {key: value for key,
                             value in retrieve_dict.items() if key in attrs}
        return retrieve_dict
