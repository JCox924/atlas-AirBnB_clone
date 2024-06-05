#!/usr/bin/python3
"""
Defines the City class that inherits from BaseModel.
"""

from models.base_model import BaseModel

class City(BaseModel):
    """Represents a city for the AirBnB clone project."""
    state_id = ""  # will be State.id
    name = ""
