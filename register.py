from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import render_template
from flask import request
from flask import redirect
from flask import abort
from flask import make_response
import sqlite3

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return do_the_registration(request.form['uname'], request.form['pwd'])
    else: 
        return show_the_registration_form();
def show_the_registration_form():
    return render_template('register.html',page=url_for('register'))
def do_the_registration(u,p):
    con = sqlite3.connect('registered_users.db')
    try:
        con.execute('CREATE TABLE users (name TEXT, pwd INT)')
        print ('Table created successfully');
    except:
        pass
    
    con.close()  
    
    con = sqlite3.connect('registered_users.db')
    con.execute("INSERT INTO users values(?,?);", (u, p))
    con.commit()
    con.close()  

    return show_the_login_form()
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login(request.form['uname'], request.form['pwd'])
    else:
        return show_the_login_form()
def show_the_login_form():
    return render_template('login.html',page=url_for('login'))
def do_the_login(u,p):
    con = sqlite3.connect('registered_users.db')
    cur = con.cursor();
    cur.execute("SELECT count(*) FROM users WHERE name=? AND pwd=?;", (u, p))
    if(int(cur.fetchone()[0]))>0:                                               
        return f'<H1>Success!</H1>'
    else:
        abort(403)   
@app.errorhandler(403)
def wrong_details(error):
    return render_template('wrong_details.html'), 403


