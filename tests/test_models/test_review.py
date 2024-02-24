#!/usr/bin/python3
"""
Unittest for Review (review.py)
"""
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """Defines the test cases for the Review class."""

    def setUp(self):
        """Set up for the tests."""
        self.review_instance = Review()

    def test_instance_creation(self):
        """Tests the creation of review instance."""
        self.assertIsInstance(self.review_instance, Review)

    def test_attributes_exist(self):
        """Tests that Review class has the required attributes."""
        self.assertTrue(hasattr(Review, "place_id"))
        self.assertTrue(hasattr(Review, "user_id"))
        self.assertTrue(hasattr(Review, "text"))

    def test_attribute_types(self):
        """Tests type of Review attributes."""
        self.assertIsInstance(self.review_instance.place_id, str)
        self.assertIsInstance(self.review_instance.user_id, str)
        self.assertIsInstance(self.review_instance.text, str)

if __name__ == '__main__':
    unittest.main()
