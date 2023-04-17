from public.config import *
from routes import *

@app.route("/")
def index():
    return "backend"

if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)