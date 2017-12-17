import os
import json

from werkzeug import security

WORKING_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = security.gen_salt(32)
    DEBUG = False
    LOGGING_FORMAT = '%(asctime)s [%(name)d] [%(levelname)s] %(message)s'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True


class Development(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(WORKING_DIR, 'data-dev.sqlite')
    dev_config_path = 'config.json'

    with open(dev_config_path) as json_file:
        config = json.load(json_file)

    GITHUB_USERNAME = config['GITHUB_USERNAME']



class Predix(Config):
    if os.getenv('VCAP_SERVICES'):
        vcap_services = os.getenv('VCAP_SERVICES')

        if 'postgres' in vcap_services:
            postgres_config = vcap_services['postgres'][0]
        else:
            postgres_config = vcap_services['postgres-2.0'][0]

        SQLALCHEMY_DATABASE_URI = postgres_config['credentials']['uri']
        SQLALCHEMY_DATABASE_NAME = postgres_config['name']
        SQLALCHEMY_DATABASE_LABEL = postgres_config['label']
