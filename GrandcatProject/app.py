import os
import subprocess  
from geopy.geocoders import Nominatim

import bs4 as bs
import urllib.request
from PIL import Image
from flask import Flask
from parsage import *
from flask import request
from flask import url_for
from flask import jsonify
from geopy.geocoders import Nominatim
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

Bootstrap(app)


LISTE = []

    
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)



class Echange(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dateHeure = db.Column(db.String(80), unique=True)
    message = db.Column(db.Text(200), unique=True)





        
@app.route('/', methods=['GET','POST'])
def home():
  
    address=""
    yo = request.args.get("input")
    #geolocalisation.recherche(yo, address)


    mess = address
    return render_template("home.html",message=yo, mess = mess)

@app.route('/registration', methods=["GET", "POST"])
def registration():
   
    yo = request.form['test']
    address = []
    path = "https://www.google.com/maps/search/{}".format(yo)

    #geolocalisation.recherche(yo, address)

    roots.root()
    message1 = ["SALUT"]
    
    geocoder = Nominatim()
    location = geocoder.geocode(yo, True, 30)
 
   
    print((location.latitude, location.longitude))
    print(location.address)
    return render_template("home.html",message1=message1)


@app.route('/about')
def about():
    return render_template("pages/about.html")



@app.route('/demo')
def demo():
    return render_template("pages/demo.html")


@app.route("/recup_data",methods=["POST"])
def recup_data():
    return jsonify({"a": "dict", "returned": "becomes", "a": "JSON object"}) 


@app.route('/yo', methods=['GET','POST'])
def yo():
    return render_template("pages/yo.html")


@app.route('/coucou', methods=['GET','POST'])
def coucou():
    yo = request.args.get("test")

    return render_template("pages/coucou.html")

    
@app.errorhandler(404)
def page_not_found(error):
    
    return render_template("errors/404.html"), 404

        
if __name__=="__main__":
    db.create_all()
    app.run(debug=True, port=3000)
    home()

    
    
    
    
    
    
  #ne prend pas encompte self et donc les classes GGrrrr
