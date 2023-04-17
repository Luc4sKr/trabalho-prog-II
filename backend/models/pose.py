from public.config import *


class Pose(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pose_name = db.Column(db.Text)

    def __str__(self):
        return f"{self.id}, {self.pose_name}"

    def json(self):
        return{
            "id": self.id,
            "pose": self.pose_name
        }