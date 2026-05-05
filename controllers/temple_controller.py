


from flask import request, jsonify
from db import db

from models.temple import Temples, TemplesSchema
from utils.reflection import populate_object

temple_schema = TemplesSchema()
temples_schema = TemplesSchema(many=True)


def add_temple():
    post_data = request.form if request.form else request.get_json()

    new_record = Temples.new_temple_obj()
    populate_object(new_record, post_data)

    try:
        db.session.add(new_record)
        db.session.commit()

    except:
        db.session.rollback()
        return jsonify({"message": "unable to create temple"}), 400

    return jsonify({
        "message": "temple created",
        "results": temple_schema.dump(new_record)
    }), 201


def get_all_temples():
    query = db.session.query(Temples).all()
    return jsonify(temples_schema.dump(query)), 200


def get_temple_by_id(temple_id):
    query = db.session.query(Temples).filter(Temples.temple_id == temple_id).first()

    if not query:
        return jsonify({"message": "temple not found"}), 404

    return jsonify(temple_schema.dump(query)), 200


def update_temple(temple_id):
    post_data = request.form if request.form else request.get_json()

    query = db.session.query(Temples).filter(Temples.temple_id == temple_id).first()

    if not query:
        return jsonify({"message": "temple not found"}), 404

    populate_object(query, post_data)

    try:
        db.session.commit()

    except:
        db.session.rollback()
        return jsonify({"message": "unable to update temple"}), 400

    return jsonify({
        "message": "temple updated",
        "results": temple_schema.dump(query)
    }), 200


def delete_temple(temple_id):
    query = db.session.query(Temples).filter(Temples.temple_id == temple_id).first()

    if not query:
        return jsonify({"message": "temple not found"}), 404

    query.is_active = False

    try:
        db.session.commit()
        
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete temple"}), 400

    return jsonify({"message": "temple deactivated"}), 200

