#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(idx):
        return my_list
    else: 
        my_list.insert(idx, element)
        return my_list