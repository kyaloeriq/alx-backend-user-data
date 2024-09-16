#!/usr/bin/env python3
"""
SessionAuth module for managing session IDs.
"""

import uuid
from .auth import Auth


class SessionAuth(Auth):
    """
    SessionAuth class for managing session-based authentication.
    """
    # Class attribute to store session IDs and associated user IDs
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Create a session ID for a given user_id.
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        # Generate a session ID using uuid4
        session_id = str(uuid.uuid4())

        # Store the session_id with the associated user_id in the dictionary
        self.user_id_by_session_id[session_id] = user_id

        # Return the generated session ID
        return session_id
