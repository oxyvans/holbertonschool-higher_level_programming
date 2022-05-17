#!/usr/bin/python3
"""first class"""


class Square:
    """square whit size"""

    def __init__(self, size=0, position=(0, 0)):
        """optional"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """return pos"""
        return self.__position

    @position.setter
    def position(self, value):
        """checks"""
        if ((type(value) is not tuple) or (len(value) != 2) or
                (type(value[0]) is not int) or (value[0] < 0) or
                (type(value[1]) is not int) or (value[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """area"""
        return self.__size * self.__size

    def my_print(self):
        """print square"""
        if self.size == 0:
            print("")
        else:
            for n in range(self.position[1]):
                print("")
            for i in range(self.size):
                for s in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print("")

    def __str__(self):
        """print"""
        for n in range(self.position[1]):
            print("")
        for i in range(self.size):
            for s in range(self.position[0]):
                print(" ", end="")
            for j in range(self.size):
                print("#", end="")
            if (i != self.size - 1):
                print("")
        return("")
