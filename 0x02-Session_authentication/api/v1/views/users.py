# api/v1/views/users.py

from flask import jsonify, abort, request
from models.user import User
from api.v1.views import app_views

@app_views.route('/api/v1/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """Retrieve a User object by ID or 'me' for the authenticated user"""
    if user_id == 'me':
        if request.current_user is None:
            abort(404)
        return jsonify(request.current_user.to_dict())
    
    user = User.get(user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())
