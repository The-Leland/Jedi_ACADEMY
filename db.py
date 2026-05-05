


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

__all__ = ("db", "ma", "init_db")

db = SQLAlchemy()
ma = Marshmallow()

def init_db(app=None, db_instance=db, ma_instance=ma):

    if isinstance(app, Flask) and isinstance(db_instance, SQLAlchemy) and isinstance(ma_instance, Marshmallow):
        db_instance.init_app(app)
        ma_instance.init_app(app)
        
    else:
        raise ValueError("cannot init db without app, db, and ma objects")



