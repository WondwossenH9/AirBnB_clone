#!/usr/bin/python3
"""
User module.
Defines a User class that inherits from BaseModel.
"""

from models.base_model import BaseModel

class User(BaseModel):
    """Represents the User with email, password, first_name, and last_name attributes."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
