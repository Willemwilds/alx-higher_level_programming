#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    keys = [x for x, y in a_dictionary.items() if y == value]
    for key in keys:
        del a_dictionary[key]
    return a_dictionary
