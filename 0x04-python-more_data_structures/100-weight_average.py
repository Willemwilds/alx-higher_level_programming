#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    weight_sum = 0
    weights = 0

    for x, y in my_list:
        weight_sum += x * y
        weights += y

    if weights == 0:
        return 0

    return weight_sum / weights
