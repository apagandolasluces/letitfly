from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from app.models.database import db
from flask import Blueprint, render_template, abort  # Blueprints

# local import
from instance.config import app_config


def create_app(config_name):
    # creates flask application
    app = FlaskAPI(__name__, instance_relative_config=True)

    # register blueprint here

    # set configurations
    app.config.from_object(app_config[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # initialize database with application
    db.init_app(app)

    return app
