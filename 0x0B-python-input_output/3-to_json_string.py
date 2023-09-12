#!/usr/bin/python3
"""
This module creates a function that converts python object
to JSON string.
"""
import json


def to_json_string(my_obj):
    """
    Returns the json representatio of an object"
    """
    return json.dumps(my_obj)
