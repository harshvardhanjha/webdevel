from flask import Flask, url_for, render_template, redirect, request, session, flash, g
from functools import wraps
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
import os

# import sqlite3
app = Flask(__name__)
bcrypt = Bcrypt(app)

# config
app.config.from_object(os.environ['APP_SETTINGS'])

# create the sqlalchemy object

db = SQLAlchemy(app)
from models import *
# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap


@app.route('/')
@login_required
def hello_world():
	return 'Hello World!'

@app.route('/user')
def hello_user(username = None):
	return render_template('user.html', username = 'admin')

@app.route('/login', methods = ['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid Credentials Please try again'
		else:
			session['logged_in'] = True
			flash('You were just logged in')
			return redirect(url_for('ind'))
	return render_template('login.html', error = error)

@app.route('/logout')
@login_required
def logout():
	session.pop('logged_in', None)
	flash('You were just logged out')
	return redirect(url_for('wel'))

@app.route('/index')
def ind():
	posts = db.session.query(BlogPost).all()
	return render_template('index.html', posts = posts)


@app.route('/welcome')
def wel():
	return render_template('welcome.html')
 
if __name__ == '__main__':
    app.run()

