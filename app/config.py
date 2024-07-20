from datetime import timedelta

class Config:
    JWT_SECRET_KEY = 'tu_super_secreto'
    JWT_TOKEN_LOCATION = ['headers']
    JWT_HEADER_NAME = 'Authorization'
    JWT_HEADER_TYPE = 'Bearer'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=1)
    CORS_HEADERS = 'Content-Type'

class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'

class QAConfig(Config):
    DEBUG = False
    ENV = 'qa'

class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'

config_by_name = dict(
    dev=DevelopmentConfig,
    qa=QAConfig,
    prod=ProductionConfig
)