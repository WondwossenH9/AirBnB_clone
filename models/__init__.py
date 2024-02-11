#!/usr/bin/python3
from models.engine.file_storage import FileStorage
"""
Initializes the package, creating an instance of
FileStorage and reloading existing objects
from the JSON file.
"""


storage = FileStorage()
storage.reload()

from models import storage


class BaseModel:
    # Existing definitions...

    def save(self):
        """
        Calls save() method of storage, updating
        the updated_at attribute.
        """
        self.updated_at = datetime.now()
        storage.save()

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance. If creating from a
        dictionary (kwargs), set attributes accordingly.
        Otherwise, set default attributes and
        add instance to storage.
        """
        if kwargs:
            # Existing initialization from kwargs...
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)  # Add the new instance to storage
