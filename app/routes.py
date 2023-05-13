from flask import render_template, jsonify, session, redirect, request, url_for, flash
from app import app, db
from app.models import user, conversations
import json

# CHANGED STATIC FOLDER -> TEMPLATES FOR TESTING. ADD STATIC BACK LATER.
@app.route('/')
def home():
    return render_template("base.html", title="base")

@app.route('/history')
def history():
      return render_template("history-page.html")

@app.route('/chat')
def chat():
      return render_template("chat-page.html")

@app.route('/create', methods = ['GET','POST'])
def create():
    if request.method == "POST":
        # TO DO -> store form data in session
        username = request.form["username"]
        session["username"] = username
        email = request.form["email"]
        session["email"] = email
        password = request.form["password"]
        session["password"] = password

        # TO DO -> check if email is already in DB
        email_exists = user.query.filter_by(email=email).first()
        if email_exists:
            flash("email already in use")
        else: 
            new_user = user(name=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            return "successfully created new user"
    else:
        return render_template("create.html")

@app.route('/login', methods = ['GET','POST'])
def login():
    if "username" in session:
        render_template("history-page.html")
    else:
        render_template("login.html")
        #  TO DO -> check login data (exists + is correct)
        email_exists = user.query.filter_by(email=email).first()
        if email_exists:
            # TO DO -> check password is correct
            # if data is correct -> create session + render history page
            if request.method == "POST":
                email = request.form["email"]
                session["email"] = email
                password = request.form["password"]
                session["password"] = password
                render_template("history-page.html")

@app.route('/logout')
def logout():
     session.pop("username", None)
     return "logged out"