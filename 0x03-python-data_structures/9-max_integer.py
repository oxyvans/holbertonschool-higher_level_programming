#!/usr/bin/python3

def max_integer(my_list=[]):
    if not(my_list) or len(my_list) == 0:
        return (None)
    max = my_list[0]
    for n in range(len(my_list)):
        if max < my_list[n]:
            max = my_list[n]
    return (max)
