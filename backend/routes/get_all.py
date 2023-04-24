from public.config import *
from public.generate_response import *

from models.category import Category
from models.book import Book

@app.route("/list/<string:model_class>")
def list(model_class: str):
    try:
        data = None
        json_list = []

        if model_class.lower() == "category":
            data = db.session.query(Category).all()

        if model_class.lower() == "book":
            data = db.session.query(Book).all()

        if data:
            json_list = [obj.json() for obj in data]
            return generate_response(200, model_class, json_list)
        
        return generate_response(404, "error", "Resource not found")
    
    except Exception as e:
        return generate_response(404, "error", f"Error: {e}")

