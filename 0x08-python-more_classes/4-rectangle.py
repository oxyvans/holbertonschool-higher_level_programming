#!/usr/bin/python3
"""Simple rectangle"""


class Rectangle:
    """an empty rectangle"""
    def __init__(self, width=0, height=0):
        """add settings"""
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

    def area(self):
        """area"""
        return self.height * self.width

    def perimeter(self):
        """perimeter"""
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """print"""
        res = ""
        if self.height == 0 or self.width == 0:
            return (res)
        else:
            for i in range(self.height):
                for j in range(self.width):
                    res += "#"
                if (i != self.height - 1):
                    res += "\n"
            return res

    def __repr__(self):
        """printable representation"""
        return ("Rectangle(" + str(self.width) + "," + str(self.height) + ")")
