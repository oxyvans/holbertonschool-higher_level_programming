#!/usr/bin/python3
""" Almost a circle """


from .rectangle import Rectangle


class Square(Rectangle):
    """ Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ init method """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ info """
        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """ size """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value
