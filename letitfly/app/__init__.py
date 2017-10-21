from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, render_template, abort  # Blueprints

# local import
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # POST /register
    @app.route("/register", methods=['POST'])
    def hello():
        return "Hello World!"

    return app
