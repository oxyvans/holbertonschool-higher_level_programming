#!/usr/bin/python3
""" Inheritance """


def inherits_from(obj, a_class):
    """ Task 4 """
    return ((type(obj) != a_class) and (issubclass(type(obj), a_class)))
