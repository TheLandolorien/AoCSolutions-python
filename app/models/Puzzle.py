from datetime import datetime
from app.models import db


class Puzzle(db.Model):
    __tablename__ = 'puzzle'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    title = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    input_id = db.Column(db.Integer, db.ForeignKey('input.id'))
    input = db.relationship('Input', backref=db.backref('puzzle', lazy=True))

    db.UniqueConstraint('date', 'title', 'part_nbr', name='uix_puzzle')

    def __repr__(self):
        return '[Date={}, Puzzle={}, Part={}]'.format(Puzzle.date, Puzzle.title, Puzzle.part_nbr)


class Input(db.Model):
    __tablename__ = 'input'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '[Input={}, Text={}...]'.format(Input.id, Input.text[0:10])
