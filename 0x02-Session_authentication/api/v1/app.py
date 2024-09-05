# api/v1/app.py

from flask import Flask, jsonify, request
from api.v1.views.index import index_bp
from api.v1.auth.basic_auth import BasicAuth  # Make sure you import BasicAuth

app = Flask(__name__)

auth = BasicAuth()

@app.before_request
def before_request():
    """Filter before each request"""
    request.current_user = auth.current_user(request)

# Register blueprints
app.register_blueprint(index_bp)

# Error handling and other routes remain the same...

if __name__ == '__main__':
    import os
    host = os.getenv('API_HOST', '0.0.0.0')
    port = int(os.getenv('API_PORT', 5000))
    app.run(host=host, port=port)
