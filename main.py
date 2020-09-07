from flask import Flask, Response, jsonify, request
from flask_pymongo import PyMongo
from Authentication.password import encrypt, is_password
from Authentication import services

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/Contact"
mongo = PyMongo(app)
collection = mongo.db["users"]

services.mongo = mongo


@app.route('/signup', methods=["POST"])
def signup():
    form = request.form
    [submit, msg] = services.signUpAuth(
        form["email"], form["password"], form["username"], form["name"])
    print(submit)
    return msg


@app.route('/login', methods=["POST"])
def login():
    error = None
    form = request.form
    [auth, msg] = services.authenticate(form["email"], form["password"])
    if auth:
        return "Logged in"  # need to add actual session and so on
    else:
        return msg


if __name__ == "__main__":
    app.run(debug=True)
