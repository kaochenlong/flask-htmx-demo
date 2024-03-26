from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("posts/index.html")


@app.route("/posts/new")
def new_post():
    return render_template("posts/new.html")


@app.route("/posts/create", methods=["POST"])
def create_post():
    return redirect(url_for("home"))


@app.route("/posts/<int:id>")
def show_post(id):
    return render_template("posts/show.html")


@app.route("/posts/<int:id>/edit")
def edit_post(id):
    return render_template("posts/edit.html", id=id)


@app.route("/posts/<int:id>", methods=["POST"])
def update_post(id):
    return redirect(url_for("show_post", id=id))


@app.route("/htmx-demo")
def htmx_demo():
    return render_template("htmx/demo.html")
