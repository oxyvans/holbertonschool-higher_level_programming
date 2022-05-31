#!/usr/bin/python3
""" Inheritance """


Rectangle = __import__('9-rectangle').Rectangle
"""imports class"""


class Square(Rectangle):
    """ square """

    def __init__(self, size):
        """ square """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
