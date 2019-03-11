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
import wikipediaapi


app = Flask(__name__)



LISTE = []
LISTE_PHRASE = []
LISTE_WIKI = []
LOCALISATION_WIKI = []

LISTE_PAYS = ["France", "Francemétropolitaine"]

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
    liste = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    data_wiki = request.form['data']

    nettoyage = apostrohpe(data_wiki)
    dernier_mot = parsing_texte(nettoyage)
    
    
    search = searching(dernier_mot)
    print(search[0],'74777777777777777777777777777777777777777')


    c = 0
    for i in search[0]:
        
        if i == ",":
            c+=1
        elif i == " ":
            pass
        else:
            liste[c].append(i)
            
    
    c1 = 0

    print(liste)

    parsing_list = []
    parsing_list_2 = []

    no_number = ""
    no_country = ""

    integer = False

    for i in liste:
        i = "".join(i)
  

        for j in i:
            try:
                j = int(j)
                if type(j) == int:

                    integer = True
            except:
                pass

        if integer == True:
            pass
        else:
            parsing_list.append(i)
            
        integer = False



    country = False
    for i in parsing_list:
        print(i)
        if i == []:
            pass

        else:
            for j in LISTE_PAYS:
                if j == i:
                    country = True
            
            if country == True:
                pass

            else:
                parsing_list_2.append(i)
                
        country = False

    print("pars", parsing_list_2)




    
    page = "cc"
    if data_wiki:
        return jsonify({'data':page})

    #return jsonify({'error':'...'})


 


    






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
     

