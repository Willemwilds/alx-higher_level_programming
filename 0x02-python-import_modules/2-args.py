#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    import os

    argument = sys.argv
    length = len(argument) - 1

    if length < 1:
        print("{:d} arguments.".format(length))
    elif length == 1:
        print("{:d} argument:\n{}: {}".format(length, length, argument[1]))
    else:
        print("{:d} arguments:".format(length))
        for i in argument[1:]:
            print("{:d}: {}".format(argument.index(i), i))
