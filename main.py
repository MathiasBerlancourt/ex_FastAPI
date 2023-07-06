from fastapi import FastAPI, Header
from authentification import isAuthenticated, isAdmin
import csv
import random


api = FastAPI(title="API QUIZZ")


@api.get("/data")
def get_data(username: str = Header(...), password: str = Header(...)):
    """get_data nous permet de lire notre fichier csv
     et nous renvoie notre csv sous forme de dictionnaire
     on doit indiquer son username et son mdp pour accéder à la requête
     exemple:
     curl -X GET "http://localhost:8000/data" -H "username: alice" -H "password: wonderland"

    """
    data = []
    if isAuthenticated(username, password):
        with open('assets/questions.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)

        # Retourne le contenu du fichier csv sous forme de dictionnaire
        return data

    else:
        return {"status": "error", "message": "mauvais username ou mot de passe"}


@api.get("/APIstatus")
def APIstatus():
    """APIstatus nous permet de savoir si l'API est en marche"""
    return {"status": "success",
            "message": "l'API est en marche"}


@api.get("/quizz")
def get_quizz(use: str, subject: str, username: str = Header(...), password: str = Header(...)):
    """qet_quizz nous permet d'avoir un quizz généré aléatoirement en fonction 
    du sujet (subject) et de l'utilisation (use) choisie. L'utilisateur doit s'authentifier pour accéder à ce quizz
    exemple:
     curl -X GET "http://localhost:8000/quizz?use=Test%20de%20positionnement&subject=BDD" -H "username: alice" -H "password: wonderland"
    """
    quizz_selected = []
    if isAuthenticated(username, password):
        with open('assets/questions.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row['subject'] == subject and row['use'] == use:
                    quizz_selected.append(row)

        # je "mélange" mon quizz aléatoirement avec la fonction shuffle du paskage random :
        random.shuffle(quizz_selected)
        return quizz_selected
    else:
        return {"status": "error", "message": "mauvais username ou mot de passe"}
