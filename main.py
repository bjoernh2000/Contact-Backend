from flask import Flask, Response, jsonify, request
from flask_pymongo import PyMongo
from password import encrypt, is_password

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/Contact"
mongo = PyMongo(app)
collection = mongo.db["users"]


@app.route('/', methods=["GET"])
def hello():
    return "Hello World!"


@app.route('/signup', methods=["POST"])
def signup():
    error = None
    if mongo.db.users.find_one({"email": request.form["email"]}, {"_id": 0}) or mongo.db.users.find_one({"username": request.form["username"]}, {"_id": 0}):
        error = "Username or Email has been taken, please choose another."
        return False
    else:
        document = {
            "email": request.form["email"],
            "username": request.form["username"],
            "password": encrypt(request.form["password"]),
            "user": "customer"
        }
        mongo.db.users.insert_one(document)
        return True


if __name__ == "__main__":
    app.run(debug=True)
