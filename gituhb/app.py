from flask import Flask, render_template
from mocks impos Post

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


@app.route('/blog')
def blog():
    posts = Post.all()
    return render_template("posts/posts_html.html", posts=posts)


@app.route('/blog/posts/<int:id>')
def post_show(id):


    post = Post.find(id)
    return render_template("posts/show_html.html", post = post)



@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404


if __name__=="__main__":
    
    app.run(debug=True, port=3000)
    home()


















    
