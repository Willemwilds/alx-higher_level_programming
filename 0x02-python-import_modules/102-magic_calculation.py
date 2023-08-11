#!/usr/bin/python3

def magic_calculation(a, b):
    from magic_calculation-102_ import add, sub

    if a < b:
        c = add(a, b)
        for x in range(4, 6):
            c = add(c, x)
        return c
    else:
        return sub(a, b)
