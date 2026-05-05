


from flask import request, jsonify
from db import db

from models.course import Courses, CoursesSchema
from utils.reflection import populate_object

course_schema = CoursesSchema()
courses_schema = CoursesSchema(many=True)


def add_course():
    post_data = request.form if request.form else request.get_json()

    new_record = Courses.new_course_obj()
    populate_object(new_record, post_data)

    if not new_record.instructor_id or not new_record.course_name:
        return jsonify({"message": "missing required fields"}), 400

    try:
        db.session.add(new_record)
        db.session.commit()

    except:
        db.session.rollback()
        return jsonify({"message": "unable to create course"}), 400

    return jsonify({"message": "course created", "results": course_schema.dump(new_record)}), 201


def get_all_courses():
    query = db.session.query(Courses).all()
    return jsonify(courses_schema.dump(query)), 200


def get_course_by_id(course_id):
    query = db.session.query(Courses).filter(Courses.course_id == course_id).first()

    if not query:
        return jsonify({"message": "course not found"}), 404

    return jsonify(course_schema.dump(query)), 200


def update_course(course_id):
    post_data = request.form if request.form else request.get_json()

    query = db.session.query(Courses).filter(Courses.course_id == course_id).first()

    if not query:
        return jsonify({"message": "course not found"}), 404

    populate_object(query, post_data)

    try:
        db.session.commit()

    except:
        db.session.rollback()
        return jsonify({"message": "unable to update course"}), 400

    return jsonify({
        "message": "course updated",
        "results": course_schema.dump(query)
    }), 200


def delete_course(course_id):
    query = db.session.query(Courses).filter(Courses.course_id == course_id).first()

    if not query:
        return jsonify({"message": "course not found"}), 404

    try:
        db.session.delete(query)
        db.session.commit()
        
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete course"}), 400

    return jsonify({"message": "course deleted"}), 200


def get_courses_by_difficulty(difficulty):
    query = db.session.query(Courses).filter(Courses.difficulty == difficulty).all()
    return jsonify(courses_schema.dump(query)), 200
