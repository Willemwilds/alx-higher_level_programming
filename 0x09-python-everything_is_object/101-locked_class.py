#!/usr/bin/python3

"""This module defines LockedClass"""


class LockedClass:
    """
        This class prevents the
        creation of other instances except
        first_name
    """

    __slots__ = ["first_name"]
