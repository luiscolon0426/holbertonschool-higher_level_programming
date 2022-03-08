#!/usr/bin/python3
def multiple_returns(sentence):
    data = [0, ""]

    data[0] = len(sentence)
    if data[0] == 0:
        data[1] = None
    else:
        data[1] = sentence[0:1]

    return tuple(data)
