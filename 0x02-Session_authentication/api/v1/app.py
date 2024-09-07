#!/usr/bin/env python3
"""
This is the main entry point for the API.
"""

from flask import Flask, jsonify
from os import getenv

from api.v1.views import app_views
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth
from api.v1.auth.session_auth import SessionAuth

app = Flask(__name__)
app.register_blueprint(app_views)

auth = None
auth_type = getenv('AUTH_TYPE')

if auth_type == 'basic_auth':
    auth = BasicAuth()
elif auth_type == 'session_auth':
    auth = SessionAuth()


@app.before_request
def before_request():
    """
    Handle authentication before processing requests.
    """
    if auth:
        request.current_user = auth.current_user(request)


@app.route('/api/v1/status', methods=['GET'], strict_slashes=False)
def status():
    """
    Returns the status of the API.
    """
    return jsonify({"status": "OK"})

# Other configurations and routes...


if __name__ == '__main__':
    host = getenv('API_HOST', '0.0.0.0')
    port = int(getenv('API_PORT', 5000))
    app.run(host=host, port=port)
