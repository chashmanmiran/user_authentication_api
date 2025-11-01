
from flask import Flask, render_template, session, redirect, url_for, request
from flask import Blueprint
from flask_bcrypt import Bcrypt
from models import User
from extensions import db
from sqlalchemy import or_

blp = Blueprint("main", __name__,)

@blp.route("/")
def home():
    if "username" in session:
        return redirect(url_for('main.dashboard'))
    return render_template("index.html")


#login
@blp.route("/login", methods=["POST"])
def login():
    username = (request.form.get("username") or "").strip()
    password = request.form.get("password") or ""
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        session['username'] = username
        return redirect(url_for('main.dashboard'))
    else:
        return render_template("index.html")

#register
@blp.route("/register", methods=["POST"])
def register():
    email = (request.form.get("email") or "").strip()
    username = (request.form.get("username") or "").strip()
    password = request.form.get("password") or ""
    user = User.query.filter(or_(
    User.username == username,
    User.email == email
        )).first()
    if user:
        return render_template("index.html", error="User already exists!")
    else:
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        session['username'] = username
        return redirect(url_for('main.dashboard'))

#dashboard
@blp.route("/dashboard")
def dashboard():
    if "username" in session:
        return render_template("dashboard.html", username=session['username'])
    return redirect(url_for('main.home'))

#logout
@blp.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('main.home'))