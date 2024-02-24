#!/usr/bin/python3
"""
Unittest for the Place (place.py)
"""
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    """Defines the test cases for the Place class."""

    def setUp(self):
        """Set up for the tests."""
        self.place_instance = Place()

    def test_instance_creation(self):
        """Tests the creation of place instance."""
        self.assertIsInstance(self.place_instance, Place)

    def test_attributes_exist(self):
        """Test that Place class has the required attributes."""
        self.assertTrue(hasattr(Place, "city_id"))
        self.assertTrue(hasattr(Place, "user_id"))
        self.assertTrue(hasattr(Place, "name"))
        self.assertTrue(hasattr(Place, "description"))
        self.assertTrue(hasattr(Place, "number_rooms"))
        self.assertTrue(hasattr(Place, "number_bathrooms"))
        self.assertTrue(hasattr(Place, "max_guest"))
        self.assertTrue(hasattr(Place, "price_by_night"))
        self.assertTrue(hasattr(Place, "latitude"))
        self.assertTrue(hasattr(Place, "longitude"))
        self.assertTrue(hasattr(Place, "amenity_ids"))

    def test_attribute_types(self):
        """Test the type of Place attributes."""
        self.assertIsInstance(self.place_instance.city_id, str)
        self.assertIsInstance(self.place_instance.user_id, str)
        self.assertIsInstance(self.place_instance.name, str)
        self.assertIsInstance(self.place_instance.description, str)
        self.assertIsInstance(self.place_instance.number_rooms, int)
        self.assertIsInstance(self.place_instance.number_bathrooms, int)
        self.assertIsInstance(self.place_instance.max_guest, int)
        self.assertIsInstance(self.place_instance.price_by_night, int)
        self.assertIsInstance(self.place_instance.latitude, float)
        self.assertIsInstance(self.place_instance.longitude, float)
        self.assertIsInstance(self.place_instance.amenity_ids, list)

if __name__ == '__main__':
    unittest.main()
