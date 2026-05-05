


from flask import request, jsonify
from db import db

from models.master import Masters, MastersSchema
from utils.reflection import populate_object

master_schema = MastersSchema()
masters_schema = MastersSchema(many=True)


def add_master():
    post_data = request.form if request.form else request.get_json()

    new_record = Masters.new_master_obj()
    populate_object(new_record, post_data)

    try:
        db.session.add(new_record)
        db.session.commit()
        
    except:
        db.session.rollback()
        return jsonify({"message": "unable to create master"}), 400

    return jsonify({
        "message": "master created",
        "results": master_schema.dump(new_record)
    }), 201


def get_all_masters():
    query = db.session.query(Masters).all()
    return jsonify(masters_schema.dump(query)), 200


def get_master_by_id(master_id):
    query = db.session.query(Masters).filter(Masters.master_id == master_id).first()

    if not query:
        return jsonify({"message": "master not found"}), 404

    return jsonify(master_schema.dump(query)), 200


def update_master(master_id):
    post_data = request.form if request.form else request.get_json()

    query = db.session.query(Masters).filter(Masters.master_id == master_id).first()

    if not query:
        return jsonify({"message": "master not found"}), 404

    populate_object(query, post_data)

    try:
        db.session.commit()

    except:
        db.session.rollback()
        return jsonify({"message": "unable to update master"}), 400

    return jsonify({
        "message": "master updated",
        "results": master_schema.dump(query)
    }), 200


def delete_master(master_id):
    query = db.session.query(Masters).filter(Masters.master_id == master_id).first()

    if not query:
        return jsonify({"message": "master not found"}), 404

    query.max_padawans = 0  

    try:
        db.session.commit()

    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete master"}), 400

    return jsonify({"message": "master deactivated"}), 200
