


from flask import Blueprint
from controllers import crystal_controller
from lib.authenticate import auth

crystal = Blueprint("crystal", __name__)

@crystal.route("/crystal", methods=["POST"])
@auth
def add_crystal():
    return crystal_controller.add_crystal()

@crystal.route("/crystal", methods=["GET"])
@auth
def get_all_crystals():
    return crystal_controller.get_all_crystals()

@crystal.route("/crystal/<uuid:crystal_id>", methods=["GET"])
@auth
def get_crystal_by_id(crystal_id):
    return crystal_controller.get_crystal_by_id(crystal_id)

@crystal.route("/crystal/<uuid:crystal_id>", methods=["PUT"])
@auth
def update_crystal(crystal_id):
    return crystal_controller.update_crystal(crystal_id)

@crystal.route("/crystal/<uuid:crystal_id>", methods=["DELETE"])
@auth
def delete_crystal(crystal_id):
    return crystal_controller.delete_crystal(crystal_id)

@crystal.route("/crystal/rarity/<rarity_level>", methods=["GET"])
@auth
def get_crystals_by_rarity(rarity_level):
    return crystal_controller.get_crystals_by_rarity(rarity_level)

