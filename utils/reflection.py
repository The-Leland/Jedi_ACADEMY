


from db import db

def populate_object(model_obj, data):
    for key, value in data.items():
        if hasattr(model_obj, key):
            setattr(model_obj, key, value)
