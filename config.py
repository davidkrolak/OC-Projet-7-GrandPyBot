import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    GOOGLE_CLOUD_TOKEN_BACK = os.environ.get('GOOGLE_CLOUD_TOKEN_BACK')
    GOOGLE_CLOUD_TOKEN_FRONT = os.environ.get('GOOGLE_CLOUD_TOKEN_FRONT')
