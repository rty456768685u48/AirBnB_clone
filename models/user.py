#!/usr/bin/env python3
""""class User module"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    A class representing a User.

    Public class attributes:
    - email (string): Email of the user.
    - password (string): Password of the user.
    - first_name (string): First name of the user.
    - last_name (string): Last name of the user.

    Inherits from BaseModel, which provides common attributes and methods.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ Inherits from Basemodel init"""
        super().__init__(**kwargs)
