#!/usr/bin/env python3
"""
This module defines the views for User objects
"""

from models.user import User
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """
    Retrieves a User object by ID or returns the current authenticated User
    """
    if user_id == "me":
        if request.current_user is None:
            abort(404)
        return jsonify(request.current_user.to_dict())

    user = User.get(user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())
