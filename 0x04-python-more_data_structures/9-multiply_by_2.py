#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    res = a_dictionary.copy()
    for key in res:
        res[key] *= 2
    return res
