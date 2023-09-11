#!/usr/bin/python3
"""
This module defines a function which checks if a class if a
subclass of another class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is a subclass of a_class, otherwise
    false.
    """

    return type(obj) != a_class and isinstance(obj, a_class)
