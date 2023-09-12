#!/usr/bin/python3
"""
This module defines a function that creates an object from
a json file.
"""
import json


def load_from_json_file(filename):
    """
    Returns a python object from the json string.
    """

    with open(filename, 'w') as file:
        python_file = json.load(file)
        return python_file
