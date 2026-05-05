


from flask import request, jsonify
from datetime import datetime, timedelta
from flask_bcrypt import check_password_hash

from db import db
from models.user import Users
from models.auth_token import AuthTokens, AuthTokenSchema
from utils.reflection import populate_object

auth_token_schema = AuthTokenSchema()
auth_tokens_schema = AuthTokenSchema(many=True)


def login_user():
    post_data = request.form if request.form else request.get_json()

    email = post_data.get("email")
    password = post_data.get("password")

    if not email or not password:
        return jsonify({"message": "invalid login"}), 401

    user_query = db.session.query(Users).filter(Users.email == email).first()

    if not user_query:
        return jsonify({"message": "invalid login"}), 401

    if not check_password_hash(user_query.password, password):
        return jsonify({"message": "invalid password"}), 401

    now = datetime.utcnow()
    expired_tokens = db.session.query(AuthTokens).filter(
        AuthTokens.user_id == user_query.user_id,
        AuthTokens.expiration_date < now
    ).all()

    for token in expired_tokens:
        db.session.delete(token)

    expiration = now + timedelta(hours=12)
    new_token = AuthTokens(user_id=user_query.user_id, expiration_date=expiration)

    try:
        db.session.add(new_token)
        db.session.commit()

    except:
        db.session.rollback()
        return jsonify({"message": "unable to create token"}), 400

    return jsonify({
        "message": "auth success",
        "auth_info": auth_token_schema.dump(new_token)
    }), 201


def logout_user(auth_info):

    try:
        db.session.delete(auth_info)
        db.session.commit()
        
    except:
        db.session.rollback()
        return jsonify({"message": "unable to logout"}), 400

    return jsonify({"message": "logout successful"}), 200
