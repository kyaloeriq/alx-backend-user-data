#!/usr/bin/env python3
"""
This module sets up and runs a Flask web application for the API.
"""

from flask import Flask, jsonify, abort
from api.v1.views.index import index_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(index_bp)

# Error handler for 401 Unauthorized
@app.errorhandler(401)
def unauthorized_error(error):
    """
    Handle 401 Unauthorized errors.
    """
    response = jsonify({"error": "Unauthorized"})
    response.status_code = 401
    return response


# Other app configurations and routes
if __name__ == '__main__':
    import os
    host = os.getenv('API_HOST', '0.0.0.0')
    port = int(os.getenv('API_PORT', 5000))
    app.run(host=host, port=port)
