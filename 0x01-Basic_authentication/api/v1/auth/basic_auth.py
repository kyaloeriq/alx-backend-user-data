#!/usr/bin/env python3
"""
Module for BasicAuth class that implements basic authentication.
"""

from typing import TypeVar, Tuple
from models.user import User
from api.v1.auth.auth import Auth
import base64

UserType = TypeVar('User', bound=User)

class BasicAuth(Auth):
    """
    BasicAuth class to handle Basic Authentication mechanisms
    """
    def extract_base64_authorization_header(
            self, authorization_header: str
            ) -> str:
        """
        Extracts the Base64 part of the Authorization header
        """
        if authorization_header is None or not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        # Return the part after "Basic "
        return authorization_header[len("Basic "):]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str
            ) -> str:
        """
        Decodes the Base64 string (base64_authorization_header)
        """
        if base64_authorization_header is None or not isinstance(base64_authorization_header, str):
            return None

        try:
            # Decode the Base64 string
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            # Return None if decoding fails (invalid Base64)
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str
            ) -> Tuple[str, str]:
        """
        Extracts user email and password from the decoded Base64
        """
        if decoded_base64_authorization_header is None or not isinstance(decoded_base64_authorization_header, str):
            return None, None

        # Check if the string contains a colon
        if ':' not in decoded_base64_authorization_header:
            return None, None

        # Split the string into email and password
        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str
            ) -> UserType:
        """
        Retrieves the User instance based on the provided email and password
        """
        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None

        # Search for the user in the database by email
        users = User.search({'email': user_email})
        if not users:
            return None

        # Search method returns a list of users, we take the first match
        user = users[0]

        # Check if the password is valid
        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> UserType:
        """
        Retrieves the User instance for a request
        """
        if request is None:
            return None

        # Get the authorization header
        authorization_header = request.headers.get('Authorization')
        if not authorization_header:
            return None

        # Extract Base64 part
        base64_auth_header = self.extract_base64_authorization_header(authorization_header)
        if base64_auth_header is None:
            return None

        # Decode Base64 part
        decoded_auth_header = self.decode_base64_authorization_header(base64_auth_header)
        if decoded_auth_header is None:
            return None

        # Extract user credentials
        user_email, user_pwd = self.extract_user_credentials(decoded_auth_header)
        if user_email is None or user_pwd is None:
            return None

        # Retrieve the User object
        return self.user_object_from_credentials(user_email, user_pwd)

