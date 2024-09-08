#!/usr/bin/env python3
# api/v1/views/index.py
from flask import Blueprint, jsonify, abort

index_bp = Blueprint('index', __name__)

@index_bp.route('/', methods=['GET'])
def index():
    """Base route."""
    return jsonify({"message": "OK"}), 200

@index_bp.route('/api/v1/unauthorized', methods=['GET'])
def unauthorized():
    """Endpoint to trigger 401 Unauthorized error."""
    abort(401)
