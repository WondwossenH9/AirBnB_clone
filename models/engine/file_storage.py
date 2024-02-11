#!/usr/bin/python3
"""
Defines the FileStorage class that serializes the
instances to a JSON file and
deserializes JSON file to instances.
"""

import json
from models.base_model import BaseModel


class FileStorage:
    """
    Serializes instances to a JSON file
    and deserializes the JSON file
    to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with
        key <obj class name>.id.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON
        file (path: __file_path).
        """
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects and
        (if file exists, otherwise do nothing).
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objects = json.load(f)
            for key, value in objects.items():
                cls_name = key.split(".")[0]
                if cls_name == "BaseModel":
                    obj = BaseModel(**value)
                # Extend with other classes as needed
                FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
