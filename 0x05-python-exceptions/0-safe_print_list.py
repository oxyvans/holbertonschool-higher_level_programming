#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0
    nb_print = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            nb_print += 1
        except (ValueError, TypeError, IndexError):
            continue
    print("")
    return nb_print
