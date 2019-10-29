import os

'''
    Remember to switch to HerokuConfig for deployment
'''

class MainConfig():
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(MainConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SECRET_KEY = b'219bdfb6e05fe9c4bc427230c597694474beb6b3f6e307e744743a270a3c531c'
    DEBUG = True

    # custom variable. whether changes can be written to database
    DATABASE_ACCESS = True

class HerokuConfig(MainConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = False

    DATABASE_ACCESS = False
