from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Creating the app
app = Flask(__name__)

# Setting some database parameters
basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(basedir,'my_amazing_db.db')}"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"]='1af12478ed31cc1a5e02595fe83a33b085b399bc25926d5e'

# Creating the database
db = SQLAlchemy(app)

from my_flask_app import routes