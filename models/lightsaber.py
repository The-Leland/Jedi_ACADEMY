


import uuid
import marshmallow as ma
from sqlalchemy.dialects.postgresql import UUID

from db import db


class Lightsabers(db.Model):
    __tablename__ = "Lightsabers"

    saber_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    owner_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Users.user_id"), nullable=False)
    crystal_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Crystals.crystal_id"), nullable=False)

    saber_name = db.Column(db.String(), unique=True, nullable=False)
    hilt_material = db.Column(db.String())
    blade_color = db.Column(db.String())
    is_completed = db.Column(db.Boolean(), default=False)

    owner = db.relationship("Users", back_populates="lightsabers")
    crystal = db.relationship("Crystals", back_populates="sabers")

    def __init__(self, owner_id, crystal_id, saber_name, hilt_material, blade_color, is_completed=False):
        self.owner_id = owner_id
        self.crystal_id = crystal_id
        self.saber_name = saber_name
        self.hilt_material = hilt_material
        self.blade_color = blade_color
        self.is_completed = is_completed

    def new_lightsaber_obj():
        return Lightsabers(
            owner_id=None,
            crystal_id=None,
            saber_name=None,
            hilt_material=None,
            blade_color=None,
            is_completed=None
        )


class LightsabersSchema(ma.Schema):
    saber_id = ma.fields.UUID()
    owner_id = ma.fields.UUID()
    crystal_id = ma.fields.UUID()
    saber_name = ma.fields.String()
    hilt_material = ma.fields.String()
    blade_color = ma.fields.String()
    is_completed = ma.fields.Boolean()

    class Meta:
        fields = (
            "saber_id",
            "owner_id",
            "crystal_id",
            "saber_name",
            "hilt_material",
            "blade_color",
            "is_completed",
        )





