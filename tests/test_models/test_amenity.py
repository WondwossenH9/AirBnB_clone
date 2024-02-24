#!/usr/bin/python3
"""
Unittest for Amenity (amenity.py)
"""
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Defines the test cases for the Amenity class."""

    def setUp(self):
        """Sets up for tests."""
        self.amenity_instance = Amenity()

    def test_instance_creation(self):
        """Tests the creation of amenity instance."""
        self.assertIsInstance(self.amenity_instance, Amenity)

    def test_attributes_exist(self):
        """Tests that Amenity class has the required attributes."""
        self.assertTrue(hasattr(Amenity, "name"))

    def test_attribute_types(self):
        """Tests the type of Amenity attributes."""
        self.assertIsInstance(self.amenity_instance.name, str)

if __name__ == '__main__':
    unittest.main()
