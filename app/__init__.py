from flask import Flask

from flask_sqlalchemy import SQLAlchemy 
from flask_jwt import JWT
from flask_cors import CORS
db = SQLAlchemy()

from .models import authenticate , identity


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    
    db.init_app(app)
    CORS(app)
    jwt = JWT(app, authenticate, identity)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint)

    return app
