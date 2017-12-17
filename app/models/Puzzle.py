from datetime import datetime
import sqlalchemy
from app.models import db


class Puzzle(db.Model):
    __tablename__ = 'puzzle'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, unique=True)
    title = db.Column(db.String, nullable=False)
    input = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '[Date={}, Puzzle={}, Input={}...]'.format(Puzzle.date,
                                                          Puzzle.title,
                                                          Puzzle.input[0:10])

    @staticmethod
    def prepare(date, title, input_data):
        existing_puzzles = db.session.query(Puzzle) \
            .filter(Puzzle.date == date) \
            .all()

        for existing_puzzle in existing_puzzles:
            db.session.delete(existing_puzzle)
            db.session.commit()

        return Puzzle(date=date, title=title, input=input_data)

    @staticmethod
    def get_available_dates():
        dates = db.session.query(Puzzle.date).all()
        puzzle_dates = {}
        for d in dates:
            puzzle_date = d.date
            if puzzle_date.year not in puzzle_dates:
                puzzle_dates[puzzle_date.year] = []
            puzzle_dates[puzzle_date.year].append(puzzle_date.day)
        return puzzle_dates

    @staticmethod
    def get_puzzle_input(puzzle_date):
        result = db.session.query(Puzzle.input) \
            .filter(Puzzle.date == puzzle_date) \
            .first()
        return result[0].strip() if result else None

