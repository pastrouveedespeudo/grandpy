from PIL import Image
from flask import Flask
from flask import url_for
from flask import render_template

from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def home():
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
