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
        if attrs is None:
            return self.__dict__
        
        student_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                student_dict[attr] = getattr(self, attr)
            return student_dict
