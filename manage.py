import os
import click
from datetime import datetime

from flask_migrate import Migrate

from app import create_app
from app.models import db
from app.puzzle import Scraper

from app.models.Puzzle import Puzzle, Input

app = create_app(os.getenv('FLASK_CONFIG', 'Development'))

# Flask Extension Initialization
db.init_app(app)
migrate = Migrate(app, db)


# Custom Commands
@app.cli.command()
@click.option('--year', default=datetime.today().year, help='Advent of Code Event Year')
def scrape(year):
    """Scrap Puzzles from Site"""
    scraper = Scraper()
    scraper.update(year)

