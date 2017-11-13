from flask import request
from flask_api import FlaskAPI

from app.models.database import db
from app.routes.user_routes import authenticate, register
from app.routes.ride_routes import request_ride, search_for_ride
from instance.config import app_config

# currently only being used by hello
from app.models.users_model import User
from app.models.drives_model import Rides


def create_app(config_name):
    # creates flask application
    app = FlaskAPI(
            __name__,
            instance_relative_config=True,
            static_url_path='/assets',
            static_folder='../html/light-bootstrap-dashboard-master/assets',
            template_folder='../html/light-bootstrap-dashboard-master',
            )

    # register blueprint here

    # set configurations
    app.config.from_object(app_config[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

    # initialize database with application
    db.init_app(app)

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
    @app.route('/auth', methods=['POST', 'GET'])
    def auth():
        return authenticate(request)

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
    @app.route('/register', methods=['POST', 'GET'])
    def reg():
        return register(request)

    @app.route("/request", methods=['POST', 'GET'])
    def req_ride():
        return request_ride(request)


    """
    GET /search
    Find all the imcompleted ride requests
    Only driver can access this API
    Return JSON: List of imcompleted ride requests
    """
    @app.route("/search", methods=['GET'])
    def search_ride():
        return search_for_ride(request)

    @app.route("/history", methods=['GET'])
    def get_history():
        return get_drive_history(request)

    @app.route("/test", methods=['GET'])
    def hello():
        temp_user = User(
                first_name='Test',
                last_name='Test Last',
                credit_card=1234,
                email='test3211@t1e.scom',
                driver=False,
                username='13211testnsame',
                password='test',
                date_created='test',
                date_modified='test'
                )
        temp_user.save()
        temp_user1 = User(
                first_name='Test',
                last_name='Test Last',
                credit_card=1234,
                email='tes3t1j21@t11e.com',
                driver=False,
                username='2wk121te1stname',
                password='test',
                date_created='test',
                date_modified='test'
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

    @app.route("/", methods=['GET'])
    def defalt():
        return 'Hello from server'

    return app
