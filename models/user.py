#!/usr/bin/python3
"""
Defines the User class that inherits from BaseModel.
"""

from models.base_model import BaseModel

class User(BaseModel):
    """Represents a user for the AirBnB clone project."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
