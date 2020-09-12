# project/__init__.py
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import csv


app = Flask(__name__)

@app.route("/home", endpoint='home')
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
def compare():
    return render_template("cloudiness.html")
@app.route("/correlations", endpoint='correlations')
def correlations():
    return render_template("correlations.html")
@app.route("/data", methods=['GET', 'POST'], endpoint='data')
def data():
    if request.method == 'GET':
        # to read csv file 
        df = pd.read_csv("data/processed/cities.csv") 
        # fig = go.Figure(data=[go.Table( header=dict(values=list(df.columns),
        #     fill_color='orange',
        #     align='left'),
        #     cells=dict(values=[df["City"], df["Country"], df["Latitude"], df["Longitude"], df["Date"], df["Cloudiness"],
        # 	df["Humidity"],	df["Max Tempature"], df["Wind Speed"], fill_color='tan', align='left'))])
        # fig.show()
        # , tables=[df.to_html(classes='data')], titles=df.columns.values)
        return render_template("data.html", tables=[df.to_html(classes='data')], titles=df.columns.values)
    elif request.method == 'POST':
        results = []
        data_csv = request.form.get('data_csv').split('\n')
        reader = csv.DictReader(data_csv)
        for info in reader: 
            results.append(dict(info))
        fieldnames = list(results[0].keys())
        # [key for key in results[0].keys()]
        return render_template("data.html", results=results, fieldnames=fieldnames, len=len) 
#run the app
if __name__ == "__main__":
    app.run(debug=True)