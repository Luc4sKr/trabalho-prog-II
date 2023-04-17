from public.config import *
from routes import *

@app.route("/")
def index():
    return "backend"

if __name__ == "__main__":
    app.run(debug=True)