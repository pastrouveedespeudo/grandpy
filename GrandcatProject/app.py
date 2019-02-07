import os
import subprocess  
from geopy.geocoders import Nominatim
import request
from bs4 import *
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
from datetime import datetime
import mysql.connector
import requests



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

Bootstrap(app)


LISTE = []
LISTE_PHRASE = []
LISTE_WIKI = []
LOCALISATION_WIKI = []
LISTE_WIKI_PARSE = []
LISTE4 = [[],[],[],[],[],[],[],[],[],[],[],
             [],[],[],[],[],[],[],[],[],[],[]]

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
    LOCALISATION_WIKI.append(location.address)
    
    #we stoking it into variable and return it
    return a, b, c


def parsing_texte(data):
    """Here we'll go to parsing data"""
    """if user input sentences: Salut GrandPY ! Est-ce que tu connais l'adresse de"""
    """we juste take the last word from the sentece"""
    #Salut GrandPY ! Est-ce que tu connais l'adresse de openclassrooms
    liste = []
    liste2 = [[],[],[],[],[],[],[],[],[],[],[],[],[]]

    
    phrase_accroche = "Salut GrandPY ! Est-ce que tu connais l'adresse de"
    a = str(data).find(str(phrase_accroche))
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
        LISTE_PHRASE.append(dataa)
        
        

    elif a <= 0:
        pass
    #ici on va faire le bot

    else:
        pass
    #sois y'a rien et on envoie erreur soit chais pas




def select_wikipedia():
    liste = [[],[],[],[],[],[],[],[],[],[],[],
             [],[],[],[],[],[],[],[],[],[],[]]
    liste2 = []
     
    c=0
    
    for i in LOCALISATION_WIKI[-1]:
        for j in i:
            if j == ",":
                c+=1
            else:
                liste[c].append(j)

    for i in liste:
        if i == []:
            pass
        else:
            liste2.append(i)
    
    for i in liste2:
        LISTE_WIKI_PARSE.append("".join(i))

  

    for i in LISTE_WIKI_PARSE:
        search_wikipedia(i)
            
    

def search_wikipedia(para):
    """Here we just parsing data from source code from wikipedia"""
    """We searching all <p> from source code"""
    """we take it into liste, and we add it to a new liste"""
    """except sentence begening by (cf one two three)"""
    """In a last time we add it again... to a finally liste"""
    """without /n"""
    
    liste = []
    liste2 = []
    liste3 = []
    compteur = 0
    
    
    path = "https://fr.wikipedia.org/wiki/{}".format(para)

    one = "Vous pouvez partager vos connaissances en"
    two = "Géolocalisation"
    three = " sur un des projets-frères de Wikipédia"
    
    requete = requests.get(path)
    page = requete.content
    soup = BeautifulSoup(page, "html.parser")
    
    propriete = soup.find_all("p")
    for i in propriete:
        liste.append(i.get_text())

    c = 0
    for i in liste:
        c+=1
        
        a = str(i).find(one)
        b = str(i).find(two)
        c = str(i).find(three)
      
        if a >= 0 or b >= 0 or c >= 0:
            pass
        else:
            liste2.append(i)

    
    for i in liste2:
        for j in i:
            if j == "\n":
                pass
            else:
                liste3.append(j)

    liste3 = "".join(liste3)
    #print(liste3)
    a = str(liste3).find(str("la page demandée est vide ou contient"))
    b = str(liste3).find(str("Soit vous avez mal écrit"))
    
    if a < 0 and b < 0 and liste3 != "modifier ":
        LISTE4[compteur].append(str(liste3))
        compteur+=1
        #et ajouter a laliste
    liste3 = []  
    
 

        
@app.route('/')
def home():
    """Here we just display home page"""

    title_page = "HOME"
    return render_template("home.html",title_page=title_page)





@app.route('/wiki', methods=["POST"]) 
def wiki():
    
    data_wiki = request.form['data']
    searching(data_wiki)
    select_wikipedia()
  

    
    if data_wiki:
        
        return jsonify({'data':LISTE4[0][0]})

    return jsonify({'error':'...'})



@app.route('/data', methods=["POST"])
def data():
    """Here, we just recup data with request form"""
    """from jquerry function() who define content from input"""
    
    data = request.form['data']
   
    parsing_texte(data)
 
    
    date = datetime.now()
    date = str(date)
    
    LISTE.append("<div style='font-style:italic;'>A {}</div>".format(date))

    LISTE.append("<div><strong>Votre question: </strong></div>")
    LISTE.append("<div style='font-style:italic'>{}</div>".format(data))
    

    
    if data and LISTE_PHRASE == []:
        
        #we take arg from data
        #we stoking variables into var variable
        
        var = searching(data)
        
        LISTE.append("<div style='font-style:italic'><strong>Addresse trouvée: </strong></div>")
        LISTE.append("<div><strong>{}</strong></div>".format(var))
        LISTE.append("<br>")
        
        return jsonify({'data':LISTE})


    elif LISTE_PHRASE != []:
        
        print(LISTE_PHRASE)
        var = searching(str(LISTE_PHRASE[-1]))
        
        LISTE.append("<div style='font-style:italic'><strong>Addresse trouvée: </strong></div>")
        LISTE.append("<div><strong>{}</strong></div>".format(var))
        LISTE.append("<br>")
        
        return jsonify({'data':LISTE})



    return jsonify({'error':'...'})









    
@app.route('/login', methods=["POST"])
def login():
    
    data = request.form['data']
    if data:
        
        bienvenu = "<h1>Bienvenu {} !! le mettre dans une bulle a coté du chat </h1>".format(data)

        return jsonify({'data':bienvenu})

    return jsonify({'error':'...'})



@app.route('/registration', methods=["GET", "POST"])
def registration():
    """This function can be couple to database"""
    """for eventually account"""
    #faudra mettre <name> ca dit coucou le nom
    return render_template("home.html")

        




@app.route('/inscription')
def inscription():
    title_page = "INSCRIPTION"
    return render_template("pages/inscription.html", title_page=title_page)



def search_picture(phrase, liste1):
    """Here we capture picture from google image"""
    """again we go to source code, we capturing all <img>"""
    """and we take it"""
    
    self.phrase = phrase

    liste = []
    self.liste1 = liste1
    
    path =  "https://www.google.co.in/search?q={0}&source=lnms&tbm=isch"
    path1 = path.format(self.phrase)
    requete = requests.get(path1)
    page = requete.content
    soup = BeautifulSoup(page, "html.parser")  
    propriete = soup.find_all("img")
    
    with open("requete.py", "w") as file:
        file.write(str(propriete))
                
    with open("requete.py", "r") as file2:
        b = file2.read()
    liste.append(b)


    for i in range(1):
        a = str(liste).find(str("src"))
        b = str(liste).find(str('" width='))
        
        url = liste[0][a+2:b-3]
        image = str("image_"+self.phrase+str(i)+".jpg")

        liste[0] = liste[0][b:-3]

        urllib.request.urlretrieve(str(url), image)

        self.liste1.append(image)

#a verifier liste1 je sais plus a quoi ca sert








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
def contact():
    return render_template("pages/yo.html")




    
@app.errorhandler(404)
def page_not_found(error):
    
    return render_template("errors/404.html"), 404


if __name__== "__main__":
    
    db.create_all()
    app.run(debug=True, port=3000)
    home()
     

