from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
import hashlib


DATABASE = 'database.db'


app = Flask(__name__)
app.secret_key = "Jacques"
con= sqlite3.connect(DATABASE)
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
            username VARCHAR(20) PRIMARY KEY NOT NULL,     
            password VARCHAR(20) NOT NULL)
            """)
con.commit()
con.close()


@app.route("/")
def index():
    return render_template('login.html')

@app.route("/index", methods=["GET"])
def home():
    return render_template('index.html')

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template('signup.html')
    else:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()
        encoded = request.form["password"].encode()
        hash = hashlib.sha256(encoded).hexdigest()
        print(hash)
        cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", 
                            (request.form["username"],hash))
        con.commit()
        con.close()
    return "Signup successful"
    

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()
        encoded = request.form["password"].encode()
        hash = hashlib.sha256(encoded).hexdigest()
        print(hash)
        cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", 
                            (request.form["username"], hash))
        match = len(cur.fetchall())
        con.commit()
        con.close()
        if  match == 0:
            return "Login Failed"
        else:
            session["username"] = request.form["username"]
            return render_template('index.html')

@app.route("/logout")
def logout():
    session.pop("username", None)
    return render_template('login.html')

@app.route("/password", methods=["GET", "POST"])
def password():
    if request.method == "GET":
        if 'username' in session:
            return render_template('password.html')
        else:
            return render_template('login.html')
    else:
        if 'username' in session:
            con = sqlite3.connect(DATABASE)
            cur = con.cursor()
            hash = hashlib.sha256(request.form["password"].encode()).hexdigest()
            print(hash)
            cur.execute("UPDATE users SET password = ? WHERE username = ?", 
                                (hash, session["username"]))
            con.commit()
            con.close()
            return "Password updated"
        else:
            return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)