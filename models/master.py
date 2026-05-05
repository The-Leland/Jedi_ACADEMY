


import uuid
import marshmallow as ma
from sqlalchemy.dialects.postgresql import UUID

from db import db


class Masters(db.Model):
    __tablename__ = "Masters"

    master_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Users.user_id"), nullable=False)
    master_name = db.Column(db.String(), unique=True, nullable=False)
    specialization = db.Column(db.String())
    years_training = db.Column(db.Integer())
    max_padawans = db.Column(db.Integer())

    user = db.relationship("Users", back_populates="master")
    padawans = db.relationship("Padawans", back_populates="master")
    courses = db.relationship("Courses", back_populates="instructor")

    def __init__(self, user_id, master_name, specialization, years_training, max_padawans):
        self.user_id = user_id
        self.master_name = master_name
        self.specialization = specialization
        self.years_training = years_training
        self.max_padawans = max_padawans

    def new_master_obj():
        return Masters(
            user_id=None,
            master_name=None,
            specialization=None,
            years_training=None,
            max_padawans=None
        )


class MastersSchema(ma.Schema):
    master_id = ma.fields.UUID()
    user_id = ma.fields.UUID()
    master_name = ma.fields.String()
    specialization = ma.fields.String()
    years_training = ma.fields.Integer()
    max_padawans = ma.fields.Integer()

    class Meta:
        fields = (
            "master_id",
            "user_id",
            "master_name",
            "specialization",
            "years_training",
            "max_padawans"
        )




