#!/usr/bin/python3
""" task 6 """

from sys import argv
from requests import post


if __name__ == "__main__":
    value = {"email": argv[2]}
    r = post(argv[1], data=value)
    print(r.text)
