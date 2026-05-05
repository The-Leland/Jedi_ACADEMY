


import uuid
import marshmallow as ma
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

from db import db


class PadawanCourses(db.Model):
    __tablename__ = "PadawanCourses"

    padawan_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Padawans.padawan_id"), primary_key=True)
    course_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Courses.course_id"), primary_key=True)

    enrollment_date = db.Column(db.DateTime(), default=datetime.now)
    completion_date = db.Column(db.DateTime(), nullable=True)
    final_score = db.Column(db.Float(), nullable=True)

    padawan = db.relationship("Padawans", back_populates="courses")
    course = db.relationship("Courses", back_populates="enrollments")

    def __init__(self, padawan_id, course_id, enrollment_date=None, completion_date=None, final_score=None):
        self.padawan_id = padawan_id
        self.course_id = course_id
        self.enrollment_date = enrollment_date or datetime.now()
        self.completion_date = completion_date
        self.final_score = final_score

    def new_padawan_course_obj():
        return PadawanCourses(
            padawan_id=None,
            course_id=None,
            enrollment_date=None,
            completion_date=None,
            final_score=None
        )


class PadawanCoursesSchema(ma.Schema):
    padawan_id = ma.fields.UUID()
    course_id = ma.fields.UUID()
    enrollment_date = ma.fields.DateTime()
    completion_date = ma.fields.DateTime(allow_none=True)
    final_score = ma.fields.Float(allow_none=True)

    class Meta:
        fields = (
            "padawan_id",
            "course_id",
            "enrollment_date",
            "completion_date",
            "final_score",
        )


