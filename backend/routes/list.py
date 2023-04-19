from public.config import *
from public.generate_response import *

from models.minion import *


@app.route("/list/<string:model_class>")
def list(model_class: str):
    try:
        data = None
        json_list = []

        if model_class.lower() == "minions":
            data = db.session.query(Minion).all()

        if model_class.lower() == "widths":
            data = db.session.query(Width).all()
        
        if model_class.lower() == "heights":
            data = db.session.query(Height).all()

        if model_class.lower() == "hairs":
            data = db.session.query(HairStyle).all()

        if model_class.lower() == "poses":
            data = db.session.query(Pose).all()

        if data:
            json_list = [obj.json() for obj in data]
            return generate_response(200, model_class, json_list)
        
        return generate_response(404, "error", "Resource not found")
    
    except Exception as e:
        return generate_response(404, "error", f"Error: {e}")

