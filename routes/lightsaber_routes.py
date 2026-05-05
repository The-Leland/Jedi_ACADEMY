


from flask import Blueprint
from controllers import lightsaber_controller
from lib.authenticate import auth

lightsaber = Blueprint("lightsaber", __name__)

@lightsaber.route("/lightsaber", methods=["POST"])
@auth
def add_lightsaber():
    return lightsaber_controller.add_lightsaber()

@lightsaber.route("/lightsaber", methods=["GET"])
@auth
def get_all_lightsabers():
    return lightsaber_controller.get_all_lightsabers()

@lightsaber.route("/lightsaber/<uuid:saber_id>", methods=["GET"])
@auth
def get_lightsaber_by_id(saber_id):
    return lightsaber_controller.get_lightsaber_by_id(saber_id)

@lightsaber.route("/lightsaber/<uuid:saber_id>", methods=["PUT"])
@auth
def update_lightsaber(saber_id):
    return lightsaber_controller.update_lightsaber(saber_id)

@lightsaber.route("/lightsaber/<uuid:saber_id>", methods=["DELETE"])
@auth
def delete_lightsaber(saber_id):
    return lightsaber_controller.delete_lightsaber(saber_id)
