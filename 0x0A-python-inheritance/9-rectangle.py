#!/usr/bin/python3
"""
This module imports BaseGeometry class and creates Rectangle classes
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """"
    The class inherits the BaseGeometry class.
    """

    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
