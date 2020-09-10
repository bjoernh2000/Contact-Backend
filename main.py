from flask import Flask, Response, jsonify, request, make_response
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
    [auth, session] = services.authenticate(form["email"], form["password"])
    if auth:
        ret = make_response("Success")
        ret.set_cookie("SID", str(session.sessionID),
                       expires=session.dateExpires)
        return ret
    else:
        ret = session
        return ret


@app.route('/logout', methods=["POIST"])
def logout():
    return "WIP"


if __name__ == "__main__":
    app.run(debug=True)
