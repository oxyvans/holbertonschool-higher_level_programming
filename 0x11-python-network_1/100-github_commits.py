#!/usr/bin/python3
""" task 100 """

from sys import argv
from requests import get


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    r = requests.get(url)
    commits = r.json()
    for i in range(10):
        print(commits.get('sha'), end=': ')
        print(commits.get('commit').get('author').get('name'))
