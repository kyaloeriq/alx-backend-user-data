#!/usr/bin/env python3
# models/base.py

class BaseModel:
    """
    A base class for models.
    This class can be extended by other models to inherit common functionalities.
    """

    def __init__(self, id: int = None):
        """Initialize the base model with an optional ID."""
        self.id = id

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return self.__dict__

    def __repr__(self):
        """Return a string representation of the model."""
        return f"<{self.__class__.__name__} {self.to_dict()}>"
