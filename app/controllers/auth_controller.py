from flask import Blueprint, jsonify, request
from jsonschema import validate, ValidationError
from flask_jwt_extended import create_access_token
from app.services.auth_service import login_schema, create_jwt

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        validate(request.json, login_schema)
    except ValidationError as e:
        return jsonify(message='Invalid request format'), 400

    username = request.json.get('username')
    password = request.json.get('password')

    if username == 'admin' and password == 'password':
        token = create_jwt(username)
        return jsonify(token=token), 200
    else:
        return jsonify(message='Invalid credentials'), 401