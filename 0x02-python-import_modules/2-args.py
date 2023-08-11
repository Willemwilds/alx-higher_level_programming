#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    argument = sys.argv
    length = len(argument) - 1

    if length < 1:
        print("{} arguments.".format(length))
    elif length == 1:
        print("{} argument:\n{}: {}".format(length, length, argument[1]))
    else:
        print("{} arguments:".format(length))
        for i in argument:
            print("{}: {}".format(argument[i], i]))
