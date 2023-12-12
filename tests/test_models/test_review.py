#!/usr/bin/python3
"""
This defines the test suite for the Review class.
"""

import os
import models
import unittest
import json
from datetime import datetime
from models.review import Review


class TestReviewInstantiation(unittest.TestCase):
    """
    We are testing the instantiation of the Review class.
    """
    def test_create_instance(self):
        review = Review()
        self.assertIsInstance(review, Review)

    def test_attributes(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == "__main__":
    unittest.main()

