#!/usr/bin/python3
"""
Initializes the models package and sets up the storage system.
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
