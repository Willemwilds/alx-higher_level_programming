#!/usr/bin/python3
"""
This module creates the Baee class
"""
import json


class Base:
    """
    The class defines objects ids.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        A static method that converts dictionaries to json
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves the class instances to a file
        """

        if list_objs is None:
            list_objs = []

    file_name = cls.__name__ + ".json"

    with open(filename, "w") as file:
        obj_list = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(obj_list)
        file.write(json_str)

    @classmethod
    def create(cls, **dictionary):
        """
        The class method creates a dummy instance
        """

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dunmmy = cls(1)
        else:
            return None

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        The class method loads class instances from file
        """

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
            pass

        return instance_list
