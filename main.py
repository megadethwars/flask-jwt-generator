from flask import Flask, jsonify,request
from flask import Flask, jsonify, request
from jsonschema import validate, ValidationError
from flask_jwt_extended import jwt_required,JWTManager,create_access_token
from datetime import timedelta
from flask_cors import CORS
from dotenv import load_dotenv
import os


# app = Flask(__name__)
# CORS(app)
# login_schema = {
#     "type": "object",
#     "properties": {
#         "username": {"type": "string"},
#         "password": {"type": "string"}
#     },
#     "required": ["username", "password"]
# }

# app.config['JWT_SECRET_KEY'] = 'tu_super_secreto'  # Asegúrate de tener esta línea para configurar tu clave secreta
# app.config['JWT_TOKEN_LOCATION'] = ['headers']  # Agrega esta línea para especificar la ubicación del token
# app.config['JWT_HEADER_NAME'] = 'Authorization'  # Esta es la configuración que falta
# app.config['JWT_HEADER_TYPE'] = 'Bearer'  # Opcional, si quieres especificar un tipo de encabezado diferente al predeterminado 'Bearer'
# app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=1)

# # JSON schema for login request
# jwt = JWTManager(app)

# @app.route('/')
# @jwt_required()
# def hello():
#     return jsonify(message='Hello, World!')


# @app.route('/list')
# @jwt_required()
# def getlist():
#     return jsonify(message='Hello, AAdolf Hitler')

# @app.route('/login', methods=['POST'])
# def login():
#     # Validate login request JSON
#     try:
#         validate(request.json, login_schema)
#     except ValidationError as e:
#         return jsonify(message='Invalid request format'), 400

#     # Check login credentials
#     username = request.json.get('username')
#     password = request.json.get('password')

#     if username == 'admin' and password == 'password':
#         # Create JWT token
#         token = create_jwt(username)

#         # Return token as response
#         return jsonify(token=token), 200
#     else:
#         return jsonify(message='Invalid credentials'), 401

# def create_jwt(username):
    
#     token = create_access_token(identity=username)
#     return token

# if __name__ == '__main__':
#     app.run(debug=True)



from app.appFile import create_app

load_dotenv()
config_name = os.getenv('FLASK_ENV')

app = create_app(config_name)

if __name__ == '__main__':
    app.run(debug=True)