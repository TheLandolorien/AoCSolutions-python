from datetime import datetime
from app.models import db


class Puzzle(db.Model):
    __tablename__ = 'puzzle'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    title = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    input_id = db.Column(db.Integer, db.ForeignKey('input.id'))
    input = db.relationship('Input', backref=db.backref('puzzle', cascade='all, delete-orphan', lazy=True))

    db.UniqueConstraint('date', 'title', 'part_nbr', name='uix_puzzle')

    def __repr__(self):
        return '[Date={}, Puzzle={}, Part={}]'.format(Puzzle.date, Puzzle.title, Puzzle.part_nbr)

    @staticmethod
    def prepare(date, title, input_data):
        existing_puzzles = db.session.query(Puzzle) \
            .filter(Puzzle.date == date,
                    Puzzle.title == title) \
            .all()

        for existing_puzzle in existing_puzzles:
            db.session.delete(existing_puzzle)
            db.session.commit()

        input_id = db.session.query(Input.id).filter(Input.text == input_data).first()[0]
        return Puzzle(date=date, title=title, input_id=input_id)


class Input(db.Model):
    __tablename__ = 'input'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '[Input={}, Text={}...]'.format(Input.id, Input.text[0:10])

    @staticmethod
    def prepare(text):
        existing_inputs = db.session.query(Input) \
            .filter(Input.text == text) \
            .all()

        for existing_input in existing_inputs:
            db.session.delete(existing_input)
            db.session.commit()

        return Input(text=text)

