#!/usr/bin/python3
"""This script Defines our user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class for user
    Attributes:
        email: email address
        password: password for your login
        first_name: first name
        last_name: last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
