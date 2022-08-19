#!/usr/bin/python3
""" task 5"""

from sys import argv
from requests import get


if __name__ == "__main__":
    r = get(argv[1])
    print(r.headers.get("X-Request-Id"))
