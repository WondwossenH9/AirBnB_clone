#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Tests the functionality of the BaseModel class."""

    def test_init(self):
        """Tests the initialization of the BaseModel instances."""
        instance = BaseModel()
        self.assertTrue(isinstance(instance, BaseModel))
        self.assertTrue(hasattr(instance, "id"))
        self.assertTrue(hasattr(instance, "created_at"))
        self.assertTrue(hasattr(instance, "updated_at"))
        self.assertTrue(isinstance(instance.created_at, datetime))
        self.assertTrue(isinstance(instance.updated_at, datetime))

    def test_to_dict(self):
        """Tests the dictionary representation of the BaseModel instances."""
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict["__class__"], "BaseModel")
        self.assertEqual(instance_dict["id"], instance.id)
        self.assertTrue("created_at" in instance_dict)
        self.assertTrue("updated_at" in instance_dict)

    def test_save(self):
        """Tests the save method of the BaseModel instances."""
        instance = BaseModel()
        old_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(old_updated_at, instance.updated_at)

if __name__ == '__main__':
    unittest.main()
