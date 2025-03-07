from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method== "GET":
        return render_template("signup.html")
    
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('index.html')