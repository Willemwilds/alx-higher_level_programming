#!/usr/bin/python3
"""
This module defines the function add_new_attribute.
"""


def add_new_attribute(obj, name, value):
    """
    This function adds new attribute to an object.
    """

    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")