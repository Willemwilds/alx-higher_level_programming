#!/usr/bin/python3
"""
This module defines MyInt class.
"""


class MyInt(int):

    """
    Returns opposite values of the operators '==' and '!='
    """
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
