import os
import bs4 as bs
import urllib.request
from PIL import Image
from flask import Flask
from flask import request
from flask import url_for
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
Bootstrap(app)

LISTE = []



@app.route('/', methods=["GET","POST"])
def home():
    yo = {"ok":"ta DAZDZgros pd"}
    print("salut")
    if request.method == "POST":
        message = request.form["input"]
        LISTE.append(message)
        return render_template("home.html",message=message)
    

    else:

        return render_template("home.html")

@app.route('/about')
def about():
    return render_template("pages/about.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404

if __name__=="__main__":
    
    app.run(debug=True, port=3000)
    home()
