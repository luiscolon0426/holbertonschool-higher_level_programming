#!/usr/bin/python3
''' Write a Python script that fetches
https://intranet.hbtn.io/status
'''

from urllib import request


if __name__ == "__main__":
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        data = response.read()
        print("Body response:")
        print("    - type: {}".format(type(data)))
        print("    - content: {}".format(data))
        print("    - utf8 content: {}".format(data.decode("UTF-8")))
