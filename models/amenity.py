#!/usr/bin/python3
'''class that is inherent of our BaseModel'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''class of the amenity'''

    name = ""

    def __init__(self, *args, **kwargs):
        '''init for Amenity'''
        super().__init__(*args, **kwargs)

