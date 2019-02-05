import os
import subprocess  
from geopy.geocoders import Nominatim
import request
import bs4 as bs
import urllib.request
from PIL import Image
from flask import Flask
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




    
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)



class Echange(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dateHeure = db.Column(db.String(80), unique=True)
    message = db.Column(db.Text(200), unique=True)





        
@app.route('/')
def home():
    """Here we just display home page"""
    return render_template("home.html")

def searching(parametre):
    """Here we searching from Python modul(geopy.geocoders)"""
    """address from the input from html page"""
    
    geocoder = Nominatim(user_agent="app.py")
    #parametre is data recup from data()
    
    location = geocoder.geocode(parametre, True, 30)
    localisation = location.address
    localisation = str(localisation)

    #define data from geopy.geocoders into var
    a = location.address
    b = location.latitude
    c = location.longitude

    #we stoking it into variable and return it
    return a, b, c


def parsing_texte(data):
    """Here we'll go to parsing data"""
    """if user input sentences: Salut GrandPY ! Est-ce que tu connais l'adresse de"""
    """we juste take the last word from the sentece"""
    
    liste = []
    liste2 = [[],[],[],[],[],[],[],[],[],[],[],[],[]]

    
    phrase_accroche = "Salut GrandPY ! Est-ce que tu connais l'adresse de"
    a =str(data).find(str(phrase_accroche))
    if a >= 0 :
       
        liste.append(data)

        c=0
        for i in liste:
            for j in i :
                liste2[c].append(j)
                if j == " ":
                    c+=1

        c=0
        for i in liste2:
            if i == "" or i == [] :
               pass
            else:
                c+=1
        liste2 = liste2[0:c]
        dataa = "".join(liste2[-1])
        print(dataa)


    elif a <= 0:
        pass
    #ici on va faire le bot

    else:
        pass
    #sois y'a rien et on envoie erreur soit chais pas

def search_wikipedia():
    pass


def search_picture():
    pass



@app.route('/data', methods=["POST"])
def data():
    """Here, we just recup data with request form"""
    """from jquerry function() who define content from input"""
    data = request.form['data']
    print(data)
    if data :
        #we take arg from data (recup input stuff u know bia calm)
        #we stoking variables into var variable
        var = searching(data)
        return jsonify({'data':var})

    return jsonify({'error':'...'})





@app.route('/registration', methods=["GET", "POST"])
def registration():
    """This function can be couple to database"""
    """for eventually account"""
    #faudra mettre <name> ca dit coucou le nom
    return render_template("home.html")

        
@app.route('/demo')
def demo():
     #accueil
     return render_template("pages/demo.html")


@app.route('/about', methods=["POST"])
def about():
    email = request.form['email']
    name = request.form['name']
    

    if name:
        name = name
        jo = "coucou"
        return jsonify({'name':name+ " " +jo})


    
    
    return jsonify({'error':'Missing data!'})
 
    


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


if __name__== "__main__":
    
    db.create_all()
    app.run(debug=True, port=3000)



    home()
     

