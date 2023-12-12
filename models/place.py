#!/usr/bin/python3
'''class of the Base Model'''
from models.base_model import BaseModel


class Place(BaseModel):
    '''class of our Place'''

    user_id = ""
    name = ""
    city_id = ""
    description = ""
    number_bathrooms = 0
    number_rooms = 0
    max_guest = 0
    price_by_night = 0
    longitude = 0.0
    latitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        '''initializes the class of our Place'''
        super().__init__(*args, **kwargs)

