#!/usr/bin/python3
""" Inheritance """


class MyInt(int):
    """ my int reloko """

    def __ne__(self, other):
        """ invertir ne """
        return True

    def __eq__(self, other):
        """ invertir eq """
        return False
