


from flask import Blueprint, request, jsonify
from controllers import auth_token_controller
from db import db
from models.auth_token import AuthTokens

auth = Blueprint("auth", __name__)

@auth.route("/user/auth", methods=["POST"])
def login_user():
    return auth_token_controller.login_user()

@auth.route("/logout", methods=["DELETE"])
def logout_user():
    token = None
    auth_header = request.headers.get("Authorization")

    if auth_header and auth_header.startswith("Bearer "):
        token = auth_header.split(" ", 1)[1]

    else:
        data = request.get_json(silent=True) or {}
        token = data.get("auth_token") or data.get("token")

    if not token:
        return jsonify({"message": "missing token"}), 400

    auth_info = db.session.query(AuthTokens).filter(AuthTokens.auth_token == token).first()
    
    if not auth_info:
        return jsonify({"message": "invalid token"}), 404

    return auth_token_controller.logout_user(auth_info)




