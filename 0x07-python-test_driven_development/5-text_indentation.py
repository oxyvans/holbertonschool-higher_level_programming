#!/usr/bin/python3

def text_indentation(text):
    """text indentation"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    c = 0
    while(c < len(text)):
        if text[c] == '.' or text[c] == '?' or text[c] == ':':
            print(text[c])
            print()
            c += 1
            while(text[c] == ' '):
                c += 1
        else:
            print(text[c],end="")
            c += 1
