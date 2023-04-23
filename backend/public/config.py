from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

path = os.path.dirname(os.path.abspath(__file__))
db_file = os.path.join(path, 'database.db')

app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_file}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
