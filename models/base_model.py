#!/usr/bin/python3
"""
This module defines the BaseModel class, which serves as the base class for all
other model classes, providing common attributes and methods.
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    BaseModel defines common attributes and methods for other classes.

    Attributes:
        id (str): Unique identifier for each instance, using UUID4.
        created_at (datetime): The datetime when an instance is created.
        updated_at (datetime): The datetime when an instance is last updated.
    """

    def __init__(self):
        """
        Initializes a new instance of the BaseModel class, setting the id,
        created_at, and updated_at attributes.
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance, including
        the class name, id, and dictionary of attributes.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at attribute to the current datetime, indicating
        when the object was last modified.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the instance's
        __dict__, including the class name under '__class__' key, and
        converting datetime attributes to strings in ISO format.
        """
        dict_rep = self.__dict__.copy()
        dict_rep['__class__'] = self.__class__.__name__
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.updated_at.isoformat()
        return dict_rep
