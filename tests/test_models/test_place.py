#!/usr/bin/python3
"""
this defines the test suite for the Place class.
"""""
import unittest
import os
import models
import json
from models.place import Place
from datetime import datetime



class TestPlaceInstantiation(unittest.TestCase):
    def test_create_instance(self):
        place = Place()
        self.assertIsInstance(place, Place)

    def test_attributes(self):
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()

