#!/usr/bin/python3

def max_integer(my_list=[]):
    max = 0
    if not(my_list) or len(my_list) == 0:
        return (None)
    for n in range(len(my_list)):
        if max < my_list[n]:
            max = my_list[n]
    return (max)
