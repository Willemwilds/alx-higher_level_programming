#!/usr/bin/python3

"""
    This module deals creates Rectangle class.
"""


class Rectangle:
    """ Initialises width and height of Rectangle"""

    def __init__(self, width=0, height=0):
        """ Initialises width and height
        Args:
            width: width of the rectangle
            height: height of the rectangle
        Raises:
            TypeError: error if non integer is passed
            ValueError: error if value less tjan zero.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value
