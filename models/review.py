#!/usr/bin/python3
"""
Defines the Review class that inherits from BaseModel.
"""

from models.base_model import BaseModel

class Review(BaseModel):
    """Represents a review for the AirBnB clone project."""
    place_id = ""  # will be Place.id
    user_id = ""  # will be User.id
    text = ""
