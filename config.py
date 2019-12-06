import os


class Config:
    '''
    General configuration parent class
    '''
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://emmanuel:lilfranken@localhost/feelings'
    # UPLOADED_PHOTOS_DEST = "app/static/photos"
    SECRET_KEY="verysecret"
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    


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
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://moringa:abc@localhost/feeling"


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
