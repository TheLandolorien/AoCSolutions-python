# AoCSolutions-python
Python (3.6) solutions to Advent of Code Exercises.

Solutions are served over Flask app and Puzzle information (titles and inputs) are stored in SQLite database via web scraper.

The scrape only supports GitHub authentication.

## Getting Started

First, download this repository using `git`.

```shell
git clone https://github.com/futuregarnet/AoCSolutions-python.git
cd AoCSolutions-python
```

### Install tools

If you don't have them already, you'll need node, bower and gulp to be installed globally on your machine.  

1. Install [Python3](https://www.python.org/downloads/).  This includes pip - the Python package management system.  

### Install the dependencies
Change directory into the new project you just cloned, then install dependencies.

```shell
pip install -r requirements
```

Note: You may want to use Python virtual environments to help manage requirements across Python versions [virtualenv](https://github.com/pypa/virtualenv)

### Flask Environment Variable
You will need to set the `FLASK_APP` env in order to run this Flask-based application.

```shell
export FLASK_APP=manage.py
```

### GitHub Configuration

The scraper looks for your GitHub username in a file called `config.json`. Copy the template:

```shell
cp config-template.json config.json
```

Then, replace the **&lt;GITHUB_USERNAME&gt;** placeholder with your GitHub username.

You will need a GitHub account that has already authorized Advent of Code.
Go to the the [AoC GitHub Login page](http://adventofcode.com/auth/github) to authorize GitHub access to AoC for the first time.

## Database Configuration
You will need to initialize the database and scrape puzzle information before proceeding.
Use the following commands to create a data-dev.sqlite file as your SQLite database and store all of the puzzle information. 

```shell
flask db init
flask db upgrade
flask scrape
```

You will be prompted for your GitHub password.
Python will try to mask your password input but custom terminals may display your password (i.e. PyCharm).
However, your password is not stored or saved and is only used to authenticate with GitHub (see: [scraper source code](https://github.com/futuregarnet/AoCSolutions-python/blob/master/app/scraper/__init__.py)).

## Running Flask
Once the database is setup use the following to run the application:

```shell
flask run
```
**NOTE**: `FLASK_APP` will still need to be set in order to avoid errors.

Navigate to [localhost:5000](http://localhost:5000) to select puzzle solutions.
