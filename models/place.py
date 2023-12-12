#!/usr/bin/python3
"""Method that creates our Place of class"""

from models.base_model import BaseModel

class Place(BaseModel):
    """ Our Class for managing the place objects."""

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

