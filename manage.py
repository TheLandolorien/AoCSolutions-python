import os

from flask_migrate import Migrate

from app import create_app
from app.models import db
from app.scraper import Scraper

from app.models.Puzzle import Puzzle

app = create_app(os.getenv('FLASK_CONFIG', 'Development'))

# Flask Extension Initialization
db.init_app(app)
migrate = Migrate(app, db)


# Custom Commands
@app.cli.command()
def scrape():
    """Scrap Puzzles from Site
    """
    scraper = Scraper()
    scraper.scrape()
