#!/usr/bin/env python3
"""
HTTP status code for a request unauthorized
"""
from flask import Blueprint, jsonify, abort
from api.v1.views import app_views

# Create a Blueprint instance for the index routes
index_bp = Blueprint('index', __name__)


@index_bp.route('/', methods=['GET'])
def index():
    """
    Route returns a JSON response with a simple "OK" message
    """
    return jsonify({"message": "OK"}), 200


@index_bp.route('/api/v1/unauthorized', methods=['GET'])
def unauthorized():
    """
    Endpoint to trigger 401 Unauthorized error.
    """
    abort(401)


@index_bp.route('/api/v1/unauthorized/', methods=['GET'])
def unauthorized_with_trailing_slash():
    """
    Endpoint to trigger 401 Unauthorized error.
    """
    abort(401)


@index_bp.route('/api/v1/forbidden', methods=['GET'])
def forbidden():
    """
    Trigger 403 Forbidden error.
    """
    abort(403)


@index_bp.route('/api/v1/forbidden/', methods=['GET'])
def forbidden_with_trailing_slash():
    """
    Trigger 403 Forbidden error.
    """
    abort(403)


@index_bp.route('/api/v1/status', methods=['GET'])
def status():
    """
    This route returns a JSON response with a simple "OK" message
    """
    return jsonify({"status": "OK"}), 200


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """
    Returns the status of the API
    """
    return "OK", 200
