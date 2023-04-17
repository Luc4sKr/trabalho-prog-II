
from public.config import *


class HairStyle(db.Model):
    id = db.Column (db.Integer, primary_key=True)
    hair_name = db.Column(db.Text)

    def __str__(self):
        return f"{self.id}, {self.hair_name}"
    
    def json(self):
        return{
            "id": self.id,
            "hair_name": self.hair_name
        }