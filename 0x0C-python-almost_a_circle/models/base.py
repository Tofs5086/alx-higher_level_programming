#!/usr/bin/python3

class Base:
    """ The Base class for the other models
    Private Class Attributes:
    __nb_objects (int): This is the Number of instantiated beses
    """

    __nb_objects = 0

    def __init__(self,id=None):
        """
        This is a class constructor.

        Args:
        id (int, optional):Unique identifier for the object. Defaults to none
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


