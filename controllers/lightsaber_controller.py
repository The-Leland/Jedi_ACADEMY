


from flask import request, jsonify
from db import db

from models.lightsaber import Lightsabers, LightsabersSchema
from utils.reflection import populate_object

lightsaber_schema = LightsabersSchema()
lightsabers_schema = LightsabersSchema(many=True)


def add_lightsaber():
    post_data = request.form if request.form else request.get_json()
    print("POST DATA:", post_data)

    new_record = Lightsabers.new_lightsaber_obj()
    populate_object(new_record, post_data)

    if not new_record.owner_id or not new_record.crystal_id or not new_record.saber_name:
        return jsonify({"message": "missing required fields"}), 400

    try:
        db.session.add(new_record)
        db.session.commit()

    except:
        db.session.rollback()
        return jsonify({"message": "unable to create lightsaber"}), 400

    return jsonify({
        "message": "lightsaber created",
        "results": lightsaber_schema.dump(new_record)
    }), 201



def get_all_lightsabers():
    query = db.session.query(Lightsabers).all()
    return jsonify(lightsabers_schema.dump(query)), 200


def get_lightsaber_by_id(saber_id):
    query = db.session.query(Lightsabers).filter(Lightsabers.saber_id == saber_id).first()

    if not query:
        return jsonify({"message": "lightsaber not found"}), 404

    return jsonify(lightsaber_schema.dump(query)), 200


def update_lightsaber(saber_id):
    post_data = request.form if request.form else request.get_json()

    query = db.session.query(Lightsabers).filter(Lightsabers.saber_id == saber_id).first()

    if not query:
        return jsonify({"message": "lightsaber not found"}), 404

    populate_object(query, post_data)

    try:
        db.session.commit()

    except:
        db.session.rollback()
        return jsonify({"message": "unable to update lightsaber"}), 400

    return jsonify({
        "message": "lightsaber updated",
        "results": lightsaber_schema.dump(query)
    }), 200


def delete_lightsaber(saber_id):
    query = db.session.query(Lightsabers).filter(Lightsabers.saber_id == saber_id).first()

    if not query:
        return jsonify({"message": "lightsaber not found"}), 404

    try:
        db.session.delete(query)
        db.session.commit()
        
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete lightsaber"}), 400

    return jsonify({"message": "lightsaber deleted"}), 200

