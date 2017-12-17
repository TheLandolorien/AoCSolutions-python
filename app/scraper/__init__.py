import re
import sys
import requests
from getpass import getpass
from datetime import date, datetime
from bs4 import BeautifulSoup

from flask import current_app as app

from app.models.Puzzle import Puzzle
from app.models import db

AOC_URL = 'http://adventofcode.com'
ADVENT = 12
START_YEAR = 2015


class Scraper:
    def __init__(self):
        self.session = requests.Session()
        self.today = datetime.today()

    def authenticate(self):
        login_url = 'https://github.com/session'
        auth_url = '{}/auth/github'.format(AOC_URL)

        response = self.session.get(auth_url)
        auth_soup = BeautifulSoup(response.text, 'html.parser')
        authenticity_token = auth_soup \
            .find(attrs={'action': '/session'}) \
            .find(attrs={'name': 'authenticity_token'})['value']

        username = app.config['GITHUB_USERNAME']
        data = {
            'authenticity_token': authenticity_token,
            'login': username,
            'password': getpass(prompt='GitHub Password: ')
        }

        response = self.session.post(login_url, data=data)
        del data

        github_soup = BeautifulSoup(response.text, 'html.parser')
        return github_soup.find('div', class_='user', string=re.compile(username))

    def scrape(self):
        authenticated = self.authenticate()
        print('Scraping puzzles...', end='')
        sys.stdout.flush()
        if authenticated:
            for year in range(START_YEAR, self.today.year + 1):
                for day in range(1, 26):
                    completed = self.add_puzzle(date(year, ADVENT, day))
                    if not completed:
                        break  # No more puzzles available
            db.session.remove()
            print('done.')
        else:
            print('error!')
            print('Could not log into GitHub as {}.'.format(app.config['GITHUB_USERNAME']))
            print('Check if password is correct or if Advent of Code needs to be reauthorized.')

    def add_puzzle(self, puzzle_date):
        puzzle_url = '{}/{}/day/{}'.format(AOC_URL, puzzle_date.year, puzzle_date.day)
        puzzle_response = self.session.get(puzzle_url)

        if puzzle_response.status_code == 200:
            # Get Puzzle
            puzzle_soup = BeautifulSoup(puzzle_response.text, 'html.parser')
            puzzle_name = puzzle_soup.h2.string.replace('-', '').strip().split(': ')[-1]

            # Get Input
            input_url = '{}/{}/day/{}/input'.format(AOC_URL, puzzle_date.year, puzzle_date.day)
            input_response = self.session.get(input_url)
            string = input_response.text

            # Insert into database
            puzzle = Puzzle.prepare(date=puzzle_date, title=puzzle_name, input_data=string)
            db.session.add(puzzle)
            db.session.commit()
            return True

        return False
