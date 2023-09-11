#!/usr/bin/python3
"""
This module imports BaseGeometry class and creates Rectangle classes
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class inherits from BaseGeometry class.
    """

    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
