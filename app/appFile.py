from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from datetime import timedelta
from .config import config_by_name

def create_app(config_name):
    app = Flask(__name__)
    CORS(app)

    app.config.from_object(config_by_name[config_name])

    # app.config['JWT_SECRET_KEY'] = 'AZHFKKJJKJKDSD12321337485345'
    # app.config['JWT_TOKEN_LOCATION'] = ['headers']
    # app.config['JWT_HEADER_NAME'] = 'Authorization'
    # app.config['JWT_HEADER_TYPE'] = 'Bearer'
    # app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=1)

    jwt = JWTManager(app)

    # Registrar Blueprints
    from app.controllers.auth_controller import auth_bp
    from app.controllers.main_controller import main_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    return app