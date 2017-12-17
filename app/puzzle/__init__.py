import re
import sys
import requests
from getpass import getpass
from datetime import date
from bs4 import BeautifulSoup

from app.models.Puzzle import Puzzle, Input
from app.models import db

AOC_URL = 'http://adventofcode.com'
DECEMBER = 12


class Scraper:
    def __init__(self):
        self.session = requests.Session()

    def authenticate(self):
        login_url = 'https://github.com/session'
        auth_url = '{}/auth/github'.format(AOC_URL)

        response = self.session.get(auth_url)
        auth_soup = BeautifulSoup(response.text, 'html.parser')
        authenticity_token = auth_soup \
            .find(attrs={'action': '/session'}) \
            .find(attrs={'name': 'authenticity_token'})['value']

        username = input('GitHub Username: ')
        password = getpass(prompt='GitHub Password: ')
        data = {
            'authenticity_token': authenticity_token,
            'login': username,
            'password': password
        }

        response = self.session.post(login_url, data=data)

        github_soup = BeautifulSoup(response.text, 'html.parser')
        return github_soup.find('div', class_='user', string=re.compile(username))

    def update(self, year):
        authenticated = self.authenticate()
        print('Scraping puzzles...', end='')
        sys.stdout.flush()
        if authenticated:
            for day in range(1, 26):
                puzzle_date = date(year, DECEMBER, day)

                # Get HTML
                puzzle_url = '{}/{}/day/{}'.format(AOC_URL, year, day)
                response = self.session.get(puzzle_url)
                day_soup = BeautifulSoup(response.text, 'html.parser')

                if day_soup.title:
                    puzzle_name = day_soup.title.string
                    # Get Input
                    input_url = '{}/{}/day/{}/input'.format(AOC_URL, year, day)
                    response = self.session.get(input_url)
                    input_str = response.text

                    # Insert into database
                    puzzle_input = Input(text=input_str)
                    db.session.add(puzzle_input)
                    input_id = db.session.query(Input.id).filter(Input.text == input_str).first()[0]
                    puzzle = Puzzle(date=puzzle_date, title=puzzle_name, input_id=input_id)
                    db.session.add(puzzle)

            db.session.commit()
            db.session.remove()
            print('done.')
        else:
            print('error!')
            print('Could not log into GitHub.')
