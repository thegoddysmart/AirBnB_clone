#!/usr/bin/python3
"""
A module for testing the console
"""

import unittest
import os
import sys
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class TestHBNBCommandPrompt(unittest.TestCase):
    """
    Test the HBNB command console prompt
    """

    def test_prompt(self):
        """
        Test the prompt
        """
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_prompt_empty(self):
        """
        Test the prompt if empty
        """
        self.assertNotEqual(" ", HBNBCommand.prompt)


class TestHBNBCommandHelp(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def test_help(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.console.onecmd("help")
            self.assertIn("Documented commands (type help <topic>):", mock_stdout.getvalue())


class TestHBNBCommandExit(unittest.TestCase):
    def setUp():
        self.console = HBNBCommand()

    def test_exit(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.console.onecmd("quit"))


class TestHBNBCommandCreate(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def test_create_instance(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            key = "BaseModel." + output
            self.assertIn(key, storage.all())


class TestHBNBCommandShow(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def test_show_command(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            obj_id = mock_stdout.getvalue().strip()
            self.console.onecmd(f"show BaseModel {obj_id}")
            expected_output = f"[BaseModel] ({obj_id})"
            self.assertIn(expected_output, mock_stdout.getvalue().strip())


class TestHBNBCommandDestroy(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def test_destroy_command(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            obj_id = mock_stdout.getvalue().strip()
            self.console.onecmd(f"destroy BaseModel {obj_id}")
            key = "BaseModel." + obj_id
            self.assertNotIn(key, storage.all())


class TestHBNBCommandAll(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def test_all_command(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create User")
            self.console.onecmd("all")
            self.assertIn("[BaseModel]", mock_stdout.getvalue().strip())
            self.assertIn("[User]", mock_stdout.getvalue().strip())


class TestHBNBCommandUpdate(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def test_update_command(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            obj_id = mock_stdout.getvalue().strip()
            self.console.onecmd(f"update BaseModel {obj_id} name 'test'")
            key = "BaseModel." + obj_id
            self.assertIn("name", storage.all()[key].__dict__)
            self.assertEqual(storage.all()[key].name, "test")


if __name__ == "__main__":
    unittest.main()

