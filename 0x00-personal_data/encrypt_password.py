#!/usr/bin/env python3
"""
This module contains:
- hash_password function to hash user passwords securely using bcrypt.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt, returning the hashed password as a byte string.
    
    Args:
        password (str): The password to hash.
    
    Returns:
        bytes: The salted and hashed password.
    """
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password using the generated salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    
    return hashed_password
