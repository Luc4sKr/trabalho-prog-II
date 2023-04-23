from public.config import *
from public.generate_response import *


@app.route("/include/<string:model_class>", methods=["POST"])
def include(model_class: str):
    data = request.get_json()
    try:
        new = None

        print(data)

        if (model_class.lower() == "minion"):
            new = Minion(**data)

        db.session.add(new)
        db.session.commit()

        return generate_response(200, "minion", new.json(), "successfully created")

    except Exception as e:
        return generate_response(400, "minion", {}, f"Error: {e}")