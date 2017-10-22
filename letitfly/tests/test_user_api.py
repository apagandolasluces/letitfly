import unittest
import os
import json
from app import create_app, db


class UserAPITestCase(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.user_data = {
                "first_name": "a",
                "last_name": "a",
                "credit_card": 1234,
                "email": "1.@.1c12om",
                "driver": False,
                "username": "n1a2me",
                "password": "a"
                }
        self.missing_value_user_data = {
                "first_name": "a",
                "last_name": "a",
                # "credit_card": 1234, "email": "1.@.1c12om",
                "driver": False,
                "username": "n1a2me",
                "password": "a"
                }
        self.user_auth_data = {
                "username": "n1a2me",
                "password": "a"
                }
        self.missing_value_user_auth_data = {
                "password": "a"
                }
        self.wrong_username_user_auth_data = {
                "username": "1n1a2me",
                "password": "a"
                }
        self.wrong_pw_user_auth_data = {
                "username": "1n1a2me",
                "password": "a"
                }
        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()

    """Helper methods"""
    def jsonify(self, data):
        return json.loads(data.decode('utf-8'))

    def register(self, data):
        return self.client().post(
                '/register',
                data=json.dumps(data),
                content_type='application/json'
                )

    def auth(self, data):
        return self.client().post(
                '/auth',
                data=json.dumps(data),
                content_type='application/json'
                )

    """Testing cases"""

    """Testing POST /register"""
    def test_GET_hello(self):
        """Test it can call GET /hello and get hello"""
        res = self.client().get('/hello')
        self.assertEqual(res.status_code, 200)
        self.assertIn('hello', str(res.data))

    def test_POST_register(self):
        """Test it returns 201 """
        res = self.register(self.user_data)
        res_in_json = self.jsonify(res.data)
        self.assertEqual(res.status_code, 201)
        self.assertIn('New user created', str(res_in_json['message']))

    def test_POST_register_missing_attr(self):
        """Test it returns 400 when one or more value is missing"""
        res = self.register(self.missing_value_user_data)
        res_in_json = self.jsonify(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertIn('Missing value', str(res_in_json['err']))

    def test_POST_register_dup_attr(self):
        """Test it returns 400 when email or 
        username already taken (duplicate)"""
        self.register(self.user_data)
        res = self.register(self.user_data)
        res_in_json = self.jsonify(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertIn('Duplicate value', str(res_in_json['err']))

    """Testing POST /auth"""
    def test_POST_auth(self):
        """Test it returns 200 with correct username and password"""
        self.register(self.user_data)
        res = self.auth(self.user_auth_data)
        res_in_json = self.jsonify(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertIn(
                'You logged in successfully',
                str(res_in_json['message']))
        self.assertIsNotNone(res_in_json['access_token'])

    def test_POST_auth_missing_value(self):
        """Test it returns 500 for missing value"""
        res = self.auth(self.missing_value_user_auth_data)
        res_in_json = self.jsonify(res.data)
        self.assertEqual(res.status_code, 500)
        self.assertIn(
                'username',
                str(res_in_json['err']))

    def test_POST_auth_wrong_username(self):
        """Test it returns 401 for wrong username"""
        self.register(self.user_data)
        res = self.auth(self.wrong_username_user_auth_data)
        res_in_json = self.jsonify(res.data)
        print(str(res.data))
        self.assertEqual(res.status_code, 401)
        self.assertIn(
                'Invalid username or password',
                str(res_in_json['err']))

    def test_POST_auth_wrong_password(self):
        """Test it returns 401 for wrong password"""
        self.register(self.user_data)
        res = self.auth(self.wrong_username_user_auth_data)
        res_in_json = self.jsonify(res.data)
        print(str(res.data))
        self.assertEqual(res.status_code, 401)
        self.assertIn(
                'Invalid username or password',
                str(res_in_json['err']))

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
