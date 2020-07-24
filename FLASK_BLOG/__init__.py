from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "e158a7b4ce29efc15f753a0cb7ddcad2"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)

from FLASK_BLOG import route