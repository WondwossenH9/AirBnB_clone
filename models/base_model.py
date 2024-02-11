#!/usr/bin/python3
"""
Defines the BaseModel class.
"""

from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """Defines all common attributes/methods
    for other classes."""

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key in ('created_at', 'updated_at'):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """Updates updated_at with current datetime
        and saves to file."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all
        keys/values of __dict__."""
        dict_rep = dict(self.__dict__)
        dict_rep['__class__'] = self.__class__.__name__
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.updated_at.isoformat()
        return dict_rep

    def __str__(self):
        """Returns the string representation
        of the BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
