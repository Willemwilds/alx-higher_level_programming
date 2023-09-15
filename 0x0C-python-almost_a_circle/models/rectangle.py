#!/usr/bin/python3
"""
This module defines the Rectangle class
"""


class Rectangle(Base):
    """
    This class inherits from the Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super.__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            return self.__width

        @setter.width
        def width(self, value):
            if type(value) != int:
                raise TypeError("{}must be an integer".format(value))
            self.__width = value

        @property
        def height(self):
            return self.height = __height

        @setter.height
        def height(self, value):
            self.__height = value

        @property
        def x(self):
            self.x = __x

        @setter.x
        def x(self, value):
            self.__x = value

        @property
        def y(self):
            return self.__y

        @setter.y
        def y(self, value):
            self.__y = value
