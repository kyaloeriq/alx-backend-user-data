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
        Args:
            user_id (str): The user's ID to associate with a session.
        Returns:
            str: The generated session ID, or None if user_id is invalid.
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        # Generate a session ID using uuid4
        session_id = str(uuid.uuid4())

        # Store the session_id with the associated user_id in the dictionary
        self.user_id_by_session_id[session_id] = user_id

        # Return the generated session ID
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Retrieve a user ID based on a session ID.
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        # Retrieve the user ID associated with the session
        return self.user_id_by_session_id.get(session_id)
