from pymongo import MongoClient
from flask import Flask, render_template, jsonify
import pandas as pd
from flask_cors import CORS

# render_template is for option 2 (monolith)
client = MongoClient("mongodb://localhost:27017")

app = Flask(__name__)
CORS(app)

db = client.Global_Coffee_Consumption
collection1 = db.Coffee_DomesticConsumption
collection2 = db.Coffee_ImportersConsumption
collection3 = db.Coffee_exports
collection4 = db.Coffee_imports
collection5 = db.Coffee_production

@app.route("/api/v1.0/Coffee_DomesticConsumption")
def exportConsumption():
    results =  pd.DataFrame(collection1.find({}, {"_id": 0, "id":0})).to_dict(orient="list")
    return jsonify(results)
    

@app.route("/api/v1.0/Coffee_ImportersConsumption")
def importConsumption():
    results = pd.DataFrame(collection2.find({}, {"_id": 0, "id":0})).to_dict(orient="list")
    return jsonify(results)


@app.route("/api/v1.0/Coffee_exports")
def exports():
    results = pd.DataFrame(collection3.find({}, {"_id": 0, "id":0})).to_dict(orient="list")
    return jsonify(results)
 

@app.route("/api/v1.0/Coffee_imports")
def imports():
    results = pd.DataFrame(collection4.find({}, {"_id": 0, "id":0})).to_dict(orient="list")
    return jsonify(results)
 

@app.route("/api/v1.0/Coffee_production")
def production():
    results = pd.DataFrame(collection5.find({}, {"_id": 0, "id":0})).to_dict(orient="list")
    return jsonify(results)
     

# @app.route("/api/v1.0/Coffee_DomesticConsumption/<Country>")
# def exportCountries(country):
#     results = list(exporters_consumption.find({}, {"Country": country}, {"_id": 0}))
#     return jsonify(results)

# @app.route("/api/v1.0/Coffee_ImportersConsumption/<Country>")
# def importCountries(country):
#     results = list(importers_consumption.find({}, {"Country": country}, {"_id": 0}))
#     return jsonify(results)


# use command line 
# cd Desktop/global-coffee-analysis
# flask run

# now that you have an api for your data, send it

# @app.route("/")
# def home():
#     results = list(collection.find({}, {"Country": country}, {"_id": 0}))
#     return render_template("index.html", coffee=results, title="Global Coffee Dashboard")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", title="Dashboard")

if __name__ == "__main__":
    app.run(debug=True)
