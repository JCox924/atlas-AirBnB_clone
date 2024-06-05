#!/usr/bin/python3
"""
Defines unittests for models/place.py.
Unittest classes:
    TestPlace_instantiation
    TestPlace_save
    TestPlace_to_dict
"""

import unittest
from datetime import datetime
from time import sleep
from models.place import Place

class TestPlace_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), Place._Place__objects)

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_is_public_str(self):
        self.assertEqual(str, type(Place.city_id))

    def test_user_id_is_public_str(self):
        self.assertEqual(str, type(Place.user_id))

    def test_name_is_public_str(self):
        self.assertEqual(str, type(Place.name))

    def test_description_is_public_str(self):
        self.assertEqual(str, type(Place.description))

    def test_number_rooms_is_public_int(self):
        self.assertEqual(int, type(Place.number_rooms))

    def test_number_bathrooms_is_public_int(self):
        self.assertEqual(int, type(Place.number_bathrooms))

    def test_max_guest_is_public_int(self):
        self.assertEqual(int, type(Place.max_guest))

    def test_price_by_night_is_public_int(self):
        self.assertEqual(int, type(Place.price_by_night))

    def test_latitude_is_public_float(self):
        self.assertEqual(float, type(Place.latitude))

    def test_longitude_is_public_float(self):
        self.assertEqual(float, type(Place.longitude))

    def test_amenity_ids_is_public_list(self):
        self.assertEqual(list, type(Place.amenity_ids))

    def test_two_places_unique_ids(self):
        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id)

class TestPlace_save(unittest.TestCase):
    """Unittests for testing save method of the Place class."""

    def test_one_save(self):
        place = Place()
        sleep(0.05)
        first_updated_at = place.updated_at
        place.save()
        self.assertLess(first_updated_at, place.updated_at)

    def test_two_saves(self):
        place = Place()
        sleep(0.05)
        first_updated_at = place.updated_at
        place.save()
        second_updated_at = place.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        place.save()
        self.assertLess(second_updated_at, place.updated_at)

class TestPlace_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Place class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        place = Place()
        self.assertIn("id", place.to_dict())
        self.assertIn("created_at", place.to_dict())
        self.assertIn("updated_at", place.to_dict())
        self.assertIn("__class__", place.to_dict())

    def test_to_dict_contains_added_attributes(self):
        place = Place()
        place.middle_name = "Condo"
        place.my_number = 69
        self.assertEqual("Condo", place.middle_name)
        self.assertIn("my_number", place.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        place = Place()
        place_dict = place.to_dict()
        self.assertEqual(str, type(place_dict["created_at"]))
        self.assertEqual(str, type(place_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.now()
        place = Place()
        place.id = "123456"
        place.created_at = place.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(place.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        place = Place()
        self.assertNotEqual(place.to_dict(), place.__dict__)

if __name__ == "__main__":
    unittest.main()
