#!/usr/bin/env python3
"""
Module for BasicAuth class that implements basic authentication mechanisms.
"""

from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """
    BasicAuth class that inherits from Auth.
    """
    def extract_base64_authorization_header(
            self, authorization_header: str
            ) -> str:
        """
        Extracts the Base64 part of the Authorization header
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
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
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            # Decode the Base64 string
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            # Return None if decoding fails (invalid Base64)
            return None
    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Extracts user email and password from the decoded Base64
        """
        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        # Check if the string contains a colon
        if ':' not in decoded_base64_authorization_header:
            return None, None

        # Split the string into email and password
        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password
