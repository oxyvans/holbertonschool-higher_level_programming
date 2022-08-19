#!/usr/bin/python3
""" task 4 """
from requests import get


if __name__ == "__main__":
    r = get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
