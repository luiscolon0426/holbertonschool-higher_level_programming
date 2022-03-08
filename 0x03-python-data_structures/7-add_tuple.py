#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = [0, 0]

    for a in range(2):
        try:
            new_tuple[a] += tuple_a[a]
        except:
            new_tuple[a] += 0
        try:
            new_tuple[a] += tuple_b[a]
        except:
            new_tuple[a] += 0

    return tuple(new_tuple)
