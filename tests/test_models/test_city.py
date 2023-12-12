#!/usr/bin/python3
"""
This defines the test suit for the City class.
"""

import unittest
import os
import models
from models.city import City
from datetime import datetime
import time


class TestCityInstantiation(unittest.TestCase):
    """we are testing the instantiation of the City class."""
    def test_create_instance(self):
        city = City()
        self.assertIsInstance(city, City)

    def test_attributes(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_two_cities_unique_ids(self):
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_two_cities_different_created_at(self):
        city1 = City()
        time.sleep(0.05)
        city2 = City()
        self.assertLess(city1.created_at, city2.created_at)

    def test_two_cities_different_updated_at(self):
        city1 = City()
        time.sleep(0.05)
        city2 = City()
        self.assertLess(city1.updated_at, city2.updated_at)

    def test_instantiation_with_kwargs(self):
        date = datetime.today()
        date_iso = date.isoformat()
        city = City(id="345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(city.id, "345")
        self.assertEqual(city.created_at, date)
        self.assertEqual(city.updated_at, date)

    def test_none_args(self):
        city = City(None)
        self.assertNotIn(None, city.__dict__.values())

    def test_instantiation_with_no_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()

