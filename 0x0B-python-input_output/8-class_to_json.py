#!/usr/bin/python3
"""
This module defines a function that returns the dictionary
description for json serialization of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description for json serialization of
    obj.
    """

    return obj.__dict__