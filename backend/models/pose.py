from public.config import *


class Pose(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pose_name = db.Column(db.Text)

    def __str__(self):
        return

    def json(self):
        return