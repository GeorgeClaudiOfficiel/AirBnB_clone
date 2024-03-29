#!/usr/bin/python3
"""
This is our review module
"""
from models.base_model import BaseModel

class Review(BaseModel):
    """
    Review class inherits from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes Review instance
        """
        super().__init__(*args, **kwargs)

