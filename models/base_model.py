#!/usr/bin/python3
"""
This module defines the BaseModel class,
which serves as the base class for all
other model classes, providing
common attributes/methods.
"""

from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel:
    """
    BaseModel defines common attributes and methods for other classes.
    Attributes are set dynamically via the __init__ method,
    allowing for instantiation from a dictionary representation.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance. If creating from a dictionary (kwargs),
        set attributes accordingly. Otherwise, set default attributes and
        add instance to storage.
        """
        if kwargs:
            # Existing initialization from kwargs...
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)  # Add the new instance to storage

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Calls save() method of storage, updating the updated_at attribute.
        """
        self.updated_at = datetime.now()
        storage.save()

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
        return dict_repdef save(self):
        """
        Calls save() method of storage, updating the updated_at attribute.
        """
        self.updated_at = datetime.now()
        storage.save()
