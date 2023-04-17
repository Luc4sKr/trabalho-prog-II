from public.config import *
from public.generate_response import *

from models.minion import *
from models.width import *


@app.route("/list/<string:model_class>")
def list(model_class: str):
    try:
        data = None
        json_list = []

        if model_class.lower() == "minions":
            data = db.session.query(Minion).all()

        if model_class.lower() == "width":
            data = db.session.query(Width).all()
        
        print(model_class)

        if data:
            json_list = [obj.json() for obj in data]
            return generate_response(200, model_class, json_list)
        
        return generate_response(404, "error", "Resource not found")
    
    except Exception as e:
        return str(e)

