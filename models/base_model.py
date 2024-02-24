#!/usr/bin/python3
"""
This module defines the BaseModel class which serves as the base class
for all other classes including common attributes
and methods that will be inherited by other classes.
"""

import uuid
from datetime import datetime

class BaseModel:
    """
    Defines base model with common attributes and methods for other classes.
    Attributes are id, created_at, and updated_at. It also provides methods to
    update attributes and convert object properties to a dictionary.
    """

    def __init__(self):
        """
        Initializes a new instance of BaseModel, setting the id, created_at,
        and updated_at attributes.
        """
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance.
        Also adds the __class__ key with the class name of the object and
        change datetime attributes to strings in ISO format.
        """
        dict_rep = self.__dict__.copy()
        dict_rep["__class__"] = self.__class__.__name__
        dict_rep["created_at"] = dict_rep["created_at"].isoformat()
        dict_rep["updated_at"] = dict_rep["updated_at"].isoformat()
        return dict_rep
