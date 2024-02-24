#!/usr/bin/python3
"""
This module holds unittests for BaseModel class.
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """
    Tests cases for the BaseModel class.
    """

    def test_init(self):
        """
        Tests the initialization of BaseModel instances.
        """
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_str(self):
        """
        Tests the __str__ method of BaseModel instances.
        """
        instance = BaseModel()
        expected_str_format = "[BaseModel] ({}) {}".format(instance.id, instance.__dict__)
        self.assertEqual(str(instance), expected_str_format)

    def test_save(self):
        """
        Tests the save method of BaseModel instances.
        """
        instance = BaseModel()
        old_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(old_updated_at, instance.updated_at)

    def test_to_dict(self):
        """
        Tests the to_dict method of BaseModel instances.
        """
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict['__class__'], 'BaseModel')
        self.assertIsInstance(instance_dict['created_at'], str)
        self.assertIsInstance(instance_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
