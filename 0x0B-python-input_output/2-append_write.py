#!/usr/bin/python3
""" Input/Output """


def append_write(filename="", text=""):
    """ task 2 """
    with open(filename, 'a', encoding="utf-8") as f:
        a = f.write(text)
    return a
