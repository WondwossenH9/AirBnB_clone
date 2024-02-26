#!/usr/bin/python3
...
from models.user import User

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project."""
    ...
    class_dict = {
        "BaseModel": BaseModel,
        "User": User
    }
    ...
    # Implement create, show, destroy, all, update as before,
    # now including support for User.

