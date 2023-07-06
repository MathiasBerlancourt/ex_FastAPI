import json

with open('assets/users_db.json', 'r') as file:
    users_db = json.load(file)


def isAuthenticated(username, password):
    for user, user_password in users_db.items():
        if user == username and user_password == password:
            return True
    return False


def isAdmin(username, password):
    if username == "admin" and password == "4dm1N":
        return True
    return False
