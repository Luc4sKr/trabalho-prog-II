from public.config import *
from public.generate_response import *

from models.category import Category
from models.book import Book 

@app.route("/include/<string:model_class>", methods=["POST"])
def include(model_class: str):
    data = request.get_json()
    try:
        new = None
        response = None

        if (model_class.lower() == "category"):
            new = Category(**data)
            response = generate_response(200, "category", new.json(), "successfully created")

        if (model_class.lower() == "Book"):
            new = Book(**data)
            response = generate_response(200, "book", new.json(), "successfully created")

        db.session.add(new)
        db.session.commit()

        return response

    except Exception as e:
        return generate_response(400, "Error", {}, f"Error: {e}")