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

        sorted_list = sorted(self)

        for item in sorted_list:
            print(item, end=' ')
        print()
