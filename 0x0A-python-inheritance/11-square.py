#!/usr/bin/python3
"""
This module imports Rectangle class and creates Square class.
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """"
    The class inherits the Rectangle class.
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
