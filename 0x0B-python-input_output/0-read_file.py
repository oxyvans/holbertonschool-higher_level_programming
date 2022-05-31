#!/usr/bin/python3
""" Input/Output """


def read_file(filename=""):
    """ task 0 """
    with open('filename', 'r', encoding="utf-8") as f:
        r = f.read()
    print(r)
