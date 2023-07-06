from fastapi import FastAPI
from isAuthentificated import isAuthentificated, isAdmin
import csv
import json

with open('assets/users_db.json', 'r') as file:
    users_db = json.load(file)

print(users_db)


api = FastAPI(title="API QUIZZ")


def get_quizz():
    """get quizz nous permet de lire notre fichier csv
     et nous renvoie notre csv sous forme de dictionnaire """
    data = []
    with open('assets/questions.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)

    # Retourne le contenu du fichier csv sous forme de dictionnaire

    return data


quizz_data = get_quizz()


@api.get("/APIstatus")
def APIstatus():
    """APIstatus nous permet de savoir si l'API est en marche"""
    return {"status": "success",
            "message": "l'API est en marche"}
