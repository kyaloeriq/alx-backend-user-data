#!/usr/bin/env python3
"""
Module for BasicAuth class that implements basic authentication.
"""

from typing import TypeVar
from models.user import User
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """
    BasicAuth class to handle Basic Authentication mechanisms.
    """

    def extract_base64_authorization_header(
            self, authorization_header: str
            ) -> str:
        """
        Extracts the Base64 part of the Authorization header.
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        # Return the part after "Basic ".
        return authorization_header[len("Basic "):]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str
            ) -> str:
        """
        Decodes the Base64 string (base64_authorization_header).
        """
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            # Decode the Base64 string.
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            # Return None if decoding fails (invalid Base64).
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str
            ) -> (str, str):
        """
        Extracts user email and password from the decoded Base64.
        """
        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        # Check if the string contains a colon.
        if ':' not in decoded_base64_authorization_header:
            return None, None

        # Split the string into email and password.
        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str
            ) -> TypeVar('User'):
        """
        Retrieves the User instance based on the provided email and password.
        """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        # Search for the user in the database by email.
        users = User.search({'email': user_email})
        if not users:
            return None

        # Search method returns a list of users, we take the first match.
        user = users[0]

        # Check if the password is valid.
        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the User instance for the request based
        """
        if request is None:
            return None

        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        base64_auth_header = self.extract_base64_authorization_header(
                auth_header
                )
        if base64_auth_header is None:
            return None

        decoded_base64_auth_header = self.decode_base64_authorization_header(
                base64_auth_header
                )
        if decoded_base64_auth_header is None:
            return None

        email, password = self.extract_user_credentials(
                decoded_base64_auth_header
                )
        if email is None or password is None:
            return None

        return self.user_object_from_credentials(email, password)
