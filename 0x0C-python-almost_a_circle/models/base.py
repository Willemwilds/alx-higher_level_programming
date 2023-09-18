#!/usr/bin/python3
"""
This module defines the Base class which other modules inherit from.
"""
import json


class Base:
    """
    This class is the class in which the triangle class inherits from
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        This function initializes the class attributes
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This function converts the list dictionaries to json string
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This function receives a lists of object and save them to a file
        """
        if list_objs is None:
            list_objs = []

        file_name = cls.__name__ + ".json"

        with open(file_name, mode='w', encoding='utf-8') as file:
            obj_list = [obj.to_dictionary() for obj in list_objs]
            json_str = cls.to_json_string(obj_list)
            file.write(json_str)

    @classmethod
    def create(cls, **dictionary):
        """
        This function creates a dummy instances of a class
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            return None

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Load instances from a JSON file and return a list of instances."""
        file_name = cls.__name__ + ".json"
        instance_list = []

        try:
            with open(file_name, mode='r', encoding='utf-8') as file:
                json_data = file.read()
                dict_list = json.loads(json_data)

                for item in dict_list:
                    instance = cls.create(**item)
                    instance_list.append(instance)

        except FileNotFoundError:
            pass  # If the file doesn't exist, return an empty list

        return instance_list
