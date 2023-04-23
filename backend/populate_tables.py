from public.config import *

from models.category import Category

def populate_all():
    category()

def category():
    add([
        Category(category_name="Sci-Fi"),
        Category(category_name="Fantasy"),
        Category(category_name="Romance"),
        Category(category_name="Satire"),
        Category(category_name="Horror"),
        Category(category_name="Murder Mistery"),
        Category(category_name="Thriller"),
        Category(category_name="Non-Fiction")
    ])
    db.session.commit()
    
def add(list_of_items: list):
    for item in list_of_items:
        db.session.add(item)

if __name__ == "__main__":
    with app.app_context():
        populate_all()

        print("=-" * 40)
        print("TABELAS POPULADAS")
        print("=-" * 40)