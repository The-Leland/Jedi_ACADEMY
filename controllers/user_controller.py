


from flask import request, jsonify
from db import db

from models.user import Users, UsersSchema
from models.auth_token import AuthTokens
from models.lightsaber import Lightsabers
from utils.reflection import populate_object

from flask_bcrypt import generate_password_hash

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)



def add_user():
    post_data = request.form if request.form else request.get_json()

    new_record = Users.new_user_obj()
    populate_object(new_record, post_data)

    if new_record.password:
        new_record.password = generate_password_hash(new_record.password).decode("utf-8")

    try:
        db.session.add(new_record)
        db.session.commit()

    except Exception:
        db.session.rollback()
        return jsonify({"message": "unable to create user"}), 400

    return jsonify({
        "message": "user created",
        "results": user_schema.dump(new_record)
    }), 201


def get_all_users():
    query = db.session.query(Users).all()
    return jsonify(users_schema.dump(query)), 200


def get_user_by_id(user_id):
    query = db.session.query(Users).filter(Users.user_id == user_id).first()

    if not query:
        return jsonify({"message": "user not found"}), 404

    return jsonify(user_schema.dump(query)), 200


def update_user(user_id):
    post_data = request.form if request.form else request.get_json()

    query = db.session.query(Users).filter(Users.user_id == user_id).first()

    if not query:
        return jsonify({"message": "user not found"}), 404

    populate_object(query, post_data)

    if post_data and "password" in post_data:
        new_password = post_data.get("password")
        if new_password:
            query.password = generate_password_hash(new_password).decode("utf-8")

    try:
        db.session.commit()

    except Exception:
        db.session.rollback()
        return jsonify({"message": "unable to update user"}), 400

    return jsonify({
        "message": "user updated",
        "results": user_schema.dump(query)
    }), 200


def delete_user(user_id):
    query = db.session.query(Users).filter(Users.user_id == user_id).first()

    if not query:
        return jsonify({"message": "user not found"}), 404

   
    db.session.query(AuthTokens).filter(AuthTokens.user_id == user_id).delete(synchronize_session=False)
    db.session.query(Lightsabers).filter(Lightsabers.owner_id == user_id).delete(synchronize_session=False)

    query.is_active = False

    try:
        db.session.commit()
        
    except Exception:
        db.session.rollback()
        return jsonify({"message": "unable to delete user"}), 400

    return jsonify({"message": "user deactivated"}), 200
