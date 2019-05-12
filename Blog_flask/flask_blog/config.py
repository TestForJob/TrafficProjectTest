import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'fet24934t4g9xwxkrk5z44cosrk3v22fadhwnl1fpg5cqkqp0g'
    SQLALCHEMY_DATABASE_URI = 'postgresql://blog_admin:111@localhost/blog_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True