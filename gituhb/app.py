from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home_html.html")


@app.route('/about')
def about():
    return render_template("pages/about_html.html")


@app.route('/contact')
def contact():
    return render_template("pages/contact_html.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404


if __name__=="__main__":
    
    app.run(debug=True, port=3000)
    home()
