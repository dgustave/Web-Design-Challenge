import os, sys

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# 1. Define base flask configuration. 
class Config(object): 

    DEBUG = False
    TESTING = False

    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

class DevelopmentConfig(Config): 
    DEBUG = True
    
class ProductionConfig(Config): 
    DEBUG = False
    pass

class TestingConfig(Config):
    TESTING = True


# Dictionary maps name to configuration
Config = {
    'development': DevelopmentConfig, 
    'production': ProductionConfig, 
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
