from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import requests

DATABASE = 'database.db'


app = Flask(__name__)
con= sqlite3.connect(DATABASE)
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
            username VARCHAR(20) PRIMARY KEY NOT NULL,     
            password VARCHAR(20) NOT NULL)
            """)
con.commit()
con.close()


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template('signup.html')
    else:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()
        cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", 
                            (request.form["username"], request.form["password"]))
        con.commit()
        con.close()
    return "Signup successful"
    

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('index.html')
    else:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", 
                            (request.form["username"], request.form["password"]))
        match = len(cur.fetchall())
        con.commit()
        con.close()
        if  match == 0:
            return "Login Failed"
        else:
            return "Welcome" + request.form["username"]


if __name__ == "__main__":
    app.run(debug=True)