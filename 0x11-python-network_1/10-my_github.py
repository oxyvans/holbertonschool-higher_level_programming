#!/usr/bin/python3
""" task 10 """

import requests
from sys import argv

if __name__ == "__main__":
    credentials = (argv[1], argv[2])
    r = requests.get('https://api.github.com/user', auth=credentials)
    print(r.json().get('id'))
