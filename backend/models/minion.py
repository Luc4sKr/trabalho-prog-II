from public.config import *

class HairStyle(db.Model):
    id = db.Column (db.Integer, primary_key = True)
    hairname = db.Column (db.Text)


class Amountofeyes(db.Model):
    id = db.Column (db.Integer, primary_key = True)
    amount = db.Column (db.Integer)

class Height (db.Model):
    id = db.Column (db.Integer, primary_key = True)
    height = db.Column (db.Text)31 minutes ago
LICENSE
Initial commit
38 minutes ago
README.md
Initial commit
38 minutes ago
README.md
trabalho-prog-II
Repositório para o trabalho de Programação II

About
Repositório para o trabalho de Programação II

Resources
 Readme
License


class Minion(db.Model):
    id = db.Column (db.Integer, primary_key = True)
    name = db.Column (db.Text) #name do bicho
    hair_id= db.Column (db.Integer,db.ForeignKey(HairStyle.id), nullable =False)
    hair = db.relationship ("HairStyle")
    eyes_id = db.Column (db.Integer,db.ForeignKey(Amountofeyes.id), nullable =False)
    eyes = db.relationship ("Amountofeyes")
    height_id = db.Column (db.Integer,db.ForeignKey(Height.id), nullable =False)
    height = db.relationship ("Height")


