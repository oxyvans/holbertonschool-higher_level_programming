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
