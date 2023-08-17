#!/usr/bin/python3

def best_score(a_dictionary):
    largest = max(a_dictionary.values())
    for key in a_dictionary:
        if a_dictionary[key] == largest:
            return key
        else:
            return None
