import unittest
import os
import json
from app import create_app, db


class UserAPITestCase(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.value_user_data = {
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
                # "credit_card": 1234,
                "email": "1.@.1c12om",
                "driver": False,
                "username": "n1a2me",
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
        return self.client().post('/register', data=data)

    def test_GET_hello(self):
        """Test it can call GET /hello and get hello"""
        res = self.client().get('/hello')
        self.assertEqual(res.status_code, 200)
        self.assertIn('hello', str(res.data))

    def test_POST_register(self):
        """Test it returns 201 """
        res = self.register(self.value_user_data)
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
        """Test it returns 400 when one or more value is missing"""
        res = self.register(self.missing_value_user_data)
        res_in_json = self.jsonify(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertIn('Missing value', str(res_in_json['err']))

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
