from flask import render_template
from app import app


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
    return "create account here"

@app.route('/login', methods = ['GET','POST'])
def login():
    return "login here"
