#!/usr/bin/python3
"""
This defines the test suite for the Amenity class.
"""
import unittest
import os
import models
from datetime import datetime
from models.amenity import Amenity
from time import sleep


class TestAmenityInstantiation(unittest.TestCase):
    """
    We are testing the instantiation of the Amenity class.
    """
    def test_create_instance(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_two_amenities_unique_ids(self):
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_two_amenities_different_created_at(self):
        amenity1 = Amenity()
        sleep(0.05)
        amenity2 = Amenity()
        self.assertLess(amenity1.created_at, amenity2.created_at)

    def test_two_amenities_different_updated_at(self):
        amenity1 = Amenity()
        sleep(0.05)
        amenity2 = Amenity()
        self.assertLess(amenity1.updated_at, amenity2.updated_at)

    def test_name_is_public_class_attribute(self):
        amenity = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", amenity.__dict__)

    def test_instance_with_kwargs(self):
        date = datetime.today()
        date_iso = date.isoformat()
        amenity = Amenity(id="345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(amenity.id, "345")
        self.assertEqual(amenity.created_at, date)
        self.assertEqual(amenity.updated_at, date)

    def test_none_args(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)

