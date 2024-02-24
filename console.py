#!/usr/bin/python3
"""
Updated command interpreter to manage your application's objects.
"""

import cmd
from models import storage
from models.base_model import BaseModel
from shlex import split

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    class_names = ["BaseModel"]

    def do_quit(self, arg):
        """Quits the command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit program"""
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        args = split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.class_names:
            print("** class doesn't exist **")
            return
        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on class name and id."""
        args = split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.class_names:
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
        if args[0] not in self.class_names:
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
        """Prints all string representation of all instances based or not on class name."""
        args = split(arg)
        if args and args[0] not in self.class_names:
            print("** class doesn't exist **")
            return
        objects = storage.all()
        print_list = []
        for key in objects:
            if not args or args[0] == objects[key].__class__.__name__:
                print_list.append(str(objects[key]))
        print(print_list)

    def do_update(self, arg):
        """Updates an instance based on class name and id by adding or updating attribute."""
        args = split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.class_names:
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
        setattr(storage.all()[key], args[2], args[3])
        storage.all()[key].save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
