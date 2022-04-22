#!/usr/bin/python3
'''
Write a Python script that takes your
GitHub credentials (username and password)
and uses the GitHub API to display your id
'''
import requests
import sys
if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    url = 'https://api.github.com/user'
    req = requests.get(url, auth=(user, passwd))
    print(req.json().get('id'))
