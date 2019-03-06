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

def searching(parametre):
    """Here we searching from Python modul(geopy.geocoders)"""
    """address from the input from html page"""
    print(parametre,"ooooooooooooooooooooooooooooooooop")
    geocoder = Nominatim(user_agent="app.py")
    #parametre is data recup from data()
    
    location = geocoder.geocode(parametre, True, 30)
    localisation = location.address
    localisation = str(localisation)

    #define data from geopy.geocoders into var
    a = location.address
    b = location.latitude
    c = location.longitude

    return a, b, c



                 
@app.route('/')
def home():
    """Here we just display home page"""

    title_page = "HOME"
    return render_template("home.html",title_page=title_page)




@app.route('/wiki', methods=["POST"]) 
def wiki():
    b = ""
    data_wiki = request.form['data']

    nettoyage = apostrohpe(data_wiki)
    dernier_mot = parsing_texte(nettoyage)
    
    print(dernier_mot,'74777777777777777777777777777777777777777')
    search = searching(dernier_mot)
    print(search,"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    c = select_wikipedia(search)

    
    if data_wiki:
        print(c)
        print(search,"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        return jsonify({'data':c})

    #return jsonify({'error':'...'})

    



def select_wikipedia(para):
    liste = [[],[],[],[],[],[],[],[],[],[],[],
             [],[],[],[],[],[],[],[],[],[],[]]
    liste2 = []

    LISTE4 = [[],[],[],[],[],[],[],[],[],[],[],
             [],[],[],[],[],[],[],[],[],[],[]]

  
    LISTE_WIKI_PARSE = []
    c=0

    para = str(para)
    for i in para:
   
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

    print(LISTE_WIKI_PARSE,"89749879879879879879879879878")
    
    c = 0
    for i in LISTE_WIKI_PARSE:
        if i == []:
            pass
        else:
            print(i)
            a = search_wikipedia(i)
            LISTE4[c].append(a)

        c+=1
    print(LISTE4)
    if LISTE4 == []:
        return "Rien n'a été trouvé cha c bizzard ma gueule"
    
    return LISTE4


def search_wikipedia(para):

    
    LISTE4 = [[],[],[],[],[],[],[],[],[],[],[],
             [],[],[],[],[],[],[],[],[],[],[]]
    
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
    #print(LISTE4)
    return LISTE4
 







@app.route("/recup_data",methods=["POST"])
def recup_data():
    return jsonify({"a": "dict", "returned": "becomes", "a": "JSON object"}) 




@app.route('/data', methods=["POST"])
def data():
    """Here, we just recup data with request form"""
    """from jquerry function() who define content from input"""
    
    data = request.form['data']

    nettoyage = apostrohpe(data)
    dernier_mot = parsing_texte(nettoyage)

    print(dernier_mot,"ouplapalpalpalpalpalpalpalpalaplpalaplapla")
     
    
    
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


  
    




def parsing_texte(data):
    """Here we'll go to parsing data"""
    """if user input sentences: Salut GrandPY ! Est-ce que tu connais l'adresse de"""
    """we juste take the last word from the sentece"""
    print(data,"coucocuocuocuocuocuocuoc")
    liste = []
    liste2 = [[],[],[],[],[],[],[],[],[],[],[],[],[]]

    
    phrase_accroche = "Salut GrandPY ! Est-ce que tu connais le adresse"
    a = str(data).find(str(phrase_accroche))
    print(a)
    if a >= 0 :
        mot = apostrohpe(data)
        liste.append(mot)

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
        
        
        print(dataa,"5555555555555555555555555555555555555")
        return dataa

    else:
        print(data,"5555555555555555555555555555555555555")
        return data



def apostrohpe(data):

   
    phrase_accroche = "Salut GrandPY ! Est-ce que tu connais l'adresse"
    
    a = str(data).find(str(phrase_accroche))
    
    if a >= 0:
        
        liste = []
        for i in data:
            liste.append(i)
      

        mot = []
        c = 0
        for i in liste:
            
            if liste[c] == "'":
                liste[c] = "e"
                mot.append(liste[c])
                mot.append(" ")  
            else:
                mot.append(liste[c])    
                
            c+=1

        mot = "".join(mot)

        return mot

    else:
        return data





    
@app.errorhandler(404)
def page_not_found(error):
    
    return render_template("errors/404.html"), 404


if __name__== "__main__":
    
    db.create_all()
    app.run(debug=True, port=3000)
    home()
     

