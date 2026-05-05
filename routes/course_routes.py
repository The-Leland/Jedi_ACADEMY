


from flask import Blueprint
from controllers import course_controller
from lib.authenticate import auth

course = Blueprint("course", __name__)

@course.route("/course", methods=["POST"])
@auth
def add_course():
    return course_controller.add_course()

@course.route("/course", methods=["GET"])
@auth
def get_all_courses():
    return course_controller.get_all_courses()

@course.route("/course/<uuid:course_id>", methods=["GET"])
@auth
def get_course_by_id(course_id):
    return course_controller.get_course_by_id(course_id)

@course.route("/course/<uuid:course_id>", methods=["PUT"])
@auth
def update_course(course_id):
    return course_controller.update_course(course_id)

@course.route("/course/<uuid:course_id>", methods=["DELETE"])
@auth
def delete_course(course_id):
    return course_controller.delete_course(course_id)

@course.route("/course/difficulty/<difficulty>", methods=["GET"])
@auth
def get_courses_by_difficulty(difficulty):
    return course_controller.get_courses_by_difficulty(difficulty)
