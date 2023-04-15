from public.config import *


class Height (db.Model):
    id = db.Column (db.Integer, primary_key = True)
    height = db.Column (db.Text)

    def __str__(self):
        return
    
    def json(self):
        return