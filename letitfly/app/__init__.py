from flask_api import FlaskAPI, status
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, render_template, abort, request, jsonify  # Blueprints

# For route
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp
from sqlalchemy import exc
import sys

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
    @app.route("/register", methods=['POST'])
    def register():
        # Check if all required attr exist
        # first_name
        # last_name
        # credit_card
        # driver
        # username
        # passowrd
        # if (!request.data or !request.data.get('first_name') or
        #         !request.data.get('last_name') or !request.data.get('credit_card') or
        #         !request.data.get('email') or !request.data.get('driver') or
        #         !request.data.get('username') or !request.data.get('password')):
        #     content = {'err': 'One or more necessary data is missing'}
        #     return content, status.HTTP_400_BAD_REQUEST

        try:
            user_data = request.data
            temp_user = users_model.Users(
                    first_name=user_data.get('first_name'),
                    last_name=user_data.get('last_name'),
                    credit_card=user_data.get('credit_card'),
                    email=user_data.get('email'),
                    driver=user_data.get('driver'),
                    username=user_data.get('username'),
                    password=user_data.get('password'),
                    )
            temp_user.save()
            content = {'message': 'New user created'}
            status_code = status.HTTP_201_CREATED
        except exc.IntegrityError:
            content = {'err': 'One or more necessary data is missing'}
            e = sys.exc_info()[0]
            content = {'err': 'Error from SQLAlchemy', 'info': 'Error: %s' % e}
            status_code = status.HTTP_400_BAD_REQUEST
        except:
            e = sys.exc_info()[0]
            content = {'err': 'Something went wrong', 'info': 'Error: %s' % e}
            status_code = status.HTTP_400_BAD_REQUEST
        finally:
            return content, status_code

    @app.route("/test", methods=['GET'])
    def hello():
        temp_user = users_model.Users(
                first_name='Test',
                last_name='Test Last',
                credit_card=1234,
                email='test311@t1e.scom',
                driver=False,
                username='1311testnsame',
                password='test'
                )
        temp_user.save()
        temp_user1 = users_model.Users(
                first_name='Test',
                last_name='Test Last',
                credit_card=1234,
                email='tes3t21@t11e.com',
                driver=False,
                username='2121te1stname',
                password='test'
                )
        temp_user1.save()
        temp_ride = drives_model.Rides(
                customer=temp_user,
                driver=temp_user1,
                start_location='Test Last',
                end_location='Test Last',
                time_finished='Test Last',
                )
        temp_ride.save()

        return "Hello World!"

    return app
