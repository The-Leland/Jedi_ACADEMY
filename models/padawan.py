


import uuid
import marshmallow as ma
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

from db import db


class Padawans(db.Model):
    __tablename__ = "Padawans"

    padawan_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    master_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Masters.master_id"), nullable=False)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Users.user_id"), nullable=False)
    species_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Species.species_id"), nullable=False)

    padawan_name = db.Column(db.String(), unique=True, nullable=False)
    age = db.Column(db.Integer())
    training_level = db.Column(db.Integer())
    graduation_date = db.Column(db.DateTime(), nullable=True)

    master = db.relationship("Masters", back_populates="padawans")
    user = db.relationship("Users", back_populates="padawan")
    species = db.relationship("Species", back_populates="padawans")
    courses = db.relationship("PadawanCourses", back_populates="padawan", cascade="all, delete")

    def __init__(self, master_id, user_id, species_id, padawan_name, age, training_level, graduation_date=None):
        self.master_id = master_id
        self.user_id = user_id
        self.species_id = species_id
        self.padawan_name = padawan_name
        self.age = age
        self.training_level = training_level
        self.graduation_date = graduation_date

    def new_padawan_obj():
        return Padawans(
            master_id=None,
            user_id=None,
            species_id=None,
            padawan_name=None,
            age=None,
            training_level=None,
            graduation_date=None
        )


class PadawansSchema(ma.Schema):
    padawan_id = ma.fields.UUID()
    master_id = ma.fields.UUID()
    user_id = ma.fields.UUID()
    species_id = ma.fields.UUID()
    padawan_name = ma.fields.String()
    age = ma.fields.Integer()
    training_level = ma.fields.Integer()
    graduation_date = ma.fields.DateTime(allow_none=True)

    class Meta:
        fields = (
            "padawan_id",
            "master_id",
            "user_id",
            "species_id",
            "padawan_name",
            "age",
            "training_level",
            "graduation_date",
        )



