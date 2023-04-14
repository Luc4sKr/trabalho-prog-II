from public.config import *

class HairStyle(db.Model):
    id = db.Column (db.Integer, primary_key = True)
    hairname = db.Column (db.Text)


class Amountofeyes(db.Model):
    id = db.Column (db.Integer, primary_key = True)
    amount = db.Column (db.Integer)

class Height (db.Model):
    id = db.Column (db.Integer, primary_key = True)
    height = db.Column (db.Text)

class Minion(db.Model):
    id = db.Column (db.Integer, primary_key = True)
    name = db.Column (db.Text) #name do bicho
    hair_id= db.Column (db.Integer,db.ForeignKey(HairStyle.id), nullable =False)
    hair = db.relationship ("HairStyle")
    eyes_id = db.Column (db.Integer,db.ForeignKey(Amountofeyes.id), nullable =False)
    eyes = db.relationship ("Amountofeyes")
    height_id = db.Column (db.Integer,db.ForeignKey(Height.id), nullable =False)
    height = db.relationship ("Height")


