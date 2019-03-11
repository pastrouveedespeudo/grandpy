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
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import mysql.connector
import requests



app = Flask(__name__)



LISTE = []
LISTE_PHRASE = []
LISTE_WIKI = []
LOCALISATION_WIKI = []

def searching(parametre):
    """Here we searching from Python modul(geopy.geocoders)"""
    """address from the input from html page"""
    print(parametre)
    geocoder = Nominatim(user_agent="app.py")
    #parametre is data recup from data()
    
    location = geocoder.geocode(parametre, True, 30)
    localisation = location.address
    localisation = str(localisation)

    #define data from geopy.geocoders into var
    a = location.address
    b = location.latitude
    c = location.longitude
    print(a,b,c,"999999999999999999999999999999999999999999999999999999")
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
    print(para,"46498789798798fezzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
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

    #print(LISTE_WIKI_PARSE,"89749879879879879879879879878")
    
    c = 0
    for i in LISTE_WIKI_PARSE:
        if i == []:
            pass
        else:
            print(i)
            a = search_wikipedia(i)
            LISTE4[c].append(a)

        c+=1

    print("oyéoyéoyéoyéoéyoéyoéyoyéoyé")
    liliste = []
    if LISTE4 == []:
        return "Rien n'a été trouvé cha c bizzard ma gueule"

    lliste = []
    for i in LISTE4:
        lliste.append(i)
        with open("yo.py", "w", errors = "ignore") as file:
            file.write(str(lliste))

    liste5 = []
    for i in lliste:
        if i == [] or i == [[[], [], [], [], [], [], [], [], [], [], []]]:
            pass
        else:
            if i[0] == []:
                pass
            else:
                c= 0
                for j in i[0][0]:
                    for k in j:
                        c+=1

                if c < 200:
                    pass
                elif c > 10000:
                    pass
                else:
                    liste5 = i[0][0]

    with open("yo.py","w") as file:
        file.write(str(liste5[0][:2000]))
    return str(liste5[0][:2000]) + "..."


def search_wikipedia(para):

    
    LISTE4 = [[],[],[],[],[],[],[],[],[],[],[]]
    
    liste = []
    liste2 = []
    liste3 = []
    compteur = 0
    
    print(para,"000000000012345678913456789")
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
        
    liste3 = []  
    #print(LISTE4)
    return LISTE4
 









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
    

    
    if data:
        
        var = searching(dernier_mot)
        print(var,"coucouuuuuuuuuuuuuu548468")
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
        
        
        #print(dataa,"5555555555555555555555555555555555555")
        return dataa

    else:
        #print(data,"5555555555555555555555555555555555555")
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
    

    app.run(debug=True, port=3000)
    home()
     

