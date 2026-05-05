


import uuid
import marshmallow as ma
from sqlalchemy.dialects.postgresql import UUID

from db import db


class Crystals(db.Model):
    __tablename__ = "Crystals"

    crystal_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    crystal_type = db.Column(db.String(), unique=True, nullable=False)
    origin_planet = db.Column(db.String())
    rarity_level = db.Column(db.String())
    force_amplify = db.Column(db.Float())

    sabers = db.relationship("Lightsabers", back_populates="crystal")

    def __init__(self, crystal_type, origin_planet, rarity_level, force_amplify):
        self.crystal_type = crystal_type
        self.origin_planet = origin_planet
        self.rarity_level = rarity_level
        self.force_amplify = force_amplify

    def new_crystal_obj():
        return Crystals(
            crystal_type=None,
            origin_planet=None,
            rarity_level=None,
            force_amplify=None
        )


class CrystalsSchema(ma.Schema):
    crystal_id = ma.fields.UUID()
    color = ma.fields.String()
    rarity = ma.fields.String()
    origin_planet = ma.fields.String()
    is_stable = ma.fields.Boolean()

    lightsabers = ma.fields.Nested("LightsabersSchema", many=True)

    class Meta:
        fields = (
            "crystal_id",
            "color",
            "rarity",
            "origin_planet",
            "is_stable",
            "lightsabers",
        )



