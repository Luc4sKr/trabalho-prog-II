from public.config import *
from models import *
from public.populate_tables import populate_all

if __name__ == "__main__":

    with app.app_context():

        if os.path.exists(db_file) :
            os.remove(db_file)

        db.create_all()
        populate_all()
