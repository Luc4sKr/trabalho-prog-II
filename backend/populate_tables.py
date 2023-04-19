from public.config import *

from models.minion import Minion
from models.width import Width
from models.height import Height
from models.hair_style import HairStyle
from models.pose import Pose

def populate_all():
    populate_width()
    populate_height()
    populate_pose()
    populate_hair()
    

def populate_width():
    add([
        Width(width="Default", css_width_reference="--default-width", css_dungarees_reference="--minion-dungarees-default"),
        Width(width="Small", css_width_reference="--small-width", css_dungarees_reference="--minion-dungarees-small"),
        Width(width="High", css_width_reference="--high-width", css_dungarees_reference="--minion-dungarees-high")
    ])
    db.session.commit()


def populate_height():
    add([
        Height(height="Default", css_height_reference="--default-height"),
        Height(height="Small", css_height_reference="--small-height"),
        Height(height="High", css_height_reference="--high-height"),
    ])
    db.session.commit()


def populate_pose():
    add([
        Pose(pose_name="T-pose", css_pose_reference="--t-pose"),
        Pose(pose_name="Default", css_pose_reference="--default-pose")
    ])
    db.session.commit()


def populate_hair():
    add([
        HairStyle(hair_name="Bald"),
        HairStyle(hair_name="Mohican")
    ])
    db.session.commit()


def add(list_of_items: list):
    for item in list_of_items:
        db.session.add(item)

if __name__ == "__main__":
    with app.app_context():
        populate_all()

        print("=-" * 40)
        print("TABELAS POPULADAS")
        print("=-" * 40)