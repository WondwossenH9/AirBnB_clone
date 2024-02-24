#!/usr/bin/python3
"""
Module to serialize instances to a JSON file and deserialize JSON file to instances.
"""

import json
from models.base_model import BaseModel
from models.user import User  # Import additional models here

class FileStorage:
    """
    Handles the serialization and deserialization of BaseModel instances and subclasses.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns dictionary of objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds an object to internal objects dictionary.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes objects to the JSON file.
        """
        obj_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes JSON file to objects, if the file exists.
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
            for obj_id, obj_data in obj_dict.items():
                cls_name = obj_data['__class__']
                cls = globals()[cls_name]  # Dynamically get class from globals()
                self.__objects[obj_id] = cls(**obj_data)
        except FileNotFoundError:
            pass
