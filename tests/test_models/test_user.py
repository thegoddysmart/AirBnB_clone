#!/usr/bin/python3
"""
This defines the test suite for the User class.
"""
import unittest
import os
import models
from datetime import datetime
from models.user import User
from time import sleep


class TestUser_instantiation(unittest.TestCase):
    """We are testing instantiation for the User class."""

    def test_no_args(self):
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(User.last_name))

    def test_two_users_unique_ids(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_two_users_different_created_at(self):
        user1 = User()
        sleep(0.05)
        user2 = User()
        self.assertLess(user1.created_at, user2.created_at)

    def test_two_users_different_updated_at(self):
        user1 = User()
        sleep(0.05)
        user2 = User()
        self.assertLess(user1.updated_at, user2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_rep = repr(dt)
        user0 = User()
        user0.id = "123456"
        user0.created_at = user0.updated_at = dt
        user_str = user0.__str__()
        self.assertIn("[User] (123456)", user_str)
        self.assertIn("'id': '123456'", user_str)
        self.assertIn("'created_at': " + dt_rep, user_str)
        self.assertIn("'updated_at': " + dt_rep, user_str)

    def test_args_unused(self):
        user0 = User(None)
        self.assertNotIn(None, user0.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        date_iso = dt.isoformat()
        user0 = User(id="345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(user0.id, "345")
        self.assertEqual(user0.created_at, dt)
        self.assertEqual(user0.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()

