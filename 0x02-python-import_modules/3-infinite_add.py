#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    arguments = sys.argv[1:]
    total = 0

    for num in arguments:
        total += int(num)
    print("{:d}".format(total))
