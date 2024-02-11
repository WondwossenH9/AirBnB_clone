#!/usr/bin/python3
"""
A module for a command interpreter for the HBNB project.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for the HBNB project.
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass

    def do_help(self, arg):
        """Displays the help documentation"""
        super().do_help(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
