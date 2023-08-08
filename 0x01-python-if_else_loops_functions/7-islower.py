#!/usr/bin/python3

def islower(c):
    if not c.isidentifier():
        if c.islower():
            return True
        else:
            return False
