


from flask import Blueprint
from controllers import species_controller
from lib.authenticate import auth

species = Blueprint("species", __name__)

@species.route("/species", methods=["POST"])
@auth
def add_species():
    return species_controller.add_species()

@species.route("/species", methods=["GET"])
@auth
def get_all_species():
    return species_controller.get_all_species()

@species.route("/species/<uuid:species_id>", methods=["GET"])
@auth
def get_species_by_id(species_id):
    return species_controller.get_species_by_id(species_id)

@species.route("/species/<uuid:species_id>", methods=["PUT"])
@auth
def update_species(species_id):
    return species_controller.update_species(species_id)

@species.route("/species/<uuid:species_id>", methods=["DELETE"])
@auth
def delete_species(species_id):
    return species_controller.delete_species(species_id)
