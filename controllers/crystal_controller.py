


from flask import request, jsonify
from db import db

from models.crystal import Crystals, CrystalsSchema
from utils.reflection import populate_object

crystal_schema = CrystalsSchema()
crystals_schema = CrystalsSchema(many=True)


def add_crystal():
    post_data = request.form if request.form else request.get_json()

    new_record = Crystals.new_crystal_obj()
    populate_object(new_record, post_data)

    try:
        db.session.add(new_record)
        db.session.commit()

    except:
        db.session.rollback()
        return jsonify({"message": "unable to create crystal"}), 400

    return jsonify({
        "message": "crystal created",
        "results": crystal_schema.dump(new_record)
    }), 201


def get_all_crystals():
    query = db.session.query(Crystals).all()
    return jsonify(crystals_schema.dump(query)), 200


def get_crystal_by_id(crystal_id):
    query = db.session.query(Crystals).filter(Crystals.crystal_id == crystal_id).first()

    if not query:
        return jsonify({"message": "crystal not found"}), 404

    return jsonify(crystal_schema.dump(query)), 200


def update_crystal(crystal_id):
    post_data = request.form if request.form else request.get_json()

    query = db.session.query(Crystals).filter(Crystals.crystal_id == crystal_id).first()

    if not query:
        return jsonify({"message": "crystal not found"}), 404

    populate_object(query, post_data)

    try:
        db.session.commit()

    except:
        db.session.rollback()
        return jsonify({"message": "unable to update crystal"}), 400

    return jsonify({
        "message": "crystal updated",
        "results": crystal_schema.dump(query)
    }), 200


def delete_crystal(crystal_id):
    query = db.session.query(Crystals).filter(Crystals.crystal_id == crystal_id).first()

    if not query:
        return jsonify({"message": "crystal not found"}), 404

    try:
        db.session.delete(query)
        db.session.commit()
        
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete crystal"}), 400

    return jsonify({"message": "crystal deleted"}), 200


def get_crystals_by_rarity(rarity_level):
    query = db.session.query(Crystals).filter(Crystals.rarity_level == rarity_level).all()
    return jsonify(crystals_schema.dump(query)), 200


