#!/usr/bin/pytho3
''' module with find_peak '''


def find_peak(list_of_integers):
    """ comment """
    li = list_of_integers
    l = len(li)
    if l == 0:
        return
    m = l // 2
    if (m == l - 1 or li[m] >= li[m + 1]) and (m == 0 or li[m] >= li[m - 1]):
        return li[m]
    if m != l - 1 and li[m + 1] > li[m]:
        return find_peak(li[m + 1:])
    return find_peak(li[:m])
