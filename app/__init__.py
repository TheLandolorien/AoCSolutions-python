import logging

from flask import Flask
from app.api import api


def create_app(env):
    app = Flask(__name__, static_folder='public')
    app.config.from_object('config.{}'.format(env))

    # Register Blueprints
    app.register_blueprint(api)

    # Logging Configuration
    logger = logging.getLogger(__name__)
    logger_level = logging.DEBUG if app.config['DEBUG'] else logging.INFO
    logger.setLevel(logger_level)
    handler = logging.StreamHandler()
    handler.setLevel(logger_level)
    formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return app
