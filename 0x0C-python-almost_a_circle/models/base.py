#!/usr/bin/python3
import json


class Base:
    """ The Base class for the other models
    Private Class Attributes:
    __nb_objects (int): This is the Number of instantiated bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        This is a class constructor.

        Args:
        id (int, optional): Unique identifier for the object. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): List of instances that inherit from Base.
        """
        if list_objs is None:
            list_objs = []

        file_name = cls.__name__ + ".json"
        json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])

        with open(file_name, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list represented by json_string.

        Args:
            json_string (str): JSON string representing a list of dictionaries.

        Returns:
            list: List represented by json_string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set.

        Args:
            **dictionary: Double pointer to a dictionary.

        Returns:
            Base: Instance with attributes set based on the provided dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)  # Creating a dummy Rectangle instance
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)  # Creating a dummy Square instance
        else:
            raise ValueError("Unsupported class for create method")

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances loaded from a file.

        Returns:
            list: List of instances loaded from the file.
        """
        file_name = cls.__name__ + ".json"

        try:
            with open(file_name, 'r') as file:
                json_string = file.read()
                list_of_dicts = cls.from_json_string(json_string)
                return [cls.create(**obj_dict) for obj_dict in list_of_dicts]
        except FileNotFoundError:
            return []

