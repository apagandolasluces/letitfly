from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, render_template, abort, request  # Blueprints

# For route
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp

# local import
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from app.models import drives_model, users_model

    # POST /auth
    # Flask-JWT auto generate /auth

    # POST /register
    @app.route("/test", methods=['GET'])
    def hello():
        temp_user = users_model.Users(
                first_name='Test',
                last_name='Test Last',
                credit_card=1234,
                email='test@te.com',
                driver=False,
                username='testname',
                password='test'
                )
        temp_user.save()
        temp_ride = drives_model.Rides(
                user_test=temp_user,
                start_location='Test Last',
                end_location='Test Last',
                time_finished='Test Last',
                )
        temp_ride.save()

        return "Hello World!"

    return app
