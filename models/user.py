


import uuid
import marshmallow as ma
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

from db import db



class Users(db.Model):
    __tablename__ = "Users"

    user_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    force_rank = db.Column(db.String(), nullable=False)
    midi_count = db.Column(db.Integer(), nullable=False)
    is_active = db.Column(db.Boolean(), default=True)
    joined_date = db.Column(db.DateTime(), default=datetime.now)

    padawan = db.relationship("Padawans", back_populates="user", uselist=False)
    master = db.relationship("Masters", back_populates="user", uselist=False)
    lightsabers = db.relationship("Lightsabers", back_populates="owner")
    tokens = db.relationship("AuthTokens", back_populates="user", cascade="all, delete")

    def __init__(self, username, email, password, force_rank, midi_count):
        self.username = username
        self.email = email
        self.password = password
        self.force_rank = force_rank
        self.midi_count = midi_count



    def new_user_obj():
        return Users(
            username=None,
            email=None,
            password=None,
            force_rank=None,
            midi_count=None
        )



class UsersSchema(ma.Schema):
    user_id = ma.fields.UUID()
    email = ma.fields.String()
    username = ma.fields.String()
    role = ma.fields.String()
    is_active = ma.fields.Boolean()

    class Meta:
        fields = (
            "user_id",
            "email",
            "username",
            "role",
            "is_active"
        )





