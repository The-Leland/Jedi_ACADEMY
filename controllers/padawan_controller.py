


from flask import request, jsonify
from db import db

from models.padawan import Padawans, PadawansSchema
from models.padawan_course import PadawanCourses
from utils.reflection import populate_object

padawan_schema = PadawansSchema()
padawans_schema = PadawansSchema(many=True)



def add_padawan():
    post_data = request.form if request.form else request.get_json()

    new_record = Padawans.new_padawan_obj()
    populate_object(new_record, post_data)

    try:
        db.session.add(new_record)
        db.session.commit()

    except:
        db.session.rollback()
        return jsonify({"message": "unable to create padawan"}), 400

    return jsonify({
        "message": "padawan created",
        "results": padawan_schema.dump(new_record)
    }), 201


def get_all_padawans():
    query = db.session.query(Padawans).all()
    return jsonify(padawans_schema.dump(query)), 200


def get_padawan_by_id(padawan_id):
    query = db.session.query(Padawans).filter(Padawans.padawan_id == padawan_id).first()

    if not query:
        return jsonify({"message": "padawan not found"}), 404

    return jsonify(padawan_schema.dump(query)), 200


def update_padawan(padawan_id):
    post_data = request.form if request.form else request.get_json()

    query = db.session.query(Padawans).filter(Padawans.padawan_id == padawan_id).first()

    if not query:
        return jsonify({"message": "padawan not found"}), 404

    populate_object(query, post_data)

    try:
        db.session.commit()

    except:
        db.session.rollback()
        return jsonify({"message": "unable to update padawan"}), 400

    return jsonify({
        "message": "padawan updated",
        "results": padawan_schema.dump(query)
    }), 200


def promote_padawan(padawan_id):
    query = db.session.query(Padawans).filter(Padawans.padawan_id == padawan_id).first()

    if not query:
        return jsonify({"message": "padawan not found"}), 404

    query.training_level = (query.training_level or 0) + 1
    query.graduation_date = datetime.utcnow()

    try:
        db.session.commit()

    except:
        db.session.rollback()
        return jsonify({"message": "unable to promote padawan"}), 400

    return jsonify({
        "message": "padawan promoted",
        "results": padawan_schema.dump(query)
    }), 200


def delete_padawan(padawan_id):
    query = db.session.query(Padawans).filter(Padawans.padawan_id == padawan_id).first()

    if not query:
        return jsonify({"message": "padawan not found"}), 404

    db.session.query(PadawanCourses).filter(PadawanCourses.padawan_id == padawan_id).delete(synchronize_session=False)

    try:
        db.session.delete(query)
        db.session.commit()
        
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete padawan"}), 400

    return jsonify({"message": "padawan deleted"}), 200

