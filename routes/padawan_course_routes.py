


from flask import Blueprint
from controllers import padawan_course_controller
from lib.authenticate import auth

padawan_course = Blueprint("padawan_course", __name__)

@padawan_course.route("/padawan-course", methods=["POST"])
@auth
def add_padawan_course():
    return padawan_course_controller.add_padawan_course()

@padawan_course.route("/padawan-course", methods=["GET"])
@auth
def get_all_padawan_courses():
    return padawan_course_controller.get_all_padawan_courses()

@padawan_course.route("/padawan-course/<uuid:padawan_id>/<uuid:course_id>", methods=["GET"])
@auth
def get_padawan_course(padawan_id, course_id):
    return padawan_course_controller.get_padawan_course(padawan_id, course_id)

@padawan_course.route("/padawan-course/<uuid:padawan_id>/<uuid:course_id>", methods=["PUT"])
@auth
def update_padawan_course(padawan_id, course_id):
    return padawan_course_controller.update_padawan_course(padawan_id, course_id)

@padawan_course.route("/padawan-course/<uuid:padawan_id>/<uuid:course_id>", methods=["DELETE"])
@auth
def delete_padawan_course(padawan_id, course_id):
    return padawan_course_controller.delete_padawan_course(padawan_id, course_id)
