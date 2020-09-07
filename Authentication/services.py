from uuid import uuid4
from Authentication.password import encrypt, is_password


def authenticate(email, password):
    hashed = encrypt(password)
    user = mongo.db.users.find_one({"email": email}, {"_id": 0})
    if user:
        if is_password(password, user["password"]):
            return True, "Session"
    return False, "Invalid credentials, please try again."


def signUpAuth(email, password, username, name):
    hashed = encrypt(password)
    if mongo.db.users.find_one({"email": email}, {"_id": 0}) or mongo.db.users.find_one({"username": username}, {"_id": 0}):
        return False, "Username or Email has been taken, please choose another."
    else:
        try:
            document = {
                "email": email,
                "username": username,
                "password": encrypt(password),
                "name": name,
                "id": uuid4()
            }
            mongo.db.users.insert_one(document)
            return True, "It worked"
        except:
            return False, "error in storing"
