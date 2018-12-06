import os

class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY')
    MAPBOX_TOKEN = os.environ.get('MAPBOX_TOKEN')


