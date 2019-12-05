import os


class Config:
    '''
    General configuration parent class
    '''
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://charles:123@localhost/feeling'
    # UPLOADED_PHOTOS_DEST = "app/static/photos"
    SECRET_KEY="verysecret"

    


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestConfig(Config):
    """
    Test configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    """
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://charles:123@localhost/feeling_test"


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG=True


config_options = {
    "development": DevConfig,
    "production": ProdConfig,
    "test": TestConfig
}
