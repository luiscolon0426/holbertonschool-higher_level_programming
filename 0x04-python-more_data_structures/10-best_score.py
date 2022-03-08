#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    return sorted(a_dictionary, key=a_dictionary.get)[-1]
