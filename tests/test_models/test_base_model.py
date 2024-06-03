#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime
import os

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def tearDown(self):
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_init(self):
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_to_dict(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")

    def test_save(self):
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, old_updated_at)

    def test_str(self):
        obj = BaseModel()
        expected_str = f"[BaseModel] ({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), expected_str)
    
    def test_create_from_dict(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        new_obj = BaseModel(**obj_dict)
        self.assertEqual(obj.id, new_obj.id)
        self.assertEqual(obj.created_at, new_obj.created_at)
        self.assertEqual(obj.updated_at, new_obj.updated_at)
        self.assertEqual(obj.__class__, new_obj.__class__)

    def test_storage_save_reload(self):
        obj = BaseModel()
        obj.save()
        storage.save()
        storage.reload()
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, storage.all())
        self.assertEqual(obj.id, storage.all()[key].id)
        self.assertEqual(obj.created_at, storage.all()[key].created_at)
        self.assertEqual(obj.updated_at, storage.all()[key].updated_at)

if __name__ == "__main__":
    unittest.main()
