#!/usr/bin/python3
"""
Defines the Place class that inherits from BaseModel.
"""

from models.base_model import BaseModel

class Place(BaseModel):
    """Represents a place for the AirBnB clone project."""
    city_id = ""  # will be City.id
    user_id = ""  # will be User.id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []  # will be a list of Amenity.id
