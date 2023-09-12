#!/usr/bin/python3
"""
This module defines a function that writes an object to a
text file using json representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Returns a json file of the object.
    """
    with open(filename, 'w') as json_file:
        return json.dump(my_obj, json_file)
