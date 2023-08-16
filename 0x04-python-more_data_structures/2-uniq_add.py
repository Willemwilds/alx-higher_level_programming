#!/usr/bin/python3

def uniq_add(my_list=[]):
    elements = set(my_list)
    total = 0
    for num in elements:
        total = total + num
    return total
