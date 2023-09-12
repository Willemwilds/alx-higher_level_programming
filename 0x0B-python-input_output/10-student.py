#!/usr/bin/python3
"""
This module creates the class Student.
"""


class Student:
    """
    This class initialises some class attributes and creates
    a public method
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if all(attrs) == str:
            for item in attrs:
                return self.__item__
        return self.__dict__
