#!/usr/bin/python3
"""
Unittest for State (state.py)
"""
import unittest
from models.state import State
from datetime import datetime

class TestState(unittest.TestCase):
    """Defines the test cases for the State class."""

    def test_instance_creation(self):
        """Tests the creation of State instance."""
        instance = State()
        self.assertTrue(isinstance(instance, State))

    def test_attribute_types(self):
        """Tests the type of the State attributes."""
        instance = State()
        instance.name = "California"
        self.assertEqual(instance.name, "California")

if __name__ == '__main__':
    unittest.main()
