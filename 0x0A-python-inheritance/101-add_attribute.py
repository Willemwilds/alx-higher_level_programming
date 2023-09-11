#!/usr/bin/python3
"""
This module defines the function add_new_attribute.
"""


def add_new_attribute(obj, name, value):
    """
    This function adds new attribute to an object.
    """

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
