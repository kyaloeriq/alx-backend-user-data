#!/usr/bin/env python3
# api/v1/app.py

from flask import Flask, jsonify
from api.v1.views.index import index_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(index_bp)

@app.errorhandler(401)
def unauthorized_error(error):
    """Handle 401 Unauthorized errors."""
    response = jsonify({"error": "Unauthorized"})
    response.status_code = 401
    return response

# Other app configurations and routes
