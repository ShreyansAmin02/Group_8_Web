# This file is responsible for handling the main
# pages in our web application
# M for model
# V for views
# C for controller

# But this is for V part of the MVC architecture

from flask import Blueprint, render_template, request
from flask import session
from .models import Event

viewsbp = Blueprint('main', __name__)


@viewsbp.route("/")
def index():
    return render_template('index.html')
