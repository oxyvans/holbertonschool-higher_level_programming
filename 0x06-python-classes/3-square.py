#!/usr/bin/python3
"""first class"""


class Square:
    """square whit size"""

    def __init__(self, size=0):
        """check and add size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area"""
        return self.__size * self.__size
