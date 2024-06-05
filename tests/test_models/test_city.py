#!/usr/bin/python3
"""
Defines unittests for models/city.py.
Unittest classes:
    TestCity_instantiation
    TestCity_save
    TestCity_to_dict
"""

import unittest
from datetime import datetime
from time import sleep
from models.city import City

class TestCity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), City._City__objects)

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_public_str(self):
        self.assertEqual(str, type(City.state_id))

    def test_name_is_public_str(self):
        self.assertEqual(str, type(City.name))

    def test_two_cities_unique_ids(self):
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

class TestCity_save(unittest.TestCase):
    """Unittests for testing save method of the City class."""

    def test_one_save(self):
        city = City()
        sleep(0.05)
        first_updated_at = city.updated_at
        city.save()
        self.assertLess(first_updated_at, city.updated_at)

    def test_two_saves(self):
        city = City()
        sleep(0.05)
        first_updated_at = city.updated_at
        city.save()
        second_updated_at = city.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        city.save()
        self.assertLess(second_updated_at, city.updated_at)

class TestCity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the City class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        city = City()
        self.assertIn("id", city.to_dict())
        self.assertIn("created_at", city.to_dict())
        self.assertIn("updated_at", city.to_dict())
        self.assertIn("__class__", city.to_dict())

    def test_to_dict_contains_added_attributes(self):
        city = City()
        city.middle_name = "Tulsa"
        city.my_number = 69
        self.assertEqual("Tulsa", city.middle_name)
        self.assertIn("my_number", city.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        city = City()
        city_dict = city.to_dict()
        self.assertEqual(str, type(city_dict["created_at"]))
        self.assertEqual(str, type(city_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.now()
        city = City()
        city.id = "123456"
        city.created_at = city.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(city.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        city = City()
        self.assertNotEqual(city.to_dict(), city.__dict__)

if __name__ == "__main__":
    unittest.main()
