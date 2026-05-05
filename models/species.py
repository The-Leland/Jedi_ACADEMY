


import uuid
import marshmallow as ma
from sqlalchemy.dialects.postgresql import UUID

from db import db


class Species(db.Model):
    __tablename__ = "Species"

    species_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    species_name = db.Column(db.String(), unique=True, nullable=False)
    homeworld = db.Column(db.String())
    force_sensitive = db.Column(db.Boolean())
    avg_lifespan = db.Column(db.Integer())

    padawans = db.relationship("Padawans", back_populates="species")

    def __init__(self, species_name, homeworld, force_sensitive, avg_lifespan):
        self.species_name = species_name
        self.homeworld = homeworld
        self.force_sensitive = force_sensitive
        self.avg_lifespan = avg_lifespan

    def new_species_obj():
        return Species(
            species_name=None,
            homeworld=None,
            force_sensitive=None,
            avg_lifespan=None
        )


class SpeciesSchema(ma.Schema):
    species_id = ma.fields.UUID()
    species_name = ma.fields.String()
    homeworld = ma.fields.String()
    forse_sensitive = ma.fields.Boolean()
    avg_lifespan = ma.fields.Integer()

    padawans = ma.fields.Nested("PadawansSchema", many=True)

    class Meta:
        fields = (
            "species_id",
            "species_name",
            "homeworld",
            "forse_sensitive",
            "avg_lifespan",
            "padawans",
        )


