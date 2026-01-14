from flask import Flask, render_template, request,flash
from hasher import *

#test email
test_mail = "email123@gmail.com"

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    password = request.form.get("password")
    email = request.form.get("email")

    if not email and not password:
        print("email and Password not received")
        return "No password received"

    check1 = hash_check(password) #hash of inputted password
    check2 = hash_check("hello world") #we will check hash of stored password

    result = hash_verify(check1, check2) #verifying whether both hashes are similar for auth

    if result and email == test_mail:
        
        return "Access",200
    
    else:
        
        return "Denied",403

app.run(host="127.0.0.1",port=80,debug=True)
