#!/usr/bin/python3
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """Tests the functionality of the User class."""

    def test_user_attributes(self):
        """Tests the User class has the expected attributes."""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

if __name__ == '__main__':
    unittest.main()
