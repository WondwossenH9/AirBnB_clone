#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """Tests the functionality of FileStorage class."""

    def test_all(self):
        """Tests all returns the __objects dict."""
        storage = FileStorage()
        all_objs = storage.all()
        self.assertIsInstance(all_objs, dict)

    def test_new(self):
        """Tests new adds object to the __objects dict."""
        storage = FileStorage()
        instance = BaseModel()
        storage.new(instance)
        key = f"{instance.__class__.__name__}.{instance.id}"
        self.assertIn(key, storage.all())

    def test_save(self):
        """Tests save properly saves objects to file."""
        # This test may need to create a temporary file or mock file I/O operations

    def test_reload(self):
        """Test that reload properly loads objects from file."""
        # Similar to test_save, this might require mocking or temp files

if __name__ == '__main__':
    unittest.main()
