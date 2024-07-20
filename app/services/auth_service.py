from flask_jwt_extended import create_access_token

login_schema = {
    "type": "object",
    "properties": {
        "username": {"type": "string"},
        "password": {"type": "string"}
    },
    "required": ["username", "password"]
}

def create_jwt(username):
    return create_access_token(identity=username)