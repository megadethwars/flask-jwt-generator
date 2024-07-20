from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@jwt_required()
def hello():
    return jsonify(message='Hello, World!')

@main_bp.route('/list')
@jwt_required()
def getlist():
    return jsonify(message='Hello, Adolf Hitler')