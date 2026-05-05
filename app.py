


from flask import Flask
import os
from db import *
from utils.blueprints import register_blueprints
from flask_marshmallow import Marshmallow


FLASK_HOST = os.environ.get("FLASK_HOST", "127.0.0.1")
FLASK_PORT = int(os.environ.get("FLASK_PORT", 5000))

DATABASE_SCHEME = os.environ.get("DATABASE_SCHEME")
DATABASE_USER = os.environ.get("DATABASE_USER")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
DATABASE_ADDRESS = os.environ.get("DATABASE_ADDRESS")
DATABASE_PORT = os.environ.get("DATABASE_PORT")
DATABASE_NAME = os.environ.get("DATABASE_NAME")


app = Flask(__name__)


if DATABASE_SCHEME and DATABASE_USER and DATABASE_PASSWORD and DATABASE_ADDRESS and DATABASE_PORT and DATABASE_NAME:
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"{DATABASE_SCHEME}{DATABASE_USER}:{DATABASE_PASSWORD}"
        f"@{DATABASE_ADDRESS}:{DATABASE_PORT}/{DATABASE_NAME}"
    )

if not app.config.get("SQLALCHEMY_DATABASE_URI"):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///jedi_academy.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)
ma = Marshmallow(app)


register_blueprints(app)


def create_tables():
    with app.app_context():
        print("Creating tables...")
        db.create_all()
        print("Tables created successfully")


if __name__ == "__main__":
    create_tables()
    app.run(host=FLASK_HOST, port=FLASK_PORT)
