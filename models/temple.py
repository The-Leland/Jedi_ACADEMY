


import uuid
import marshmallow as ma
from sqlalchemy.dialects.postgresql import UUID

from db import db


class Temples(db.Model):
    __tablename__ = "Temples"

    temple_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    temple_name = db.Column(db.String(), unique=True, nullable=False)
    planet = db.Column(db.String())
    master_count = db.Column(db.Integer())
    padawan_limit = db.Column(db.Integer())
    is_active = db.Column(db.Boolean(), default=True)


    def __init__(self, temple_name, planet, master_count, padawan_limit, is_active=True):
        self.temple_name = temple_name
        self.planet = planet
        self.master_count = master_count
        self.padawan_limit = padawan_limit
        self.is_active = is_active



    def new_temple_obj():
        return Temples(
            temple_name=None,
            planet=None,
            master_count=None,
            padawan_limit=None,
            is_active=None
        )


class TemplesSchema(ma.Schema):
    temple_id = ma.fields.UUID()
    temple_name = ma.fields.String()
    planet = ma.fields.String()
    master_count = ma.fields.Integer()
    padawan_limit = ma.fields.Integer()
    is_active = ma.fields.Boolean()

    masters = ma.fields.Nested("MastersSchema", many=True)
    padawans = ma.fields.Nested("PadawansSchema", many=True)

    class Meta:
        fields = (
            "temple_id",
            "temple_name",
            "planet",
            "master_count",
            "padawan_limit",
            "is_active",
            "masters",
            "padawans",
        )

