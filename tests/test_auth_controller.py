import json
import unittest
from flask import Flask
from app.controllers.auth_controller import auth_bp
from flask_jwt_extended import JWTManager 

class AuthControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['JWT_SECRET_KEY'] = 'tu_secreto_jwt'  # Configura tu secreto JWT aquí
        self.jwt = JWTManager(self.app)  # Inicializa JWTManager con la aplicación Flask
        self.app.register_blueprint(auth_bp)
        self.client = self.app.test_client()

    def test_login_with_valid_credentials(self):
        data = {
            'username': 'admin',
            'password': 'password'
        }
        response = self.client.post('/login', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.json)

    def test_login_with_invalid_credentials(self):
        data = {
            'username': 'admin',
            'password': 'wrong_password'
        }
        response = self.client.post('/login', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json['message'], 'Invalid credentials')

    def test_login_with_invalid_request_format(self):
        data = {
            'username': 'admin'
        }
        response = self.client.post('/login', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'Invalid request format')

if __name__ == '__main__':
    unittest.main()