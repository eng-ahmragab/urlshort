import os
from os import path
from dotenv import load_dotenv #pipenv install python-dotenv


#load the environment variables from .env
load_dotenv(dotenv_path='.env')
print("[*] Loaded .env environment variables")






class Config:
    """
    Use this class to share any default attributes with any subsequent
    classes that inherit from Config.
    """
    DEBUG = False
    #We use CSRF Tokens to validate the HTTP Post requests, so we set a secret token 
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #app configs for file upload
    MAX_CONTENT_LENGTH = 1024 * 1024 #allow content up to 1MB
    UPLOAD_EXTENSIONS = ['.jpg', '.png', '.gif']
    UPLOAD_FOLDER = path.realpath('urlshort/uploads')





class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'




class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db_testing.sqlite'





class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")





