#!/usr/bin/python3
"""Inheritance"""


def add_attribute(mc, name, other):
    """attribute"""
    if hasattr(mc, '__dict__'):
        setattr(mc, name, other)
    else:
        raise TypeError("can't add new attribute")
