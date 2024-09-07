#!/usr/bin/env python3
"""Module for User class"""

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def to_dict(self):
        """Returns a dictionary representation of the User instance"""
        return {
            "id": self.id,
            "name": self.name
        }
