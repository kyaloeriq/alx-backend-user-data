# api/v1/views/users.py
from flask import Blueprint, jsonify

users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['GET'])
def get_users():
    """Fetch all users."""
    # Replace with actual user fetching logic
    return jsonify({"users": []}), 200
