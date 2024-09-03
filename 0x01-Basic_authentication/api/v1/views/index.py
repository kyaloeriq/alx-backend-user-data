#!/usr/bin/env python3
# api/v1/views/index.py

from flask import Blueprint, abort

index_bp = Blueprint('index', __name__)


@index_bp.route('/api/v1/unauthorized', methods=['GET'])
def unauthorized():
    """Endpoint that raises a 401 Unauthorized error."""
    abort(401)
