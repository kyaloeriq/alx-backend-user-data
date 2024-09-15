#!/usr/bin/env python3
"""
App module for the API
"""

from api.v1.views import app_views
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth
from api.v1.auth.session_auth import SessionAuth  # Import SessionAuth
from flask import Flask, request, jsonify, abort
from models import storage
from os import getenv

app = Flask(__name__)

# Retrieve the auth mechanism to use
auth = None
auth_type = getenv("AUTH_TYPE")

if auth_type == "basic_auth":
    auth = BasicAuth()
elif auth_type == "session_auth":  # Switch to SessionAuth
    auth = SessionAuth()
else:
    auth = Auth()


@app.before_request
def before_request():
    """
    Function executed before each request to ensure authentication.
    Assigns the current authenticated user to request.current_user.
    """
    if auth is not None:
        excluded_paths = [
            '/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/'
        ]
        if not auth.require_auth(request.path, excluded_paths):
            return
        if auth.authorization_header(request) is None:
            abort(401)
        request.current_user = auth.current_user(request)
        if request.current_user is None:
            abort(403)


@app.teardown_appcontext
def close_db(error):
    """ Closes the database session """
    storage.close()


app.register_blueprint(app_views)

if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = getenv("HBNB_API_PORT", "5000")
    app.run(host=host, port=port, threaded=True)
