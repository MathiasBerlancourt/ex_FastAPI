import json

with open('assets/users_db.json', 'r') as file:
    users_db = json.load(file)


def isAuthentificated(username, password):
    for user in users_db:
        if user["username"] == username and user["password"] == password:
            return True
    return False


def isAdmin(username, password):
    if username == "admin" and password == "4dm1N":
        return True
    else:
        return False
