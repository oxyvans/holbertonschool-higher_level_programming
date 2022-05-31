#!/usr/bin/python3
""" Input/Output """


from sys import *


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
filename = "add_item.json"

try:
    lis = load_from_json_file(filename)
except FileNotFoundError:
    lis = []

res = lis + argv[1:]
save_to_json_file(res, filename)
