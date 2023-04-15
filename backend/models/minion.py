from public.config import *

from .amount_of_eyes import AmountOfEyes
from .height import Height
from .hair_style import HairStyle
from .pose import Pose


class Minion(db.Model):
    id = db.Column (db.Integer, primary_key = True)
    name = db.Column (db.Text)

    hair_id= db.Column(db.Integer, db.ForeignKey(HairStyle.id), nullable=False)
    eyes_id = db.Column(db.Integer, db.ForeignKey(AmountOfEyes.id), nullable=False)
    height_id = db.Column(db.Integer, db.ForeignKey(Height.id), nullable=False)
    pose_id = db.Column(db.Integer, db.ForeignKey(Pose.id), nullable=False)

    hair = db.relationship ("HairStyle")
    eyes = db.relationship ("AmountOfEyes")
    height = db.relationship ("Height")
    pose = db.relationship ("Pose")

    def __str__(self):
        return

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "hair_id": self.hair_id,
            "eyes_id": self.eyes_id,
            "height_id": self.hair_id,
            "pose_id": self.pose_id,

            "hair": self.hair.json()
            # ... 
        }


