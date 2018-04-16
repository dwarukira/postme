import os
import datetime
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET = os.getenv('SECRET')
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    UPLOAD_FOLDER = '{}/uploads/'.format(BASE_DIR)
    
class ConfigDev(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(BASE_DIR, 'test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    JWT_SECRET_KEY = 'test123'
    JWT_EXPIRATION_DELTA= datetime.timedelta(300000)

class ConfigPro(Config):
    DEBUG=False

config = {
        'DEV':ConfigDev,
        'PRO':ConfigPro
}


