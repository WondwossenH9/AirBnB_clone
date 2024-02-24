#!/usr/bin/python3
"""Defines a BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents a BaseModel for HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initializes new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): A key/value pair of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for m, n in kwargs.items():
                if m == "created_at" or m == "updated_at":
                    self.__dict__[m] = datetime.strptime(n, tform)
                else:
                    self.__dict__[m] = n
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at to current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return dictionary of BaseModel instance.

        Including key/value pair __class__ representing
        class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Returns print/str representation of BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
