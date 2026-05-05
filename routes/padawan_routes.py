


from flask import Blueprint
from controllers import padawan_controller
from lib.authenticate import auth

padawan = Blueprint("padawan", __name__)

@padawan.route("/padawan", methods=["POST"])
@auth
def add_padawan():
    return padawan_controller.add_padawan()

@padawan.route("/padawan", methods=["GET"])
@auth
def get_all_padawans():
    return padawan_controller.get_all_padawans()

@padawan.route("/padawan/<uuid:padawan_id>", methods=["GET"])
@auth
def get_padawan_by_id(padawan_id):
    return padawan_controller.get_padawan_by_id(padawan_id)

@padawan.route("/padawan/<uuid:padawan_id>", methods=["PUT"])
@auth
def update_padawan(padawan_id):
    return padawan_controller.update_padawan(padawan_id)

@padawan.route("/padawan/<uuid:padawan_id>/promote", methods=["PUT"])
@auth
def promote_padawan(padawan_id):
    return padawan_controller.promote_padawan(padawan_id)

@padawan.route("/padawan/<uuid:padawan_id>", methods=["DELETE"])
@auth
def delete_padawan(padawan_id):
    return padawan_controller.delete_padawan(padawan_id)

