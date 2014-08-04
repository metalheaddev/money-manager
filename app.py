__author__ = 'sivins'

from flask import Flask, render_template, redirect, url_for, \
    request, session, flash, get_flashed_messages, g
from functools import wraps
import sqlite3

app = Flask(__name__)

app.secret_key = "my precious"
app.database = "sample.db"

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
def home():
    g.db = connect_db()
    cur = g.db.execute('select * from expenses')
    #Here's the readable way to make our list
    expenses = []
    for row in cur.fetchall():
        expenses.append(dict(date=row[0], amount=row[1], description=row[2], category=row[3]))
    #Here's another way to do the same thing but with just one line:
    #expenses = [dict(date=row[0], amount=row[1], description=row[2], category=row[3]) for row in cur.fetchall()]
    g.db.close()
    return render_template('index.html', expenses=expenses)


@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('You were just logged in!')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were just logged out!')
    return redirect(url_for('welcome'))


def welcome():
    return render_template("welcome.html")

def connect_db():
    return sqlite3.connect(app.database)


if __name__ == '__main__':
    app.run(debug=True)