#!/usr/bin/python3
"""
Module for entry point of the command interpreter.
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for HBNB application.
    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit program
        """
        print("")
        return True

    def emptyline(self):
        """
        Method called when an empty line is entered into the prompt.
        If not overridden, repeats the last nonempty command.
        """
        pass

    def do_help(self, arg):
        """
        Lists available commands with "help" or more help with "help cmd".
        """
        super().do_help(arg)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
