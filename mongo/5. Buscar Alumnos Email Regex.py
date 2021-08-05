from pymongo import MongoClient

client = MongoClient("mongodb://localhost/python-master")

db = client["python-master"]

alumnosCollection = db["alumnos"]

query = {
    "email": { "$regex": r"@gmail", "$options": "i" }
}

for alumno in alumnosCollection.find(query):
    print(alumno)

client.close()