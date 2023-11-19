#!/usr/bin/python3
"""Here are the blueprint for our api's"""
from flask import Blueprint

app_views = Blueprint('app_view', __name__, url_prefix='/api/v1')

from api.v1.views.products import *
from api.v1.views.store import *
from api.v1.views.users import *