#!/usr/bin/python3
"""Module for our State class"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class that inherits from our own BaseModel

    Attributes:
        name (str): The name of the state.
    """

    name = ""

