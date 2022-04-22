#!/usr/bin/python3
'''
Write a Python script that fetches
https://intranet.hbtn.io/status
'''
from requests import get


if __name__ == "__main__":

    resp = get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(resp.text)))
    print("\t- content: {}".format(resp.text))
