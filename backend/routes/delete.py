from public.config import *
from public.generate_response import *

from models.category import Category
from models.book import Book

@app.route("/delete/<string:model_class>/<int:id>", methods=["DELETE"])
def delete(model_class: str, id: int):
    try:
        data = None
        
        if model_class.lower() == "category":
            data = db.session.query(Category).get(id)
            db.session.delete(data)
            db.session.commit()

        if model_class.lower() == "book":
            data = db.session.query(Book).get(id)
            db.session.delete(data)
            db.session.commit()

        if data:
            return generate_response(200, model_class, {}, "successfully deleted")
        
        return generate_response(404, "error", "Resource not found")

    except Exception as e:
        return generate_response(404, "error", f"Error: {e}")