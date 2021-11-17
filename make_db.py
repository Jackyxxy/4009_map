from flask import Flask
from flask import render_template
import sqlite3 


app = Flask(__name__)

@app.route('/students')
def students():

    con = sqlite3.connect('mydatabase.db')

    try:
        con.execute('CREATE TABLE students (name TEXT, id INT)')
        print ('Table created successfully');
    except:
        pass

    con.close()

    con = sqlite3.connect("mydatabase.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * from students")
    rows = cur.fetchall();

    return render_template("students.html",rows = rows)
