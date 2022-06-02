#!/usr/bin/python3
""" Almost a circle """

class Base:
    """ base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ init method """
        if id == None:
            Base.__nb_objects += 1
            self.id =  Base.__nb_objects
        else:
            self.id = id
