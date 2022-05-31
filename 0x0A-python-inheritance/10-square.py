#!/usr/bin/python3
""" Inheritance """


Rectangle = __import__('9-rectangle').Rectangle
"""imports class"""


class Square(Rectangle):
    """ square """

    def __init__(self, size):
        """ square """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area"""
        return self.__size * self.__size
