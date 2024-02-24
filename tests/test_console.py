#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
import console
HBNBCommand = console.HBNBCommand

class TestHBNBCommand(unittest.TestCase):
    """Tests the console module HBNBCommand class."""

    def test_quit(self):
        """Tests the quit command exits program."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertRaises(SystemExit, HBNBCommand().onecmd, "quit")

    def test_EOF(self):
        """Tests the EOF command exits program."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertRaises(SystemExit, HBNBCommand().onecmd, "EOF")

    def test_help(self):
        """Tests help command if it prints the expected text."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            output = f.getvalue().strip()
            self.assertIn("Documented commands", output)

    def test_create_missing_class(self):
        """Tests create command with a missing class name."""
        cmd = "create"
        expected = "** class name missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
            self.assertEqual(f.getvalue(), expected)

    def test_show_missing_class(self):
        """Tests show command with a missing class name."""
        cmd = "show"
        expected = "** class name missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
            self.assertEqual(f.getvalue(), expected)


if __name__ == '__main__':
    unittest.main()
