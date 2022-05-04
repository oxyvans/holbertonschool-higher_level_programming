#!/usr/bin/python3
def search_replace(my_list, search, replace):
    res = my_list.copy()
    for i in range(len(my_list)):
        if my_list[i] is search:
            res[i] = replace
    return(res)
