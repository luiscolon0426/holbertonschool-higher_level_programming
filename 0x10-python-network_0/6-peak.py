#!/usr/bin/python3
''' module with find_peak '''


def find_peak(list_of_integers):
    """ comment """
    li = list_of_integers
    leng = len(li)
    if leng == 0:
        return None
    if leng == 1:
        return
    if li[0] >= li[1]:
        return li[0]
    elif li[-1] >= li[-2]:
        return li[-1]
    for i in range(1, leng - 1):
        if li[i] >= li[i - 1] and li[i] >= li[i + 1]:
            return li[i]
