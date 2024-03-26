from models.post import db, Post
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./db.sqlite"
db.init_app(app)


@app.route("/")
def home():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template("posts/index.html", posts=posts)


@app.route("/posts/new")
def new_post():
    return render_template("posts/new.html")


@app.route("/posts/create", methods=["POST"])
def create_post():
    title = request.form["title"]
    content = request.form["content"]

    post = Post(title=title, content=content)
    db.session.add(post)
    db.session.commit()

    return redirect(url_for("home"))


@app.route("/posts/<int:id>")
def show_post(id):
    post = Post.query.get(id)

    return render_template("posts/show.html", post=post)


@app.route("/posts/<int:id>/edit")
def edit_post(id):
    post = Post.query.get(id)

    return render_template("posts/edit.html", post=post)


@app.route("/posts/<int:id>", methods=["POST"])
def update_post(id):
    post = Post.query.get(id)

    title = request.form["title"]
    content = request.form["content"]

    post.title = title
    post.content = content

    db.session.commit()

    return redirect(url_for("show_post", id=id))


@app.route("/htmx-demo")
def htmx_demo():
    return render_template("htmx/demo.html")


if __name__ == "__main__":
    with app.app_context():
        print("Creating database...")
        db.create_all()

    app.run(debug=True, port=3000)
