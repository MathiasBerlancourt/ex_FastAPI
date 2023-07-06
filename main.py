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


@api.post("/question")
def post_question(
    question: str,
    subject: str,
    use: str,
    responseA: str,
    responseB: str,
    responseC: str,
    responseD: str,
    remark: str,
    username: str = Header(...),
    password: str = Header(...),
):
    """post_question permet d'ajouter une question à la bdd. Un compte admin est nécessaire. Les clés subject, use, question, response A...D et remark doivent être complétées. On peut mettre un champ vide.
    exemple:
curl -X POST "http://localhost:8000/question" -H "username: admin" -H "password: 4dm1N" -H "subject: BDD" -H "use: Test%20de%20positionnement" -H "question: Quelle%20est%20la%20réponse%20de%20test%20?" -H "responseA: answer%20de%20test42" -H "responseB: answer%20de%20test42" -H "responseC: answer%20de%20test42" -H "responseD: answer%20de%20test42" -H "remark: test42"
    """
    if isAdmin(username, password):
        with open("assets/questions.csv", "a") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(
                [question, responseA, responseB, responseC,
                    responseD, remark, subject, use]
            )
        return {"status": "success", "message": "Question ajoutée avec succès."}
    else:
        return {"status": "error", "message": "Mauvais nom d'utilisateur ou mot de passe."}
