#!/usr/bin/python3


def add_new_attribute(obj, attr_name, attr_value):
    if not hasattr(obj, '__dict__') and not hasattr(type(obj), '__slots__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
