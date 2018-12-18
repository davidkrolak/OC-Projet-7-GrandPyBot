import os

class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY')
    GOOGLE_CLOUD_TOKEN = os.environ.get('GOOGLE_CLOUD_TOKEN')
