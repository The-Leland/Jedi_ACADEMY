


from flask import request, jsonify
from db import db

from models.species import Species, SpeciesSchema
from utils.reflection import populate_object

species_schema = SpeciesSchema()
species_list_schema = SpeciesSchema(many=True)


def add_species():
    post_data = request.form if request.form else request.get_json()

    new_record = Species.new_species_obj()
    populate_object(new_record, post_data)

    try:
        db.session.add(new_record)
        db.session.commit()

    except:
        db.session.rollback()
        return jsonify({"message": "unable to create species"}), 400

    return jsonify({
        "message": "species created",
        "results": species_schema.dump(new_record)
    }), 201


def get_all_species():
    query = db.session.query(Species).all()
    return jsonify(species_list_schema.dump(query)), 200


def get_species_by_id(species_id):
    query = db.session.query(Species).filter(Species.species_id == species_id).first()

    if not query:
        return jsonify({"message": "species not found"}), 404

    return jsonify(species_schema.dump(query)), 200


def update_species(species_id):
    post_data = request.form if request.form else request.get_json()

    query = db.session.query(Species).filter(Species.species_id == species_id).first()

    if not query:
        return jsonify({"message": "species not found"}), 404

    populate_object(query, post_data)

    try:
        db.session.commit()

    except:
        db.session.rollback()
        return jsonify({"message": "unable to update species"}), 400

    return jsonify({
        "message": "species updated",
        "results": species_schema.dump(query)
    }), 200


def delete_species(species_id):
    query = db.session.query(Species).filter(Species.species_id == species_id).first()

    if not query:
        return jsonify({"message": "species not found"}), 404

    try:
        db.session.delete(query)
        db.session.commit()
        
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete species"}), 400

    return jsonify({"message": "species deleted"}), 200


