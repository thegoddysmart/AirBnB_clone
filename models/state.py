#!/usr/bin/python3
'''Module for our State class'''

from models.base_model import BaseModel

class State(BaseModel):
    '''
    Class of state that inherits from our own BaseModel

    Attributes:
        name (str): our name of state.
    '''

    name = ""

