#!/usr/bin/python3
"""
This module defines the function add_new_attribute.
"""


def add_new_attribute(obj, attr_name, attr_value):
    """
    This function adds new attribute to an object.
    """

    if not hasattr(obj, '__dict__') and not hasattr(type(obj), '__slots__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
