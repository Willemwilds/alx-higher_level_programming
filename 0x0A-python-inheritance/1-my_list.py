#!/usr/bin/python3
"""
This module creates a MyList class that inherits from list
"""


class MyList:
    """
    creates MyList class
    """

    def print_sorted(self):
        """
        This function prints the list in ascending order.
        """

        print(sorted(self))
