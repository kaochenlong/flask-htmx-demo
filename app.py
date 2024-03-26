from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("posts/index.html")


@app.route("/posts/new")
def new_post():
    return render_template("posts/new.html")
