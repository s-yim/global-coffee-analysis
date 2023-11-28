from pymongo import MongoClient
from flask import Flask, render_template, jsonify

# render_template is for option 2 (monolith)
client = MongoClient("mongodb://localhost:27017/")

app = Flask(__name__)

db = client.Global_Coffee_Consumption
exporters_consumption = db.Coffee_DomesticConsumption
importers_consumption = db.Coffee_ImportersConsumption
exports_collection = db.Coffee_exports
imports_collection = db.Coffee_imports
production_collection = db.Coffee_production

@app.route("/api/v1.0/Coffee_DomesticConsumption")
def exportConsumption():
    year_col_pairs = ["1990/91","1991/92","1992/93","1993/94","1994/95","1995/96","1996/97","1997/98","1998/99","1999/00","2000/01","2001/02","2002/03","2003/04",
                    "2004/05","2005/06","2006/07","2007/08","2008/09","2009/10","2010/11","2011/12","2012/13","2013/14","2014/15","2015/16","2016/17","2017/18","2018/19","2019/20"
"]
    results = list(exporters_consumption.find({}, {"Total_domestic_consumption": 0}))
    return results

@app.route("/api/v1.0/Coffee_ImportersConsumption")
def importConsumption():
    results = list(importers_consumption.find({}, {"Total_import_consumption": 0}))
    return results

@app.route("/api/v1.0/Coffee_exports/<Country>")
def exports(country):
    results = list(exports_collection.find({}, {"Country": country}, {"_id": 0}))
    return results  

@app.route("/api/v1.0/Coffee_imports/<Country>")
def imports(country):
    results = list(imports_collection.find({}, {"Country": country}, {"_id": 0}))
    return results      

@app.route("/api/v1.0/Coffee_production")
def production():
    results = list(production_collection.find({}, {"_id": 0}))
    return results         

@app.route("/api/v1.0/Coffee_DomesticConsumption/<Country>")
def exportCountries(country):
    results = list(exporters_consumption.find({}, {"Country": country}, {"_id": 0}))
    return jsonify(results)

@app.route("/api/v1.0/Coffee_ImportersConsumption/<Country>")
def importCountries(country):
    results = list(importers_consumption.find({}, {"Country": country}, {"_id": 0}))
    return jsonify(results)


# use command line 
# cd Desktop/global-coffee-analysis
# flask run

# now that you have an api for you data, send it

@app.route("/")
def home():
    results = list(collection.find({}, {"Country": country}, {"_id": 0}))
    return render_template("index.html", coffee=results, title="Global Coffee Dashboard")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)



