from public.config import *
from .category import Category

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    author = db.Column(db.Text)
    grade = db.Column(db.Integer)
    resume = db.Column(db.Text)
    reading_time = db.Column(db.Integer)
    
    category_id = db.Column(db.Integer, db.ForeignKey(Category.id), nullable=False)

    category = db.relationship("Category")

    def __str__(self):
        return f"ID: {self.id}, CATEGORY_ID: {self.category_id}, {self.title}"
    
    def json(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "grade": self.grade,
            "resume": self.resume,
            "reading_time": self.reading_time,
            "category_id": self.category_id,

            "category": self.category.json()
        }

