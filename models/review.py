#!/usr/bin/python3
'''class of our inherent BaseModel'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''class of the Review'''

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        '''initializes for the Review'''
        super().__init__(*args, **kwargs)

