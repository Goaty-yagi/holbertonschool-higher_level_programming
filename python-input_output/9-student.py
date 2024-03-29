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
        - to_json(self): Return dict retrieved from the instance.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
