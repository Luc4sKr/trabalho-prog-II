from public.config import *


class Height(db.Model):
    id = db.Column (db.Integer, primary_key=True)
    height = db.Column(db.Text)

    def __str__(self):
        return f"{self.id}, {self.height}"
    
    def json(self):
        return{
            "id": self.id,
            "height": self.height
        }