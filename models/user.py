#!/usr/bin/python3
'''class of our user which inherents from BaseModel'''
from models.base_model import BaseModel


class User(BaseModel):
    '''rep. for our class User'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""

