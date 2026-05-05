


from flask import Blueprint
from controllers import temple_controller
from lib.authenticate import auth

temple = Blueprint("temple", __name__)

@temple.route("/temple", methods=["POST"])
@auth
def add_temple():
    return temple_controller.add_temple()

@temple.route("/temple", methods=["GET"])
@auth
def get_all_temples():
    return temple_controller.get_all_temples()

@temple.route("/temple/<uuid:temple_id>", methods=["GET"])
@auth
def get_temple_by_id(temple_id):
    return temple_controller.get_temple_by_id(temple_id)

@temple.route("/temple/<uuid:temple_id>", methods=["PUT"])
@auth
def update_temple(temple_id):
    return temple_controller.update_temple(temple_id)

@temple.route("/temple/<uuid:temple_id>", methods=["DELETE"])
@auth
def delete_temple(temple_id):
    return temple_controller.delete_temple(temple_id)

