# project/__init__.py
# Initialize Global Dependencies:
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import jinja2
db = SQLAlchemy()


def create_app(config = None):
    app = Flask(__name__)
    # load default configuration
    if app.config["ENV"] == "production":
        app.config.from_object("config.ProductionConfig")
    elif app.config["ENV"] == "testing":
        app.config.from_object("config.TestingConfig")
    else:
        app.config.from_object("config.DevelopmentConfig")
    print(f'ENV is set to: {config["ENV"]}')
    from . import  views
    views.init_app(app)
    db.init_app(app)
    return app
app = create_app()

