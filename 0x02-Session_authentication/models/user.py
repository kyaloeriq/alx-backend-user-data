#!/usr/bin/env python3
# models/user.py

from models.base import BaseModel

class User(BaseModel):
    """
    A class representing a user.
    This class extends the BaseModel and includes user-specific fields.
    """

    def __init__(self, id: int = None, username: str = "", email: str = ""):
        """Initialize the user with ID, username, and email."""
        super().__init__(id=id)
        self.username = username
        self.email = email

    def __repr__(self):
        """Return a string representation of the user."""
        return f"<User {self.to_dict()}>"
