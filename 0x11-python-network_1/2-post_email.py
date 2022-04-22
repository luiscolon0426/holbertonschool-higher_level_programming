#!/usr/bin/python3
''' Write a Python script that takes in a URL
and an email, sends a POST request to the
passed URL with the email as a parameter,
and displays the body of the response
(decoded in utf-8)
'''

from urllib import request
from urllib import parse
from sys import argv


if __name__ == "__main__":
    email = {"email": argv[2]}
    req = request.Request(argv[1], parse.urlencode(email).encode('UTF-8'))
    try:
        with request.urlopen(req) as response:
            data = response.read()
            print("{}".format(data.decode("UTF-8")))
    except ConnectionRefusedError:
        pass
