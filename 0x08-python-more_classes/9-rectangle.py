#!/usr/bin/python3
"""Simple rectangle"""


class Rectangle:
    """an empty rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """add settings"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                    res += str(self.print_symbol)
                if (i != self.height - 1):
                    res += "\n"
            return res

    def __repr__(self):
        """printable representation"""
        return ("Rectangle(" + str(self.width) + ", " + str(self.height) + ")")

    def __del__(self):
        """delete"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """biggest rectangle"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """cls == Rectangle, the first parameter of @classmethod is a class"""
        return cls(size, size)
