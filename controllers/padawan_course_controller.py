


from flask import request, jsonify
from db import db

from models.padawan_course import PadawanCourses, PadawanCoursesSchema
from utils.reflection import populate_object

padawan_course_schema = PadawanCoursesSchema()
padawan_courses_schema = PadawanCoursesSchema(many=True)


def add_padawan_course():
    post_data = request.form if request.form else request.get_json()

    new_record = PadawanCourses.new_padawan_course_obj()
    populate_object(new_record, post_data)

    try:
        db.session.add(new_record)
        db.session.commit()

    except:
        db.session.rollback()
        return jsonify({"message": "unable to enroll padawan"}), 400

    return jsonify({
        "message": "padawan enrolled",
        "results": padawan_course_schema.dump(new_record)
    }), 201


def get_all_padawan_courses():
    query = db.session.query(PadawanCourses).all()
    return jsonify(padawan_courses_schema.dump(query)), 200


def get_padawan_course(padawan_id, course_id):
    query = db.session.query(PadawanCourses).filter(
        PadawanCourses.padawan_id == padawan_id,
        PadawanCourses.course_id == course_id
    ).first()

    if not query:
        return jsonify({"message": "enrollment not found"}), 404

    return jsonify(padawan_course_schema.dump(query)), 200


def update_padawan_course(padawan_id, course_id):
    post_data = request.form if request.form else request.get_json()

    query = db.session.query(PadawanCourses).filter(
        PadawanCourses.padawan_id == padawan_id,
        PadawanCourses.course_id == course_id
    ).first()

    if not query:
        return jsonify({"message": "enrollment not found"}), 404

    populate_object(query, post_data)

    try:
        db.session.commit()

    except:
        db.session.rollback()
        return jsonify({"message": "unable to update enrollment"}), 400

    return jsonify({
        "message": "enrollment updated",
        "results": padawan_course_schema.dump(query)
    }), 200


def delete_padawan_course(padawan_id, course_id):
    query = db.session.query(PadawanCourses).filter(
        PadawanCourses.padawan_id == padawan_id,
        PadawanCourses.course_id == course_id
    ).first()

    if not query:
        return jsonify({"message": "enrollment not found"}), 404

    try:
        db.session.delete(query)
        db.session.commit()
        
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete enrollment"}), 400

    return jsonify({"message": "enrollment deleted"}), 200


