#!/usr/bin/python 3
"""firstly defines the rectangle class"""


class Rectangle:
    """This represents the Rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """This gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("The width should be an integer")
        elif vaule < 0:
            raise ValueError("The width mut be greater than 0")
        else:
            self.__width = value


    @propert
    def height(self):
        """This gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(vale, int):
            raise TypeError("The height must be an interger")
        elif value < 0:
            raise ValueError("The height must be greater than 0")
        else:
            self.__height = value
