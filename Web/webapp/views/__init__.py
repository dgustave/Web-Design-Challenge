from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
from app import db
# List all routes that are available.

@app.route("/home")
def home():
    return render_template("base.html")

def init_app(app):
    db.init_app(app)
