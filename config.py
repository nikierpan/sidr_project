from os import environ
from pathlib import Path
from dotenv import load_dotenv
BASE_DIR = Path(__file__).resolve().parent

dotenv_path = BASE_DIR.joinpath('.env')
if Path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Config:
    SECRET_KEY = environ.get('SECRET_KEY')

    MAIL_SERVER = environ.get('MAIL_SERVER', 'smtp.mail.ru')
    MAIL_PORT = int(environ.get('MAIL_PORT', '465'))
    MAIL_USE_SSL = True
    MAIL_USERNAME = environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = environ.get('MAIL_PASSWORD')
    MAIL_SUBJECT_PREFIX = environ.get('MAIL_SUBJECT_PREFIX')
    MAIL_SENDER = environ.get('MAIL_SENDER')

    ADMIN = environ.get('ADMIN')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = environ.get('DEV_DATABASE_URL')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = environ.get('TEST_DATABASE_URL')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}