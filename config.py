import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'mum'
    LOG_TO_STDOUT = bool(int(os.environ.get('LOG_TO_STDOUT')))
