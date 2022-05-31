#!/usr/bin/python3
""" Input/Output """


def write_file(filename="", text=""):
    """ task 1 """
    with open('filename', 'w', encoding="utf-8") as f:
        w = f.write(text)
    return w
