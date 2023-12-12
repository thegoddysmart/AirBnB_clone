#!/usr/bin/python3
'''class which is inherent of BaseModel'''
from models.base_model import BaseModel


class City(BaseModel):
    '''class of city'''

    state_id = ""
    name = ""


    def __init__(self, *args, **kwargs):
        '''initializes for the City'''
        super().__init__(*args, **kwargs)

