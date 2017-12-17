import os

from flask import Blueprint

from app.models.Puzzle import Puzzle

api = Blueprint('api', __name__)

@api.context_processor
def get_dates():
    return dict(get_dates=Puzzle.get_available_dates())

from app.api import solutions
