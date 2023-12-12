#!/usr/bin/python3
"""file_storage.py module"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place


class FileStorage():
    """
    FileStorage class,
    """
    __file_path = "file.json"
    __objects = {}



    def all(self):
        """
        Returns our dictionary __objects.
        """
        return self.__objects

    def save(self):
        """
        Serializes __objects to our JSON file (path: __file_path).
        """
        new_dict = {key: value.to_dict() for key, value in
                    self.__objects.items()}
        with open(self.__file_path, mode='w') as my_file:
            json.dump(new_dict, my_file)

    def new(self, obj):
        """
        Sets in __objects obj with key <obj class name>.id
        """
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj
    
    def reload(self):
        """
        Deserializes our JSON file to __objects.
        """
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, mode='r') as my_file:
                    new_dict = json.load(my_file)

                for key, value in new_dict.items():
                    class_name = value.get('__class__')
                    obj = eval(f"{class_name}(**value)")
                    self.__objects[key] = obj

            except FileNotFoundError:
                pass

