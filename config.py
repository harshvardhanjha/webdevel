import os

# default config
class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = '\xc3\xea\xc6\xed\xc9\xc6Kz\x9ft\xfbf\xcbD\x9b..C\x17\xb2"\xd5S\xed'
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
	# print SQLALCHEMY_DATABASE_URI

class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevelopmentConfig(BaseConfig):
	DEBUG = True

class ProductionConfig(BaseConfig):
	DEBUG = False