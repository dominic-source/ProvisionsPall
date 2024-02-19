#!/usr/bin/python3
"""Here are the blueprint for our api's"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from provisionspall_web.api.v1.views.products import *
from provisionspall_web.api.v1.views.store import *
from provisionspall_web.api.v1.views.users import *
from provisionspall_web.api.v1.views.location import *