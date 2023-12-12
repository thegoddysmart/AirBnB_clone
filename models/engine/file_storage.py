#!/usr/bin/python3
"""file_storage.py module"""
from models.base_model import BaseModel
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.review import Review
from models.state import State
from models.user import User
import json


class FileStorage():
    """
    FileStorage class:
    """
    __file_path = "file.json"
    __objects = {}

    def save(self):
        """
        A public instance module that serializes __objects
        to JSON file (path: __file_path)
        Variables:
        new_dict [dict] -- keys, values to build JSON.
        """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict().copy()
        with open(FileStorage.__file_path, mode='w') as my_file:
            json.dump(new_dict, my_file)

    def new(self, obj):
        """
        A public instance module that sets in __objects
        the obj with key <obj class name>.id
        Variables:
        key [str] -- key generated
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def all(self):
        """
        A public instance method to return the
        dictionary __objects.
        """
        return FileStorage.__objects

    def reload(self):
        """
        A public instance module for deserializing a JSON
        file to __objects
        """
        try:
            with open(FileStorage.__file_path, mode='r') as my_file:
                new_dict = json.load(my_file)

            for key, value in new_dict.items():
                class_name = value.get('__class__')
                obj = eval(class_name + '(**value)')
                FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass

