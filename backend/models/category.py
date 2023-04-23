from public.config import *

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.Text)

    def __str__(self):
        return f"ID: {self.id}, CATEGORY: {self.category_name}"
    
    def json(self):
        return {
            "id": self.id,
            "category_name": self.category_name
        }