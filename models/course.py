


import uuid
import marshmallow as ma
from sqlalchemy.dialects.postgresql import UUID

from db import db


class Courses(db.Model):
    __tablename__ = "Courses"

    course_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    instructor_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Masters.master_id"), nullable=False)

    course_name = db.Column(db.String(), unique=True, nullable=False)
    difficulty = db.Column(db.String())
    duration_weeks = db.Column(db.Integer())
    max_students = db.Column(db.Integer())

    
    instructor = db.relationship("Masters", back_populates="courses")
    enrollments = db.relationship("PadawanCourses", back_populates="course", cascade="all, delete")

    def __init__(self, instructor_id, course_name, difficulty, duration_weeks, max_students):
        self.instructor_id = instructor_id
        self.course_name = course_name
        self.difficulty = difficulty
        self.duration_weeks = duration_weeks
        self.max_students = max_students

    def new_course_obj():
        return Courses(
            instructor_id=None,
            course_name=None,
            difficulty=None,
            duration_weeks=None,
            max_students=None
        )



class CoursesSchema(ma.Schema):
    course_id = ma.fields.UUID()
    instructor_id = ma.fields.UUID()
    course_name = ma.fields.String()
    difficulty = ma.fields.String()
    duration_weeks = ma.fields.Integer()
    max_students = ma.fields.Integer()

    class Meta:
        fields = (
            "course_id",
            "instructor_id",
            "course_name",
            "difficulty",
            "duration_weeks",
            "max_students",
        )



