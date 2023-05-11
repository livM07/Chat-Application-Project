from flask import render_template
from app import app

@app.route('/')
def index():
    return "Hello World!"

@app.route('/create', methods = ['POST'])
def create():
    return "create account here"

@app.route('/login', methods = ['POST'])
def login():
    return "login here"
