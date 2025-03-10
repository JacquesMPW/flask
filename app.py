from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os

DATABASE = 'database.db'

app = Flask(__name__)
con = sqlite3.connect(DATABASE)
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
            username VARCHAR(20) PRIMARY KEY NOT NULL,     
            password VARCHAR(20) NOT NULL)
            """)
con.commit()
con.close()

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        cur.execute("""INSERT INTO users (username,password)
        VALUES(?,?)""",(request.form['Username'],request.form['Password']));
        con.commit()
        con.close()
    return "Signup Successful"

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
