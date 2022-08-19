#!/usr/bin/python3
""" task 2"""

from sys import argv
import urllib.parse
import urllib.request


if __name__ == "__main__":
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
