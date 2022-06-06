#!/usr/bin/python3
""" Almost a circle """


import json


class Base:
    """ base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ init method """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to json string """
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ salve """
        lis = []
        for i in list_objs:
            lis.append(cls.to_dictionary(i))
        res = cls.to_json_string(lis)
        filename = ("{}.json".format(cls.__name__))

        with open(filename, "w", encoding="utf-8") as f:
            f.write(res)
