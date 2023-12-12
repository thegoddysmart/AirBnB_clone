#!/usr/bin/python3
"""
this defines the test suite for the State class.
"""
import unittest
import os
import models
import json
from models.state import State
from datetime import datetime
from models.review import Review


class TestStateInstantiation(unittest.TestCase):
    """
    We are testing the instantiation of the State class.
    """
    def test_create_instance(self):
        state = State()
        self.assertIsInstance(state, State)

    def test_attributes(self):
        state = State()
        self.assertEqual(state.name, "")


if __name__ == "__main__":
    unittest.main()

