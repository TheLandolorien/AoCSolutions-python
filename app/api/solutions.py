from datetime import datetime

from flask import render_template

from app.api import api


@api.route('/', defaults={'year': datetime.today().year, 'day': 1})
@api.route('/<year>/day/<day>')
def solution(year, day):
    return render_template('solution.html', year=year, day=day)
