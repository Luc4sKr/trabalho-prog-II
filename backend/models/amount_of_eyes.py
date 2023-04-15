from public.config import *


class AmountOfEyes(db.Model):
    id = db.Column (db.Integer, primary_key = True)
    amount = db.Column(db.Integer)

    def __str__(self):
        return
    
    def json(self):
        return