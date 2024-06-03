#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid

class TestBaseModel(unittest.TestCase):
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

if __name__ == "__main__":
    unittest.main()
