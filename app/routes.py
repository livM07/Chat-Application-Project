from flask import render_template, jsonify, session, redirect, request, url_for, flash
from app import app, db
from app.forms import LoginForm, CreateForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import user
import json

# CHANGED STATIC FOLDER -> TEMPLATES FOR TESTING. ADD STATIC BACK LATER.
@app.route('/')
def home():
    return render_template("base.html", title="base")

@app.route('/history')
@login_required
def history():
      return render_template("history-page.html")

@app.route('/chat')
def chat():
      return render_template("chat-page.html")

# WORKS!!
@app.route('/create', methods = ['GET','POST'])
def create():
    if current_user.is_authenticated:
        return redirect(url_for('history'))
    
    form = CreateForm()

    if form.validate_on_submit():
         currentUser = user(name=form.name.data, email=form.email.data)
         currentUser.set_password(form.password.data)
         db.session.add(currentUser)
         db.session.commit()
         flash('Account created successfully!')
         return redirect(url_for('login'))

    return render_template("create.html", form=form)

# WORKS!!
@app.route('/login', methods = ['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("history"))

    form = LoginForm()

    if form.validate_on_submit():
          currentUser = user.query.filter_by(email=form.email.data).first()
          if currentUser is None:
            flash('email is not in DB')
            return redirect(url_for('login'))
          elif not currentUser.check_password(form.password.data):
               flash('password is incorrect')
               return redirect(url_for('login'))
          login_user(currentUser)
          return redirect(url_for('history'))
    else:
        flash("unsuccessful")
    return render_template('login.html', form=form)    

@app.route('/logout')
def logout():
     logout_user()
     return redirect(url_for('login'))