from public.config import *

from models.minion import Minion
from models.width import Width
from models.height import Height
from models.hair_style import HairStyle
from models.pose import Pose

if __name__ == "__main__":

    with app.app_context():

        if os.path.exists(db_file) :
            os.remove(db_file)

        db.create_all()

        widths_list = [
            {
                "width": "default",
                "css_width_reference": "--default-width",
                "css_dungarees_reference": "--minion--dungarees-default"
            },
            {
                "width": "small",
                "css_width_reference": "--small-width",
                "css_dungarees_reference": "--minion--dungarees-small"
            },
            {
                "width": "high",
                "css_width_reference": "--high-width",
                "css_dungarees_reference": "--minion--dungarees-high"
            }
        ]

        for item in widths_list:
            new_width = Width(**item)
            db.session.add(new_width)

        
        db.session.commit()
