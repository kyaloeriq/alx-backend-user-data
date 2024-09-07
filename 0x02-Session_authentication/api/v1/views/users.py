#!/usr/bin/env python3
"""
This module defines the view for handling user-related operations,
including retrieving user data by ID or retrieving the
authenticated user's data.
"""

from flask import jsonify, abort, request
from models.user import User
from api.v1.views import app_views


@app_views.route(
        '/api/v1/users/<user_id>', methods=['GET'], strict_slashes=False
        )
def get_user(user_id):
    """
    Retrieve a User object by ID or 'me' for the authenticated user.

    Args:
        user_id (str): The ID of the user or 'me' to retrieve the
        authenticated user.

    Returns:
        Response: JSON response containing the user data or
        404 error if not found.
    """
    if user_id == 'me':
        if request.current_user is None:
            abort(404)
        return jsonify(request.current_user.to_dict())

    user = User.get(user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())
