


import functools
from flask import request, jsonify
from datetime import datetime
from uuid import UUID

from db import db
from models.auth_token import AuthTokens


def validate_uuid4(uuid_string):
    
    try:
        UUID(uuid_string, version=4)
        return True
    
    except:
        return False


def validate_token(request_obj):
    auth_token = request_obj.headers.get("auth")

    if not auth_token or not validate_uuid4(auth_token):
        return False

    existing_token = (
        db.session.query(AuthTokens)
        .filter(AuthTokens.auth_token == auth_token)
        .first()
    )

    if not existing_token:
        return False

    if existing_token.expiration_date > datetime.now():
        return existing_token

    return False


def fail_response():
    return jsonify({"message": "authentication required"}), 401


def auth(func):
    @functools.wraps(func)
    def wrapper_auth(*args, **kwargs):
        auth_info = validate_token(request)

        if auth_info:
            return func(*args, **kwargs)
        
        else:
            return fail_response()

    return wrapper_auth
