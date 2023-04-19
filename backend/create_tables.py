from public.config import *
from models import *

if __name__ == "__main__":

    with app.app_context():

        if os.path.exists(db_file) :
            os.remove(db_file)

        db.create_all()

        print("=-" * 40)
        print("TABELAS CRIADAS")
        print("=-" * 40)