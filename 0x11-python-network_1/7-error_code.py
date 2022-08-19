#!/usr/bin/python3
"""sends a request to the passed URL and displays the body of the response"""
from sys import argv
from requests import get


if __name__ == "__main__":
    r = get(argv[1])
    if r.status_code < 400:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
