from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method== "GET":
        return render_template("signup.html")
    else:
        f = open("login.txt", "w")
        f.write(request.form["Username"] + "\n" )
        f.write(request.form["Password"])
        f.close()
    return "Signup succesful"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('index.html')
    else:
        Username = request.form["Username"]
        Password = request.form["Password"]
        f = open("login.txt", "r")
        un = f.readline().strip()
        pw = f.readline()
        if  Password == pw and Username == un:
            return "Hello " + Username
        else:
            return "Login Failed"
