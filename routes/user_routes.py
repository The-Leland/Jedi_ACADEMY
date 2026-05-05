


from flask import Blueprint
from controllers import user_controller
from lib.authenticate import auth

user = Blueprint("user", __name__)

@user.route("/user", methods=["POST"])
def add_user():
    return user_controller.add_user()

@user.route("/user", methods=["GET"])
@auth
def get_all_users():
    return user_controller.get_all_users()

@user.route("/user/<uuid:user_id>", methods=["GET"])
@auth
def get_user_by_id(user_id):
    return user_controller.get_user_by_id(user_id)

@user.route("/user/<uuid:user_id>", methods=["PUT"])
@auth
def update_user(user_id):
    return user_controller.update_user(user_id)

@user.route("/user/<uuid:user_id>", methods=["DELETE"])
@auth
def delete_user(user_id):
    return user_controller.delete_user(user_id)
