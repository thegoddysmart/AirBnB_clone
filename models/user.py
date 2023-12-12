#!/usr/bin/python3
"""This is our script defines the User class."""

from models.base_model import BaseModel

class User(BaseModel):
    """This represents any User."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

