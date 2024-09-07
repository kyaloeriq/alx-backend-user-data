#!/usr/bin/env python3
# api/v1/app.py

from flask import Flask, jsonify, request
from api.v1.views.index import index_bp
from api.v1.auth.basic_auth import BasicAuth
import os

app = Flask(__name__)
app.register_blueprint(app_views)

# Check the value of AUTH_TYPE environment variable
auth_type = os.getenv('AUTH_TYPE')

# Determine the authentication mechanism based on AUTH_TYPE
if auth_type == 'session_auth':
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()
else:
    auth = BasicAuth()

@app.before_request
def before_request():
    """Filter before each request"""
    request.current_user = auth.current_user(request)

# Register blueprints
app.register_blueprint(index_bp)

@app.errorhandler(401)
def unauthorized_error(error):
    """Handle 401 Unauthorized errors."""
    response = jsonify({"error": "Unauthorized"})
    response.status_code = 401
    return response

# Other app configurations and routes
if __name__ == '__main__':
    import os
    host = os.getenv('API_HOST', '0.0.0.0')
    port = int(os.getenv('API_PORT', 5000))
    app.run(host=host, port=port)
