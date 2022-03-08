#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is not None:

        new = my_list.copy()

        for a in range(len(my_list)):
            if my_list[a] % 2 == 0:
                new[a] = True
            else:
                new[a] = False

        return (new)
