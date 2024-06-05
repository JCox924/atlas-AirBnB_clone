#!/usr/bin/python3
"""
Defines unittests for models/review.py.
Unittest classes:
    TestReview_instantiation
    TestReview_save
    TestReview_to_dict
"""

import unittest
from datetime import datetime
from time import sleep
from models.review import Review

class TestReview_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), Review._Review__objects)

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_is_public_str(self):
        self.assertEqual(str, type(Review.place_id))

    def test_user_id_is_public_str(self):
        self.assertEqual(str, type(Review.user_id))

    def test_text_is_public_str(self):
        self.assertEqual(str, type(Review.text))

    def test_two_reviews_unique_ids(self):
        review1 = Review()
        review2 = Review()
        self.assertNotEqual(review1.id, review2.id)

class TestReview_save(unittest.TestCase):
    """Unittests for testing save method of the Review class."""

    def test_one_save(self):
        review = Review()
        sleep(0.05)
        first_updated_at = review.updated_at
        review.save()
        self.assertLess(first_updated_at, review.updated_at)

    def test_two_saves(self):
        review = Review()
        sleep(0.05)
        first_updated_at = review.updated_at
        review.save()
        second_updated_at = review.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        review.save()
        self.assertLess(second_updated_at, review.updated_at)

class TestReview_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Review class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        review = Review()
        self.assertIn("id", review.to_dict())
        self.assertIn("created_at", review.to_dict())
        self.assertIn("updated_at", review.to_dict())
        self.assertIn("__class__", review.to_dict())

    def test_to_dict_contains_added_attributes(self):
        review = Review()
        review.middle_name = "I would never recommend this even to my worst enemy"
        review.my_number = 69
        self.assertEqual("I would never recommend this even to my worst enemy", review.middle_name)
        self.assertIn("my_number", review.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        review = Review()
        review_dict = review.to_dict()
        self.assertEqual(str, type(review_dict["created_at"]))
        self.assertEqual(str, type(review_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.now()
        review = Review()
        review.id = "123456"
        review.created_at = review.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Review',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(review.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        review = Review()
        self.assertNotEqual(review.to_dict(), review.__dict__)

if __name__ == "__main__":
    unittest.main()
