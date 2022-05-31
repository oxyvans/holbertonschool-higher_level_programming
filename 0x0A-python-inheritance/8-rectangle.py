#!/usr/bin/python3
""" Inheritance """

BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""import class"""


class Rectangle(BaseGeometry):
    """ Rectangle """
    def __init__(self, width, height):
        """init"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
