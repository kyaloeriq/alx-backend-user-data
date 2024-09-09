#!/usr/bin/env python3
# api/v1/auth/auth.py
"""
This module contains the Auth class, a template for all authentication systems.
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Class to manage API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determine if a path requires authentication.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Retrieve the authorization header from the request.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieve the current user from the request.
        """
        return None
