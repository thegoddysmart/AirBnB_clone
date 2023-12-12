#!/usr/bin/python3
"""
This defines a module for BaseModel unittest

Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import unittest
import models
from models.base_model import BaseModel
from datetime import datetime
import os
import time


class TestBaseModelInstantiation(unittest.TestCase):
    """
    Test cases for the instantiation of BaseModel.
    """

    def setUp(self):
        """Set up a clean environment before each test."""
        # this ensures that the file storage is clean
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """Remove the json file after each test."""
        # this ensures that the file storage is clean
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_create_instance(self):
        """Test creating an instance of BaseModel."""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)

    def test_id_generation(self):
        """Test if id is generated as expected."""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_created_at(self):
        """Test if created_at is a datetime object."""
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)

    def test_updated_at(self):
        """Test if updated_at is a datetime object."""
        model = BaseModel()
        self.assertIsInstance(model.updated_at, datetime)

    def test_custom_attributes(self):
        """Test if custom attributes can be added to the instance."""
        model = BaseModel()
        model.name = "John"
        self.assertEqual(model.name, "John")

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_init_with_kwargs_convert_datetime(self):
        """Test if __init__ handles kwargs correctly."""
        data = {
            "id": "123",
            "created_at": "2022-01-01T12:00:00.000000",
            "updated_at": "2022-01-01T12:30:00.000000",
            "custom_attribute": "value"
        }
        model = BaseModel(**data)
        self.assertEqual(model.id, "123")
        self.assertEqual(model.created_at, datetime(2022, 1, 1, 12, 0, 0))
        self.assertEqual(model.updated_at, datetime(2022, 1, 1, 12, 30, 0))
        self.assertEqual(model.custom_attribute, "value")


class TestBaseModelSave(unittest.TestCase):
    """
    Test cases for BaseModel save method.
    """

    def setUp(self):
        """Set up a clean environment before each test."""
        # this ensures that the file storage is clean
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """Remove the json file after each test."""
        # this ensures that the file storage is clean
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_save_updates_updated_at(self):
        """Test if calling save updates the updated_at attribute."""
        model = BaseModel()
        original_updated_at = model.updated_at
        time.sleep(0.1)  # adding a delay
        model.save()
        self.assertNotEqual(original_updated_at, model.updated_at)

    def test_save_to_file(self):
        """Test if save writes to the file."""
        model = BaseModel()
        model.save()
        with open("file.json", "r") as file:
            content = file.read()
            self.assertIn(model.id, content)


class TestBaseModelToDict(unittest.TestCase):
    """
    Test cases for BaseModel to_dict method.
    """

    def setUp(self):
        """Set up a clean environment before each test."""
        # Ensure that the file storage is clean
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """Clean up after each test."""
        # Ensure that the file storage is clean
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_to_dict_type(self):
        """Test the return type of to_dict."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(dict, type(model_dict))

    def test_to_dict_contains_correct_keys(self):
        """Test if to_dict contains all the necessary keys."""
        model = BaseModel()
        model_dict = model.to_dict()
        expected = ["id", "created_at", "updated_at", "__class__"]
        self.assertEqual(expected, list(model_dict.keys()))

    def test_to_dict_contains_correct_updated_at_value(self):
        """Test if to_dict contains the correct updated_at value."""
        model = BaseModel()
        model_dict = model.to_dict()
        iso = model.updated_at.isoformat()
        self.assertEqual(iso, model_dict["updated_at"])

    def test_to_dict_representation(self):
        """Test if to_dict returns the expected dictionary."""
        model = BaseModel()
        model_dict = model.to_dict()
        expected_keys = ["id", "created_at", "updated_at", "__class__"]
        for key in expected_keys:
            self.assertIn(key, model_dict)

    def test_to_dict_with_arg(self):
        """Test to_dict method with an argument."""
        model = BaseModel()
        with self.assertRaises(TypeError):
            model.to_dict(None)


if __name__ == "__main__":
    unittest.main()

