from public.config import *


class Pose(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pose_name = db.Column(db.Text)
    css_pose_reference = db.Column(db.Text)

    def __str__(self):
        return f"{self.id}, {self.pose_name}, {self.css_pose_reference}"

    def json(self):
        return{
            "id": self.id,
            "pose_name": self.pose_name,
            "css_pose_reference": self.css_pose_reference
        }