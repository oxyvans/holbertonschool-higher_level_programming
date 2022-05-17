#!/usr/bin/python3
"""first class"""


class Square:
    """square whit size"""
    
    def __init__(self, size=0):
        """add size"""
        self.__size = size

    @property
    def size(self):
        """return size"""
        return self.__size

    @size.setter
    def size(self, value):
        """check and add size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area"""
        return self.__size * self.__size
