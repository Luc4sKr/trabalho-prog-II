
from public.config import *


class HairStyle(db.Model):
    id = db.Column (db.Integer, primary_key=True)
    hair_name = db.Column(db.Text)

    def __str__(self):
        return
    
    def json(self):
        return