#!/usr/bin/python3
""" Almost a circle """


from .base import Base


class Rectangle(Base):
    """class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init method Rectangle """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def validation_pos(self, name, value):
        """ validaton pos """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def validation_size(self, name, value):
        """ validaton size """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    @property
    def width(self):
        """return width"""
        return self.__width

    @width.setter
    def width(self, width):
        """ validation """
        self.validation_size("width", width)
        self.__width = width

    @property
    def height(self):
        """return height"""
        return self.__height

    @height.setter
    def height(self, height):
        """ validation """
        self.validation_size("height", height)
        self.__height = height

    @property
    def x(self):
        """return x"""
        return self.__x

    @x.setter
    def x(self, x):
        """ validation """
        self.validation_pos("x", x)
        self.__x = x

    @property
    def y(self):
        """return y"""
        return self.__y

    @y.setter
    def y(self, y):
        """ validation """
        self.validation_pos("y", y)
        self.__y = y

    def area(self):
        """ area """
        return (self.width * self.height)

    def display(self):
        """ display """

        if (self.width == 0 or self.height == 0):
            print("")
        else:
            for n in range(self.y):
                print("")
            for i in range(self.height):
                for k in range(self.x):
                    print(" ", end="")
                for j in range(self.width):
                    print("#", end="")
                print("")

    def __str__(self):
        """ info """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format
                (self.id, self.x, self.y, self.width, self.height))

    
