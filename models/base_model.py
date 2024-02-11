#!/usr/bin/python3
"""
This module defines the BaseModel class,
which serves as the base class for all
other model classes, providing
common attributes/methods.
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    BaseModel defines common attributes and methods for other classes.
    Attributes are set dynamically via the __init__ method,
    allowing for instantiation from a dictionary representation.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel. If kwargs is provided,
        sets attributes according to key-value pairs within,
        excluding '__class__'. Otherwise, generates a new id
        and sets created_at and updated_at.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key in ('created_at', 'updated_at'):
                    # Convert string datetime to datetime object
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            now = datetime.now()
            self.created_at = now
            self.updated_at = now

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the 'updated_at' attribute to the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of
        the instance's __dict__, including the class name
        under '__class__' and converting datetime attributes
        to strings in ISO format.
        """
        dict_rep = self.__dict__.copy()
        dict_rep['__class__'] = self.__class__.__name__
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.updated_at.isoformat()
        return dict_rep
