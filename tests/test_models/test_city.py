#!/usr/bin/python3
"""
Unittest for City (city.py)
"""
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """Defines the test cases for the City class."""

    def setUp(self):
        """Set up for the tests."""
        self.city_instance = City()

    def test_instance_creation(self):
        """Test creation of city instance."""
        self.assertIsInstance(self.city_instance, City)

    def test_attributes_exist(self):
        """Tests that the City class has the required attributes."""
        self.assertTrue(hasattr(City, "state_id"))
        self.assertTrue(hasattr(City, "name"))

    def test_attribute_types(self):
        """Tests the type of City attributes."""
        self.assertIsInstance(self.city_instance.state_id, str)
        self.assertIsInstance(self.city_instance.name, str)

if __name__ == '__main__':
    unittest.main()
