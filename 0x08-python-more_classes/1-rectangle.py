#!/usr/bin/python3
"""Simple rectangle"""


class Rectangle:
    """an empty rectangle"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        """return height"""
        return self.__height

    @height.setter
    def height(self, value):
        """check and add size"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """return width"""
        return self.__width

    @width.setter
    def width(self, value):
        """check and add size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
