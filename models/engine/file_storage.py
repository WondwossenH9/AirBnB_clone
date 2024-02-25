#!/usr/bin/python3
"""
This module defines the class FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances.
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """A class that serializes instances to a JSON file and deserializes JSON file to instances."""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj:
            self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Serializes __objects to JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as f:
            json.dump({obj_id: obj.to_dict() for obj_id, obj in self.__objects.items()}, f)

    def reload(self):
        """Deserializes JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                objs = json.load(f)
            for obj_id, obj_data in objs.items():
                cls_name = obj_data['__class__']
                cls = eval(cls_name)  # Use eval to dynamically instantiate objects based on cls_name
                self.__objects[obj_id] = cls(**obj_data)
        except FileNotFoundError:
            pass
