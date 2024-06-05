#!/usr/bin/python3
"""
Defines unittests for models/user.py.
Unittest classes:
    TestUser_instantiation
    TestUser_save
    TestUser_to_dict
"""

import unittest
from datetime import datetime
from time import sleep
from models.user import User

class TestUser_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""

    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), User._User__objects)

    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(User.last_name))

    def test_two_users_unique_ids(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

class TestUser_save(unittest.TestCase):
    """Unittests for testing save method of the User class."""

    def test_one_save(self):
        user = User()
        sleep(0.05)
        first_updated_at = user.updated_at
        user.save()
        self.assertLess(first_updated_at, user.updated_at)

    def test_two_saves(self):
        user = User()
        sleep(0.05)
        first_updated_at = user.updated_at
        user.save()
        second_updated_at = user.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        user.save()
        self.assertLess(second_updated_at, user.updated_at)

class TestUser_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the User class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        user = User()
        self.assertIn("id", user.to_dict())
        self.assertIn("created_at", user.to_dict())
        self.assertIn("updated_at", user.to_dict())
        self.assertIn("__class__", user.to_dict())

    def test_to_dict_contains_added_attributes(self):
        user = User()
        user.middle_name = "Paul"
        user.my_number = 69
        self.assertEqual("Paul", user.middle_name)
        self.assertIn("my_number", user.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(str, type(user_dict["created_at"]))
        self.assertEqual(str, type(user_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.now()
        user = User()
        user.id = "123456"
        user.created_at = user.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'User',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(user.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        user = User()
        self.assertNotEqual(user.to_dict(), user.__dict__)

if __name__ == "__main__":
    unittest.main()
