


from flask import Blueprint
from controllers import master_controller
from lib.authenticate import auth

master = Blueprint("master", __name__)

@master.route("/master", methods=["POST"])
@auth
def add_master():
    return master_controller.add_master()

@master.route("/master", methods=["GET"])
@auth
def get_all_masters():
    return master_controller.get_all_masters()

@master.route("/master/<uuid:master_id>", methods=["GET"])
@auth
def get_master_by_id(master_id):
    return master_controller.get_master_by_id(master_id)

@master.route("/master/<uuid:master_id>", methods=["PUT"])
@auth
def update_master(master_id):
    return master_controller.update_master(master_id)

@master.route("/master/<uuid:master_id>", methods=["DELETE"])
@auth
def delete_master(master_id):
    return master_controller.delete_master(master_id)


