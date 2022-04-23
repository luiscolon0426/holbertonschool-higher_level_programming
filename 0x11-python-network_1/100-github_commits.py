#!/usr/bin/python3
"""
Python script that shows the last 10 commits of a repository
in GitHub
"""
import requests
import sys


if __name__ == "__main__":

    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(sys.argv[2], sys.argv[1]))
    if r.status_code >= 400:
        print('None')
    else:
        for com in r.json()[:10]:
            print("{}: {}".format(com.get('sha'),
                                  com.get('commit').get('author').get('name')))
