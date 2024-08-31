#!/usr/bin/env python3
"""
This module contains:
- hash_password function to hash user passwords securely using bcrypt.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt, returning the hashed password
    """
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password using the generated salt
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates that the provided password matches the hashed password
    """
    # Use bcrypt to check if the provided password matches the hashed password
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
