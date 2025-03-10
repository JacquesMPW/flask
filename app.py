from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

DATABASE = 'database.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row 
    return conn

app = Flask(__name__)
conn = get_db_connection
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
            username VARCHAR(20) PRIMARY KEY NOT NULL,     
            password VARCHAR(20) NOT NULL)
            """)
conn.commit()
conn.close()

def signup_user(username, password):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO users (id, username, email, first_name, last_name, password_hash)
        VALUES (?, ?)
    ''', (username, password))

    conn.commit()
    conn.close()

    return 'Signup successful! Please log in.'

@app.route("/signup", methods=["GET", "POST"])
def signup():
    username = request.form['username']
    password = request.form['password']  

    message = signup_user(username, password)
    flash(message)

    if 'Signup successful!' in message:
        return redirect(url_for('homepage'))
    
    return redirect(url_for('index'))

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('signup.html')
    else:
        Username = request.form["Username"]
        Password = request.form["Password"]
        if  Password == "123" and Username == "bob":
            return "Hello " + Username
        else:
            return "Login Failed"
