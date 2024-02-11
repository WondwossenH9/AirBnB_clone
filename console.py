#!/usr/bin/python3
"""
Module for command interpreter to manage application's objects.
"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    class_dict = {
        "BaseModel": BaseModel,
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, arg):
        """Create new instance of BaseModel, saves it, and print id."""
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.class_dict:
            print("** class doesn't exist **")
            return
        instance = self.class_dict[arg]()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Print string representation based on class name and id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in self.class_dict:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in self.class_dict:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Print string representation of
        all instances based on or not on the class name.
        """
        if arg and arg not in self.class_dict:
            print("** class doesn't exist **")
            return
        instances = storage.all().values()
        if arg:
            instances = [instance for instance in instances
                         if instance.__class__.__name__ == arg]
        for instance in instances:
            print(instance)

    def do_update(self, arg):
        """Updates instance by class name and id by
        adding, updating attribute."""
        args = arg.split()
        if not arg:
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
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        instance = storage.all()[key]
        setattr(instance, args[2], args[3].strip('"'))
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
