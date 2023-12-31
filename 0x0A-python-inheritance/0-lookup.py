#!/usr/bin/python3
"""
This module creates the lookup function.
"""


def lookup(obj):
    """
    Returns list of available attributes and methods
    of an object.
    """

    return dir(obj)
