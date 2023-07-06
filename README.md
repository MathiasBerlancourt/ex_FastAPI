# ex_FastAPI ⚡️

### Clone it

Open a terminal and follow this step:

```console
git clone https://github.com/MathiasBerlancourt/ex_FastAPI

```

### Run it

Run the server with:

<div class="termy">

```console
$ uvicorn main:app --reload

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

</div>

The command `uvicorn main:app` refers to:

- `main`: the file `main.py` (the Python "module").
- `app`: the object created inside of `main.py` with the line `app = FastAPI()`.
- `--reload`: make the server restart after code changes. Only do this for development.

## Use it

### With Postman

Download & install Postman 👉 <https://www.postman.com/downloads/>

Postman is a standalone software testing API (Application Programming Interface) platform to build, test, design, modify, and document APIs. It is a simple Graphic User Interface for sending and viewing HTTP requests and responses.

### On CLI

Open a new terminal and enter you API call following the documentation

##API documentation

# On swagger

On your browser check the API url with '/docs' endpoint

# Endpoints

### GET /APIstatus

Endpoint to check the API connection

```console
curl -X GET "http://localhost:8000/APIstatus"

```

### GET /data

Endpoint wich return the quizz database

<b>Headers :</b>

- username (required)
- password (required)

```console
     curl -X GET "http://localhost:8000/data -H "username: <username>" -H "password: <password>"

```

### GET /quizz

Endpoint to get a quizz with randomized questions order. The user need to choose a subject an use

<b>Headers :</b>

- username (required)
- password (required)

<b>Params :</b>

- use (required)
- subject (required)

```console
     curl -X GET "http://localhost:8000/quizz?use=Test%20de%20positionnement&subject=BDD" -H "username: <username>" -H "password: <password>"


```

### POST /question

Endpoint to add a question to the questions database. the user need to add subject, use, question, response A...D et remark doivent être complétées. The user can fill a blank string.
An admin access is mandatory.

<b>Headers :</b>

- username (required)
- password (required)

<b>Params :</b>

- use (required)
- subject (required)
- question (required)
- responseA (required)
- responseB (required)
- responseC (required)
- responseD (required)
- remark (required)

```console
curl -X POST "http://localhost:8000/question" -H "username: admin" -H "password: 4dm1N" -H "subject: BDD" -H "use: Test de positionnement" -H "question: Quelle est la réponse de test%" -H "responseA: answer de test42" -H "responseB: answer de test42" -H "responseC: answer de test42" -H "responseD: answer de test42" -H "remark: test42"


```

## Test it : set of test

### GET /data

```console
     curl -X GET "http://localhost:8000/data" -H "username: alice" -H "password: wonderland"

```

### GET /quizz

```console
     curl -X GET "http://localhost:8000/quizz?use=Test%20de%20positionnement&subject=BDD" -H "username: alice" -H "password: wonderland"

```

### POST /question

```console
curl -X POST "http://localhost:8000/question" -H "username: admin" -H "password: 4dm1N" -H "subject: BDD" -H "use: Test de positionnement" -H "question: Quelle est la réponse de test%" -H "responseA: answer de test42" -H "responseB: answer de test42" -H "responseC: answer de test42" -H "responseD: answer de test42" -H "remark: test42"

```
