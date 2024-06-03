#!/usr/bin/python3
import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()
        self.file_path = self.storage._FileStorage__file_path
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """Tear down test environment"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_file_path(self):
        """Test that file path is correct"""
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_objects(self):
        """Test that objects dictionary is initially empty"""
        self.assertEqual(self.storage._FileStorage__objects, {})

    def test_new(self):
        """Test that new adds an object to __objects"""
        obj = BaseModel()
        self.storage.new(obj)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage._FileStorage__objects)
        self.assertEqual(self.storage._FileStorage__objects[key], obj)

    def test_save_create_file(self):
        """Test that save creates a file"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path), "No file created by save")

    def test_reload(self):
        """Test that reload correctly loads objects from file"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all(), "Object not loaded by reload")
        self.assertEqual(self.storage.all()[key].id, obj.id)

if __name__ == "__main__":
    unittest.main()

