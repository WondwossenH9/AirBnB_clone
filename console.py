#!/usr/bin/python3
"""
Command interpreter module for managing application objects.
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from shlex import split

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    class_dict = {
        "BaseModel": BaseModel,
        "User": User,
    }

    def do_quit(self, arg):
        """Quits command to exit program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit program"""
        print("")
        return True

    def emptyline(self):
        """Do nothing upon receiving empty line."""
        pass

    def do_create(self, arg):
        """Creates new instance of BaseModel, saves it to the JSON file, and prints the id."""
        args = split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.class_dict:
            print("** class doesn't exist **")
            return
        new_instance = self.class_dict[args[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Shows the string representation of an instance based on class name and id."""
        args = split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.class_dict:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id."""
        args = split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.class_dict:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representations of all instances based or not on class name."""
        args = split(arg)
        if args and args[0] not in self.class_dict:
            print("** class doesn't exist **")
            return
        print_list = [str(obj) for key, obj in storage.all().items() if not args or key.startswith(args[0])]
        print(print_list)

    def do_update(self, arg):
        """Updates an instance based on class name and id by adding or updating attribute."""
        args = split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.class_dict:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        instance = storage.all()[key]
        setattr(instance, args[2], args[3])
        instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
