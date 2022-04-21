#!/usr/bin/python3
'''
function that finds a peak in a list of unsorted integers
'''


def find_peak(list_of_integers):
    '''
    finds a peak in a list of unsorted integers
    '''
    li = list_of_integers
    if len(li) == 0:
        return None
    if len(li) == 1:
        return
    if li[0] >= li[1]:
        return li[0]
    elif li[-1] >= li[-2]:
        return li[-1]
    for i in range(1, len(li) - 1):
        if li[i] >= li[i - 1] and li[i] >= li[i + 1]:
            return li[i]
