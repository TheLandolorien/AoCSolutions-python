import re
import sys
import requests
from getpass import getpass
from datetime import date
from bs4 import BeautifulSoup

from flask import current_app as app

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

        username = app.config['GITHUB_USERNAME']
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
        try:
            date(year, DECEMBER, 1)  # Validate date

            authenticated = self.authenticate()
            print('Scraping puzzles...', end='')
            sys.stdout.flush()
            if authenticated:
                for day in range(1, 26):
                    puzzle_date = date(year, DECEMBER, day)

                    puzzle_url = '{}/{}/day/{}'.format(AOC_URL, year, day)
                    response = self.session.get(puzzle_url)

                    if response.status_code == 200:
                        # Get Puzzle
                        puzzle_soup = BeautifulSoup(response.text, 'html.parser')
                        puzzle_name = puzzle_soup.h2.string.replace('-', '').strip().split(': ')[-1]

                        # Get Input
                        input_url = '{}/{}/day/{}/input'.format(AOC_URL, year, day)
                        response = self.session.get(input_url)
                        string = response.text

                        # Insert into database
                        with db.session.no_autoflush:
                            puzzle_input = Input.prepare(text=string)
                            db.session.add(puzzle_input)
                            db.session.commit()

                            puzzle = Puzzle.prepare(date=puzzle_date, title=puzzle_name, input_data=string)
                            db.session.add(puzzle)
                            db.session.commit()
                    else:
                        break  # No more puzzles available for selected year

                db.session.remove()
                print('done.')
            else:
                print('error!')
                print('Could not log into GitHub as {}.'.format(app.config['GITHUB_USERNAME']))
                print('Check if password is correct or if Advent of Code needs to be reauthorized.')

        except TypeError:
            print('error!')
            print('Invalid year: {}'.format(year))
