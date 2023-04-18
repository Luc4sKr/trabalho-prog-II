from public.config import *

from models.minion import Minion
from models.width import Width
from models.height import Height
from models.hair_style import HairStyle
from models.pose import Pose

def populate_all():
    add(populate_width())
    add(populate_height())

    db.session.commit()
    

def populate_width():
    return [
        Width(width="Default", css_width_reference="--default-width", css_dungarees_reference="--minion-dungarees-default"),
        Width(width="Small", css_width_reference="--small-width", css_dungarees_reference="--minion-dungarees-small"),
        Width(width="High", css_width_reference="--high-width", css_dungarees_reference="--minion-dungarees-high")
    ]

def populate_height():
    return [
        Height(height="Default", css_height_reference="--default-height"),
        Height(height="Small", css_height_reference="--small-height"),
        Height(height="High", css_height_reference="--high-height"),
    ]


def add(list_of_items):
    for item in list_of_items:
        db.session.add(item)