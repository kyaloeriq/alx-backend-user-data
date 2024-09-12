#!/usr/bin/env python3
"""
This module contains the Auth class, a template for all authentication systems.
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Class to manage API authentication"""

    def require_auth(self, path: str, excluded_paths: list) -> bool:
        """
        Determines if authentication is required based on the path
        """
        if path is None or not isinstance(excluded_paths, list):
            return True

        # Normalize path by ensuring it does not have trailing slashes
        if path.endswith('/'):
            path = path[:-1]

        for excluded_path in excluded_paths:
            # Normalize excluded path by removing trailing slashes
            if excluded_path.endswith('/'):
                excluded_path = excluded_path[:-1]

            # Check if the excluded path ends with '*', indicating a wildcard
            if excluded_path.endswith('*'):
                # Match if the beginning of the path matches
                if path.startswith(excluded_path[:-1]):
                    return False
            elif path == excluded_path:
                return False

        # If no matches were found, authentication is required
        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieve the authorization header from the request.
        """
        if request is None:
            return None

        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return None

        return auth_header

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieve the current user from the request.
        """
        return None
