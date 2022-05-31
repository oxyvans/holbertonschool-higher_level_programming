#!/usr/bin/python3
""" Input/Output """


import json

def load_from_json_file(filename):
    """ task 6 """
    with open(filename, 'r', encoding="utf-8") as f:
         x = json.load(f)
    return x
