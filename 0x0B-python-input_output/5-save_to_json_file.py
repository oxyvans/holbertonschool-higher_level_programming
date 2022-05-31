#!/usr/bin/python3
""" Input/Output """


import json


def save_to_json_file(my_obj, filename):
    """task 5 """
    with open(filename, 'w', encoding="utf-8") as f:
        x = json.dumps(my_obj)
        f.write(x)
