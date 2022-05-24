#!/usr/bin/python3

def text_indentation(text):
    """text indentation"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = False
    for c in text:
        if not flag:
            if c == ' ':
                continue
            else:
                flag = True
        if flag:
            if c == '.' or c == '?' or c == ':':
                print(c)
                print()
                flag = False
            else:
                print(c, end="")
