#!/usr/bin/python3
"""
This module creates the BaseGeometry class.
"""


class BaseGeometry:
    """
    This class defines a public instance method - area and integer_validator
    """

    def area(self):
        """
        Raises an Exception
        """

        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Raises TypeError if 'value' is not an integer.
        Raises ValueError if value is less than or equal to 0.
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        