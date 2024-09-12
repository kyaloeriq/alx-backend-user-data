#!/usr/bin/env python3
"""
This module sets up the Flask application for the API, including configuration
"""

from api.v1.views.index import index_bp
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)

app.register_blueprint(index_bp)

# Initialize auth to None
auth = None

# Load the appropriate authentication class based on AUTH_TYPE
auth_type = os.getenv('AUTH_TYPE')
if auth_type == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif auth_type == 'auth':
    from api.v1.auth.auth import Auth
    auth = Auth()


@app.before_request
def before_request_handler():
    """Handler for filtering requests before they are processed."""
    if auth is None:
        return
    # List of paths that do not require authentication
    excluded_paths = [
            '/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/'
            ]

    # If the request path does not require authentication, do nothing
    if not auth.require_auth(request.path, excluded_paths):
        return
    # request does not contain Authorization header, raise 401 Unauthorized
    if auth.authorization_header(request) is None:
        abort(401)
    # If the current user is not found, raise 403 Forbidden
    if auth.current_user(request) is None:
        abort(403)


@app.errorhandler(401)
def unauthorized_error(error):
    """Handle 401 Unauthorized errors."""
    response = jsonify({"error": "Unauthorized"})
    response.status_code = 401
    return response


@app.errorhandler(403)
def forbidden_error(error):
    """Handle 403 Forbidden errors."""
    response = jsonify({"error": "Forbidden"})
    response.status_code = 403
    return response


# Other app configurations and routes
if __name__ == '__main__':
    host = os.getenv('API_HOST', '0.0.0.0')
    port = int(os.getenv('API_PORT', 5000))
    app.run(host=host, port=port)
