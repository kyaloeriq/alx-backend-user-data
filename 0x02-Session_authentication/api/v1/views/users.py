#!/usr/bin/env python3
"""
View for User objects that handles all default RESTful API actions.
"""

from models.user import User
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage

@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """
    Retrieves a User by ID. If the user_id is 'me', returns the current authenticated user.
    """
    if user_id == "me":
        if request.current_user is None:
            abort(404)
        return jsonify(request.current_user.to_dict())

    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())
