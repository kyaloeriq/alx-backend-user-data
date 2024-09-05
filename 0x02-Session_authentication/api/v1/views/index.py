# api/v1/views/index.py
from flask import Blueprint, jsonify

index_bp = Blueprint('index', __name__)

@index_bp.route('/', methods=['GET'])
def index():
    """Base route."""
    return jsonify({"message": "OK"}), 200
