#!/usr/bin/python3
"""
This module defines a function that converts json string
to python object.
"""
import json


def from_json_string(my_str):
    """
    Returns a python object represented by json string.
    """

    return json.load(my_str)
