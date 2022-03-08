#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_lis = []
    _2_ = search
    _84_ = replace
    for i in my_list:
        if i == _2_:
            new_lis.append(_84_)
        else:
            new_lis.append(i)
    return new_lis
