import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv.get('app/database/app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
