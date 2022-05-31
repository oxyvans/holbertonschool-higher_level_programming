#!/usr/bin/python3
""" Input/Output """


class Student:
    """ class """

    def __init__(self, first_name, last_name, age):
        """ init """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ json """
        if type(attrs) is not list:
            return self.__dict__
        else:
            res = {}
            for i in attrs:
                if i in self.__dict__:
                    res[i] = self.__dict__[i]
            return res

    def reload_from_json(self, json):
        """ task 11 """
        if json:
            self.__dict__ = json
