# project/__init__.py
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html")

#run the app
if __name__ == "__main__":
    app.run(debug=True)