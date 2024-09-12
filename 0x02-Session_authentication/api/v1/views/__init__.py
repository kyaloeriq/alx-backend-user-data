#!/usr/bin/env python3
"""
This module initializes the app_views Blueprint for the Flask application.
"""

from flask import Blueprint

# Initialize the app_views Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import views so they are registered with the blueprint
from api.v1.views.users import *
