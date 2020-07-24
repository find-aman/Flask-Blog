from flask import render_template, url_for, flash, redirect
from FLASK_BLOG import app
from FLASK_BLOG.forms import RegistrationForm, LoginForm
from FLASK_BLOG.models import User, Post


posts = [
    {
        "author": "Aman Gupta",
        "title": "Blog Post 1",
        "content": "First Post Content",
        "date_posted": "18-April-2020",
    },
    {
        "author": "Akash Gupta",
        "title": "Blog Post 2",
        "content": "Second Post Content",
        "date_posted": "19-April-2020",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account Created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Lognin unsuccessful. Please check username and password", "danger")
    return render_template("login.html", title="Login", form=form)

