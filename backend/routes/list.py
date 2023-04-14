from public.config import *
from public.generate_response import *

from models.minion import *


@app.route("/list/<string:class>")
def list(model_class: str):
    data = None

    if model_class.lower() == "minion":
        data = db.session.query(Minion).all()
    

    if data:
        json_list = [obj.json() for obj in data]

    return generate_response(200, "minions", json_list)