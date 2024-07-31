import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:232004@localhost:5432/')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)

    class Config:
        SECRET_KEY = 'your_secret_key'
        SQLALCHEMY_TRACK_MODIFICATIONS = False

    class DevelopmentConfig(Config):
        SQLALCHEMY_DATABASE_URI = 'sqlite:///dev_database.db'
        DEBUG = True

    class ProductionConfig(Config):
        SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:232004@localhost:5432/bibliotheque'
        DEBUG = False


class ProductionConfig:
    pass


class DevelopmentConfig:
    pass