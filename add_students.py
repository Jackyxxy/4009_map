from flask import Flask
from flask import url_for
from flask import render_template
from flask import request
import sqlite3

app = Flask(__name__)

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        return do_the_add(request.form['name'], request.form['ID'])
    else:
        return show_the_add_form();
def show_the_add_form():
    return render_template('add_student.html',page=url_for('add_student'))
def do_the_add(u,i):
    con = sqlite3.connect('my_student_database.db')
    try:
        con.execute('CREATE TABLE students (name TEXT, id INT)')
        print ('Table created successfully');
    except:
        pass
    
    con.close()  
    
    con = sqlite3.connect('my_student_database.db')
    con.execute("INSERT INTO students values(?,?);", (u,i))
    con.commit()
    con.close()  
    
    return show_the_add_form()
@app.route('/students')
def students():
    con = sqlite3.connect("my_student_database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * from students")
    rows = cur.fetchall();

    return render_template("students.html",rows = rows)

