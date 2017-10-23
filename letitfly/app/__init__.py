from flask_api import FlaskAPI, status
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, render_template, abort, request, make_response, jsonify  # Blueprints

# For route
from sqlalchemy import exc
from functools import wraps

# local import
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from app.models.drives_model import Rides
    from app.models.users_model import Users

    # POST /authenticate
    """
    Sample
    POST /authenticate
    Host: localhost:5000
    Content-Type: application/json

    {
        "username": "joe",
        "password": "pass"
    }
    """
    @app.route('/auth', methods=['POST'])
    def authenticate():
        try:
            # Get the user object using their email (unique to every user)
            user = Users.query.filter_by(
                    username=request.data['username']
                    ).first()

            # Try to authenticate the found user using their password
            if user and user.password_is_valid(request.data['password']):
                # Generate the access token.
                # This will be used as the authorization header
                access_token = user.generate_token(user.user_id)
                if access_token:
                    response = {
                            'message': 'You logged in successfully.',
                            'access_token': access_token.decode()
                            }
                    return make_response(jsonify(response)), 200
            else:
                # User does not exist. Therefore, we return an error message
                response = {
                        'err': 'Invalid username or password, Please try again'
                        }
                return make_response(jsonify(response)), 401

        except Exception as e:
            # Create a response containing an string error message
            response = {'err': str(e)}
            # Return a server error using the HTTP Error
            # Code 500 (Internal Server Error)
            return make_response(jsonify(response)), 500

    # POST /register
    """
    Sample json data
    {
        "first_name": "a",
        "last_name": "a12",
        "credit_card": 1234,
        "email": "1.@.1c22o1m1",
        "driver": false,
        "username": "na21211me",
        "password": "a"
    }
    """
    @app.route('/register', methods=['POST'])
    def register():
        try:
            user_data = request.data
            temp_user = Users(
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
        except exc.OperationalError as e:
            # SQLalchemy missing value
            content = {'err': 'Missing value', 'info': 'Error: %s' % e}
            status_code = status.HTTP_400_BAD_REQUEST
        except exc.IntegrityError as e:
            # SQLalchemy insertion error (such as duplicate value)
            content = {'err': 'Duplicate value', 'info': 'Error: %s' % e}
            status_code = status.HTTP_400_BAD_REQUEST
        except Exception as e:
            content = {'err': 'Something went wrong', 'info': 'Error: %s' % e}
            status_code = status.HTTP_400_BAD_REQUEST
        finally:
            return content, status_code

    """
    Helper methods
    get request object and parse access token
    """
    def parse_access_token(req):
        try:
            auth_header = request.headers.get('Authorization')
            return auth_header.split(" ")[1]
        except Exception as e:
            return

    @app.route("/request", methods=['POST'])
    def request_ride():
        access_token = parse_access_token(request)
        # Access token found
        if(access_token):
            try:
                # Decode access token and get user_id that
                # belongs to the user who requested the ride
                user_id = Users.decode_token(access_token)
                ride_data = request.data
                user = Users.find_one_user_by_user_id(user_id)
                temp_ride = Rides(
                        customer=user,
                        # driver is null at this moment
                        start_location='Test Last',
                        end_location='Test Last',
                        )
                temp_ride.save()
                response = {'message': 'Ride requested successfully'}
                status_code = status.HTTP_201_CREATED
            except Exception as e:
                response = {'err': 'Something went wrong', 'info': 'Error: %s' % e}
                status_code = status.HTTP_400_BAD_REQUEST
            finally:
                return response, status_code
        # Access token found
        else:
            response = {'err': 'No access token found'}
            status_code = status.HTTP_400_BAD_REQUEST
            return response, status_code

    @app.route("/test", methods=['GET'])
    def hello():
        temp_user = Users(
                first_name='Test',
                last_name='Test Last',
                credit_card=1234,
                email='test311@t1e.scom',
                driver=False,
                username='1311testnsame',
                password='test'
                )
        temp_user.save()
        temp_user1 = Users(
                first_name='Test',
                last_name='Test Last',
                credit_card=1234,
                email='tes3t21@t11e.com',
                driver=False,
                username='2121te1stname',
                password='test'
                )
        temp_user1.save()
        temp_ride = Rides(
                customer=temp_user,
                driver=temp_user1,
                start_location='Test Last',
                end_location='Test Last',
                time_finished='Test Last',
                )
        temp_ride.save()

        return "Hello World!"

    @app.route("/hello", methods=['GET'])
    def say_hello():
        return 'hello'

    return app
