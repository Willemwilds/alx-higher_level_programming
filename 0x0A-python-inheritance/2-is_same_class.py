#!/usr/bin/python3

"""
This module creates function to determine if a particular
object is an instance of a specified class
"""


def is_same_class(obj, a_class):
    """
    Retruns True if obj is an instance of a_class,
    else returns False
    """

    return type(obj) is a_class
