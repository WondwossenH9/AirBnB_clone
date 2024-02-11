#!/usr/bin/python3
"""
Initializes the package, creating an
instance of FileStorage and reloading
existing objects from the JSON file.
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
