import os
import bs4 as bs
import urllib.request
from PIL import Image
from flask import Flask
from flask import request
from flask import url_for
from flask import jsonify
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
Bootstrap(app)


LISTE = []


@app.route('/', methods=["GET", "POST"])
def home():

    yo = request.args.get("input")
 
    path = "https://www.google.com/maps/search/{}".format(yo)
    print(yo,"548498464874648")
    print("COUCOUUUUUUUUUUUUUUUUUUU")
    print("COUCOUUUUUUUUUUUUUUUUUUU")
    print("COUCOUUUUUUUUUUUUUUUUUUU")
    print("COUCOUUUUUUUUUUUUUUUUUUU")
    return render_template("home.html",path=path)


@app.route('/about')
def about():

    a = request.args.get("a",0,type=int)
    b = request.args.get("b",0,type=int)
    resutat=a + b
    print(resutat)
    return render_template("pages/about.html",resutat=resutat)


@app.route('/yo',methods=['GET','POST']) 
def yo():

    if request.method == "GET":
        return render_template("pages/yo.html")
    else:
        print("post")
        print(request.args)
        return render_template("pages/yo.html")
        


@app.route('/demo')
def demo():
    return render_template("pages/demo.html")








@app.route('/registration', methods=['GET','POST'])
def process():
    yo = request.args.get("input")
 
    if request.method == "POST":
        message = request.form["input"]
        LISTE.append(message)
        
        return render_template("pages/registration.html",message=LISTE)
    
    else:

        return render_template("pages/registration.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404

if __name__=="__main__":
    
    app.run(debug=True, port=3000)
    home()
