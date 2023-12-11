#!/usr/bin/python3
"""
This defines a module for FileStorage unittest

Unittest classes:
    TestFileStorageInstantiation
    TestFileStorageAllMethod
    TestFileStorageNewMethod
    TestFileStorageSaveMethod
"""

import unittest
import os
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorageInstantiation(unittest.TestCase):
    """
    We are testing instantiation of the FileStorage class.
    """

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorageAllMethod(unittest.TestCase):
    """
    Test cases for the all() method of FileStorage.
    """

    def setUp(self):
        """this cleans up before each test."""
        # this ensures that the file storage is clean
        if os.path.exists("file.json"):
            os.remove("file.json")
        self.storage = FileStorage()

    def tearDown(self):
        """This cleans up after each test."""
        # this ensures that the file storage is clean
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all_returns_dict(self):
        """test if all() returns a dictionary."""
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)


class TestFileStorageNewMethod(unittest.TestCase):
    """
    Test cases for the new() method of FileStorage.
    """

    def setUp(self):
        """this cleans up before each test."""
        # this ensures that the file storage is clean
        if os.path.exists("file.json"):
            os.remove("file.json")
        self.storage = FileStorage()
        self.model = BaseModel()

    def tearDown(self):
        """This cleans up after each test."""
        # this ensures that the file storage is clean
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_new_adds_object(self):
        """test if new() adds an object to the dictionary."""
        self.storage.new(self.model)
        objects = self.storage.all()
        self.assertIn(self.model, objects.values())


class TestFileStorageSaveMethod(unittest.TestCase):
    """
    Test cases for the save() method of FileStorage.
    """

    def setUp(self):
        """this cleans up before each test."""
        # this ensures that the file storage is clean
        if os.path.exists("file.json"):
            os.remove("file.json")
        self.storage = FileStorage()
        self.model = BaseModel()

    def tearDown(self):
        """This cleans up after each test."""
        # this ensures that the file storage is clean
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_save_updates_file(self):
        """test if save() writes to the file."""
        self.storage.new(self.model)
        self.storage.save()
        with open("file.json", "r") as file:
            content = file.read()
            self.assertIn(self.model.id, content)


if __name__ == "__main__":
    unittest.main()

