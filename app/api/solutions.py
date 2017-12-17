from datetime import datetime
from importlib import import_module
from flask import render_template

from app.api import api
from app.models.Puzzle import Puzzle

ADVENT = 12

@api.route('/', defaults={'year': datetime.today().year, 'day': 1})
@api.route('/<int:year>/day/<int:day>')
def solution(year, day):
    try:
        puzzle_solution = import_module('app.solutions.{}.day_{}'.format(year, day))
        puzzle_date = datetime(year, ADVENT, day).date()
        puzzle_input = Puzzle.get_puzzle_input(puzzle_date)
        part_1 = puzzle_solution.part_1(puzzle_input)
        part_2 = puzzle_solution.part_2(puzzle_input)
    except ModuleNotFoundError:
        part_1 = None
        part_2 = None
    return render_template('solution.html', year=year, day=day, part_1_solution=part_1, part_2_solution=part_2)
