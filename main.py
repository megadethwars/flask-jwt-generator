from flask import Flask, jsonify,request
from flask import Flask, jsonify, request
from jsonschema import validate, ValidationError
from flask_jwt_extended import jwt_required,JWTManager,create_access_token
from datetime import timedelta
from flask_cors import CORS
from dotenv import load_dotenv
import os

from app.appFile import create_app

load_dotenv()
config_name = os.getenv('FLASK_ENV')

app = create_app(config_name)

if __name__ == '__main__':
    app.run(debug=True)