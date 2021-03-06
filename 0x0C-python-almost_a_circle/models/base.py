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
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ salve """
        lis = []
        if list_objs is None:
            list_objs = []
        for i in list_objs:
            lis.append(cls.to_dictionary(i))
        res = cls.to_json_string(lis)
        filename = ("{}.json".format(cls.__name__))

        with open(filename, "w", encoding="utf-8") as f:
            f.write(res)

    @staticmethod
    def from_json_string(json_string):
        """ from j a s """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ create """
        if cls.__name__ == "Rectangle":
            res = cls(1, 1)
        elif cls.__name__ == "Square":
            res = cls(1)
        res.update(**dictionary)
        return res

    @classmethod
    def load_from_file(cls):
        """ load from file """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, encoding="utf-8") as f:
                info = f.read()
        except FileNotFoundError:
            return []
        lis = cls.from_json_string(info)
        ins = []
        for i in lis:
            ins.append(cls.create(**i))
        return ins
