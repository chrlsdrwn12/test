from application import app
from flask import render_template, jsonify, request, redirect, url_for, session, flash
import os, datetime, time
from flask import session, redirect, url_for, flash
from functools import wraps
# from application.lib.mtcmis import *

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash('You need to login first.')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def validateUser(username, password):
    users = {"userid": "david","password": "lean","alias":"RiverKwai"}
    alias = users["alias"]
    if username in users['userid'] and password == users['password']:
        return users
    return False

@app.route("/")
@login_required
def home():
    alias = '%s' % session['alias']
    print (alias)
    return render_template('index.html', alias=alias)

# set the secret key for session.  keep this really secret:
app.secret_key = 'A0Zr98j/3ysX R~XhHkH!jLWX/,?RT'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = validateUser(username, password)
        if user:
            session['username'] = user['userid']
            session['alias'] = user['alias']
            return redirect(url_for('home'))
        else:
            flash("Incorrect login.")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash("Successfully logged out.")
    return redirect(url_for('login'))