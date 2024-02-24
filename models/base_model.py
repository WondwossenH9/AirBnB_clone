#!/usr/bin/python3
"""
Updated module to define the BaseModel class to
support creation from dictionary representation.
"""

import uuid
from datetime import datetime

class BaseModel:
    """
    Defines base model with common attributes and methods for other classes.
    Also supports initialization from a dictionary.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.Dynamic initialization
        from a dictionary through **kwargs, ignoring '__class__' key and converting
        datetime strings back to datetime objects for 'created_at' and 'updated_at'.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key in ['created_at', 'updated_at']:
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of BaseModel instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the 'updated_at' attribute with current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance,
        with datetime attributes converted to strings in ISO format and adding the
        '__class__' key with class name of the object.
        """
        dict_rep = self.__dict__.copy()
        dict_rep["__class__"] = self.__class__.__name__
        dict_rep["created_at"] = dict_rep["created_at"].isoformat()
        dict_rep["updated_at"] = dict_rep["updated_at"].isoformat()
        return dict_rep
