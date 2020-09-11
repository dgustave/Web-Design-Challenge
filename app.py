# project/__init__.py
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

@app.route("/", endpoint='home')
def home():
    return render_template("index.html")
@app.route("/compare", endpoint='compare')
def compare():
    return render_template("compare.html")
@app.route("/humidity", endpoint='humidity')
def humidity():
    return render_template("humidity.html")
@app.route("/tempature", endpoint='tempature')
def tempature():
    return render_template("tempature.html")
@app.route("/windspeed", endpoint='windspeed')
def windspeed():
    return render_template("windspeed.html")
@app.route("/cloudiness", endpoint='cloudiness')
def compare(cloudiness):
    return render_template("cloudiness.html")

#run the app
if __name__ == "__main__":
    app.run(debug=True)