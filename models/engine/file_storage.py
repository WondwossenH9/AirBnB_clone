#!/usr/bin/python3
"""
Module to serialize instances to a JSON file and deserialize JSON file to instances.
"""

import json

class FileStorage:
    """
    Handles the serialization and deserialization of BaseModel instances.
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
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes objects to the JSON file.
        """
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    def reload(self):
        """
        Deserializes JSON file to objects, if file exists.
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objects = json.load(f)
                from models.base_model import BaseModel  # Import here to avoid circular import
                for k, v in objects.items():
                    cls_name = v['__class__']
                    if cls_name == 'BaseModel':
                        obj = BaseModel(**v)
                        FileStorage.__objects[k] = obj
        except FileNotFoundError:
            pass
